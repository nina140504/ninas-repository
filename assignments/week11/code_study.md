### Template for Code Reading Exercise

**1. Where did you find the code and why did you choose it? (Provide the link)**

I found this code on GitHub after spending quite a while
searching for a simpler example of a jump-and-run style game:
https://github.com/andrewthederp/Games/blob/main/platformer.py

Most of the projects I came across were way too complex,
often split across multiple files and using advanced
frameworks or structures. That made it hard to focus on
just the core mechanics I was interested in.

This one stood out because it’s just a single Python file
with everything built in. It already had working platform
spawning, jumping, and movement. It is exactly the kind of
more basic example I was hoping to find.

---

**2. What does the program do? What's the general structure of the program?**

This program is a basic platformer game made with Pygame.
The goal is to survive by jumping on platforms that fall
from the top of the screen. Some platforms give points,
some make you bounce, and others can even end the game
if you land on them. You move using the WASD keys and
jump with Space.

The main structure of the game is built around a big
main() function. It starts by setting up the screen,
fonts, colors, and the player character. It also creates
a list of random platforms that move down the screen
as the game runs.

There's a main menu you see at the start, where you can see
all the different platform types explained, and once you start
moving your character, platforms spawn and the point counter
starts counting.

The game loop handles events like key presses and timers,
spawns new platforms over time, and checks for collisions.
It also keeps track of your score and can pause the game
if you press Escape. The code uses some timers and
randomness to keep things interesting while you play.

---

**3. Function analysis: pick one function and analyze it in detail:**

The code only uses 2 functions: the main function
and one for the font. As the main function is very long 
(221 lines), I will look at the shorter font function:
```python
def get_font(path, size):
    return pygame.font.SysFont(path, size)
```

**- What does this function do?**

It creates and returns a Pygame font object you can use 
to render text with a given style and size. This allows you 
to specify font type and size centrally, rather than creating 
fonts inline everywhere.
 
**- What are the inputs and outputs?**

  - Inputs:
      - path: A string specifying the font name or path (e.g. "comicsans" or a .TTF file)
      - size: An integer representing the font size (e.g. 26, 50 or 100)
  - Output:
      - The function returns a Pygame font object set to the chosen font and size. 
      This object lets you create text images that can be drawn on the game screen.

**- How does it work (step by step)?**
    
- Receives two inputs: path (font identifier) and size
- Calls pygame.font.SysFont(path, size) which:
  - Loads a system font or TTF font based on the provided path 
  - Sets its size to the provided number.
- Returns the new font object to the caller.

---

**4. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)**

One important thing I learned from the code is that it would be better to use more functions
instead of putting everything inside one big main() function. This helps keep the code organized
and easier to read or change later.
For my own project, where I want to make a jump-and-run game with switching between
light and shadow worlds, having clear and separate functions will be very helpful.
It will let me handle the different mechanics and visuals for each world without mixing everything together.

I liked how the game uses Pygame’s event system and timers to create platforms at random times.
This adds some variety to the gameplay without making the code too complicated.
Also, the way the player can move off one edge of the screen and appear on the other side
is simple but effective. This kind of screen wrapping could be useful in many 2D games.

Another thing I liked about this sample code is how it uses simple shapes like rectangles
to represent the player and platforms. This keeps the graphics basic but makes the game logic
clearer, which is great for learning and building on later.

---

**5. What parts of the code were confusing or difficult at the beginning to understand?
Were you able to understand what it is doing after your own research?**

At first, the code was a bit confusing, especially the big main() function. 
It does a lot all at once, so it was hard to follow everything right away.
For example, this part with the platform spawn timer:
```python
SPAWNPF = pygame.USEREVENT + 1  
pygame.time.set_timer(SPAWNPF, 500)
```
I wasn’t sure how these timers worked and how often new platforms appeared. 
It took some time to understand that this event happens regularly to add new platforms.
The collision detection was also tricky. This section:
```python
for platform in platforms:  
    if platform.colliderect(player):  
        ...
```
shows how the game checks if the player is standing on a platform. 

But i didnt understand why platforms had different “height” values and how those 
affect what happens to the player.

For instance, platforms with platform.height == 8 make the player “die” by moving them off screen:
```python
if platform.height == 8:  
    player.y = 1000
```
I had to look at other parts of the code, like where platform colors are set, 
to understand what the height numbers mean.

The pause system was also a bit confusing at first, especially this part:
```python
if PAUSED and event.key not in [pygame.K_TAB, pygame.K_LALT]:  
    PAUSED = False  
    unpause_time = time.perf_counter()  
    start_time = start_time - (pause_time - unpause_time)
```
I didn’t immediately get why the timer was adjusted here. After reading about 
time.perf_counter() and timers in Pygame, it made more sense.

After doing some research on Pygame events, timers, and collision detection with Rects, 
I was able to understand the code better. But I did have to read through it in detail
several times before getting an idea of the game mechanics. It was difficult to follow each if/elif/else
and to figure out which line does what in the final game.

In the future I would definitely take a code that is structured better, uses more line breaks, has comments and more that 2 functions.
But at least I now know what to avoid in my own code and what to pay attention to when choosing code to look at.

