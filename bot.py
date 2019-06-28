from discord.ext.commands import Bot
from settings import TOKEN #THIS IS MY DISCORD TOKEN, SET TOKEN = insert token here TO RUN WITH YOUR OWN BOT
from scraper import BUILDDF, builds_string
from cpuscraper import CPUDF
from mboardscraper import MBOARDDF
from gpuscraper import GPUDF
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
        memory = GPUDF.loc[input, "Memory"]
        gpuclock = GPUDF.loc[input, "GPU Clock"]
        memclock = GPUDF.loc[input, "Memory Clock"]

        info = ("**Release Date: **" + release + "\n" +
                "**Chip: **" + chip + "\n" +
                "**Memory: **" + memory + "\n" +
                "**GPU Clock: **" + gpuclock + "\n" +
                "**Memory Clock: **" + memclock + "")
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
async def select(ctx):
    input = str(ctx.message.content[6:])
    if lastcommand == "None":
        await ctx.send("No command has been used recently. Try ?help for help!")
    elif lastcommand == "ram":
'''


client.run(TOKEN)