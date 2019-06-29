from discord.ext.commands import Bot
from settings import TOKEN #THIS IS MY DISCORD TOKEN, SET TOKEN = insert token here TO RUN WITH YOUR OWN BOT
from scraper import BUILDDF, builds_string
from cpuscraper import CPUDF
from mboardscraper import MBOARDDF
from gpuscraper import GPUDF
from casescraper import CASEDF, CASEDF1
import nltk
import pandas as pd
import asyncio

BOT_PREFIX = ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)

def find_nearest(input, datalist):
    indices = []
    for string in datalist:
        indices.append(nltk.edit_distance(input, string))
    cindex = indices.index(min(indices)) #lowest index
    closest = datalist[cindex]
    return closest

colors = []

@client.event
async def on_ready():
    print("Logged in as:\n{0} (ID: {0.id})".format(client.user))

@client.command()
async def builds(ctx):
    lastcommand = "builds"
    await ctx.send("**The available builds are: **")
    await ctx.send(builds_string)

@client.command()
async def buildinfo(ctx):
    lastcommand = "buildinfo"
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
        await ctx.send("Build not found, finding closest match... (Try copy/pasting!)")
        my_list = BUILDDF.index.values
        input = find_nearest(input, my_list)
        cpu = BUILDDF.loc[input, "CPU"]
        gpu = BUILDDF.loc[input, "GPU"]
        case = BUILDDF.loc[input, "Case"]
        price = BUILDDF.loc[input, "Price"]
        link = BUILDDF.loc[input, "Link"]
        await ctx.send("**Closest Match: " + input + "**")
        info = ("**Price: **" + price + "\n" +
                       "**CPU: **" + cpu + "\n" +
                       "**GPU: **" + gpu + "\n" +
                       "**Case: **" + case + "\n" +
                       "**Link: **" + link + "")
    await ctx.send(info)

@client.command()
async def cpu(ctx):
    lastcommand = "cpu"
    input = str(ctx.message.content[5:])
    input = input.lower()
    my_list = CPUDF.index.values
    for value in my_list:
        if input in value:
            input = value
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
                "**Integrated Graphics: **" + ig + "\n" +
                "**Thermal Design Power: **" + tdp + "")
    except:
        await ctx.send("Processor not found, finding closest match...")
        input = find_nearest(input, my_list)
        price = CPUDF.loc[input, "Price"]
        cores = CPUDF.loc[input, "Cores"]
        basespeed = CPUDF.loc[input, "Base Speed"]
        ocspeed = CPUDF.loc[input, "Overclock Speed"]
        thread = CPUDF.loc[input, "Threads"]
        tdp = CPUDF.loc[input, "Thermal Design Power"]
        ig = CPUDF.loc[input, "Integrated Graphics"]
        await ctx.send("**Closest Match: " + input + "**")
        info = ("**Price: **" + price + "\n" +
                "**Cores: **" + cores + "\n" +
                "**Threads: **" + thread + "\n" +
                "**Base Clock: **" + basespeed + "\n" +
                "**Boost Clock: **" + ocspeed + "\n" +
                "**Integrated Graphics: **" + ig + "\n" +
                "**Thermal Design Power: **" + tdp + "")
    await ctx.send(info)

@client.command()
async def gpu(ctx):
    lastcommand = "gpu"
    input = str(ctx.message.content[5:])
    input = input.lower()
    my_list = GPUDF.index.values
    for value in my_list:
        if input in value:
            input = value
    await ctx.send("**" + input + "**")
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
        await ctx.send("GPU not found, finding closest match...")
        input = find_nearest(input, my_list)
        chip = GPUDF.loc[input, "Chip"]
        release = GPUDF.loc[input, "Release"]
        memory = GPUDF.loc[input, "Memory"]
        gpuclock = GPUDF.loc[input, "GPU Clock"]
        memclock = GPUDF.loc[input, "Memory Clock"]
        await ctx.send("**Closest Match: " + input + "**")
        info = ("**Release Date: **" + release + "\n" +
                "**Chip: **" + chip + "\n" +
                "**Memory: **" + memory + "\n" +
                "**GPU Clock: **" + gpuclock + "\n" +
                "**Memory Clock: **" + memclock + "")
    await ctx.send(info)

@client.command()
async def mboard(ctx):
    lastcommand = "mboard"
    input = str(ctx.message.content[8:])
    input = input.lower()
    my_list = MBOARDDF.index.values
    for value in my_list:
        if input in value:
            input = value
    await ctx.send("**" + input + "**")
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
        await ctx.send("Motherboard not found, finding closest match...")
        input = find_nearest(input, my_list)
        price = MBOARDDF.loc[input, "Price"]
        sockets = MBOARDDF.loc[input, "Sockets"]
        formfactor = MBOARDDF.loc[input, "Form Factor"]
        ramslots = MBOARDDF.loc[input, "RAM Slots"]
        maxram = MBOARDDF.loc[input, "Max RAM"]
        await ctx.send("**Closest Match: " + input + "**")
        info = ("**Price: **" + price + "\n" +
                "**Sockets: **" + sockets + "\n" +
                "**Form Factor: **" + formfactor + "\n" +
                "**RAM Slots: **" + ramslots + "\n" +
                "**Max RAM: **" + maxram + "")
    await ctx.send(info)

@client.command()
async def case(ctx):
    global lastcommand
    lastcommand = "case"
    input = str(ctx.message.content[6:])
    await ctx.send("**" + input + "**")
    input = input.lower()
    my_list = CASEDF.index.values
    for value in my_list:
        if input in value:
            input = value
    if input not in my_list:
        await ctx.send("Case not found, finding closest match...")
        input = find_nearest(input, my_list)
        await ctx.send("**Closest Match: " + input + "**")
    caseindices = 0
    my_list = list(my_list)
    for value in my_list:
        if value == input:
            caseindices += 1
    if caseindices == 1:
        price = CASEDF.loc[input, "Price"]
        typee = CASEDF.loc[input, "Type"]
        color = CASEDF.loc[input, "Color"]
        window = CASEDF.loc[input, "Window?"]
        externals = CASEDF.loc[input, 'External 5.25" Bays']
        internals = CASEDF.loc[input, 'Internal 3.5" Bays']
        data = {'Price': price,
                'Type': typee,
                'Color': color,
                'Window?': window,
                'External 5.25" Bays': externals,
                'Internal 3.5" Bays': internals}
    else:
        price = list(CASEDF.loc[input, "Price"])
        typee = list(CASEDF.loc[input, "Type"])
        color = list(CASEDF.loc[input, "Color"])
        window = list(CASEDF.loc[input, "Window?"])
        externals = list(CASEDF.loc[input, 'External 5.25" Bays'])
        internals = list(CASEDF.loc[input, 'Internal 3.5" Bays'])
        minidata = {'Price': price,
                'Type': typee,
                'Color': color,
                'Window?': window,
                'External 5.25" Bays': externals,
                'Internal 3.5" Bays': internals}
        global SELECTEDCASEDF
        SELECTEDCASEDF = pd.DataFrame(minidata)
        colors = minidata["Color"]
        await ctx.send("__Select the color you would like with `!select (number)__")
        data = ""
        for color in colors:
            data = data + "\n" + str(colors.index(color) + 1) + ": " + color
    try:
        await ctx.send(data)
    except:
        pass


@client.command()
async def select(ctx):
    input = int(ctx.message.content[8:])
    if lastcommand == "case":
        inputindex = input - 1
        price = SELECTEDCASEDF.loc[inputindex, "Price"]
        typee = SELECTEDCASEDF.loc[inputindex, "Type"]
        color = SELECTEDCASEDF.loc[inputindex, "Color"]
        window = SELECTEDCASEDF.loc[inputindex, "Window?"]
        externals = SELECTEDCASEDF.loc[inputindex, 'External 5.25" Bays']
        internals = SELECTEDCASEDF.loc[inputindex, 'Internal 3.5" Bays']
        info = ("**Price: **" + price + "\n" +
                "**Type: **" + typee + "\n" +
                "**Color: **" + color + "\n" +
                "**Window?: **" + window + "\n" +
                '**External 5.25" Bays: **' + externals + "\n" +
                '**Internal 3.5" Bays: **' + internals + "")
        await ctx.send(info)
    else:
        await ctx.send("There's nothing to select. Try using !case")





client.run(TOKEN)