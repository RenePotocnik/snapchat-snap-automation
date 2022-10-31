import json
import time
import tkinter as tk


def calibrate_positions():
	"""
	Go through all the buttons and prompt the user to select their location on the screen.
	Save all the button positions to a JSON file.
	"""
	coords: tuple[int, int] = (0, 0)

	def get_mouse_pos(event):
		root.destroy()
		nonlocal coords
		coords = (event.x, event.y)
	
	# False for WEB version, True for mobile version
	mobile_version: bool = False

	positions: dict[str, tuple[int, int]] = {}
	steps: list[str] = [
		"Take the photo",
		"'Send To' button",
		"'Send To' input field",
		"First result",
		"Send"
		]

	input("Starting Calibration. Press enter to start\n> ")
	time.sleep(1)

	for step in steps:
		# Create the window which will get the mouse positions when clicked
		root = tk.Tk()
		root.attributes("-fullscreen", True)
		root.attributes("-topmost", True)
		root.attributes("-alpha", 0.1)
		root.bind("<Button 1>", get_mouse_pos)

		print(f"Current step: '{step}'\tPress the corresponding position on the screen.")
		root.mainloop()
		positions[step] = coords
		print(coords)
		input("Moving to the next step. Press enter to continue.\n> ")

	# Write and save the file
	file_name: str = "ButtonPosition.json"
	with open(file_name, "w") as pos_file:
		json.dump(positions, pos_file)
		print("Positions file has been saved as", file_name)


calibrate_positions()
