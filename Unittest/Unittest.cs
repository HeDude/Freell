using Microsoft.VisualStudio.TestTools.UnitTesting;
using Freell;

namespace Freell.Tests
{
    [TestClass]
    public class FreellEndToEndTests
    {
        [TestMethod]
        public void TestEducationArchitectureExample()
        {
            // Arrange
            Interpreter interpreter = new Interpreter();
            string exampleCode = "This education architecture is called Codeniacs. The root is a unit called Course.";

            // Act
            bool result = interpreter.Interpret(exampleCode);

            // Assert
            Assert.IsTrue(result);
        }

        [TestMethod]
        public void TestDifferentTypes()
        {
            // Arrange
            Interpreter interpreter = new Interpreter();
            string[] types = { "Action", "Actor", "Method", "Portfolio", "Prerequisite", "Resource", "Unit" };
            string article;

            // Act & Assert
            foreach (string type in types)
            {
                article = (type == "Action" || type == "Actor") ? "an" : "a";  // Use "an" for "Action" and "Actor"
                string code = $"This education architecture is called Codeniacs. The root is {article} {type.ToLower()} called Example.";
                Assert.IsTrue(interpreter.Interpret(code), $"Failed for type {type}");
            }
        }

        [TestMethod]
        public void TestNameCharacterLimits()
        {
            // Arrange
            Interpreter interpreter = new Interpreter();
            string[] validNames = { "NameWithNumbers123", "Name-With-Hyphen", "Name_With_Underscore" };
            string[] invalidNames = { "Name.With.Period" };  // Names that should not be allowed

            // Act & Assert for valid names
            foreach (string name in validNames)
            {
                string code = $"This education architecture is called {name}. The root is a unit called Course.";
                Assert.IsTrue(interpreter.Interpret(code), $"Failed for name {name}");
            }

            // Act & Assert for invalid names
            foreach (string name in invalidNames)
            {
                string code = $"This education architecture is called {name}. The root is a unit called Course.";
                Assert.IsFalse(interpreter.Interpret(code), $"Incorrectly passed for invalid name {name}");
            }
        }

    }
}
