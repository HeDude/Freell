from enum import Enum

class LearningGoalType(Enum):
    class CognitiveAndMetacognitive(Enum):
        KNOWLEDGE = 1
        UNDERSTANDING = 2
        APPLICATION = 3
        ANALYSIS = 4
        REFLECTION = 5

    class Affective(Enum):
        ATTENTION = 1
        INTEREST = 2
        APPRECIATION = 3
        EMPATHY = 4
        ATTITUDE = 5

    class Social(Enum):
        CONTACT = 1
        AGREEMENT = 2
        RELATIONSHIP = 3
        COOPERATION = 4
        TEAM = 5

    class Motor(Enum):
        IMAGINATION = 1
        IMITATION = 2
        AUTOMATION = 3
        DEMONSTRATION = 4
        VIRTUOSITY = 5

# Accessing Enum members and their levels:
for goal_type in LearningGoalType:
    print(goal_type)
    for level in goal_type.value:
        print('-', level)
