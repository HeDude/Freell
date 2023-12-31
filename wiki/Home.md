# Free learning language

**Freell** (pronounced as **'for real'**) is a language
that describes [free learning](https://github.com/HeDude/Freell/wiki/Free-learning)
in a way that corresponding expert rules can be understand without errors by AI.

Education designers or researchers can formulate their ideas or findings
in a intuitive and natural way that can be implemented in programs
and stimulates free learning.

## Freedom
The overarching mission of Freell is
to foster freedom in the learning process.
To achieve this, the language focuses on specifying the "what" of learning
while deliberately avoiding prescriptive directions on "how" to achieve it.
This philosophy manifests in the language's design choices,
which are meticulously aligned to support the mission of encouraging free, effective learning.
The language can be used to [convert](https://github.com/HeDude/Freell/wiki/Conversion) existing designs into architectures that allow more freedom in learning.

### Root
One of the unique design features of Freell is the enforced selection of a single root object.
Unlike in languages such as C++ where the main function serves as the entry point,
Freell mandates the choice of a root object
to serve as the foundational element of the learning structure.
This is not a mere technical requirement
but a strategic decision aimed at guiding the conscious choice
of the degree of freedom within the learning environment.

### Type
The root object acts as the cornerstone,
setting the overarching framework within which all other learning objects or units are nested.
The [type](https://github.com/HeDude/Freell/wiki/Types) of this root object
is more than a structural choice;
it is a philosophical one.
It effectively dictates the extent to which freedom is permitted or constrained
in the learning process.

By compelling the user to make a deliberate choice for the type of this root object,
Freell ensures that the resulting learning experience is
not just a random assembly of elements but a carefully orchestrated structure.
This structure is inherently aligned with the mission of Freell:
to provide as much freedom in learning as is effectively possible,
guided by the learning expertrules in the language itself.

### Method
One noteworthy exception in the type system is the inclusion of the "Method" type.
This is an acknowledgment of educational methods such as Montessori or Entrepreneurial Education,
which often define the "what" of a school organization's profile.
Even so, the language remains predominantly declarative to avoid dictating the "how" of learning.

## Self-Explanatory
Understanding that clarity is essential for promoting freedom,
Freell is designed to be self-explanatory.
It employs an [interpreter](https://github.com/HeDude/Freell/wiki/Interpreter) 
to transparently translate [declarations](https://github.com/HeDude/Freell/wiki/Declarative)
into actionable outcomes.
The development process is [test-driven](https://github.com/HeDude/Freell/wiki/Testing)
and leverages natural dialogues and visual designs as [examples](https://github.com/HeDude/Freell/wiki/Example). 
This approach not only makes the language intuitive
but also ensures that it resonates with as many people as possible,
regardless of their technical expertise.

## Natural
Reell is designed to mimic natural language in the form of [prompting](https://github.com/HeDude/Freell/wiki/Prompting) an AI for ease of use and readability.
A valid statement in the Freell language has the following general rules;
* **Case Sensitivity**: Freell is case-sensitive, 
  which means this is not equivalent to This or tHiS.
* **Whitespace**: Whitespace (spaces, tabs, and newlines) is generally ignored, except as it separates elements of the syntax.
* **End of Statement**: Every statement must end with a period (.). This mimics the natural language convention of ending sentences with a period.

**Identifiers**: Identifiers (Names) are used to name education architectures, units, actions, and other elements. The rules for valid identifiers are:
* May contain alphabets (either uppercase or lowercase).
* May contain numbers.
* May contain underscores (_).
* May contain hyphens (-).

Examples of Valid Identifiers
* Codeniacs
* Name-With-Hyphen
* Name_With_Underscore
* NameWithNumbers123

Examples of Invalid Identifiers
* Name.With.Period (Periods are reserved for the end of statements)

For more details see:
* [Conversion](https://github.com/HeDude/Freell/wiki/Conversion)
* [Delarative](https://github.com/HeDude/Freell/wiki/Declarative)
* [Example](https://github.com/HeDude/Freell/wiki/Example)
* [Free learning](https://github.com/HeDude/Freell/wiki/Free-learning)
* [Interpreter](https://github.com/HeDude/Freell/wiki/Interpreter)
* [Prompting](https://github.com/HeDude/Freell/wiki/Prompting)
* [Testing](https://github.com/HeDude/Freell/wiki/Testing)
* [Types](https://github.com/HeDude/Freell/wiki/Types)