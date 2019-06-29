# PCPartPickerBot
![PCPartPicker Logo](http://u.cubeupload.com/bradyfish/PCPartPickerLogo.png)

NOTE: I am not affiliated with PCPartPicker in any way. This bot does not represent their competence in creating discord bots.

Any questions about the bot or anything: Bradyfish#7396 on discord!
I will not post the bot's invite link as of now because I don't plan on hosting it for the time being.

Hello everyone, welcome to my bot! The goal for the week was to create a discord bot that could give out information about builds and components on the fly. This would help immensely when talking to my friends about building PCs becuase I would be able to simply show them stats and easily compare components.

Some background about myself, I'm a 16-yo high school student who codes in his spare time. I decided to create this bot using python/discord.py because I'm most comfortable with python. I've always been interested in computers and my friend group helps each other build computers often, which is where I got the inspiration for this bot.

The base of this is to gather data from different websites, mainly PCPartPicker, and store it in a place where it can then be accessed through various commands.
The "datacollector.py" file collects all of the required data from various websites using requests and Selenium and stores it in the "storeddata" folder as a .txt file. Since it's a small-scale project, I opted not to use any databases or fancy file types for storage.
Each one of the files titled "xscraper.py" is one of the files that extracts this data and, using BeautifulSoup, puts it into pandas dataframes. Each of these dataframes is imported at the top of "bot.py", the main file.

Each command basically picks out the row of the dataframe that contains the specified component and reads the component's data out to the user. There are some measures in place to ensure that typos are not an issue (find_nearest and making everything lowercase) as well as ensuring that you can type shortened versions of component names (ex. "6700k" instead of "Intel Core i7-6700k", both work).

In the case of the "case" command, some cases come in multiple colors. When this happens, the bot sends a list that the user can choose from of colors. The user can then use !select to select a number corresponding to a color and get the stats from that color.

NOTE: You do not need Selenium to run the bot, only if you wish to update the .txt files. Selenium is only used in datacollector.py.

Here are some images of the bot in action. Enjoy!

![CPU Command](http://u.cubeupload.com/bradyfish/9008ae7d1934077b7233.png)
![GPU Command](http://u.cubeupload.com/bradyfish/4311573a9e4488eee02b.png)
![CPU Command Mispelled](http://u.cubeupload.com/bradyfish/af2fc9e5f0fd44dcfc8e.png)
![Builds Command](http://u.cubeupload.com/bradyfish/bb471017ad1edf358d12.png)
![Case and Select Commands](http://u.cubeupload.com/bradyfish/3a673c1647cef615cf14.png)
![Motherboard Command](http://u.cubeupload.com/bradyfish/756f9274909bbb4540a2.png)

![GitHub Hack Week Logo](https://u.cubeupload.com/bradyfish/hackbadgeblack.png)

Thanks for checking my bot out, and have an awesome day!

