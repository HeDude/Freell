import random

def generate_question(prompt):
    """Generates a question based on the provided prompt for further qualification."""
    qualifiers = ["Can you tell me if you", "Would you say you", "Do you generally", "Do you often", "How often do you"]
    qualifier = random.choice(qualifiers)
    return f"{qualifier} {prompt.lower()}?"

def interpret_response(response):
    """Interprets the user's response and maps it to one of the predefined levels."""
    # Here you would use AI (or simple keyword matching) to interpret the response
    # For this example, I am using keyword matching as a placeholder
    if "never" in response.lower():
        return "Almost never"
    elif "rarely" in response.lower():
        return "Seldom"
    elif "sometimes" in response.lower():
        return "Sometimes"
    elif "often" in response.lower():
        return "Often"
    else:
        return "Almost always"

# Survey questions, organized in a JSON-like structure
survey_questions = {
    "questions": [
        # Relevance
        {"aspect": "Relevance", "prompt": "I prefer that my learning focuses on issues that interest me."},
        {"aspect": "Relevance", "prompt": "I found that my learning focuses on issues that interest me."},
        # Reflective thinking
        {"aspect": "Reflective thinking", "prompt": "I prefer that I think critically about my own ideas."},
        {"aspect": "Reflective thinking", "prompt": "I found that I think critically about my own ideas."},
        {"aspect": "Reflective thinking", "prompt": "I prefer that I think critically about other students' ideas."},
        {"aspect": "Reflective thinking", "prompt": "I found that I think critically about other students' ideas."},
        {"aspect": "Reflective thinking", "prompt": "I prefer that I think critically about ideas in the readings."},
        {"aspect": "Reflective thinking", "prompt": "I found that I think critically about ideas in the readings."},
        # Interactivity
        {"aspect": "Interactivity", "prompt": "I prefer that I explain my ideas to other students."},
        {"aspect": "Interactivity", "prompt": "I found that I explain my ideas to other students."},
        {"aspect": "Interactivity", "prompt": "I prefer that I ask other students to explain their ideas."},
        {"aspect": "Interactivity", "prompt": "I found that I ask other students to explain their ideas."},
        {"aspect": "Interactivity", "prompt": "I prefer that other students ask me to explain my ideas."},
        {"aspect": "Interactivity", "prompt": "I found that other students ask me to explain my ideas."},
        {"aspect": "Interactivity", "prompt": "I prefer that other students respond to my ideas."},
        {"aspect": "Interactivity", "prompt": "I found that other students respond to my ideas."},
        # Tutor support
        {"aspect": "Tutor support", "prompt": "I prefer that the tutor stimulates my thinking."},
        {"aspect": "Tutor support", "prompt": "I found that the tutor stimulates my thinking."},
        {"aspect": "Tutor support", "prompt": "I prefer that the tutor encourages me to participate."},
        {"aspect": "Tutor support", "prompt": "I found that the tutor encourages me to participate."},
        {"aspect": "Tutor support", "prompt": "I prefer that the tutor models good discourse."},
        {"aspect": "Tutor support", "prompt": "I found that the tutor models good discourse."},
        {"aspect": "Tutor support", "prompt": "I prefer that the tutor models critical self-reflection."},
        {"aspect": "Tutor support", "prompt": "I found that the tutor models critical self-reflection."},
        # Peer support
        {"aspect": "Peer support", "prompt": "I prefer that other students encourage my participation."},
        {"aspect": "Peer support", "prompt": "I found that other students encourage my participation."},
        {"aspect": "Peer support", "prompt": "I prefer that other students praise my contribution."},
        {"aspect": "Peer support", "prompt": "I found that other students praise my contribution."},
        {"aspect": "Peer support", "prompt": "I prefer that other students value my contribution."},
        {"aspect": "Peer support", "prompt": "I found that other students value my contribution."},
        {"aspect": "Peer support", "prompt": "I prefer that other students empathise with my struggle to learn."},
        {"aspect": "Peer support", "prompt": "I found that other students empathise with my struggle to learn."},
        # Interpretation
        {"aspect": "Interpretation", "prompt": "I prefer that I make good sense of other students' messages."},
        {"aspect": "Interpretation", "prompt": "I found that I make good sense of other students' messages."},
        {"aspect": "Interpretation", "prompt": "I prefer that other students make good sense of my messages."},
        {"aspect": "Interpretation", "prompt": "I found that other students make good sense of my messages."},
        {"aspect": "Interpretation", "prompt": "I prefer that I make good sense of the tutor's messages."},
        {"aspect": "Interpretation", "prompt": "I found that I make good sense of the tutor's messages."},
        {"aspect": "Interpretation", "prompt": "I prefer that the tutor makes good sense of my messages."},
        {"aspect": "Interpretation", "prompt": "I found that the tutor makes good sense of my messages."},
        # Others
        {"aspect": "Others", "prompt": "How long did this survey take you to complete?"},
        {"aspect": "Others", "prompt": "Do you have any other comments?"}
    ]
}

# Initialize an empty dictionary to store responses
responses = {}

# Iterate through the survey questions to ask them and collect responses
for question in survey_questions["questions"]:
    aspect = question["aspect"]
    prompt = question["prompt"]
    if aspect not in responses:
        responses[aspect] = {}
    
    # Generate a question using AI
    generated_question = generate_question(prompt)
    
    # Simulate user's response to generated question
    # In real life, you would collect this response from the user
    user_response = "I sometimes focus on what interests me."  # Replace this with actual user input
    
    # Interpret the user's response using AI
    interpreted_response = interpret_response(user_response)
    
    # Store the interpreted response
    responses[aspect][prompt] = interpreted_response

# Print the collected responses for review
print("\nCollected Responses:")
print(responses)