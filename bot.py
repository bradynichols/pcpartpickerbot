from discord.ext.commands import Bot
from discord import Game
import random
import requests
import time
from settings import TOKEN
from scraper import BUILDDF

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='8ball',
                description = "Answers a yes/no question.",
                brief = "Answers from the beyond.",
                aliases = ['eight_ball', 'eightball'],
                pass_context=True)
async def eight_ball(ctx):
    possible_responses = [
        "This is a resounding no",
        "It is not looking likely",
        "It is quite possible",
        "Definitely",
        "Too hard to tell",
    ]
    await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)

@client.command(name='square')
async def square(ctx, number):
    try:
        squared = int(number)**2
        await ctx.send(str(number) + " squared is " + "**" + str(squared) + "**")
    except:
        await ctx.send("That's not a number, dummy")

@client.event
async def on_ready():
    print("Logged in as:\n{0} (ID: {0.id})".format(client.user))

@client.command()
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await ctx.send("Bitcoin price is: $" + value)

@client.command()
async def builds(ctx):
    await ctx.send("The available builds are: " + builds_string)

@client.command()
async def buildinfo(ctx):
    input = str(ctx.message.content[11:])
    await ctx.send(input + " (This is just for troubleshooting)")
    try:
        cpu = BUILDDF.loc[input, "CPU"]
        gpu = BUILDDF.loc[input, "GPU"]
        case = BUILDDF.loc[input, "Case"]
        await ctx.send("```CPU: " + cpu +
                       "GPU: " + gpu +
                       "Case: " + case + "```")
    except:
        info = "Build not found, please try again! (Try copy/pasting!)"


'''
This doesn't work because i'm retarded or something
enjoy

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers: ")
        for server in client.guilds:
            print(server.name)
        time.sleep(1)

client.loop.create_task(list_servers())
'''

client.run(TOKEN)