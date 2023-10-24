using System.Collections.Generic;

namespace Freell
{
    public class Response
    {
        public Dictionary<string, string> GrammarPrompts { get; private set; }

        public Response()
        {
            GrammarPrompts = new Dictionary<string, string>
            {
                { "productStatement",     "State the product by: 'This [product] is called [Name]'" },
                { "rootStatement",        "State the root by: 'The root is [a/an] [type] called [Name]'" },
                { "identifierDefinition", "For identifier use letters, numbers, hyphens, and underscores" },
                { "nameDefinition",       "For [Name] use a unique identifier" },
                { "productDefinition",    "For [product] use 'education architecture', 'expert rule', or 'learning architecture'" },
                { "typeDefinition",       "For [type] use 'action', 'actor', 'method', 'portfolio', 'prerequisite', 'resource', or 'unit'" },
            };
        }

        public string Get(string prompt)
        {
            if (GrammarPrompts.TryGetValue(prompt, out string value))
            {
                return value;
            }
            return "Unknown prompt key";
        }
    }
}

