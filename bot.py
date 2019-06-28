from discord.ext.commands import Bot
import random
import requests
import time
from settings import TOKEN
from scraper import BUILDDF, builds_string
#from cpuscraper import CPUDF
#from ramscraper import RAMDF
#from mboardscraper import MBOARDDF
#from gpuscraper import GPUDF
from casescraper import CASEDF
import asyncio

lastcommand = "None"

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print("Logged in as:\n{0} (ID: {0.id})".format(client.user))


@client.command()
async def builds(ctx):
    await ctx.send("**The available builds are: **")
    await ctx.send(builds_string)


@client.command()
async def buildinfo(ctx):
    input = str(ctx.message.content[11:])
    await ctx.send("**" + input + "**")
    input = input.lower()
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

'''
@client.command()
async def select(ctx):
    input = str(ctx.message.content[6:])
    if lastcommand == "None":
        await ctx.send("No command has been used recently. Try ?help for help!")
    elif lastcommand == "ram":
'''

@client.command()
async def cpu(ctx):
    input = str(ctx.message.content[5:])
    await ctx.send("**" + input + "**")
    input = input.lower()
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
                "**Integrated Graphics: **" + ig + "\n" +
                "**Thermal Design Power: **" + tdp + "")
    except:
        info = "Processor not found, please try again!"
    await ctx.send(info)

@client.command()
async def gpu(ctx):
    input = str(ctx.message.content[5:])
    await ctx.send("**" + input + "**")
    input = input.lower()
    try:
        chip = GPUDF.loc[input, "Chip"]
        release = GPUDF.loc[input, "Release"]
        bus = GPUDF.loc[input, "Bus"]
        memory = GPUDF.loc[input, "Memory"]
        gpuclock = GPUDF.loc[input, "GPU Clock"]
        memclock = GPUDF.loc[input, "Memory Clock"]
        shtr = GPUDF.loc[input, "Shaders / TMUs / ROPs"]

        info = ("**Release Date: **" + release + "\n" +
                "**Chip: **" + chip + "\n" +
                "**Memory: **" + memory + "\n" +
                "**GPU Clock: **" + gpuclock + "\n" +
                "**Memory Clock: **" + memclock + "\n" +
                "**Shaders / TMUs / ROPs: **" + shtr + "")
    except:
      info = "GPU not found, please try again!"
    await ctx.send(info)

@client.command()
async def mboard(ctx):
    input = str(ctx.message.content[8:])
    await ctx.send("**" + input + "**")
    input = input.lower()
    try:
        price = MBOARDDF.loc[input, "Price"]
        sockets = MBOARDDF.loc[input, "Sockets"]
        formfactor = MBOARDDF.loc[input, "Form Factor"]
        ramslots = MBOARDDF.loc[input, "RAM Slots"]
        maxram = MBOARDDF.loc[input, "Max RAM"]

        info = ("**Price: **" + price + "\n" +
                "**Sockets: **" + sockets + "\n" +
                "**Form Factor: **" + formfactor + "\n" +
                "**RAM Slots: **" + ramslots + "\n" +
                "**Max RAM: **" + maxram + "")
    except:
      info = "Motherboard not found, please try again!"
    await ctx.send(info)

@client.command()
async def case(ctx):
    input = str(ctx.message.content[6:])
    await ctx.send("**" + input + "**")
    input = input.lower()
    try:
        price = CASEDF.loc[input, "Price"]
        typee = CASEDF.loc[input, "Type"]
        color = CASEDF.loc[input, "Color"]
        window = CASEDF.loc[input, "Window?"]
        externals = CASEDF.loc[input, 'External 5.25" Bays']
        internals = CASEDF.loc[input, 'Internal 3.5" Bays']

        info = ("**Price: **" + price + "\n" +
                "**Type: **" + typee + "\n" +
                "**Color: **" + color + "\n" +
                "**Window?: **" + window + "\n" +
                '**External 5.25" Bays: **' + externals + "\n" +
                '**Internal 3.5" Bays: **' + internals + "")
    except AttributeError:
        info = "Case not found, please try again!"
    await ctx.send(info)


'''
@client.command()
async def ram(ctx):
    lastcommand = ram
    input = str(ctx.message.content[5:])
    mauthor = str(ctx.message.author)
    await ctx.send("**" + input + "**")
    
    try:
        price = RAMDF.loc[input, "Price"]
        rtype = RAMDF.loc[input, "Type"]
        speed = RAMDF.loc[input, "Speed"]
        module = RAMDF.loc[input, "Module"]
        ppg = RAMDF.loc[input, "PPG"]
        caslat = RAMDF.loc[input, "CAS Latency"]

        info = ("**Price: **" + price + "\n" +
                "**Type: **" + rtype + "\n" +
                "**Module: **" + module + "\n" +
                "**Speed: **" + speed + "\n" +
                "**Price per Gigabyte: **" + ppg + "\n" +
                "**CAS Latency: **" + caslat + "")
    except:
        info = "Memory not found, please try again! (Try copy/pasting!)"
        
    info = "Select the configuration you would like info on using !select (1-10)"

    await ctx.send(info)
'''


'''
    @client.event
    async def on_message(message):
        if message.author.id != client.user.id and lastcommand == "ram":
            channel = message.channel
            await channel.send('Say hello!')
            def check(m):
                return m.content == '1' and m.channel == channel and message.author.id != client.user.id
            msg = await client.wait_for('message', check=check)
            await channel.send("You said 1!".format(msg))
        elif message.author.id != client.user.id and lastcommand == "gpu":
            print("Nothing")
        else:
            print("Yeet")
'''



client.run(TOKEN)