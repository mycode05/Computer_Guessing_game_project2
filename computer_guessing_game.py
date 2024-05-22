#Python project2 --computer guessing number
import random
def comp_guess(num):
    low=1
    high=num
    feedback=""
    while feedback!='c':
        if high != low:
            rad=random.randint(low,high)
        else:
            rad=high
        feedback=input(f"Is number {rad} Enter 'H' for high,'L' for low,'C' for correct number that you have guessed: ".lower())
        if feedback=='h':
            high=rad-1
        elif feedback=='l':
            low=rad+1
    print(f"Congartulations, guessed right {rad}")

number=int(input("Enter the number: "))
comp_guess(number)
