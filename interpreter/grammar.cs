using System;
using Irony.Parsing;

namespace Freell
{
    public class FreellGrammar : Grammar
    {
        public FreellGrammar() : base(false)  // false for case sensitivity
        {
            // Define Terminals
            var educationDesignName = new IdentifierTerminal("educationDesignName");
            var rootName = new IdentifierTerminal("rootName");
            var action = ToTerm("Action");
            var actor = ToTerm("Actor");
            var method = ToTerm("Method");
            var portfolio = ToTerm("Portfolio");
            var prerequisite = ToTerm("Prerequisite");
            var resource = ToTerm("Resource");
            var unit = ToTerm("Unit");
            var a = ToTerm("a");
            var an = ToTerm("an");
            var period = ToTerm(".");  // Terminal for period

            // Define Non-terminals
            var educationDesignStatement = new NonTerminal("education-design-statement");
            var rootStatement = new NonTerminal("root-statement");  // Renamed from startStatement
            var article = new NonTerminal("article");
            var type = new NonTerminal("type");
            var program = new NonTerminal("program");

            // Define Rules
            article.Rule = a | an;
            type.Rule = action | actor | method | portfolio | prerequisite | resource | unit;

            // Define the BNF-like rule for the education design statement
            educationDesignStatement.Rule = ToTerm("This education design is called") + educationDesignName + period;

            // Update the BNF-like rule for the root statement to include period
            rootStatement.Rule = ToTerm("The root is") + article + type + ToTerm("called") + rootName + period;

            // Define the BNF-like rule for the program
            program.Rule = educationDesignStatement + rootStatement;

            // Set the root non-terminal
            this.Root = program;

            // Semantic action to enforce 'a' with 'Method' and 'Portfolio', 'an' with 'Action' and 'Actor'
            rootStatement.AstConfig.NodeCreator = (context, parseNode) =>
            {
                var articleNode = parseNode.ChildNodes[1];
                var typeNode = parseNode.ChildNodes[2];

                if ((articleNode.Term.Name == "a" && (typeNode.Term.Name == "Action" || typeNode.Term.Name == "Actor" || typeNode.Term.Name == "Unit")) ||
                    (articleNode.Term.Name == "an" && (typeNode.Term.Name == "Method" || typeNode.Term.Name == "Portfolio" || typeNode.Term.Name == "Prerequisite" || typeNode.Term.Name == "Resource")))
                {
                    // Error: Incorrect article used
                    context.AddParserMessage(new ParserMessage(ParserErrorLevel.Error, parseNode.Span.Location, "Incorrect article used with type."));
                }
            };
        }
    }
}
