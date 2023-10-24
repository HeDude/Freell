using System.Collections.Generic;
using Irony.Parsing;

namespace Freell
{
    public class Evaluator
    {
        public Dictionary<string, string> GrammarPrompts = new Dictionary<string, string>
        {
            { "productStatement",     "State the product by: 'This [product] is called [Name]'." },
            { "rootStatement",        "State the root by: 'The root is [a/an] [type] called [Name]'." },
            { "identifierDefinition", "For identifier use letters, numbers, hyphens, and underscores." },
            { "nameDefinition",       "For [Name] use a unique identifier." },
            { "productDefinition",    "For [product] use 'education architecture', 'expert rule', or 'learning architecture'." },
            { "typeDefinition",       "For [type] use 'action', 'actor', 'method', 'portfolio', 'prerequisite', 'resource', or 'unit'." },
        };

        public object? Evaluate(ParseTreeNode node)
        {
            // For now, simply return true to indicate that the code is valid.
            return true;
        }
    }
}
