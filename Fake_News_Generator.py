import random

# Subjects
subjects = ["Sports", "Technology", "Politics", "Science", "Entertainment"]

# Fake headline components per subject
actions = {
    "Sports": ["wins championship", "retires suddenly", "buys a new stadium", "signs record-breaking contract"],
    "Technology": ["launches AI robot", "invents invisible phone", "hacks global network", "releases flying car"],
    "Politics": ["declares new law", "bans coffee", "builds wall around city", "runs for president again"],
    "Science": ["discovers new element", "finds life on Mars", "proves time travel possible", "creates talking plants"],
    "Entertainment": ["releases secret album", "marries alien", "joins reality show", "becomes superhero"]
}

locations = ["in New York", "in London", "in Tokyo", "worldwide", "on Mars", "at the Olympics"]

def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions[subject])
    location = random.choice(locations)
    return f"[{subject}] {action} {location}"

# Main loop
while True:
    print(generate_headline())
    more = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if more != "yes":
        print("Thanks for generating headlines!")
        break
