import supervisor
import board
import displayio


def split_screen(display):
    # Create a Group
    mygroup = displayio.Group()

    # clear the display to the REPL
    display.show(None)
    splash = board.DISPLAY.root_group  # this gets the current root_group, the REPL

    # Note: You must "display.show" your own group before adding the splash to your own group.
    # Reason: When displaying the normal REPL (for example with display.show(None), the splash
    # group is already in a group that is displayed.  To remove the splash from the displayed group,
    # you first have to display.show some other group, doing that will remove the splash from its group
    # and allow you to append it to your own group.
    display.show(mygroup)

    # resize the supervisor.splash group pixel dimensions, make it half the display height.
    supervisor.reset_terminal(display.width, display.height // 2)

    # relocate the supervisor.splash group on the display, moving it half-way down the display
    splash.y = display.height // 2
    print("Resize and move the splash screen")

    # append the supervisor.splash group to the displayed group.
    mygroup.append(splash)
    return mygroup