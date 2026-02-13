import random
first_names = ["john", "mary", "peter", "lisa", "david", "sarah"]
last_names = ["smith", "johnson", "brown", "williams", "miller", "davis"]
domain = "example.com"

def generate_email():
    first = random.choice(first_names)
    last = random.choice(last_names)
    number = random.randint(1, 999)
    return f"{first}.{last}{number}@{domain}"

for i in range(10):
    print(generate_email())
