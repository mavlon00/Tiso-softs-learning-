name = "sammy"
final_greeting = "how are you, {}?"
sammy_greeting = final_greeting.format(name)
print(sammy_greeting)

name = "paul"
paul_greeting = final_greeting.format(name)
print(paul_greeting)

# using F string

age = 34
print(f"you are {age}")

name = "sammy"
greeting = f"how are you, {name}"
print(greeting)