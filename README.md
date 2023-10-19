> For real
# Free learning language

**Freell** (pronounced as **'for real'**) is a language that describes learning in a way that expert rules can be understand without errors by AI.

Education designers or researchers can formulate their ideas or findings in a intuitive and natural way that can be implemented in programs.

## Free learning
**Freell**  is designed to promote free learning, adhering strictly to scientifically substantiated reasons for any form of imposition.
Therefore, it doesn't arbitrarily structure learning units unless strictly necessary. 
For instance, the ordering of sub-units within a unit is only justified if it's crucial for the learning process.
This is primarily the case when certain skills can only be acquired after mastering prerequisite skills, ensuring a logical and necessary progression in the learning journey.

Freell (the educational language) seeks to relieve both education architects (those orchestrating learning for others)
and learning architects (those structuring their own learning)
from the obligation of mastering effective learning strategies.
The expert rules embedded in Freell ensure the incorporation of as much freedom in the learning process as possible
without compromising effectiveness.

Scientific research affirms that more freedom in learning enables better tailoring, 
thus enhancing effectiveness.
Through Freell, architects are alleviated from the tedious, time-consuming task of structuring learning beyond necessity. 
The language, and the tools emanating from it, handle this while adhering to the core mission:
promoting as much freedom in learning as possible,
as long as it serves or does not impair effectiveness.

## Declarative programming
In the endeavor of developing a proprietary language for learning processes,
the benefits of declarative programming have been underscored.
A notable advantage of this paradigm is the brevity it brings to code, 
provided the compiler or engine is adept at optimally interpreting the declarations.
This brevity is particularly beneficial when crafting a domain-specific language (DSL),
offering a more intuitive, readable articulation of domain logic.

Conversely, Object-Oriented Programming (OOP) often entails intricate relationships and interactions among objects,
which if not meticulously managed, can spiral into spaghetti code�a tangled, hard-to-follow, and maintain codebase.
This complexity in OOP emanates from the inherent mutability and extensive inter-object relationships, 
posing a risk of obfuscating code structure and logic, 
thereby making maintenance a challenging endeavor.

Given the mission of Freell (Free Learning Language),
the adoption of declarative programming is a harmonious fit.
It embodies simplicity, eliminating unnecessary frills
and enabling users to describe learning with ease.
This straightforward approach empowers users
to focus on articulating what they wish to achieve in terms of learning,
leaving the how to the compiler.
The intelligent compiler of Freell then translates these declarations into tangible outputs
such as learngame building blocks, xAPI storage, Moodle courses, API responses, etc., 
with an underlying emphasis on facilitating free learning.
This process encapsulates the effectiveness of learning,
embedding as much of it as possible within the system,
thereby alleviating the users from the burden of overthinking the technical intricacies.
The end goal is to streamline the learning design process,
making it intuitive, effective, and user-centric,
aligning perfectly with the ethos of free, unencumbered learning that Freell aspires to promote.

Indeed, while the Freell language is designed to be declarative for user simplicity and focus on the learning objectives,
the underlying compiler that translates Freell's declarations
into actionable outputs benefits from an Object-Oriented Programming (OOP) architecture.
This OOP foundation in the compiler allows for a structured, organized approach
to handling the diverse and potentially complex translations into various outputs
like game elements, xAPI storage, Moodle courses, or API responses.
The encapsulation, inheritance, and polymorphism principles of OOP provide a robust framework
to manage, extend, and interact with the different translation modules efficiently.
This object-oriented nature of the compiler ensures that while users enjoy a straightforward, declarative interface,
the engine that powers Freell's translations is well-organized, extensible, and capable of handling the intricacies
involved in mapping learning declarations to a multitude of educational and interactive outputs.

## Interpreter Design

Based on the objectives of clarity, developability, and testability,
the decision has been made to build an interpreter for Freell.
This interpreter will not only translate the declarative Freell language into actionable outputs
but also provide insightful explanations to the user on how translations are done.
This interactive feature aims to engage users in understanding and learning about free learning architectures.

Considering the future integration with learngame development in Unity,
C# has been chosen as the programming language for building the interpreter.
Among the available tools,
the Irony .NET Compiler Construction Kit stands out for its simplicity
and suitability for this project.
Irony will aid in defining the grammar of Freell
and constructing an interpreter in a modular structure.

This modular structure is pivotal for ensuring that different parts of the codebase can be developed, 
tested, and updated independently.

A Test-Driven Development (TDD) approach will be employed
to ensure robustness and correctness of the interpreter from the outset.
Example dialogues and education architectures will serve as starting points for developing test cases.
These tests will guide the development process,
ensuring that the interpreter not only meets its functional requirements
but also serves as a learning tool for users exploring the realms of free learning architectures.

With this structure, the Freell project endeavors to provide a clear, developable, and testable platform
that not only meets its technical goals
but also fosters an environment of learning and exploration for its users.

## Testing

The validation of **Freell** hinges on three pivotal axes: Turing Completeness, conversion to recognized educational standards, and practical applicability in open ELOs like Moodle.

### Turing Completeness:

A formal proof will be conducted to ascertain Turing completeness, 
establishing Freell's capability to encapsulate complex computational logic akin to a Turing machine.

### Standard Conversion:

A set of conversion modules will be developed to translate Freell syntax into the formats 
prescribed by the Experience API (xAPI), cmi5 specification, 
and Sharable Content Object Reference Model (SCORM).
The accuracy and integrity of the conversion process will be rigorously verified 
against predefined benchmarks.

### Practical Applicability and Acceptance Testing:

Freell will be employed to design courses within open ELO environments like Moodle. 
User acceptance tests will gauge the satisfaction and efficacy from an end-user perspective. 
Concurrently, the correct prompting utilization by AI will be assessed 
through a series of specified tests, ensuring an accurate reflection of the Freell syntax 
in promoting learning objectives.

### AI Interaction Testing:

The interaction between Freell and AI's will be thoroughly examined 
to ensure that learning prompting is accurately executed, 
thereby validating Freell�s practicality in real-world educational settings.

We will engage artificial intelligence to translate various forms of learning or education descriptions into Freell, 
and subsequently reconstruct them from Freell definitions
to ascertain if the essence of learning or education remains intact. 
This challenge aims to rigorously test the semantic integrity and adaptability of Freell
in capturing and translating the core principles of learning and education across different descriptive frameworks.

This multi-faceted testing approach aims to furnish a comprehensive validation framework, 
ensuring that Freell not only adheres to theoretical computational principles 
but also seamlessly integrates with existing educational standards and platforms, 
fostering a conducive and effective learning environment.

##  Example
### Natural dialogue
```
Human: I want to build something in learning or teaching where you can add or remove a participant.
AI:    Understood. So, we're looking at a scenario where there's a learning or teaching environment, 
       and participants can join or leave, correct?
Human: Yes, exactly!
AI:    Great. Let's represent the learning or teaching environment as "lesson" and a participant as "person". 
       We'll describe the desired state of the lesson, whether a person is part of it or not.
       Does that sound good?
Human: Yes, that's what I am looking for.
```
### Prompting
```
Specify the desired state of the lesson with or without person.
```
### Freell
```
lesson = new Unit;
person = new Actor;
lesson.participants = {person};  // Desired state with person
or
lesson.participants = {};  // Desired state without person
```
### Prompting output as feedback by Freell
```
If `lesson.participants = {};` is provided,

Feedback:
The unit `lesson` exists but is now empty of participants.
```
### Respons prompting
```
The unit `lesson` exists but is now empty of participants.
```
### Respons Natural dialogue
```
AI:   The learning unit, as we call it, lesson exists, but it has no participants at the moment.
Is that what you want?
Human: No! I do not want a lesson without a person. A lesson without any person should not be allowed!
AI:    I understand your concern. A lesson with no participants doesn't serve its purpose. We can ensure that 
       there is at least one participant in a lesson at all times. Shall we proceed with this adjustment?
Human: Yes, please make that adjustment.
```
### New prompting
```
Ensure at least one participant is present in the lesson at all times.
```
### New Freell declaration
```
lesson = new Unit;
person = new Actor;
lesson.participants = {person};  // Desired state with person
// Validating the presence of at least one participant
lesson.validate = function() {
    return this.participants.length > 0;
};
If `lesson.participants = {};` is attempted,
Feedback:
Validation Failed: A lesson must have at least one participant.
```
### New respons prompting
```
Validation Failed: A lesson must have at least one participant.
```
### New Natural dialogue
```
AI: The validation of a lesson now failed because a lesson must have at least one participant. 
Would you like to add a participant or choose a different action?
```