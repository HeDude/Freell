# Create the self-regulation method
self_regulation_method = Method(level="Strategy", name="Self-Regulation")

# Create sub-methods for Self-Regulation
entrepreneurial_learning = Method(level="Tactic", name="Entrepreneurial Learning")
challenge = Method(level="Tactic", name="Challenge")
eduscrum = Method(level="Tactic", name="EduScrum")

# Add the sub-methods to the self-regulation method
self_regulation_method.add_sub_method(entrepreneurial_learning)
self_regulation_method.add_sub_method(challenge)
self_regulation_method.add_sub_method(eduscrum)

# Define sub-methods for Entrepreneurial Learning
sub_methods_el = [
    Method(level="Operational", name=name) for name in
    ["Collaboration", "Differentiation", "Creative Exploration", "Active Learning", "Open Communication", "Observation and Analysis"]
]
for sub_method in sub_methods_el:
    entrepreneurial_learning.add_sub_method(sub_method)

# Define sub-methods for Challenge
sub_methods_c = [
    Method(level="Operational", name=name) for name in
    ["Self-Devised Challenges", "Task-Driven Challenges", "Adaptive Approach", "Challenging Elements", "Feedback and Coaching", "Intrinsic Motivation", "Collaboration"]
]
for sub_method in sub_methods_c:
    challenge.add_sub_method(sub_method)

# Define sub-methods for EduScrum
sub_methods_es = [
    Method(level="Operational", name=name) for name in
    ["Hackathon", "Scrum", "Own Work", "Sprints"]
]
for sub_method in sub_methods_es:
    eduscrum.add_sub_method(sub_method)




