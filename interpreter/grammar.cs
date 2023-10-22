using System;
using Irony.Parsing;

namespace Freell
{
    public class FreellGrammar : Grammar
    {
        public FreellGrammar() : base(false)  // false for case sensitivity
        {
            // Define Terminals
            var identifier = new IdentifierTerminal("identifier");
            var action = ToTerm("Action");
            var actor = ToTerm("Actor");
            var method = ToTerm("Method");
            var portfolio = ToTerm("Portfolio");
            var prerequisite = ToTerm("Prerequisite");
            var a = ToTerm("a");
            var an = ToTerm("an");
            var period = ToTerm(".");  // Terminal for period

            // Define Non-terminals
            var startStatement = new NonTerminal("start-statement");
            var article = new NonTerminal("article");
            var type = new NonTerminal("type");
            var declaration = new NonTerminal("declaration");

            // Define Rules
            article.Rule = a | an;
            type.Rule = action | actor | method | portfolio | prerequisite ;

            // Update the BNF-like rule for the start statement to include period
            startStatement.Rule = ToTerm("The root is") + article + type + ToTerm("called") + identifier + period;

            // Set the root non-terminal
            this.Root = startStatement;

            // Semantic action to enforce 'a' with 'Method' and 'Portfolio', 'an' with 'Action' and 'Actor'
            startStatement.AstConfig.NodeCreator = (context, parseNode) =>
            {
                var articleNode = parseNode.ChildNodes[1];
                var typeNode = parseNode.ChildNodes[2];

                if ((articleNode.Term.Name == "a" && (typeNode.Term.Name == "Action" || typeNode.Term.Name == "Actor")) ||
                    (articleNode.Term.Name == "an" && (typeNode.Term.Name == "Method" || typeNode.Term.Name == "Portfolio" || typeNode.Term.Name == "Prerequisite")))
                {
                    // Error: Incorrect article used
                    context.AddParserMessage(new ParserMessage(ParserErrorLevel.Error, parseNode.Span.Location, "Incorrect article used with type."));
                }
            };
        }
    }
}