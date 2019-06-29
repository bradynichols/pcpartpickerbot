from discord.ext.commands import Bot
from settings import TOKEN #THIS IS MY DISCORD TOKEN, SET TOKEN = insert token here TO RUN WITH YOUR OWN BOT
from buildscraper import BUILDDF, builds_string
from cpuscraper import CPUDF
from mboardscraper import MBOARDDF
from gpuscraper import GPUDF
from casescraper import CASEDF
import nltk #Natural Language Toolkit, for finding closest match
import pandas as pd


BOT_PREFIX = ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)

def find_nearest(input, datalist): #Uses nltk to find the closest match in a list datalist
    indices = []
    for string in datalist:
        indices.append(nltk.edit_distance(input, string))
    closest_index = indices.index(min(indices))
    closest = datalist[closest_index]
    return closest #Returns closest word from the list


#Says in console when the bot is ready
@client.event
async def on_ready():
    print("Logged in as:\n{0} (ID: {0.id})".format(client.user))


@client.command(name="builds",
                description="Shows available PC Builds from PCPartPicker",
                brief="Shows builds")
async def builds(ctx):
    global lastcommand
    lastcommand = "builds"
    await ctx.send("**The available builds are: **")
    await ctx.send(builds_string)

@client.command(name="buildinfo",
                description="Shows information about a particular PC build from !builds",
                brief="Info about a !builds")
async def buildinfo(ctx):
    global lastcommand
    lastcommand = "buildinfo"
    input = str(ctx.message.content[11:]) #Gathers user message contents
    await ctx.send("**" + input + "**") #Returns the user's input
    input = input.lower() #Sets input to lowercase to match dataframes
    try: #Tries to use input as a key to define the variables
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
    except: #Error occurs when the input is not in the dataframe
        await ctx.send("Build not found, finding closest match... (Try copy/pasting!)")
        names_list = BUILDDF.index.values #Builds list of all build names
        input = find_nearest(input, names_list) #Finds build that's closest to input (nltk)
        cpu = BUILDDF.loc[input, "CPU"]
        gpu = BUILDDF.loc[input, "GPU"]
        case = BUILDDF.loc[input, "Case"]
        price = BUILDDF.loc[input, "Price"]
        link = BUILDDF.loc[input, "Link"]
        await ctx.send("**Closest Match: " + input + "**") #Shows the closest match
        info = ("**Price: **" + price + "\n" +
                       "**CPU: **" + cpu + "\n" +
                       "**GPU: **" + gpu + "\n" +
                       "**Case: **" + case + "\n" +
                       "**Link: **" + link + "")
    await ctx.send(info)

@client.command(name="cpu",
                description="Shows PCPartPicker information about a particular processor",
                brief="Info about a CPU")
async def cpu(ctx):
    global lastcommand
    lastcommand = "cpu"
    input = str(ctx.message.content[5:])
    input = input.lower()
    names_list = CPUDF.index.values
    for value in names_list: #Checks if the input is anywhere in the dataframe (ex. '6700k' in 'i7-6700k')
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
        input = find_nearest(input, names_list)
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

@client.command(name="gpu",
                description="Shows GPU-Z information about a particular graphics processing unit",
                brief="Info about a GPU")
async def gpu(ctx):
    global lastcommand
    lastcommand = "gpu"
    input = str(ctx.message.content[5:])
    input = input.lower()
    names_list = GPUDF.index.values
    for value in names_list:
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
        input = find_nearest(input, names_list)
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

@client.command(name="mboard",
                description="Shows PCPartPicker information about a particular motherboard",
                brief="Info about a motherboard")
async def mboard(ctx):
    global lastcommand
    lastcommand = "mboard"
    input = str(ctx.message.content[8:])
    input = input.lower()
    names_list = MBOARDDF.index.values
    for value in names_list:
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
        input = find_nearest(input, names_list)
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

colors = [] #Needed for case command
@client.command(name="case",
                description="Shows PCPartPicker information about a particular case",
                brief="Info about a Case")
async def case(ctx):
    global lastcommand
    lastcommand = "case"
    input = str(ctx.message.content[6:])
    await ctx.send("**" + input + "**")
    input = input.lower()
    names_list = CASEDF.index.values
    for value in names_list:
        if input in value:
            input = value
    if input not in names_list:
        await ctx.send("Case not found, finding closest match...")
        input = find_nearest(input, names_list)
        await ctx.send("**Closest Match: " + input + "**")
    caseindices = 0
    names_list = list(names_list)
    for value in names_list:
        if value == input:
            caseindices += 1
    if caseindices == 1:
        price = CASEDF.loc[input, "Price"]
        casetype = CASEDF.loc[input, "Type"]
        color = CASEDF.loc[input, "Color"]
        window = CASEDF.loc[input, "Window?"]
        externals = CASEDF.loc[input, 'External 5.25" Bays']
        internals = CASEDF.loc[input, 'Internal 3.5" Bays']
        data = {'Price': price,
                'Type': casetype,
                'Color': color,
                'Window?': window,
                'External 5.25" Bays': externals,
                'Internal 3.5" Bays': internals}
    else:
        price = list(CASEDF.loc[input, "Price"])
        casetype = list(CASEDF.loc[input, "Type"])
        color = list(CASEDF.loc[input, "Color"])
        window = list(CASEDF.loc[input, "Window?"])
        externals = list(CASEDF.loc[input, 'External 5.25" Bays'])
        internals = list(CASEDF.loc[input, 'Internal 3.5" Bays'])
        minidata = {'Price': price,
                    'Type': casetype,
                    'Color': color,
                    'Window?': window,
                    'External 5.25" Bays': externals,
                    'Internal 3.5" Bays': internals}
        global SELECTED_CASEDF
        SELECTED_CASEDF = pd.DataFrame(minidata)
        colors = minidata["Color"]
        await ctx.send("__Select the color you would like with `!select (number)__")
        data = ""
        for color in colors:
            data = data + "\n" + str(colors.index(color) + 1) + ": " + color
    try:
        await ctx.send(data)
    except:
        pass


#The select command checks if the last command used is case. if it is, then it allows the user to select
#a color from the menu.
lastcommand = "none"
@client.command(name="select",
                description="Selects a case color from the menu",
                brief="Select from a menu")
async def select(ctx):
    if lastcommand == "case":
        input = int(ctx.message.content[8:])
        input_index = input - 1
        price = SELECTED_CASEDF.loc[input_index, "Price"]
        casetype = SELECTED_CASEDF.loc[input_index, "Type"]
        color = SELECTED_CASEDF.loc[input_index, "Color"]
        window = SELECTED_CASEDF.loc[input_index, "Window?"]
        externals = SELECTED_CASEDF.loc[input_index, 'External 5.25" Bays']
        internals = SELECTED_CASEDF.loc[input_index, 'Internal 3.5" Bays']
        info = ("**Price: **" + price + "\n" +
                "**Type: **" + casetype + "\n" +
                "**Color: **" + color + "\n" +
                "**Window?: **" + window + "\n" +
                '**External 5.25" Bays: **' + externals + "\n" +
                '**Internal 3.5" Bays: **' + internals + "")
        await ctx.send(info)
    else:
        await ctx.send("There's nothing to select. Try using !case")


client.run(TOKEN) #Insert token here as a string