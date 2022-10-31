# Snapchat Snap Automation
Send a pre-specified number of snaps in a given interval to a single recipient 
(*multi-person snaps coming in the future*).

# Tutorial
Go to [***Web Snapchat.***](https://web.snapchat.com/)
## Calibrating button positions
This script uses you mouse to send snaps, thus you will need to calibrate the positions of a couple buttons 
(*you only do this once*).

Run `calibrate_positions.py`

You will be instructed to calibrate the button positions:

---

```text
Current step: 'Take the photo'    Press the corresponding position on the screen.
```
![Step 1](https://user-images.githubusercontent.com/76653181/199108008-6ccd0aec-d7ca-479b-bb51-e702340a3b02.png)

---

```text
Current step: ''Send To' button'    Press the corresponding position on the screen.
```

![Step 2](https://user-images.githubusercontent.com/76653181/199108397-b7d56588-5237-44f3-b9ec-a0dfbcf4e971.png)

---

```text
Current step: ''Send To' input field'    Press the corresponding position on the screen.

Current step: 'First result'    Press the corresponding position on the screen.
```
![Step 3 & 4](https://user-images.githubusercontent.com/76653181/199108639-1ffbd9b0-c608-4b8f-84ac-56abc6634588.png)

---

```text
Current step: 'Send'    Press the corresponding position on the screen.
```
![Step 5](https://user-images.githubusercontent.com/76653181/199109168-ba45634b-327a-49c8-89a2-c8d455c59950.png)

## The main functionality
Once done calibrating, run `main.py`.

You'll be prompted to enter some details - you can just press *ENTER* to select the default value.
At last, you'll input the username of the person you're sending the snaps to, a.k.a. recipient.

Then just press enter and **wait**.

If you move the window where [***Web Snapchat***](https://web.snapchat.com/) is open, you will have to recalibrate the 
button positions.

---

# Plans for future updates
- [ ] Remove mouse dependency - perhaps sending snaps using API
- [ ] Error correction - currently if your system lags, there's nothing checking for the error and making sure 
every step is done successfully
- [ ] Add ability to send snaps to multiple people at once