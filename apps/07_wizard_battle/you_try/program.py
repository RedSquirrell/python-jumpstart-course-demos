import random
import time

from you_try import actors


def main():
    show_header()
    game_loop()


def show_header():
    print("-------------------------")
    print("     Wizard Game App")
    print("-------------------------")
    print()


def game_loop():
    creatures = [
        actors.Creature("Toad", 1),
        actors.Creature("Tiger", 12),
        actors.Creature("Bat", 3),
        actors.Creature("Dragon", 50),
        actors.Creature("Evil Wizard", 1000)
    ]

    hero = actors.Wizard("Gandolf", 75)

    while True:

        active_creature = random.choice(creatures)
        print(f"A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...")
        print()

        cmd = input("Do you [a]ttack, [r]unaway or [l]ook around? ")
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print(f"The wizard {hero.name} runs hides taking time to recover...")
                time.sleep(5)
                print(f"The wizard {hero.name} returns revitalized!")
        elif cmd == "r":
            print("The wizard flees!!!")
        elif cmd == "l":
            print(f"The wizard {hero.name} takes in the surroundings and sees:")
            for c in creatures:
                print(f" * A {c.name} of level {c.level}")
        else:
            print("OK, Exiting the game....")
            break


if __name__ == '__main__':
    main()
