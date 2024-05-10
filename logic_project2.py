import gui_project2
from PIL import ImageTk, Image

def channel_one(self) -> None:
    """
    This function configures the screen for channel one.
    """
    self.image_0 = Image.open("cops_image.jpeg")
    self.resize_image0 = self.image_0.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image0)
    self.image_label.config(image=self.photo)

def channel_two(self) -> None:
    """
    This function configures the screen for channel two.
    """
    self.image_0 = Image.open("rick_and_morty.png")
    self.resize_image0 = self.image_0.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image0)
    self.image_label.config(image=self.photo)

def channel_three(self) -> None:
    """
    This function configures the screen for channel three.
    """
    self.image_0 = Image.open("spongebob.jpg")
    self.resize_image0 = self.image_0.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image0)
    self.image_label.config(image=self.photo)

def channel_four(self) -> None:
    """
    This function configures the screen for channel four.
    """
    self.image_0 = Image.open("hbo.jpeg")
    self.resize_image0 = self.image_0.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image0)
    self.image_label.config(image=self.photo)

def channel_five(self) -> None:
    """
    This function configures the screen for channel five.
    """
    self.image_0 = Image.open("cnn.jpeg")
    self.resize_image0 = self.image_0.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image0)
    self.image_label.config(image=self.photo)

def channel_six(self) -> None:
    """
    This function configures the screen for channel six.
    """
    self.image_0 = Image.open("fox_news.png")
    self.resize_image0 = self.image_0.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image0)
    self.image_label.config(image=self.photo)

def channel_seven(self) -> None:
    """
    This function configures the screen for channel seven.
    """
    self.image_0 = Image.open("sportscenter.jpeg")
    self.resize_image0 = self.image_0.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image0)
    self.image_label.config(image=self.photo)

def channel_eight(self) -> None:
    """
    This function configures the screen for channel eight.
    """
    self.image_0 = Image.open("national_geo.jpeg")
    self.resize_image0 = self.image_0.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image0)
    self.image_label.config(image=self.photo)

def channel_nine(self) -> None:
    """
    This function configures the screen for channel nine.
    """
    self.image_0 = Image.open("regular_show.jpeg")
    self.resize_image0 = self.image_0.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image0)
    self.image_label.config(image=self.photo)
def power(self) -> None:
    """
    This function will turn the power on if it is off,
    and turn it off if it is on by changing the screen to
    a black screen if it is on and whatever screen it
    was left on if off.
    """
    self.image = Image.open("blackscreen.png")
    if not self.status:
        if self.channel == 1:
            channel_one(self)
            self.status = True
        elif self.channel == 2:
            channel_two(self)
            self.status = True
        elif self.channel == 3:
            channel_three(self)
            self.status = True
        elif self.channel == 4:
            channel_four(self)
            self.status = True
        elif self.channel == 5:
            channel_five(self)
            self.status = True
        elif self.channel == 6:
            channel_six(self)
            self.status = True
        elif self.channel == 7:
            channel_seven(self)
            self.status = True
        elif self.channel == 8:
            channel_eight(self)
            self.status = True
        else:
            channel_nine(self)
            self.status = True

    else:
        self.image_1 = Image.open('blackscreen.png')
        self.resize_image1 = self.image_1.resize((250, 200))
        self.photo = ImageTk.PhotoImage(self.resize_image1)
        self.image_label.config(image=self.photo)
        self.status = False

def not_self_status(self) -> None:
    """
    This function configures the screen if the
    TV is off and any of the buttons are clicked
    or the slider is dragged.
    """
    self.image_3 = Image.open('new_candidates.jpg')
    self.resize_image_3 = self.image_3.resize((250, 200))
    self.photo = ImageTk.PhotoImage(self.resize_image_3)
    self.image_label.config(image=self.photo)

def volume_up(self) -> None:
    """
    This function turns the volume up if the TV is on
    up to the maximum volume.
    """
    if not self.status:
        not_self_status(self)
    else:
        if self.volume == 0:
            self.volume = 1
            self.progress_bar.set(1)
        elif self.volume == 1:
            self.volume = 2
            self.progress_bar.set(2)
        elif self.volume == 2:
            self.volume = 3
            self.progress_bar.set(3)
        elif self.volume == 3:
            self.volume = 4
            self.progress_bar.set(4)
        elif self.volume == 4:
            self.volume = 5
            self.progress_bar.set(5)
        elif self.volume == 5:
            self.volume = 6
            self.progress_bar.set(6)
        elif self.volume == 6:
            self.volume = 7
            self.progress_bar.set(7)
        elif self.volume == 7:
            self.volume = 8
            self.progress_bar.set(8)
        else:
            pass
def channel_up(self) -> None:
    """
    This function turns the channel up if the TV is on,
    ad loops it back to 1 if you scroll past 9.
    """
    if not self.status:
        not_self_status(self)
    else:
        if self.channel == 1:
            self.channel = 2
            channel_two(self)
        elif self.channel == 2:
            self.channel = 3
            channel_three(self)
        elif self.channel == 3:
            self.channel = 4
            channel_four(self)
        elif self.channel == 4:
            self.channel = 5
            channel_five(self)
        elif self.channel == 5:
            self.channel = 6
            channel_six(self)
        elif self.channel == 6:
            self.channel = 7
            channel_seven(self)
        elif self.channel == 7:
            self.channel = 8
            channel_eight(self)
        elif self.channel == 8:
            self.channel = 9
            channel_nine(self)
        else:
            self.channel = 1
            channel_one(self)


def  channel_down(self) -> None:
    """
    This function turns the channel down if it is
    already on and returns the volume as 9 if you
    scroll past 1.
    """
    if not self.status:
        not_self_status(self)
    else:
        if self.channel == 1:
            self.channel = 9
            channel_nine(self)
        elif self.channel == 2:
            self.channel = 1
            channel_one(self)
        elif self.channel == 3:
            self.channel = 2
            channel_two(self)
        elif self.channel == 4:
            self.channel = 3
            channel_three(self)
        elif self.channel == 5:
            self.channel = 4
            channel_four(self)
        elif self.channel == 6:
            self.channel = 5
            channel_five(self)
        elif self.channel == 7:
            self.channel = 6
            channel_six(self)
        elif self.channel == 8:
            self.channel = 7
            channel_seven(self)
        else:
            self.channel = 8
            channel_eight(self)


def volume_down(self) -> None:
    """
    This function sets the volume of the TV
    down if the TV is on, down to the minimum volume.
    """
    if not self.status:
        not_self_status(self)
    else:
        if self.volume == 0:
            pass
        elif self.volume == 1:
            self.volume = 0
            self.progress_bar.set(0)
        elif self.volume == 2:
            self.volume = 1
            self.progress_bar.set(1)
        elif self.volume == 3:
            self.volume = 2
            self.progress_bar.set(2)
        elif self.volume == 4:
            self.volume = 3
            self.progress_bar.set(3)
        elif self.volume == 5:
            self.volume = 4
            self.progress_bar.set(4)
        elif self.volume == 6:
            self.volume = 5
            self.progress_bar.set(5)
        elif self.volume == 7:
            self.volume = 6
            self.progress_bar.set(6)
        elif self.volume == 8:
            self.volume = 7
            self.progress_bar.set(7)

def button_press(self, number) -> None:
    """
    This function will change the channel based on which
    of the 9 buttons in the center is pressed if the TV is on.
    """
    if not self.status:
        not_self_status(self)
    else:
        if number == 1:
            channel_one(self)
            self.channel = 1
        elif number == 2:
            channel_two(self)
            self.channel = 2
        elif number == 3:
            channel_three(self)
            self.channel = 3
        elif number == 4:
            channel_four(self)
            self.channel = 4
        elif number == 5:
            channel_five(self)
            self.channel = 5
        elif number == 6:
            channel_six(self)
            self.channel = 6
        elif number == 7:
            channel_seven(self)
            self.channel = 7
        elif number == 8:
            channel_eight(self)
            self.channel = 8
        else:
            channel_nine(self)
            self.channel = 9

def mute(self) -> None:
    """
    This function will mute the TV if it is on. It will
    also unmute and save the previous value if the TV was
    muted.
    """
    if not self.status:
        not_self_status(self)
    else:
        if self.muted:
            self.volume = self.real_volume
            self.progress_bar.set(self.volume)
            self.muted = False
        else:
            self.real_volume = self.volume
            self.volume = 0
            self.progress_bar.set(0)
            self.muted = True

def volume_bar(self) -> None:
    """
    This function configures what the volume bar will
    do, and what volume is displayed, it also outputs an
    error if the volume is trying to be changed while the
    TV is off.
    """
    if not self.status:
        if self.volume == 0:
            self.progress_bar.set(0)
            not_self_status(self)
        elif self.volume == 1:
            self.progress_bar.set(1)
            not_self_status(self)
        elif self.volume == 2:
            self.progress_bar.set(2)
            not_self_status(self)
        elif self.volume == 3:
            self.progress_bar.set(3)
            not_self_status(self)
        elif self.volume == 4:
            self.progress_bar.set(4)
            not_self_status(self)
        elif self.volume == 5:
            self.progress_bar.set(5)
            not_self_status(self)
        elif self.volume == 6:
            self.progress_bar.set(6)
            not_self_status(self)
        elif self.volume == 7:
            self.progress_bar.set(7)
            not_self_status(self)
        else:
            self.progress_bar.set(8)
            not_self_status(self)
    elif self.muted:
        self.volume = 0
        self.progress_bar.set(0)
    else:
        if self.progress_bar.get() == 0:
            self.volume = 0
        elif self.progress_bar.get() == 1:
            self.volume = 1
        elif self.progress_bar.get() == 2:
            self.volume = 2
        elif self.progress_bar.get() == 3:
            self.volume = 3
        elif self.progress_bar.get() == 4:
            self.volume = 4
        elif self.progress_bar.get() == 5:
            self.volume = 5
        elif self.progress_bar.get() == 6:
            self.volume = 6
        elif self.progress_bar.get() == 7:
             self.volume = 7
        else:
            self.volume = 8


