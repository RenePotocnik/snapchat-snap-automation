import json
import time

import pyautogui


def get_positions(file: str) -> dict[str, list]:
    try:
        with open(file, "r") as pos_file:
            return json.load(pos_file)
    except FileNotFoundError:
        exit(f"The file named '{file}' was not found.")


def send_snaps(count: int, interval: float, delay: float, positions: dict[str, list], user: str) -> None:
    """Send snaps on snapchat using mouse movements.

	:param count: How many snaps to send
	:param interval: How often to send a snap. *{Time to send a snap} + {interval}*
	:param delay: The delay between each action/step
	:param positions: Dictionary of all the step positions 
	:param user: The recepient of the snaps
	"""
    print(f"Estimated time to complete: {(count * (len(positions) * (delay * 2))) + (count - 1) * interval}")

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

            if step == "send_to_input_field":
                pyautogui.write(user)


def main() -> None:
    # Get the position of all the steps on screen from a JSON file
    step_positions: dict[str, list] = get_positions(file="ButtonPosition.json")

    count = int(input("Amount of snaps to send (default: 10): "))
    interval = float(input("Time between each snap (default: 3): "))
    delay = float(input("Delay between actions (default: 0.4): "))
    user = input(f"Recipient: ")

    send_snaps(count=count if count else 10,
               interval=interval if interval else 3,
               delay=delay if delay else 0.4,
               positions=step_positions,
               user=user)


if __name__ == '__main__':
    main()
    exit("Done!")
