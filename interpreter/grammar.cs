using Irony.Parsing;

namespace Freell
{
    public class FreellGrammar : Grammar
    {
        public FreellGrammar() : base(true)  // true for case sensitivity
        {
            var validIdentifierPattern = @"[a-zA-Z0-9_-]+";
            var productName = new RegexBasedTerminal("productName", validIdentifierPattern);
            var rootName = new RegexBasedTerminal("rootName", validIdentifierPattern);

            var learningArchitecture = ToTerm("learning architecture");
            var expertRule = ToTerm("expert rule");
            var educationArchitecture = ToTerm("education architecture");

            var an_action = ToTerm("an action");
            var an_actor = ToTerm("an actor");
            var a_method = ToTerm("a method");
            var a_portfolio = ToTerm("a portfolio");
            var a_prerequisite = ToTerm("a prerequisite");
            var a_resource = ToTerm("a resource");
            var a_unit = ToTerm("a unit");

            var period = ToTerm(".");  // Terminal for period

            // Define Non-terminals
            var productType = new NonTerminal("product-type");
            var productStatement = new NonTerminal("product-statement");
            var rootStatement = new NonTerminal("root-statement");
            var typeWithArticle = new NonTerminal("type-with-article");
            var program = new NonTerminal("program");

            // Define Rules
            productType.Rule = learningArchitecture | expertRule | educationArchitecture;
            typeWithArticle.Rule = an_action | an_actor | a_method | a_portfolio | a_prerequisite | a_resource | a_unit;

            // Define the BNF-like rule for the product statement
            productStatement.Rule = ToTerm("This") + productType + ToTerm("is called") + productName + period;

            // Update the BNF-like rule for the root statement to include period
            rootStatement.Rule = ToTerm("The root is") + typeWithArticle + ToTerm("called") + rootName + period;

            // Define the BNF-like rule for the program
            program.Rule = productStatement + rootStatement;

            // Set the root non-terminal
            this.Root = program;
        }
    }
}