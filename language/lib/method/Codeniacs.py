import sys
sys.path.append('..')  # Adds the parent directory to the Python module path

from Method import Method
from Unit import Unit

# Create the Study unit
study = Unit(type="Study", name="Education Technology")

# Define course names for each stage
course_names = {
    "Expert": [
        "Basic Principles of Ethical Hacking in Education and ICT",
        "Agile Methodology in Educational Technology Projects",
        "Creativity and Innovation in Technology and Education",
        "Collaborative Problem Solving and Communication",
        "Specialization and Teamwork",
        "Evaluation of Hacks for Happiness Improvement and Technical Competence"
    ],
    "Base": [
        "Game", "Website", "App", "Embedded System", "IT-company"
    ],
    "Specialism": [
        "AI", "Blockchain", "Business Intelligence", "Computer-aided design", "Cybersecurity",
        "PHP", "Python", "Robotics", "SCSS", "Typescript", "Unity", "XHTML"
    ]
}

# Create and add Stage units to Study
for stage_name, courses in course_names.items():
    stage = Unit(type="Stage", name=f"Education Technology {stage_name}")
    study.add_sub_unit(stage)
    
    # Create and add Course units to Stage
    for course_name in courses:
        course = Unit(type="Course", name=course_name, level=stage_name)
        stage.add_sub_unit(course)

# Define subcourse names for each course in Specialism stage
specialism_subcourses = {
    "AI": ["Logic", "Expert System", "Optimization", "Statistics", "Neural Networks", "Machine Learning"],
    "Blockchain": ["Cryptography", "Networks", "Data Structures", "Ledger", "Blockchain"],
    "Business Intelligence": ["Search Engine Optimization", "Google Analytics", "Spreadsheet", "Luna", "Datamining"],
    "Computer-aided design": ["Design", "Image Processing", "Vector Drawing", "Video Editing", "Computer-aided Design"],
    "Cybersecurity": ["Hacking", "Ransomware", "Social Engineering", "Denial of Service Attacks", "Countermeasures"],
    "PHP": ["Fork", "Plugin", "Skin", "Module", "Program"],
    "Python": ["Fork", "Plugin", "Skin", "Module", "Program"],
    "Robotics": ["Bots", "Robot Control", "Sensing", "Kinematics", "Robot Architecture"],
    "SCSS": ["Syntax", "Effects", "Grid", "Responsive", "SASS"],
    "Typescript": ["Javascript", "Functions", "Objects", "Frameworks", "Typescript"],
    "Unity": ["Scratch", "Blockly", "Superpowers", "GoDot", "Unity"],
    "XHTML": ["HTML", "Forms", "Media", "Api", "XHTML"]
}

# Locate the Specialism stage
specialism_stage = None
for sub_unit in study.sub_units:
    if sub_unit.name == "Education Technology Specialism":
        specialism_stage = sub_unit
        break

# Add subcourses to courses in Specialism stage
for course in specialism_stage.sub_units:
    course_name = course.name
    if course_name in specialism_subcourses:
        for subcourse_name in specialism_subcourses[course_name]:
            subcourse = Unit(type="Subcourse", name=subcourse_name, level="Specialism")
            course.add_sub_unit(subcourse)
            
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





