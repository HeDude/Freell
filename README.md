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
which if not meticulously managed, can spiral into spaghetti code—a tangled, hard-to-follow, and maintain codebase.
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
thereby validating Freell’s practicality in real-world educational settings.

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
       When a participant joins, we'll add them to the lesson, and when they leave, we'll remove them from the lesson.
       Does that sound good?
Human: Yes, that's what I am looking for.
```
### Prompting
```
Create Unit called lesson.
Create Actor called person.
Add person to lesson.
Remove person from lesson.
```
### Freell
```
lesson = new Unit;
person = new Actor;
lesson += person;
lesson -= person;
```