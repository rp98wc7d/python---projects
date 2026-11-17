import random

def intro():
    print("\n" + "=" * 50)
    print("🏰 WELCOME TO THE MYSTIC ADVENTURE 🏰")
    print("=" * 50)
    print("You are a brave explorer searching for the Lost Treasure.")
    print("Your mission is to survive and find the treasure.")
    print("=" * 50)

def forest():
    print("\n🌲 You enter a dark forest.")
    print("1. Follow the strange sound")
    print("2. Continue on the path")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        print("\n🐺 A wild wolf appears!")
        fight = input("Do you fight or run? (fight/run): ").lower()

        if fight == "fight":
            if random.randint(1, 2) == 1:
                print("⚔️ You defeated the wolf!")
                return True
            else:
                print("💀 The wolf defeated you.")
                return False
        else:
            print("🏃 You successfully escaped.")
            return True

    elif choice == "2":
        print("✅ You safely pass through the forest.")
        return True

    else:
        print("Invalid choice.")
        return forest()

def cave():
    print("\n🕳️ You discover a mysterious cave.")
    print("1. Enter the cave")
    print("2. Walk around it")

    choice = input("Enter choice (1/2): ")

    if choice == "1":
        print("\n🐉 A dragon is sleeping inside!")

        action = input("Sneak or attack? (sneak/attack): ").lower()

        if action == "sneak":
            print("✅ You quietly steal a magical key.")
            return True

        elif action == "attack":
            print("🐉 The dragon wakes up!")

            if random.randint(1, 3) == 1:
                print("⚔️ You defeated the dragon!")
                return True
            else:
                print("🔥 The dragon burned you!")
                return False

    elif choice == "2":
        print("You avoid danger and continue your journey.")
        return True

    else:
        print("Invalid choice.")
        return cave()

def treasure_room():
    print("\n🚪 You reach an ancient treasure room.")
    print("There are three treasure chests:")
    print("1. Gold Chest")
    print("2. Silver Chest")
    print("3. Wooden Chest")

    lucky_chest = random.randint(1, 3)

    choice = int(input("Choose a chest (1-3): "))

    if choice == lucky_chest:
        print("\n🎉 CONGRATULATIONS!")
        print("💰 You found the Lost Treasure!")
    else:
        print("\n☠️ The chest was trapped!")
        print("Game Over!")

def play_game():
    intro()

    if not forest():
        print("\n❌ GAME OVER")
        return

    if not cave():
        print("\n❌ GAME OVER")
        return

    treasure_room()

while True:
    play_game()

    replay = input("\nWould you like to play again? (yes/no): ").lower()

    if replay != "yes":
        print("\n👋 Thanks for playing Mystic Adventure!")
        break
    else:
        print("\n Restarting the game...")