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
            var an_action = ToTerm("an action");
            var an_actor = ToTerm("an actor");
            var a_method = ToTerm("a method");
            var a_portfolio = ToTerm("a portfolio");
            var a_prerequisite = ToTerm("a prerequisite");
            var a_resource = ToTerm("a resource");
            var a_unit = ToTerm("a unit");
            var period = ToTerm(".");  // Terminal for period

            // Define Non-terminals
            var educationDesignStatement = new NonTerminal("education-design-statement");
            var rootStatement = new NonTerminal("root-statement");  // Renamed from startStatement
            var typeWithArticle = new NonTerminal("type-with-article");
            var program = new NonTerminal("program");

            // Define Rules
            typeWithArticle.Rule = an_action | an_actor | a_method | a_portfolio | a_prerequisite | a_resource | a_unit;

            // Define the BNF-like rule for the education design statement
            educationDesignStatement.Rule = ToTerm("This education architecture is called") + educationDesignName + period;

            // Update the BNF-like rule for the root statement to include period
            rootStatement.Rule = ToTerm("The root is") + typeWithArticle + ToTerm("called") + rootName + period;

            // Define the BNF-like rule for the program
            program.Rule = educationDesignStatement + rootStatement;

            // Set the root non-terminal
            this.Root = program;
        }
    }
}