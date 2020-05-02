# How to use

- Install Praw. Do this by going into the command prompt and typing "pip install praw" (note: you must have Python installed to do this, and Python must be added to the PATH variable in Windows.)
- Create an app in the Reddit settings. To do that, follow these steps:
    - Go to https://www.reddit.com/prefs/apps
    - scroll down until you see "Create another app" or if you're not a nerd like me, click the box that says "Are you a developer? Create an app..." or something like that. I don't wanna delete my apps to find out. You get the point.
    - name it whatever you would like.
    - You will see 3 selection options. "Web app," "Installed app," and "Script." For this, you will choose "Script."
    - Description: Just type jibberish text in this box.
    - About URL: just type "http://www.example.com." (Without quotes)
    - Redirect URL: Same as About URL.
    - Click "Create app"
    - Keep this tab open for the "Setting up Praw.ini" section.
    - (Optional) Install Geany text editor for easy code editing and running. I only recommend this text editor because it's easy to use and install, however, this is not an absolutely required step. It's just here if you want it to make running the bot easier. (Please Note: I am not affilated with Geany or its developers in any way, it is just the first text editor that I used when learning how to code and it made running Python scripts easier.
    - Open main.py in geany.
    - To run program in geany, simply press the F5 key.
    - Thank You and I hope you enjoy this program!


# Setting up Praw.ini.
- You will next need to setup the Praw.ini file. I have included a shell file for you within the files. It is in the folder "init praw file." You will need to rename this file to praw.ini and put it in the same folder as main.py. On many online examples, you'll see people plug their credentials straight into their main python file. I discourage doing that as it just leaves your credentials out in the open for people to see if you share that file with others and forget that your credentials are still in there.
    - Open the Praw.ini shell file from the repository.
    - Open the tab with the app you just created.
    - client_id: 2 spaces underneath your script name is the client_id. Copy and paste that into your Praw.ini file under "client_id"
    - client_secret: You will see something in the applet page you just created that says "Secret." The code to the right of that is your client secret. Copy and paste that into the client secret portion of the praw.ini file.
    - password: your reddit password
    - username: your reddit username
    - user_agent: Enter jibberish here. I just put "Idk" (without the quotes.)
    - Put the praw.ini file in the same folder that the main and replier files are. Otherwise, program will have trouble importing it.


# Instructions for running bot on Linux.
- Depending on the Operating system that you are using, Python3 may already be installed. If you're unsure if it is or not, go into the terminal and check by typing "Python3 --version." If it is installed, the output of that response will tell you which Python3 version you are running.


- If Previous step turns back an error such as "Python3 not found," type "sudo apt-get install Python3" to install Python3.


- Install pip package manager in order to install the praw module. If you already have Python pip3 installed, skip this step. If you don't, or are unsure, type "sudo apt-get install Python3-pip." (If using macOS, the command is: )


- (Optional) Install Geany text editor for easy code editing and running. I only recommend this text editor because it's easy to use and install, however, this is not an absolutely required step. It's just here if you want it to make running the bot easier. (Please Note: I am not affilated with Geany or its developers in any way, it is just the first text editor that I used when learning how to code and it made running Python scripts easier.)


- Setting up the Praw.ini. (See above: Setting up the Praw.ini file.)

- Right click in the folder where main.py is and type: "Python3 main.py" in order to run the file. If you run into any errors, file an issue report.


# Installing on MacOS
- If you already have Python3 installed, follow the Linux tutorial starting with "Install Geany" as Linux and MacOS instructions are the same. If you don't know if you have Python3 installed, type "Python3 --version" in the terminal. If this returns with something like "Python 3.7.3", make sure you have pip installed by typing "pip3 --version." If both of those come back with a version number, go to the Linux install instructions. If not, continue here.

- To install Python3 and Pip on MacOS, follow [this tutorial](https://evansdianga.com/install-pip-osx/).

- After you have installed Python3 and pip for Python3, you can follow the rest of the Linux instructions as they are the same.

# Modification instructions
- to Change the subreddit this bot searches on, change the text inside the quotes of line 27
