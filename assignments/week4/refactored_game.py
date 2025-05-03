# this is my refactored game from week 2. you have to pass 3 trials to get to the portal of shadows
# and then make the correct choice to pass though the portal.
# i now have worked on refining my use of functions, and i have added 2 more item that can be obtained,
# by adding another trial (no.3) and a scene for when you go to the mushrooms in the 1st trial.
# ENJOY!!!

import time
import sys

# constants
TEXT_DELAY = 0.02
GUARDIAN_NUMBER = 7
DAGGER_ITEM = "silver dagger"
FEATHER_ITEM = "glowing feather"
AMULET_ITEM = "stone amulet"
DEBUG = False


# functions, that get used often

# typing effect
def type_effect(text, delay=TEXT_DELAY):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# get player's valid input and make it lowercase
def decision(prompt, options):
    while True:
        type_effect(prompt)
        choice = input("> ").strip().lower()
        if choice in options:
            return choice
        type_effect(f"Invalid input. Options: {', '.join(options)}")

# get player's valid input of a number in range
def number_guess(prompt, min_val, max_val):
    while True:
        try:
            type_effect(prompt)
            guess = int(input("> ").strip())
            if min_val <= guess <= max_val:
                return guess
            else:
                type_effect(f"That number is out of range. Try a number between {min_val} and {max_val}.")
        except ValueError:
            type_effect("That's not a valid number. Try again.")

# ask to restart
def restart_game():
    choice = decision("Do you want to try again? (yes/no)", ["yes", "no"])
    if choice == "yes":
        start_game()
    else:
        type_effect("The shadows swallow you whole. GAME OVER.")


# THE GAME

def start_game():
    has_dagger = False
    has_feather = False
    has_amulet = False

    type_effect("🌲 You wake up in a dark forest. You feel dizzy and tired. The wind whispers and the fog surrounds you.")
    time.sleep(1)
    type_effect("A voice echoes: 'To return, you must pass the trials of the Portal of Shadows.'")
    time.sleep(1)

    type_effect("What is your name, traveler?")
    name = input("> ")
    type_effect(f"Welcome, {name}. Your fate is unknown... ⚔️")
    time.sleep(1.5)

    # order of the game
    has_dagger, has_feather = first_trial()

    second_trial(has_dagger, has_feather)

    has_amulet = third_trial()

    final_trial(has_feather, has_amulet)


# first trial
def first_trial():
    has_dagger = False
    has_feather = False

    path = decision("Do you go left towards the glowing mushrooms or right towards the howling trees? (left/right)",
                    ["left", "right"])

    if path == "left":
        action = decision("The mushrooms emit a soothing glow. Do you sleep or keep walking? (sleep/walk)",
                          ["sleep", "walk"])
        if action == "sleep":
            type_effect("You dream of stars... then never wake up. 💀 GAME OVER.")
            restart_game()
            return has_dagger, has_feather

        # get feather
        else:
            type_effect("You push forward. A deer with glowing antlers appears and nods to you.")
            time.sleep(1)
            type_effect("The deer leads you to a quiet spot. You find a shimmering feather.")
            choice = decision("Do you take the feather? (yes/no)", ["yes", "no"])
            if choice == "yes":
                has_feather = True
                type_effect("The feather feels warm. It may protect you from harm...")
                time.sleep(1)
            else:
                type_effect("You leave the feather. A gentle breeze passes.")
                time.sleep(1)

    # get the dagger
    else:
        item_choice = decision("You find a silver dagger. Do you take it? (yes/no)", ["yes", "no"])
        if item_choice == "yes":
            has_dagger = True
            type_effect("You feel stronger. You may need this...")
            time.sleep(1)
        else:
            type_effect("A shadow watches you. You're defenseless. It comes closer and your nightmares become reality. 💀 GAME OVER.")
            restart_game()
            return has_dagger, has_feather

    return has_dagger, has_feather


# second trial
def second_trial(has_dagger, has_feather):
    print("\nSecond trial: The Guardian blocks your path. He gives you a task.")
    time.sleep(1)

    guess = number_guess("Guess the Guardian’s number between 1 and 10:", 1, 10)

    if guess == GUARDIAN_NUMBER:
        type_effect("🎉 The Guardian nods and lets you pass.")
        time.sleep(1)
    else:
        hint = "Too low." if guess < GUARDIAN_NUMBER else "Too high."
        type_effect(f"{hint} The Guardian growls.")
        time.sleep(1)

        # win with dagger
        if has_dagger:
            type_effect("But wait... you have the silver dagger! You use it to force your way past.")
            time.sleep(1)
        else:
            type_effect("He allows you one more guess...")
            second_guess = number_guess("Try again:", 1, 10)

        # guess again
            if second_guess == GUARDIAN_NUMBER:
                type_effect("🎉 You redeem yourself. The Guardian lets you pass.")
                time.sleep(1)
            elif abs(second_guess - GUARDIAN_NUMBER) == 1:
                type_effect("😬 So close, only one off. The Guardian grunts... but lets you go.")
                time.sleep(1)
            else:
                type_effect("❌ That was way off.")
                type_effect("The Guardian strikes. 💀 GAME OVER.")
                restart_game()
                return


# third trial, get amulet
def third_trial():
    print("\nThird trial: You find a circle of ancient stones.")
    time.sleep(1)
    type_effect("A voice whispers: 'Only the worthy may claim the power within.'")

    riddle = decision("Do you step into the circle or walk away? (step/walk)", ["step", "walk"])
    if riddle == "step":
        type_effect("A stone glows and gives you a riddle: 'I can be heard but never seen, I answer without speaking, I exist only when you call. What am I?' ")
        answer = input("> ").strip().lower()
        if "echo" in answer:
            type_effect("✨ The stones tremble and leave behind a stone amulet.")
            time.sleep(1)
            return True
        else:
            type_effect("The stones fall silent. You leave with nothing.")
            time.sleep(1)
            return False
    else:
        type_effect("You avoid the circle and move on cautiously.")
        time.sleep(1)
        return False


# final trial
def final_trial(has_feather, has_amulet):
    print("\nFinal trial: You reach the Portal of Shadows.")
    time.sleep(1)

    choice = decision("Do you offer a gift or try to fight? (gift/fight)", ["gift", "fight"])

    if choice == "gift":
        if has_feather:
            type_effect("Do you offer a memory, a tear, or the feather?")
        else:
            type_effect("Do you offer a memory or a tear?")

        gift = input("> ").strip().lower()

        if gift == "memory":
            type_effect("The portal shimmers with light. You are free. 🌟 YOU WIN!")
            time.sleep(2)
        elif gift == "tear":
            type_effect("The portal drinks your sorrow... and closes. 💀 Trapped forever.")
        elif gift == "feather" and has_feather:
            type_effect("The portal accepts the feather and glows warmly. You are free. 🌟 YOU WIN!")
            time.sleep(2)
        else:
            type_effect("The portal rejects your offering. 💀 GAME OVER.")
            restart_game()

    elif choice == "fight":
        weapon = decision("Do you use your courage or your strength? (courage/strength)", ["courage", "strength"])
        if weapon == "courage":
            type_effect("Your heart burns bright. The shadows vanish. 🌟 YOU WIN!")
        elif weapon == "strength":
            if has_amulet:
                type_effect("The stone amulet glows in your hand. Strength flows through you. 🌟 YOU WIN!")
            else:
                type_effect(" You are not strong enough for this fight. The shadows consume you. 💀 GAME OVER.")
                restart_game()
                return
        restart_game()
    else:
        type_effect("You hesitate. The portal fades. 💀 GAME OVER.")
        restart_game()


# start the game
def main():
    type_effect("✨ Welcome to Portal of Shadows ✨")
    time.sleep(1)
    start_game()


if __name__ == "__main__":
    main()
