using Irony.Parsing;

namespace Freell
{
    public class Interpreter
    {
        private readonly LanguageData language;
        private readonly Parser parser;
        private readonly Evaluator evaluator;

        public Interpreter()
        {
            FreellGrammar grammar = new FreellGrammar();
            this.language = new LanguageData(grammar);
            this.parser = new Parser(this.language);
            this.evaluator = new Evaluator();
        }

        public bool Interpret(string sourceCode)
        {
            ParseTree parseTree = this.parser.Parse(sourceCode);

            if (parseTree.HasErrors())
            {
                // Handle errors here
                return false;
            }

            // Assuming parseTree is the generated ParseTreeNode
            var result = evaluator.Evaluate(parseTree.Root);

            return result is not null && (bool)result;
        }
    }
}
