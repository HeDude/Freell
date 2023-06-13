SET Learning_Approach       = "Entrepreneurial"
SET Learning_Method         = "Learning by Doing"
SET Learning_Responsibility = "Self-Directed"
SET Learning_Context        = "Real-World"
SET Learning_Collaboration  = "Collaborative"
SET Learning_Reflection     = "Reflective"
SET Learning_Perspective    = "Journey"

def is_entrepreneurial_method(method):
    required_characteristics = {
        "problem_solving_focus": True,
        "real_world_application": True,
        "risk_taking": True,
        "self_directed_learning": True,
        "collaboration": True,
        "innovation": True
    }

    for characteristic, required in required_characteristics.items():
        if characteristic not in method or method[characteristic] != required:
            return False

    return True

# Example usage:
method = {
    "problem_solving_focus": True,
    "real_world_application": True,
    "risk_taking": True,
    "self_directed_learning": True,
    "collaboration": True,
    "innovation": True
}

print(is_entrepreneurial_method(method))  # Outputs: True
