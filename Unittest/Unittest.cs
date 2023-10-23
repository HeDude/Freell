using System;
using Freell;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace FreellTests
{
    [TestClass]
    public class FreellEndToEndTests
    {
        [TestMethod]
        public void TestEducationArchitectureExample()
        {
            // Arrange
            string exampleCode = "This education architecture is called Codeniacs. The root is a unit called Course.";
            Interpreter interpreterInstance = new Interpreter();

            // Act
            object? result = interpreterInstance.Interpret(exampleCode);

            // Assert
            Assert.IsNotNull(result);
            bool isValidCode = (bool)result!;
            Assert.IsTrue(isValidCode);
        }
    }
}
