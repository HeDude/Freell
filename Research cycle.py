class ResearchCycle(Enum):
    INTRODUCTION = ('Introduction', ['Wonder/Astonishment', 'Explore/Research Question'])
    CORE = ('Core', ['Research Plan', 'Execution'])
    CLOSING = ('Closing', ['Conclusion', 'Reflection'])

    def __init__(self, stage, activities):
        self.stage = stage
        self.activities = activities


# Sample usage:
for cycle in ResearchCycle:
    print(cycle.stage)
    for activity in cycle.activities:
        print('-', activity)

# Output:
# Introduction
# - Wonder/Astonishment
# - Explore/Research Question
# Core
# - Research Plan
# - Execution
# Closing
# - Conclusion
# - Reflection
