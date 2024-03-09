# Typing Game Bot
Opens a typing game, reads the prompt, and types the prompt at whatever speed you choose

## Overview
Using Selenium in Python, I created a bot that travels to [this site](https://play.typeracer.com/) and starts a new game. This script will the read the prompt, click on the input bar, and type each character of the prompt into the input bar to generate a words per minute (WPM) score that gets displayed back to the user. The user can control how fast the script will type out the prompt by determining how many seconds the script waits between typing out each character.

## Disclaimer
This is a bot. This is not intended to be used as a way to be number one on a leaderboard. This site allows you to play as a guest, so my results are not saved to a profile and does not reflect my own personal typing speed. This is intended as a way to demonstrate Selenium for a practical use. 


## Tools and Versions Used
 - Browser: Microsoft Edge Version 122.0.2365.66
 - Windows 11 Home Desktop PC Version 22H2

 - ***More browser support coming once more testing is done***
   
## How it works

The script starts by opening the browser and going to [https://play.typeracer.com/](https://play.typeracer.com/)
Once there, we find the button on the screen that allows us to start a new game and click it.

![start button](/images/typing-start-button.jpeg)


The site will then take 8-10 seconds to find more players. During this time, our script is finding the prompt on the screen and preparing to type. 
For a full explanation of how the script accomplishes this, view the comments in the [script here.](typing-game-bot.py)

![prompt](/images/typing-prompt.jpeg)

Once all of the players are found and the game begins, the input bar is available and the script can interact with it. First things first, the script needs to click on the input to access the ability to type inside of it. Once that happens, the script will type out each character of the prompt into the input bar. 

![input bar](/images/typing-input-bar.jpeg)

![typing example](https://github.com/drewcolbert/Typing-Game-Bot/blob/main/images/typing-example.gif)


Once the race is over, a popup appears and displays the WPM. The script will find that element, extract the value, and display it to the user of the script to show them how the script performed. 


![WPM](/images/typing-WPM-display.jpeg)

<br>
<br>

## How to adjust the speed
The typing speed is determined by how long the script waits before entering the next character of the prompt. At the top of the script, there is a variable called 'time_between_inputs'. Set this value to a specific time (in seconds) that you want the script to wait before typing another character. 

- *Example:* setting 'time_between_inputs = 1' means that the script will wait 1 second before performing another action in the input bar
- *Example:* setting 'time_between_inputs = 0.5' means that the script will wait 0.5 seconds before performing another action in the input bar, and will be twice as fast as using 1 second

**WARNING:** setting 'time_between_inputs = 0' will immediately get you kicked for cheating by the site. Do not try and cheat in this way. 

Here are some values I played around with:
<br>
*NOTE:* any value that yields a WPM score of over 100 will be flagged for potential cheating
  - 0.5 = ~21 WPM
  - 0.1 = ~87 WPM
  - 0.05 = ~135 WPM
  - 0.075 = ~104 WPM
  - 0.085 = ~99 WPM

## Known Issues
There is only one current issue with the script that has only appeared on one occasion.
The way the site is set up, it splits the first word of the prompt into different HTML elements. Sometimes its 3 elements, sometimes it's 2. There was one case where the third element started with a comma (,), when the script joined the elements together, it was not ready for a comma so when it added a space before it, the prompt was incorrect and the script could not proceed. 

*Example:* if the prompt was "However, I knew it was possible", the 3 elements would be ["H", "owever", ", I knew it was possible]. When the strings were concatenated, the prompt would end up looking like this: "However , I knew it was possible". The extra space is a typo and the prompt could not be completed. I am working on a fix to it. 


## Thank you
Thank you for reading, happy typing!

