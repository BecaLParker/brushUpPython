# Foreach loop
def print_people(*people):
    for person in people:
        print("This person is", person)


# print_people("Nick", "Michael", "Bob")

# Return values from functions
def addition(num1, num2):
    return num1 + num2


sum1 = addition(1, 2)
sum2 = addition(3, 4)

# print("1st sum is", sum1, "and 2nd sum is", sum2)

# If, elif, else statements
becaAwesome = True

if becaAwesome:
    print("Beca is awesome")
elif becaAwesome == "Hamburger":
    print("Why are you a hamburger Beca?")
else:
    print("Beca is not awesome yet")
