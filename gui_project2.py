from tkinter import *
import logic_project2
from PIL import ImageTk, Image
class Gui:
    """
    This class sets up the GUI and configures it into a
    class that is pulled in the main_project2.py file.
    """
    def __init__(self, window) -> None:
        """
        This function sets up the model for the GUI and connects
        each of the buttons to its proper command in
        logic_project2.pt.
        """
        self.window = window

        self.frame_one = Frame(self.window)
        self.status = False
        self.channel = 1
        self.volume = 0
        self.muted = False
        self.power_button = Button(self.frame_one, text="Power", command=lambda:logic_project2.power(self))
        self.power_button.pack()
        self.frame_one.pack()

        self.frame_two = Frame(self.window)
        self.image = Image.open("blackscreen.png")
        self.resize_image = self.image.resize((250,200))
        self.photo = ImageTk.PhotoImage(self.resize_image)
        self.image_label = Label(self.frame_two, image=self.photo)
        self.image_label.image = self.photo
        self.image_label.pack()
        self.frame_two.pack()

        self.frame_three = Frame(self.window)
        self.progress_bar = Scale(self.frame_three, from_=0, to=8, orient=HORIZONTAL, tickinterval=1, length=250, command=lambda value: logic_project2.volume_bar(self))
        self.progress_bar.pack()
        self.frame_three.pack()

        self.frame_four = Frame(self.window)
        self.channel_one = Button(self.frame_four, text='1', width=2, height=2,command=lambda: logic_project2.button_press(self, 1))
        self.channel_two = Button(self.frame_four, text='2', width=2, height=2,command=lambda: logic_project2.button_press(self, 2))
        self.channel_three = Button(self.frame_four, text='3', width=2, height=2,command=lambda: logic_project2.button_press(self, 3))
        self.channel_one.pack(side='left')
        self.channel_two.pack(side='left')
        self.channel_three.pack(side='left')
        self.frame_four.pack()

        self.frame_five = Frame(self.window)
        self.channel_four = Button(self.frame_five, text='4', width=2, height=2,command=lambda: logic_project2.button_press(self, 4))
        self.channel_five = Button(self.frame_five, text='5', width=2, height=2,command=lambda: logic_project2.button_press(self, 5))
        self.channel_six = Button(self.frame_five, text='6', width=2, height=2,command=lambda: logic_project2.button_press(self, 6))
        self.channel_four.pack(side='left')
        self.channel_five.pack(side='left')
        self.channel_six.pack(side='left')
        self.frame_five.pack()

        self.frame_six = Frame(self.window)
        self.channel_seven = Button(self.frame_six, text='7', width=2, height=2, command=lambda: logic_project2.button_press(self, 7))
        self.channel_eight = Button(self.frame_six, text='8', width=2, height=2, command=lambda: logic_project2.button_press(self, 8))
        self.channel_nine = Button(self.frame_six, text='9', width=2, height=2, command=lambda: logic_project2.button_press(self, 9))
        self.channel_seven.pack(side='left')
        self.channel_eight.pack(side='left')
        self.channel_nine.pack(side='left')
        self.frame_six.pack()

        self.frame_seven = Frame(self.window)
        self.volume_up = Button(self.frame_seven, text="Volume Up", width=7, height=2, command= lambda: logic_project2.volume_up(self))
        self.channel_up = Button(self.frame_seven, text="Channel Up", width=7, height=2, command=lambda: logic_project2.channel_up(self))
        self.volume_up.pack(side='left')
        self.channel_up.pack(side='left')
        self.frame_seven.pack()

        self.frame_eight = Frame(self.window)
        self.volume_down = Button(self.frame_eight, text='Volume Down', width=7, height=2, command=lambda: logic_project2.volume_down(self))
        self.channel_down = Button(self.frame_eight, text='Channel Down', width=7, height=2, command=lambda: logic_project2.channel_down(self))
        self.volume_down.pack(side='left')
        self.channel_down.pack(side='left')
        self.frame_eight.pack()

        self.frame_nine = Frame(self.window)
        self.mute = Button(self.frame_nine, text='Mute', width=5, height=2, command=lambda: logic_project2.mute(self))
        self.mute.pack()
        self.frame_nine.pack()
