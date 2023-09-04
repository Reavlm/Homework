

#4.1
secret = 5
guess = 7
if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")

#4.2
small = False 
green = True
if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")


#6.1
numbers = ["3", "2", "1", "0"]
for x in numbers:
  print(x)


#6.2
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
    number += 1

#6.3
    guess_me = 5
    for number in range(10):
        if number < guess_me:
            print("too low")
        elif number == guess_me:
            print("found it!")
            break
        else:
            print("oops")
            break