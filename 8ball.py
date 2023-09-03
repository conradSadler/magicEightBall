import random
import time
import webbrowser
def Yball():
    # 8 ball eqauls 8 sides, eight possibilities
    Die = random.randint(1,8)
    WelcomeName = input("What is your name?\n")
    WelcomeNote = ("Welcome" + " " + WelcomeName + " " + "to your fortune teller! I know how good your future will be, based on your own luck! If you’re lucky, you’ll have a lucky outcome. ")
    print(WelcomeNote)
    v1 = int(input(WelcomeName + " " + "when you’re ready to roll the dice for your future, press 3."))
    if v1 == 3:
        print("Well then, lets see what your future holds....")
        if Die <= 8:
            print("Why are you playing this game, an eight ball could never fully understand your potential")
            SelfFulfillingProphecy = int(input("Press t""h""ree to read an article about self fulfilling prophecies."))
            if SelfFulfillingProphecy == 3:
                print("You will do amazing things in your life time....")
                time.sleep(4.20)
                webbrowser.open_new_tab(r"https://www.britannica.com/topic/self-fulfilling-prophecy")
        else:
            print("404 error")
    else:
        print("We Hope you play next time")
Yball()
