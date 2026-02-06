import random

ideas = [
    "A small rabbit teaches a lion a lesson",
    "A brave cat saves the forest",
    "A greedy fox learns a hard truth",
    "A tiny bird does the impossible",
    "A lazy bear changes his life"
]

idea = random.choice(ideas)

script = f"""
Once upon a time, {idea}.
In the end, everyone learned an important lesson.
"""

print("Generated Script:")
print(script)
