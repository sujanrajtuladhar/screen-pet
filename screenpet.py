# first we need to import Tkinter module
from tkinter import HIDDEN, NORMAL, Tk, Canvas


def toggle_eyes():
    # first the code checks the eyes current color: white is open, blue is closed
    current_color = c.itemcget(eye_left, 'fill')
    # this  line sets the eyes new_color to the opposit value
    new_color = c.body_color if current_color == 'white' else 'white'
    # now the  code checks if the current state of the pupils is NORMAL (visible) or HIDDEN (not visible)
    current_state = c.itemcget(pupil_left, 'state')
    # this  sets  the pupils' new state to the opposite value
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    # this is for visibility of pupils
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    # this changes color of eyes
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)


def blink():
    # close the eyes
    toggle_eyes()
    # wait 250 milliseconds then open the eyes
    root.after(250, toggle_eyes)
    # wait 3000 milliseconds then blink again
    root.after(3000, blink)


def show_happy(event):
    # the if line checks to see if the mouse-pointer is oer the pet
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        # show the pink checks
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        # show the happy mouth
        c.itemconfigure(mouth_happy, state=NORMAL)
        # hide the normal mouth
        c.itemconfigure(mouth_normal, state=HIDDEN)
        # hide the sad mouth
        c.itemconfigure(mouth_sad, state=HIDDEN)
    return


def hide_happy(event):
        # hide the pink cheeks
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    # hide the hapy mouth
    c.itemconfigure(mouth_happy, state=HIDDEN)
    # show the  normal mouth
    c.itemconfigure(mouth_normal, state=NORMAL)
    # hide the sad mouth
    c.itemconfigure(mouth_sad, state=HIDDEN)
    return


def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.itemconfigure(tongue_main, state=NORMAL)
        c.tongue_out = True
    else:
        # the tongue is already out
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.tongue_out = False


def toggle_pupils():
        # checks if eyes are crossed already
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False


def cheeky(event):
    # stick the tongue out
    toggle_tongue()
    # cross the pupils
    toggle_pupils()
    # hide the happy face
    hide_happy(event)
    # put the tongue back
    root.after(1000, toggle_tongue)
    # uncross the pupils
    root.after(1000, toggle_pupils)
    return


def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1


# it starts tkinter and opens a window
root = Tk()

# the canvas will be 400 pixels wide and 400 pixels high
c = Canvas(root, width=400, height=400)
# the background color will be dark blue
c.configure(bg='dark blue', highlightthickness=0)

c.body_color = 'SkyBlue1'
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70,
                            outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(
    255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)

# left and right of the window
foot_left = c.create_oval(
    65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(
    250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

# width=2, the mouth is a smooth line, 2 pixels wide
mouth_normal = c.create_line(
    170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)

# for happy mouth
mouth_happy = c.create_line(170, 250, 200, 282, 230,
                            250, smooth=1, width=2, state=HIDDEN)
# for sad mouth
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250,
                          smooth=1, width=2, state=HIDDEN)
tongue_main = c.create_rectangle(
    170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(
    170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

# for pink blushing cheeks
cheek_left = c.create_oval(
    70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(
    280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

# this helps to arrange things within the Tkinter window
# any command that start with c. relate to the canvas
c.pack()

# this is  handler function, Tkinter's bind() command
# this links the moving mouse-pointer to the happy face
c.bind('<Motion>', show_happy)
# c.bind('<Leave>', hide_happy)

# for double click in the window with the mouse
# c.bind('<Double–1>', cheeky)
c.bind('<Double-1>', cheeky)

c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False

# wait 1000 milliseconds then start blinking
root.after(1000, blink)
root.after(5000, sad)

# this line starts the function that looks out for input events such as mouse-click
root.mainloop()
