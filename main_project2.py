from gui_project2 import *
def main() -> None:
    """
    This function runs the GUI and configures the size
    and name of the application.
    """
    window = Tk()
    window.title('TV Remote')
    window.geometry('500x600')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()