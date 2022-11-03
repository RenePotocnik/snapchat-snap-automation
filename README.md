# Snapchat Snap Automation
Send a pre-specified number of snaps in a given interval to a single recipient 
(*multi-person snaps coming in the future*).

Useful if you're trying to *farm* SnapScore - select *10000* snaps and leave the script running overnight.\
The next morning you'll have and extra *10000* SnapScore. 

---

# Tutorial
* Run `main.py`
* To **calibrate**, select the camera interface so that the red rectangle is perfectly around the *window*
![Camera interface](https://user-images.githubusercontent.com/76653181/199706575-d1fcdde2-1cfe-448e-a4b9-cfa49985352c.png)
* Enter the **amount of snaps** to send (default: 10)
* Enter the **time between each snap** (default: 2 seconds)
* Enter the **time/delay** between each action (default: 0.4 - if the page is laggy, make the delay **higher**)
* Enter the **username** of the recipient (the person to receive the snaps)

You can press **ESCAPE** anytime to instantly stop the program.

---

# Plans for future updates
- [x] Better calibration
- [x] Force-terminate the program with a single button press
- [ ] Remove mouse dependency - perhaps sending snaps using API
- [ ] Error correction - currently if your system lags, there's nothing checking for the error and making sure 
  every step is done successfully
- [ ] Add ability to send snaps to multiple people at once
- [ ] Support for mobile version of Snapchat - over [BlueStacks](https://www.bluestacks.com/K) or [*scrcpy*](https://github.com/Genymobile/scrcpy)
- [ ] Add randomization to steps delay - could prevent/reduce bot detection
