# Introduction
Freell stands for Free Learning Language and aims to provide the maximum freedom in the learning process.
This wiki explores the various types in which Freell categorizes the learning experience,
from the most free to the most structured.

## Usage
When a learner designs his own learning proces we talk about a learning architecture.
An education architecture we get when somebody else designs the learning proces of the learner.
In this case the declaration always starts with choosing the type of the root object
to which the learning branches and the learning leaves are connected.
This choice is forced upon the education architect 
to invite thinking carefully about the amount of freedom which is granted to the learner.
Freell can also be used to formulate expert rules to be used by Freelll
when interpreting the architecture.

## Freedom
The level of freedom determines the type of the root object to be used in Freell.
This does not mean that the less free types can not be used as part of that root object.
It tells Freell mainly how to interpret the branches and leaves based on the type of the root object.
For example, if one uses Portfolio as the type of the root object and uses for example a Resource
as a child object, Freell will interpret this Resource in the light of the choice for a
education design in which the learner just learns and afterwards reports his learning
in this case by mentioning the resources it has used.
While if Resource was the type of the root object,
Freell will see the resource as a model, hint or example for the learner.

# Education architecture
## Actor
When a third party starts to design the learning experience, like a teacher or an educational designer, the learner’s freedom is reduced. We refer to this external influencer as an "Education Architect." The type **Actor** is needed.

## Portfolio
When there is an expectation for the learner to showcase what they have learned, we enter the realm of **Portfolio**." This type demands validation from an external party but still allows the learner to explore freely.

## Action
As we move toward result-oriented education, Freell identifies **Action** as the next level. In this type, the learner must demonstrate concrete actions or behaviors to show that learning (getting certain skills, learning goals, competences, attitudes, knowledge ectera) has occurred.

## Unit
If the educational designer organizes and/or divides the learning proces into units,
this further limits the freedom of the learner. Education knows schoolyears or courses for example to
divide the learning proces in time units or certain learning goals.
This division is seldom naturally or suited to the learner's free development.

## Prerequisite
Often a educational organisation will demands certain starting characteristics of the learner
to allow him or her to participate in a certain unit.
Mostly about the skills the learner already has (the previous units).

## Resource
In the context of free learning,
the "Resource" type serves as a suggestion, aid, or hint
that learners can consult for support
or as an example or model for structuring their learning process.
Importantly, the use of a "Resource" is not prescriptive;
it doesn't dictate "how" one must learn,
preserving the philosophy of free learning.
However, the choices made by the education architect in selecting
which resources to include or omit
can indeed influence the learning process and potentially make it less free.
This is particularly true for learners who are naturally more inclined
to follow guidance or established paths.

## Method
The final type before we can no longer term the learning as free is "Method." This comes into play when there are specific methodologies that the learner is expected to follow. Of course Freell will use strategies as well, but will tailor it to the learner in this way for example
* _Entrepreneurial Learning_: Suited for the productive learning style.
* _Investigative Learning_: Suited for the meaning-oriented learning style.
* _Design Learning_: Suited for the application-oriented learning style.
* _Model Learning_: Suited for the reproductive learning style.

# Learning architecture

In a Learning Architecture, having a root object is optional.
This is because the learner has the ultimate freedom to design their own learning path.
In this case, the concept of freedom is at its peak because the learner is in complete control,
thereby eliminating the backward dependencies that are often necessary
when designing education for someone else.

## Backward Dependencies

Freell allows the use of a type known as 'Method.'
While methods usually prescribe a 'how,'
which can seem antithetical to Freell's declarative nature focused on the 'what,'
there are exceptions.
For instance, educational philosophies like Dalton or Montessori could be considered a 'what'
in Freell because choosing such philosophy, profile or organization can be seen as freedom.
For example because learning the method is wished by the learner.
For example to become a Dalton teacher or an entrepreneur.

Such a choice imposes certain prerequisites.
It can be the choice itself that needs to be deliberate.
Or there is a test wheter or not the learner is best suited for the philosophy.
This introduces the first layer of backward dependency.

1. **Method**: Choosing a specific educational philosophy or method often comes with its own set of beliefs or requirements, leading us to the 'Prerequisite' type.
   
2. **Prerequisite**: Any prerequisite naturally implies the need for an organizational unit where these prerequisites are relevant. Thus, this type introduces the 'Unit' type.

3. **Unit**: A unit, being an organizational structure, implies that actions are organized in a certain manner—either sequentially over time or based on interdependencies. This necessitates the 'Action' type.

4. **Action**: In education, actions must be observable. Invisible actions like thought processes or non-implemented ideas have no value in an educational context. Therefore, observable actions lead us to the 'Portfolio' type, where these actions can be showcased.

5. **Portfolio**: The very act of showcasing actions implies the presence of an audience or evaluator even if in the case of a demand for reflection by the learner himself. The demand has no use if not specified who demands it. This introduces the 'Actor' type to specify for whom the portfolio is intended.

6. **Actor**: Besides the Portfolio dependencie, every educational architecture means someone design the learning of someone else. So there is always an "Actor."

By following this chain of backward dependencies, we can see that each type in a Freell Education Architecture triggers the necessity for other types. Each implication is not arbitrary but based on the logical progression of organizing and showcasing educational actions and activities.


In Freell, the types and their interdependencies are carefully structured to accommodate both the freedom of the learner and the necessities of educational design. These backward dependencies are not just a structural requirement but are deeply rooted in the philosophy of what Freell aims to achieve in the realm of education.

# HeDude

To instruct the AI we have some extra keywords and types.

# Conclusion
Freell aims to categorize the learning experience based on the level of freedom afforded to the learner. From designing one's own learning journey to following specific methods, Freell seeks to offer a comprehensive understanding of how freedom in learning is structured.

