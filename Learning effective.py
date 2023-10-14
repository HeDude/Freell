class LearningMethod:
    def __init__(self, real_world, collaborative, reflective, doing, journey):
        self.real_world = real_world
        self.collaborative = collaborative
        self.reflective = reflective
        self.doing = doing
        self.journey = journey

def is_effective_learning(method):
    if method.real_world and method.collaborative and method.reflective:
        if (method.doing and not method.journey) or (method.journey and not method.doing):
            return True
    return False

# Create an instance of LearningMethod for entrepreneurial learning
entrepreneurial_learning = LearningMethod(True, True, True, True, False)

# Create an instance of LearningMethod for playful learning
playful_learning = LearningMethod(True, True, True, False, True)

# Check if entrepreneurial learning is effective
print(is_effective_learning(entrepreneurial_learning))  # Outputs: True

# Check if playful learning is effective
print(is_effective_learning(playful_learning))  # Outputs: True
