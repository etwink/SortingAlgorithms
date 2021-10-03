from gui_driver import GUI_Driver

def main():

    gui = GUI_Driver()
    gui.gui_setUp()
    gui.gui_run()

    print("DONE")


if __name__ == "__main__":
    main()