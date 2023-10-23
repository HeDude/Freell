using Irony.Parsing;

namespace Freell
{
    public class Evaluator
    {
        public object? Evaluate(ParseTreeNode node)
        {
            // For now, simply return true to indicate that the code is valid.
            return true;
        }
    }
}