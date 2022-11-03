import ctypes
import json
from tkinter import *


class ScreenCrop:
    def __init__(self):
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        self.snip_surface = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self.master_screen = Tk()

        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "maroon3")
        self.picture_frame = Frame(self.master_screen, background="maroon3")
        self.picture_frame.pack(fill=BOTH, expand=YES)

        self.create_screen_canvas()

    def create_screen_canvas(self):
        self.master_screen.deiconify()

        self.snip_surface = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.snip_surface.pack(fill=BOTH, expand=YES)

        self.snip_surface.bind("<ButtonPress-1>", self.on_button_press)
        self.snip_surface.bind("<B1-Motion>", self.on_snip_drag)
        self.snip_surface.bind("<ButtonRelease-1>", self.on_button_release)

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', 0.5)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        self.master_screen.destroy()
        return event

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = int(self.snip_surface.canvasx(event.x))
        self.start_y = int(self.snip_surface.canvasy(event.y))
        self.end_x = int(self.snip_surface.canvasx(event.x))
        self.end_y = int(self.snip_surface.canvasy(event.y))
        self.snip_surface.create_rectangle(0, 0, 1, 1, outline='red', width=5, fill="maroon3")

    def on_snip_drag(self, event):
        self.end_x = int(event.x)
        self.end_y = int(event.y)
        # expand rectangle as you drag the mouse
        self.snip_surface.coords(1, self.start_x, self.start_y, self.end_x, self.end_y)


def calibrate_positions():
    """
    Prompt user to select the camera UI on web.snapchat.com.
    Create a dictionary with all the buttons and their positions inside the selected area.
    Save all the button positions to a JSON file.
    """
    while True:
        canvas = ScreenCrop()
        canvas.master_screen.mainloop()
        print(f"Selected camera UI coordinates:\n"
              f"Top:    {canvas.start_x}x{canvas.start_y}\n"
              f"Bottom: {canvas.end_x}x{canvas.end_y}")
        if "y" in input(f'{"_" * 21}\n'
                        'Confirm selected area\n'
                        '["n" to redo / "y" to continue]\n>'
                        '>'):
            break

    w_width = canvas.end_x - canvas.start_x
    w_height = canvas.end_y - canvas.start_y
    take_the_photo: tuple[float, float] = (208 / 415,
                                           683 / 738)
    send_to_button: tuple[float, float] = (315 / 415,
                                           704 / 738)
    send_to_input_field: tuple[float, float] = (200 / 415,
                                                100 / 738)
    first_result: tuple[float, float] = (375 / 415,
                                         200 / 738)
    send: tuple[float, float] = (209 / 415,
                                 702 / 738)

    positions: dict[str, tuple[int, int]] = {
        "Take the photo": (canvas.start_x + int(w_width * take_the_photo[0]),
                           canvas.start_y + int(w_height * take_the_photo[1])),
        "'Send To' button": (canvas.start_x + int(w_width * send_to_button[0]),
                             canvas.start_y + int(w_height * send_to_button[1])),
        "'Send To' input field": (canvas.start_x + int(w_width * send_to_input_field[0]),
                                  canvas.start_y + int(w_height * send_to_input_field[1])),
        "First result": (canvas.start_x + int(w_width * first_result[0]),
                         canvas.start_y + int(w_height * first_result[1])),
        "Send": (canvas.start_x + int(w_width * send[0]),
                 canvas.start_y + int(w_height * send[1]))
    }

    # Write and save the file
    file_name: str = "ButtonPosition.json"
    with open(file_name, "w") as pos_file:
        json.dump(positions, pos_file)
    print("Positions saved as:", file_name)


if __name__ == '__main__':
    input("Select the 'CAMERA UI' on web.snapchat.com.\n"
          "Press ENTER to start\n> ")
    print("Starting", end="\r")
    calibrate_positions()
    print(" " * 10, end="\r")
