![](https://repository-images.githubusercontent.com/307860000/93e34480-5e7d-11eb-9644-58b1688fc80a)

![Forks](https://img.shields.io/github/forks/clown83848474/Python-Music-Bot)
![License](https://img.shields.io/github/license/clown83848474/Python-Music-Bot.svg)
![size](https://img.shields.io/github/repo-size/clown83848474/Discord-Bot)
<img alt="Bitbucket open issues" src="https://img.shields.io/bitbucket/issues/clown83848474/Discord-Bot">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/Discord.py">

# Music Bot

> A Simple Discord.py Music Bot Using LavaLink, and that is easy to set up and run yourself!

## Features
  * Easy to run (just make sure Discord.py And Requirements is installed, and run!)
  * No external keys needed (besides a Discord Bot token and lavalink server Free!)
  * Config.py File So You Dont Need To Edit The Code
  * Simple To Use
  * Clean and beautiful Design For Embeds
  * More Updates And Commands In Future
### Requirements
  * Python +3.6V
  * Discord.py
  * youtube_dl
  * wavelink
### Setup
  * ***__1- Installing Requirements:__***
  ```
  pip install discord.py
  pip install youtube_dl
  pip install wavelink
  ```
  * ***__2- Setuping Lavalink Server:__***
  * Visit https://lavalink.darrennathanael.com TO Get Free Lavalink Server!
  * Than Add The Server Information In Config.py:
  ```py
  ############# LAVALINK ######################
  # Visit https://lavalink.darrennathanael.com TO Get Free Lavalink Server!
  host = "HOST"
  port = "PORT"
  password = "PASSWORD"
  ```
  * 2- ***__Editing config.py:__***
  ```py
  token = "YOUR_TOKEN"
  prefix = "YOUR_PREFIX"
  help_thumbnail = "URL" #You Can Use Any Url Of An Image/Gif
  ```
  **NOTE: Make Sure To Enable The Intents In Developer Portal**
  <img src="https://discordpy.readthedocs.io/en/stable/_images/discord_privileged_intents.png" >
  
  * 3- ***__Running The Code:__***
  ```sh
  python main.py
  ```
  
## Commands:
* **help**
* **join**
* **leave**
* **play**
* **stop**
* **resume**
* **volume**

## Editing
This bot (and the source code here) might not be easy to edit for inexperienced programmers. The main purpose of having the source public is to show the capabilities of the libraries, to allow others to understand how the bot works, and to allow those knowledgeable about discord.py and Discord bot development to contribute. There are many requirements and dependencies required to edit and compile it, and there will not be support provided for people looking to make changes on their own. Instead, consider making a feature request (see the above section). If you choose to make edits, please do so in accordance with the MIT License.

