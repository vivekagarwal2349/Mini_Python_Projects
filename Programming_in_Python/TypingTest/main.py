import time, textwrap, colorama
from wonderwords import RandomSentence
from colorama import Fore 
colorama.init(autoreset=True)

s = RandomSentence()

print("Welcome to the type racing game, this game will test your typing speed")
time.sleep(3)

loop='y'
while loop=='y' or loop=='yes':
    sentences = s.sentence()
    sentences2 = s.sentence()
    sentences3 = s.sentence()
    print("Your sentence to type is :-")
    format=(Fore.YELLOW + sentences + sentences2 + sentences3)
    print(textwrap.fill(format,200))
    time.sleep(3)
    print("1")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("3")
    time.sleep(0.7)
    starttime = time.time()
    useranswer=str(input("Type the above given sentence:- \n"))
    stoptime=time.time()
    totaltime= stoptime - starttime
    if useranswer==sentences + sentences2 + sentences3:
        print("You took",totaltime,"seconds to write the full sentence")

        wpm = len(useranswer)*60/(5*totaltime)
        print("You word per minute rate is",wpm)
    else:
        print("Your input was not correct!")
    loop=str(input("Do you want to play again?, input 'y' or 'yes' if you want to!\n"))
print("Thank you for playing! Bye")