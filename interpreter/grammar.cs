using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Irony.Parsing;

namespace Freell
{
    // Define the grammar of the Freell language
    // The grammar starts with the very simple language of the form: identifier = new type;
    // where "type" can be any of the defined terminal types like "Action," "Actor," etc.
    public class FreellGrammar : Grammar
    {
        public FreellGrammar() : base(false)  // false for case sensitivity
        {
            // Define Terminals
            var identifier = new IdentifierTerminal("identifier");
            var action = ToTerm("Action");
            var actor = ToTerm("Actor");
            var method = ToTerm("Method");
            var prerequisite = ToTerm("Prerequisite");
            var resource = ToTerm("Resource");
            var skill = ToTerm("Skill");
            var unit = ToTerm("Unit");
            var assignment = ToTerm("=");
            var terminator = ToTerm(";");

            // Define Non-terminals
            var statement = new NonTerminal("statement");
            var type = new NonTerminal("type");
            var declaration = new NonTerminal("declaration");

            // Define Rules
            type.Rule = action | actor | method | prerequisite | resource | skill | unit;
            declaration.Rule = identifier + assignment + "new" + type + terminator;
            statement.Rule = declaration;

            // Set the root non-terminal
            this.Root = statement;
        }
    }
}
