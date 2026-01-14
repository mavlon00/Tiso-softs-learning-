default_greeting = "there"
name = input("Enter you name: (optional)")

user_name = name or default_greeting

print(f"hello, {user_name}!")
