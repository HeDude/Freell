from enum import Enum

class OrganizationalForm(Enum):
    INDIVIDUAL = (1, 1)
    DUO = (2, 2)
    TRIAD = (3, 3)
    SMALL_GROUP = (4, 6)
    TEAM = (7, 15)
    GROUP_OF_GROUPS = (4x4, 6x6)
    COHORT = (16, None)

    def __init__(self, min_students, max_students):
        self.min_students = min_students
        self.max_students = max_students

# Accessing Enum members:
print("DUO form requires minimum", OrganizationalForm.DUO.min_students, "and maximum", OrganizationalForm.DUO.max_students, "students.")
