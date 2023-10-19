using System;
using Irony.Parsing;

namespace Freell
{
    public class Interpreter
    {
        private readonly LanguageData _languageData;
        private readonly Evaluator _evaluator;

        public Interpreter()
        {
            var grammar   = new FreellGrammar();
            _languageData = new LanguageData(grammar);
            _evaluator    = new Evaluator();
        }
        public object? Interpret(string sourceCode)
        {
            var parser = new Parser(_languageData);
            var parseTree = parser.Parse(sourceCode);
            if (parseTree.HasErrors())
            {
                throw new Exception("Syntax errors found in source code.");
            }

            var result = _evaluator.Evaluate(parseTree.Root);
            return result;
        }
    }
}
