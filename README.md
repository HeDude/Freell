> For real
# Free Learning Language

## Free Learning

**Freell** (pronounced as **'for real'**) is designed with a mission to promote free learning.
It adheres to scientifically substantiated principles
to create an effective, intuitive, and user-centric learning environment.

Freell's primary mission is to make learning as free as possible without compromising effectiveness.
Its declarative syntax enables education architects and self-learners
to focus on what they wish to achieve,
leaving the 'how' to the language itself.

## Turing-Proof Prompting
Freell uniquely combines the capabilities of an AI prompting language
with the characteristics of a Turing-proof programming language.
This powerful combination ensures that learning declarations are not just intuitive
but also robust and versatile.

## Example
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

For more technical details and in-depth examples, please refer to the [Wiki](https://github.com/HeDude/Freell/wiki).

