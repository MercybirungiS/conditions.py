print("Hello World")
num = 2
if num > 0:
    print(num, "is an prime number")
num = 6
if num > 0:
    print(num, "is a an even number")
num2 = 8
if num2 > 0:
    print("positive number")
elif num2 == 0:
    print("Zero")
else:
    print("Negative number")
# nested condition
num = int(input("Enter a number: "))

if num >= 0:
 if num == 0:
    print("Zero")
else:
    print("Positive number")
    # if else
food = 'spaghetti'
if food == 'spaghetti':
    print('Yum, my favorite!')
else:
    print("No, I won't have it. I want spaghetti!")
# simple game
choice = 'c'
if choice == 'a':
    print("You chose 'a'.")
elif choice == 'b':
    print("You chose 'b'.")
elif choice == 'c':
    print("You chose 'c'.")
else:
    print("Invalid choice.")
# reassignment
a = 5
b = a
a = 3
print(a)

# guessing game using while and if else

name = 'Birungi'
guess = input("So I'm thinking of person's name. Try to guess it: ")
pos = 0

while guess != name and pos < len(name):
    print("Nope, that's not it! Hint: letter ", end='')
    print(pos + 1, "is", name[pos] + ". ", end='')
    guess = input("Guess again: ")
    pos = pos + 1

if pos == len(name) and name != guess:
    print("Too bad, you couldn't get it.  The name was", name + ".")
else:
    print("\nGreat, you got it in", pos + 1,  "guesses!")
