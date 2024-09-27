import random

class SimpleAI:
    def __init__(self):
        self.responses = [
            "That's interesting! Tell me more.",
            "I'm not sure I understand. Could you explain further?",
            "That's a great point!",
            "I'm still learning about that topic.",
            "What do you think about that?",
        ]

    def respond(self, user_input):
        return random.choice(self.responses)

# Create an instance of the AI
ai = SimpleAI()

# Simple interaction loop
print("Simple AI: Hello! I'm a basic AI. Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Simple AI: Goodbye!")
        break
    response = ai.respond(user_input)
    print(f"Simple AI: {response}")
