import discord
import random
from discord_slash import SlashCommand

client = discord.Client()

slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@slash.slash(name="cat", description="Shows cat")
async def cat_pic(ctx):
    from os import listdir
    from os.path import isfile, join
    folder = "/home/ubuntu/python/catbot/catpics"
    animals = [f for f in listdir(folder) if isfile(join(folder, f))]
    animal = random.choice(animals)
    file = discord.File(folder + '/' + animal, filename=animal)
    embed = discord.Embed(title="Cat")
    embed.set_image(url="attachment://" + animal)
    await ctx.send(file=file, embed=embed)


@slash.slash(name="randocat", description="Cat Command 2.0")
async def randocat_pic(ctx):
    import json
    import requests

    response = requests.get("https://api.thecatapi.com/v1/images/search")
    # response.headers["x-api-key"] = "adb1f5c4-5871-4143-b810-822080facd7d"
    json_data = response.json()
    await ctx.send(json_data)


@slash.slash(name="redpanda", description="Shows red panda")
async def panda_pic(ctx):
    from os import listdir
    from os.path import isfile, join
    folder = "/home/ubuntu/python/catbot/redpandapics"
    animals = [f for f in listdir(folder) if isfile(join(folder, f))]
    animal = random.choice(animals)
    file = discord.File(folder + '/' + animal, filename=animal)
    embed = discord.Embed(title="Red Panda")
    embed.set_image(url="attachment://" + animal)
    await ctx.send(file=file, embed=embed)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    guild = message.guild.id

    async def picLoad(msg, aniType):
        if guild != 284063993155551232:
            from os import listdir
            from os.path import isfile, join
            if aniType is "panda":
                folder = "/home/ubuntu/python/catbot/redpandapics"
            elif aniType is "cat":
                folder = "/home/ubuntu/python/catbot/catpics"
            animals = [f for f in listdir(folder) if isfile(join(folder, f))]
            animal = random.choice(animals)
            file = discord.File(folder + '/' + animal, filename=animal)
            embed = discord.Embed(title=aniType)
            embed.set_image(url="attachment://" + animal)
            await msg.channel.send(file=file, embed=embed)
        else:
            channel = client.get_channel(int(748501274944602214))
            await channel.send(file=discord.File('/home/ubuntu/python/catbot/catpics/cat1.jpg'))

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
        await picLoad(message, "panda")


with open("/home/ubuntu/python/catbot/token.txt", "r") as myfile:
    data = myfile.readlines()

client.run(data[0])
