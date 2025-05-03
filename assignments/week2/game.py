import time
import sys


def type_effect(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def restart_game():
    type_effect("Do you want to try again? (yes/no): ")
    restart_choice = input().strip().lower()
    if restart_choice == 'yes':
        start_game()
    else:
        type_effect("The shadows swallow you whole. GAME OVER.")
        return


def start_game():
    has_dagger = False

    type_effect(
        "🌲 You wake up in a dark forest. You feel dizzy and tired. The wind whispers and the fog surrounds you.")
    time.sleep(1)
    type_effect("A voice echoes: 'To return, you must pass the trials of the Portal of Shadows.'")
    time.sleep(1)

    type_effect("It asks: What is your name, traveler? ")
    name = input()
    type_effect(f"Welcome, {name}. Your fate is unknown... ⚔️")
    time.sleep(1.5)

    print("\nFirst trial: Choose your path.")
    time.sleep(1.5)
    type_effect(
        "Do you go left towards the glowing mushrooms (type 'left') or right towards the howling trees (type 'right')? ")
    path = input().strip().lower()

    if path == "left":
        type_effect("The mushrooms emit a soothing glow. You feel sleepy...")
        time.sleep(1)
        type_effect("Do you sleep or keep walking? ")
        action = input().strip().lower()

        if action == "sleep":
            type_effect("You dream of stars... then never wake up. 💀 GAME OVER.")
            restart_game()
            return
        else:
            type_effect("You push forward. A deer with glowing antlers suddenly appears.")
            time.sleep(1.5)
    elif path == "right":
        type_effect("The trees scream in your ears. Your heart races.")
        time.sleep(1)
        type_effect("You find a silver dagger on the ground. Do you take it? (yes/no) ")
        item = input().strip().lower()

        if item == "yes":
            has_dagger = True
            type_effect("You feel stronger. You may need this...")
            time.sleep(1.5)
        else:
            type_effect(
                "A shadow watches you from afar. You're defenseless. It comes closer and your nightmares become reality. 💀 GAME OVER")
            restart_game()
            return
    else:
        type_effect("Confused, you walk in circles and are lost forever. 💀 GAME OVER.")
        restart_game()
        return

    second_trial(has_dagger)


def second_trial(has_dagger):
    print("\nSecond trial: The Guardian blocks your path. He gives you a simple task:")
    time.sleep(1.5)

    while True:
        type_effect("Guess the Guardian’s number between 1 and 10: ")
        try:
            guess = int(input("> ").strip())
            if 1 <= guess <= 10:
                break
            else:
                type_effect("That number is out of range. Try again.")
        except ValueError:
            type_effect("That's not a valid number. Try again.")

    if guess == 7:
        type_effect("🎉 The Guardian nods and lets you pass.")
        time.sleep(1.5)
    else:
        if guess < 7:
            type_effect("Too low. The Guardian growls.")
        else:
            type_effect("Too high. The Guardian hisses.")
        time.sleep(1)

        if has_dagger:
            type_effect("But wait... you have the silver dagger! You use it to force your way past the Guardian.")
            type_effect("The Guardian steps aside, defeated. You may pass.")
            time.sleep(1.5)
        else:
            type_effect("He allows you one more guess...")
            while True:
                type_effect("Try again: ")
                try:
                    second_guess = int(input("> ").strip())
                    if 1 <= second_guess <= 10:
                        break
                    else:
                        type_effect("That number is out of range. Try again.")
                except ValueError:
                    type_effect("That's not a valid number. Try again.")

            if second_guess == 7:
                type_effect("🎉 You redeem yourself. The Guardian lets you pass.")
                time.sleep(1.5)
            elif abs(second_guess - 7) == 1:
                type_effect("😬 So close, only one off. The Guardian grunts... but lets you go.")
                time.sleep(1.5)
            else:
                type_effect("❌ That was way off.")
                time.sleep(1)
                type_effect("The Guardian strikes. 💀 Game over.")
                restart_game()
                return

    final_trial()


def final_trial():
    print("\nFinal trial: You reach the Portal of Shadows.")
    time.sleep(1.5)
    type_effect("Do you offer a gift (type 'gift') or try to fight (type 'fight')? ")
    choice = input().strip().lower()

    if choice == "gift":
        type_effect("Do you offer a memory or a tear? ")
        gift = input().strip().lower()
        if gift == "memory":
            type_effect("The portal shimmers with light. You are free. 🌟 YOU WIN!")
            time.sleep(2)
        elif gift == "tear":
            type_effect("The portal drinks your sorrow... and closes. 💀 Trapped forever.")
        else:
            type_effect("The portal rejects your offering. 💀 GAME OVER.")
        restart_game()
    elif choice == "fight":
        type_effect("Do you use your courage or your strength? ")
        weapon = input().strip().lower()
        if weapon == "courage":
            type_effect("Your heart burns bright. The shadows vanish. 🌟 YOU WIN!")
            time.sleep(2)
        else:
            type_effect("Strength alone is not enough. The shadows consume you. 💀 GAME OVER.")
        restart_game()
    else:
        type_effect("You hesitate. The portal fades. 💀 GAME OVER.")
        restart_game()


start_game()
