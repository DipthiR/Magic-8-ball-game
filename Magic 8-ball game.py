import random

# List of possible Magic 8-Ball answers
answers = [
    "Yes, definitely",
    "It is certain",
    "Without a doubt",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Don't count on it",
    "My sources say no",
    "Very doubtful"
]

print("🎱 Welcome to the Magic 8-Ball Game! 🎱")

# Ask user for a question
question = input("Ask a yes/no question: ")

# Pick a random answer
response = random.choice(answers)

print("\nThe Magic 8-Ball says: " + response)
