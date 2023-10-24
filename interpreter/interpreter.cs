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

        public Interpretation Interpret(string code)
        {
            // Parse the code
            var tree = this.parser.Parse(code);

            // Check for errors
            if (tree.HasErrors())
            {
                return new Interpretation(false, evaluator.GrammarPrompts["productStatement"]);
            }

            // Evaluate the tree
            Evaluation evaluation = this.evaluator.Evaluate(tree.Root);

            // Check for errors in the evaluation
            if (!evaluation.Valid)
            {
                return new Interpretation(false, evaluation.Suggestion);
            }

            return new Interpretation(true, string.Empty);
        }
    }
}
