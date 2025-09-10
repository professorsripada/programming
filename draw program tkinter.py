# this is a new line

# This line gets the tools we need to make windows and draw things
import tkinter as tk

# These set up how big our window will be (like the size of a piece of paper)
WIDTH, HEIGHT = 640, 400
# This is how many pixels our star will move each time we press a key
STEP = 10

# This is like a helper that makes sure our star doesn't go off the screen
def clamp(v, lo, hi):
    return max(lo, min(hi, v))

# This creates our main window (like opening a new blank page)
root = tk.Tk()
# This puts a title on our window
root.title("Move the * with arrow keys (Q/Esc to quit)")

# This creates a white drawing area in our window
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white", highlightthickness=0)
canvas.pack()

# This puts a star (*) symbol in the middle of our window
star = canvas.create_text(WIDTH // 2, HEIGHT // 2, text="*", font=("Courier", 48), fill="black")

# This function helps move our star around
def move_star(dx, dy):
    # Get where the star is now
    x, y = canvas.coords(star)
    # Figure out where it should move to
    x_new, y_new = x + dx, y + dy

    # These lines make sure our star doesn't go off the screen
    x1, y1, x2, y2 = canvas.bbox(star)
    half_w = (x2 - x1) / 2
    half_h = (y2 - y1) / 2

    x_new = clamp(x_new, half_w, WIDTH - half_w)
    y_new = clamp(y_new, half_h, HEIGHT - half_h)

    # Move the star to its new spot
    canvas.coords(star, x_new, y_new)

# This function handles when you press keys
def on_key(event):
    k = event.keysym
    # Move left if you press left arrow or 'a'
    if k in ("Left", "a", "A"):  move_star(-STEP, 0)
    # Move right if you press right arrow or 'd'
    elif k in ("Right", "d", "D"): move_star(STEP, 0)
    # Move up if you press up arrow or 'w'
    elif k in ("Up", "w", "W"):    move_star(0, -STEP)
    # Move down if you press down arrow or 's'
    elif k in ("Down", "s", "S"):  move_star(0, STEP)
    # Close the window if you press 'q' or Escape
    elif k in ("q", "Q", "Escape"):
        root.destroy()

# Get ready to watch for key presses
canvas.focus_set()
root.bind("<Key>", on_key)

# Start running our program!
root.mainloop()