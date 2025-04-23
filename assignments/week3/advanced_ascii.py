import random
import time
import sys

# Define typing
def type_input(prompt, delay=0.05):
    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    return input()

# Accessory
silly = ["🤪", "🦄", "🧃", "🛹", "🧸", "🎮", "🎈", "💀"]
fancy = ["🎩", "👑", "💼", "🎀", "🕶", "💍", "👒", "🌹"]
random_pool = silly + fancy + ["🌟", "🐾", "📚", "😺", "🎮", "🍭", "🌈"]

# ANSI color codes
colors = ["\033[95m", "\033[97m", "\033[94m", "\033[92m", "\033[93m", "\033[91m", "\033[35m", "\033[36m", "\033[37m"]
end_color = "\033[0m"

# Name
cat_name = type_input("Give your cat a name: ")

# Width
while True:
    try:
        width = int(type_input("How many cats per row? "))
        break
    except ValueError:
        print("I don't understand, can you repeat?")

# Height
while True:
    try:
        height = int(type_input("How many rows of cats? "))
        break
    except ValueError:
        print("I don't understand, can you repeat?")

# Style
while True:
    style = type_input("Choose accessory style (silly / fancy / random): ").strip().lower()
    if style in ["silly", "fancy", "random"]:
        break
    print("I don't understand, can you repeat?")

# Colorful
while True:
    color_input = type_input("Rainbow colors? (yes / no): ").strip().lower()
    if color_input in ["yes", "no"]:
        use_color = color_input == "yes"
        break
    print("I don't understand, can you repeat?")

# Number of colors
if use_color:
    while True:
        try:
            num_colors = int(type_input(f"How many colors would you like to use (1-{min(9, width)})? "))
            if 1 <= num_colors <= min(9, width):
                break
            else:
                print(f"Please enter a number between 1 and {min(9, width)}.")
        except ValueError:
            print("I don't understand, a number please")

# Choose accessory
if style == "silly":
    chosen_pool = silly
elif style == "fancy":
    chosen_pool = fancy
else:
    chosen_pool = random_pool

# Generate cat
def generate_cat(name, accessory, color=""):
    name_accessory_line = f"{name} {accessory}".center(10)

    cat_lines = [
        f"   {name_accessory_line}",
        r"      |\___/|",
        r"      )     (",
        r"     =\     /=",
        r"       )===(",
        r"      /     \ ",
        r"      |     | ",
        r"     /       \ ",
        r"     \       / ",
        r"  _/\_/\_/\__  _/_/\_/\_",
        r"  |  |  |  |( (  |  |  | ",
        r"  |  |  |  | ) ) |  |  | ",
        r"  |  |  |  |(_(  |  |  | ",
        r"  |  |  |  |  |  |  |  | "
    ]
    max_len = max(len(line) for line in cat_lines)
    return [f"{color}{line.ljust(max_len)}{end_color}" for line in cat_lines]

# Cat grid
cat_grid = []
for _ in range(height):
    row = []

    if use_color:
        row_colors = random.sample(colors, num_colors)
        row_colors = (row_colors * ((width // num_colors) + 1))[:width]
    else:
        row_colors = ["" for _ in range(width)]

    for i in range(width):
        acc = random.choice(chosen_pool)
        col = row_colors[i]
        row.append(generate_cat(cat_name, acc, col))
    cat_grid.append(row)

# Print cat
for row in cat_grid:
    for line_index in range(len(row[0])):
        for cat in row:
            print(cat[line_index], end="")
        print()
        time.sleep(0.1)
    print("\n")
    time.sleep(0.3)
