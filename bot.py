from discord.ext.commands import Bot
from discord import Game
import random
import requests
import time
from settings import TOKEN
from scraper import BUILDDF, builds_string
from cpuscraper import CPUDF, CPUDF1

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

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
    await ctx.send("**The available builds are: **")
    await ctx.send(builds_string)


@client.command()
async def buildinfo(ctx):
    input = str(ctx.message.content[11:])
    await ctx.send("**" + input + "**")
    try:
        cpu = BUILDDF.loc[input, "CPU"]
        gpu = BUILDDF.loc[input, "GPU"]
        case = BUILDDF.loc[input, "Case"]
        price = BUILDDF.loc[input, "Price"]
        link = BUILDDF.loc[input, "Link"]
        info = ("**Price: **" + price + "\n" +
                       "**CPU: **" + cpu + "\n" +
                       "**GPU: **" + gpu + "\n" +
                       "**Case: **" + case + "\n" +
                       "**Link: **" + link + "")
    except:
        info = "Build not found, please try again! (Try copy/pasting!)"
    await ctx.send(info)


@client.command()
async def cpu(ctx):
    input = str(ctx.message.content[5:])
    await ctx.send("**" + input + "**")
    try:
        price = CPUDF.loc[input, "Price"]
        cores = CPUDF.loc[input, "Cores"]
        basespeed = CPUDF.loc[input, "Base Speed"]
        ocspeed = CPUDF.loc[input, "Overclock Speed"]
        thread = CPUDF.loc[input, "Threads"]
        tdp = CPUDF.loc[input, "Thermal Design Power"]
        ig = CPUDF.loc[input, "Integrated Graphics"]

        info = ("**Price: **" + price + "\n" +
                "**Cores: **" + cores + "\n" +
                "**Threads: **" + thread + "\n" +
                "**Base Clock: **" + basespeed + "\n" +
                "**Boost Clock: **" + ocspeed + "\n" +
                "**Integrated Graphics: **" + ig + "")
    except:
        info = "Processor not found, please try again! (Try copy/pasting!)"
    await ctx.send(info)

@client.command()
async def cpudf(ctx):
    print(CPUDF1.loc[0, "Name"])

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