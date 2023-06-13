SET Learning_Approach   = "Playful"
SET Learning_Method     = "Learning through Discovery"
SET Play_Responsibility = "Self-Directed"
SET Play_Context        = "Real-World"
SET Play_Collaboration  = "Collaborative"
SET Play_Reflection     = "Reflective"
SET Play_Perspective    = "Journey"

def is_playful_method(method):
    required_characteristics = {
        "playful_learning": True,
        "learning_through_discovery": True,
        "self_directed_play": True,
        "play_in_context": True,
        "collaborative_play": True,
        "reflective_play": True,
        "play_as_journey": True,
        "joy_and_enjoyment": True,
        "creativity": True,
        "flexibility": True,
        "active_engagement": True,
        "social_interaction": True,
        "imagination": True
    }

    for characteristic, required in required_characteristics.items():
        if characteristic not in method or method[characteristic] != required:
            return False

    return True
