import time

def introduction():
    print("Welcome to the Wizarding World!")
    time.sleep(1)
    print("You are a young wizard at Hogwarts School of Witchcraft and Wizardry.")
    time.sleep(1)
    print("Your journey is about to begin. Make choices wisely!")

def choose_house():
    print("\nYou are sorted into houses.")
    time.sleep(1)
    print("1. Gryffindor")
    print("2. Slytherin")
    print("3. Hufflepuff")
    print("4. Ravenclaw")

    while True:
        choice = input("Choose your house (1-4): ")
        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def gryffindor_story():
    print("\nWelcome to Gryffindor!")
    time.sleep(1)
    print("You quickly make friends and become known for your bravery.")
    time.sleep(1)
    print("One day, you find a mysterious door in the Gryffindor common room.")
    time.sleep(1)
    print("1. Open the door.")
    print("2. Ignore the door.")

    choice = input("What do you choose? (1-2): ")
    if choice == "1":
        print("\nYou find a hidden room full of magical creatures!")
        time.sleep(1)
        print("Congratulations! You made a new friend, a magical creature.")
    else:
        print("\nYou decide to ignore the door and focus on your studies.")

def slytherin_story():
    print("\nWelcome to Slytherin!")
    time.sleep(1)
    print("You're known for your cunning and resourcefulness.")
    time.sleep(1)
    print("One day, you overhear a secret conversation among your fellow Slytherins.")
    time.sleep(1)
    print("1. Confront them.")
    print("2. Keep quiet and gather information.")

    choice = input("What do you choose? (1-2): ")
    if choice == "1":
        print("\nYour boldness pays off, and you gain the respect of your housemates.")
        time.sleep(1)
        print("Congratulations! You become a trusted member of the Slytherin community.")
    else:
        print("\nYou decide to keep quiet, gather information, and use it to your advantage later.")

def hufflepuff_story():
     print("\n Welcome to Hufflepuff")
     time.sleep(1)
     print("You have qualities such as loyality, patience and dedication.")
     time.sleep(1)
     print("Explore the Herbology greenhouse.")
     time.sleep(1)
     print("You make your way to greenhouse,filled with variety of plants.")
     print("You noticed peculiar plant in the corner.")
     time.sleep(1)
     print("1. Approach the plant.")
     print("2. Call for Professor Sprout for assistance.")
     choice=input("What do you choose? (1/2): ")
     if choice=="1":
         print("You cautiusly approach the moving plant, keeping your wand at ready.")
         print("Suddenly the palnt move towards you to attack. ")
         time.sleep(1)
         print("You quickly cast a spell to immobilize it. Now the plant is in your control.")
         time.sleep(1)
         print("Congratulations! your bravery and quick thinking saved the day.")
     else:
         print("Professor Sprout arrives to assess the situation")
         print("Together ,you safely relocate the plant to a more suitable environment.")
         time.sleep(1)
         print("Congartulations! You demonstrate the importance of teamwork and seeking guidance.")

def ravenclaw_story():
    print("\n Welcome to Ravenclaw.")
    time.sleep(1)
    print("You are highly intellect, creative and passion for learning.")
    time.sleep(1)
    print("You are in the Ravenclaw common room.")
    time.sleep(1)
    print("1. Visit the Hogwarts library for some quiet study.")
    print("2. Attend a gathering in the common room and engage in intellectual discussions.")
    choice= input(" What do you choose? (1/2):")
    if choice =="1":
        print("Rows upon rows of books line the shelves,waiting to be exlpored.")
        print("Research a topic of interest and seek out knowledge")
        time.sleep(1)
        print("Congratulations! Your thirst for knowledge leads to new discoveries.")
    else:
        print("The atmosphere is lively with discussions on various topics")
        print("Share your latest discovery from your studies.")
        time.sleep(1)
        print("Congratulations! Your willingness to share enriches the intellectual community.")
     
# Main game loop
def main():
    introduction()
    house_choice = choose_house()

    if house_choice == 1:
        gryffindor_story()
    elif house_choice == 2:
        slytherin_story()
    elif house_choice ==3:
        hufflepuff_story()
    else:
        ravenclaw_story()
    

if __name__ == "__main__":
    main()
