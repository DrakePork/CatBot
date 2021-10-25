import discord
import random
from discord_slash import SlashCommand

client = discord.Client()

slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="fluffy animals"))


@slash.slash(name="cat", description="Shows cat")
async def cat_pic(ctx):
    from os import listdir
    from os.path import isfile, join
    folder = "/home/ubuntu/python/catbot/cat"
    animals = [f for f in listdir(folder) if isfile(join(folder, f))]
    animal = random.choice(animals)
    file = discord.File(folder + '/' + animal, filename=animal)
    embed = discord.Embed(title="Cat")
    embed.set_image(url="attachment://" + animal)
    await ctx.send(file=file, embed=embed)


# @slash.slash(name="dog", description="Shows dog")
# async def polarbear_pic(ctx):
#    from os import listdir
#    from os.path import isfile, join
#    folder = "/home/ubuntu/python/catbot/dog"
#    animals = [f for f in listdir(folder) if isfile(join(folder, f))]
#    animal = random.choice(animals)
#    file = discord.File(folder + '/' + animal, filename=animal)
#    embed = discord.Embed(title="Dog")
#    embed.set_image(url="attachment://" + animal)
#    await ctx.send(file=file, embed=embed)


@slash.slash(name="polarbear", description="Shows polarbear")
async def polarbear_pic(ctx):
    from os import listdir
    from os.path import isfile, join
    folder = "/home/ubuntu/python/catbot/polarbear"
    animals = [f for f in listdir(folder) if isfile(join(folder, f))]
    animal = random.choice(animals)
    file = discord.File(folder + '/' + animal, filename=animal)
    embed = discord.Embed(title="Polar Bear")
    embed.set_image(url="attachment://" + animal)
    await ctx.send(file=file, embed=embed)


@slash.slash(name="randocat", description="Cat Command 2.0")
async def randocat_pic(ctx):
    import requests
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    json_data = response.json()
    catUrl = json_data[0]["url"]
    embed = discord.Embed(title="Cat")
    embed.set_image(url=catUrl)
    await ctx.send(embed=embed)


@slash.slash(name="redpanda", description="Shows red panda")
async def panda_pic(ctx):
    from os import listdir
    from os.path import isfile, join
    folder = "/home/ubuntu/python/catbot/redpanda"
    animals = [f for f in listdir(folder) if isfile(join(folder, f))]
    animal = random.choice(animals)
    file = discord.File(folder + '/' + animal, filename=animal)
    embed = discord.Embed(title="Red Panda")
    embed.set_image(url="attachment://" + animal)
    await ctx.send(file=file, embed=embed)


@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return

    if message.author.id == 234658924035440640:
        await message.channel.send("wham")
    guild = message.guild.id

    async def picLoad(msg, aniType):
        if guild != 284063993155551232:
            from os import listdir
            from os.path import isfile, join
            folder = "/home/ubuntu/python/catbot/" + aniType
            animals = [f for f in listdir(folder) if isfile(join(folder, f))]
            animal = random.choice(animals)
            file = discord.File(folder + '/' + animal, filename=animal)
            embed = discord.Embed(title=aniType)
            embed.set_image(url="attachment://" + animal)
            await msg.channel.send(file=file, embed=embed)
        else:
            channel = client.get_channel(int(748501274944602214))
            await channel.send(file=discord.File('/home/ubuntu/python/catbot/cat/cat1.jpg'))

    if any(word in message.content.lower() for word in
           ["cat", "katt", "kat", "pussy", "neko", "macë", "kitte", "katu", "catua", "kotka", "maow", "gat", "eesa",
            "miu", "mau", "bushi", "kocka", "kat", "poes", "miw", "pussi", "kato", "kass", "kiisu", "domadh", "gorbe",
            "cat", "pusa", "kissa", "chat", "gnari", "pishyakan", "piscín", "cait", "kattikatze", "ket", "gata", "gati",
            "biladi", "muca", "popoki", "cha'tool", "billi", "cicamacska", "kottur", "kuching", "kutjing", "gatto",
            "bekku", "chma", "cattus", "felis", "katinas", "poocha", "kucing", "qattus", "miss", "miz", "fula",
            "shimii", "minoos", "gato", "pisica", "giat", "koshka", "kot", "marjara", "macka", "mačka", "paka", "büsi",
            "chatz", "poonai", "meo", "kedi", "kitska", "kit", "mèo", "cath", "kats", "ikati"]):
        await picLoad(message, "cat")
    elif "panda" in message.content.lower():
        await picLoad(message, "redpanda")
    elif "polarbear" in message.content.lower():
        await picLoad(message, "polarbear")
    elif "polar" in message.content.lower() and "bear" in message.content.lower():
        await picLoad(message, "polarbear")


with open("/home/ubuntu/python/catbot/token.txt", "r") as myfile:
    data = myfile.readlines()

client.run(data[0])
