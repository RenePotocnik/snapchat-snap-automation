import json
import threading
import time

import pyautogui
import keyboard

import calibrate_positions


def get_positions(file: str) -> dict[str, list]:
    """Read and load the given JSON file. Returns a dictionary of the step names and positions"""
    try:
        with open(file, "r") as pos_file:
            return json.load(pos_file)
    except FileNotFoundError:
        exit(f"The file named '{file}' was not found.")


def send_snaps(count: int, interval: float, delay: float, positions: dict[str, list], user: str) -> None:
    """Send snaps on snapchat using mouse movements.

    :param count: The amount of snaps to send
    :param interval: Time between each snap
    :param delay: The delay between each step/action
    :param positions: Dictionary including the names and positions of each step
    :param user: The username of the recipient whom the snaps will be sent to
    """
    sec_to_complete: float = (count * (len(positions) * (delay * 2))) + (count - 1) * interval
    if "n" in input(f"Estimated time to complete: "
                    f"{int(sec_to_complete / 60)} minute{'s' if int(sec_to_complete / 60) > 1 else ''}"
                    f" {int(sec_to_complete % 60)} second{'s' if int(sec_to_complete % 60) > 1 else ''}\n"
                    f"Continue? [y/n]: ").lower():
        return
    for i in range(count):
        if i:
            print("Waiting for", interval, "sec.")
            time.sleep(interval)
        print(f"Snap #{i + 1}")

        for step, coords in positions.items():
            print(step)
            time.sleep(delay)

            pyautogui.click(x=coords[0], y=coords[1])
            time.sleep(delay)

            if step == "'Send To' input field":
                pyautogui.write(user)
    pyautogui.press("esc")


def exit_on_button_press(button: str = "esc"):
    while True:
        keyboard.wait(button)
        print("Exiting")
        return True


def main() -> None:
    # Get the position of all the steps on screen from a JSON file
    step_positions: dict[str, list] = get_positions(file="ButtonPosition.json")

    count = input("Amount of snaps to send (default: 10): ")
    interval = input("Time between each snap (default: 2): ")
    delay = input("Delay between actions (default: 0.4): ")
    user: str = ""
    while not user:
        user = input(f"Recipient: ")

    main_process = threading.Thread(target=send_snaps,
                                    args=(int(count) if count else 10,
                                          float(interval) if interval else 2,
                                          float(delay) if delay else 0.4,
                                          step_positions,
                                          user),
                                    daemon=True)
    main_process.start()
    if exit_on_button_press():
        exit()


if __name__ == '__main__':
    if "n" not in input("Calibrate positions (recommended)? [y/n]:\n> "):
        calibrate_positions.calibrate_positions()
    main()
