# friend = "sammy"
# user_name = input("Enter you name: ")

# if user_name == friend:
#     print("hello, friend")
# else:
#     print("hello, strenger")

friends = ["sammy", "paul", "charles"]
family = ["jane", "Anny"]

user_name = input("Enter your name: ")

if user_name in friends:
    print("hello, frined!")
elif user_name in family:
    print("hello, family")
else:
    print("i don't know you")