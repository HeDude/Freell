using System.Collections.Generic;
using Irony.Parsing;

namespace Freell
{
    public class Evaluator
    {
        public Evaluation Evaluate(ParseTreeNode node)
        {
            // For now, simply return an Evaluation object to indicate that the code is valid.
            return new Evaluation(true, string.Empty);
        }
    }
}
