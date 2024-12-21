from gameStory.features import typeWriter, wipeClean, invalidChoice, gameOver, save, SUAVE, LVL, name

def dayTwo():
    global gameProgress
    gameProgress = "dayTwo"
    global LVL
    LVL += 1
    save()
    wipeClean()
    typeWriter(". . . ")
    typeWriter(". . . ")
    typeWriter("S A V I N G ")
    typeWriter(". . . ")
    typeWriter(". . . ")
    typeWriter("S A V I N G ")
    typeWriter(". . . ")
    typeWriter(". . . ")
    wipeClean()
    typeWriter("would you like to continue here? all progress will be saved automatically each day")
    typeWriter("OPTIONS: ")
    typeWriter("1. QUIT AND COME BACK TO SAVE FILE LATER")
    typeWriter("2. CONTINUE")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        exit()
    elif choice == "2":
        secondMorning()

    else:
        wipeClean()
        invalidChoice()
        dayTwo()
#checkpoint

def secondMorning():
    typeWriter("The sun shines through the dust caked window to your left")
    typeWriter("You look at the clock above the mantle and notice the time")
    typeWriter("   9 A. M. ?!?!?!")
    typeWriter("You usually leave at   8 : 30 ")
    typeWriter("OPTIONS: ")
    typeWriter("1. Hurry to the cafe for work!")
    typeWriter("2. Message and say you'll be late")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        cafeEnter()
    elif choice == "2":
        wipeClean()
        lateWorker()
    else:
        wipeClean()
        invalidChoice()
        secondMorning()
#begin day2




def cafeEnter():
    typeWriter("You rush out your door after slipping on your jeans in record time")
    typeWriter("Your rusted bike on the porch creaks and groans as you pedal as fast as possible")
    typeWriter("You reach to work and enter before any customers have arrived")
    typeWriter("SUAVE +2")
    global SUAVE
    SUAVE += 2
    save()
    typeWriter("Your coworker Ephram who your close to challenges you to your morning competition")
    typeWriter("OPTIONS: ")
    typeWriter("1. Play Rock Paper Scissors?")
    typeWriter("2. Decline, you're too busy! People might be there any moment.")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        #rockPaperScissors()
    elif choice == "2":
        wipeClean()
        startWork()
    else:
        wipeClean()
        invalidChoice()
        cafeEnter()
#rockPapeScis + startwork

def startWork():
    pass

def lateWorker():
    typeWriter("There's no way you'll make it in time")
    typeWriter("You don't want to look slovenly on top of be tardy...")
    typeWriter("You take out your phone and message your boss informing him you'll be a bit late")
    typeWriter("SUAVE -1")
    global SUAVE
    SUAVE -= 1
    save()
    typeWriter("You trudge downstairs and eat breakfast what will you eat?")
    typeWriter("OPTIONS: ")
    typeWriter("1. Cofee and blueberry muffin, great for a long day of work!")
    typeWriter("2. Scrambled eggs with OJ, classic breakfast.")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        carbBreaky()
    elif choice == "2":
        wipeClean()
        proteinBreaky()
    else:
        wipeClean()
        invalidChoice()
        lateWorker()
#proteinBreaky + carbBreaky

def carbBreaky():
    typeWriter("The lid of the jar audibly pops as you open your coffee beans")
    typeWriter("As the aroma of the fresh grounds fills the room you go to your freezer")
    typeWriter("You take out your ~batter puck~ and place it in the muffin tin")
    typeWriter("As the fragrant breakfast bakes & cooks you flip out your phone")
    typeWriter("OPTIONS: ")
    typeWriter("1. Read todays news? ")
    typeWriter("2. Play todays quiz! ")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        print("NEWS")
        #dailyNews()
    elif choice == "2":
        wipeClean()
        print("QUIZ")
        #dailyQuiz()
    else:
        wipeClean()
        invalidChoice()
        carbBreaky()
    

def proteinBreaky():
    typeWriter("You grab an orange give it a toss before catching it")
    typeWriter("Fresh is best after all~")
    typeWriter("You juice the orange by hand")
    typeWriter("Once you've filled a tall glass you turn to your counter")
    typeWriter("Within the porcelain chicken you have fresh eggs")
    typeWriter("Your neighbor Lucy has a few chickens for laying")
    typeWriter("You crack 3 eggs into a pan")
    typeWriter("Ignite the flame on your stove")
    typeWriter("Alternate between mixing on and off the flame while continuously stirring")
    typeWriter("You sit down with the results of your hard work in front of you: ")
    typeWriter("The eggs are fluffy and cooked to perfection, the orange juice is sweet")
    typeWriter("You pull out your phone while you eat")
    typeWriter("OPTIONS: ")
    typeWriter("1. Read todays news? ")
    typeWriter("2. Play todays quiz! ")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        print("NEWS")
        #dailyNews()
    elif choice == "2":
        wipeClean()
        print("QUIZ")
        #dailyQuiz()
    else:
        wipeClean()
        invalidChoice()
        carbBreaky()


def eatBreaky():
    typeWriter("You eat breakfast and start to head to work fully nourished")
    typeWriter("Your rusted bike on the porch groans slightly as you ease into a rythm")
    typeWriter("You reach work and see one of the regulars ordering")
    typeWriter("As you clock in as your coworker Ephram takes her order")
    typeWriter("After he finishes he turns to you and grins impishly")
    typeWriter("Tired eh? mmm Maybe a freindly game of ~ro-sham-bo~ will do the trick!")
    typeWriter("OPTIONS: ")
    typeWriter("1. Play Rock Paper Scissors?")
    typeWriter("2. Decline, you're too busy! People might be there any moment.")

    choice = input("> ")
    if choice == "1":
        wipeClean()
        #rockPaperScissors()
    elif choice == "2":
        wipeClean()
        startWork()
    else:
        wipeClean()
        invalidChoice()
        cafeEnter()
#will be called in a minigame
#rockpaperscissors + startwork


