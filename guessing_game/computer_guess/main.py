import random 


def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0
    print(f'Guess a number between 1 and {x}')

    done = False

    while guess_number != random_number and done != True: 
        temp = random_number
        choice = input(f"Is {random_number} too high (H), too low (L), or correct (C)? ").lower()
        if choice == 'h':
            random_number = random.randint(1, random_number)
            while random_number == temp: 
                if random_number == 1:
                    print('Your number is 1')
                    done = True
                    break
                else:
                    random_number = random.randint(1, random_number)

        elif choice == 'l':
            random_number = random.randint(random_number, x)
            
            if random_number == temp:
                print('your number is 10')
                done = True

        elif choice == 'c': 
            print(f'Yay! the computer guessed the number {guess_number} correctly')
            break
        else: 
            print("Your choice is invalid")


guess(10)
