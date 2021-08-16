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
    await picLoad("cat", ctx)


@slash.slash(name="redpanda", description="Shows red panda")
async def panda_pic(ctx):
    await picLoad("redpanda", ctx)


async def picLoad(aniType, ctx):
    from os import listdir
    from os.path import isfile, join
    if aniType is "redpanda":
        folder = "/home/ubuntu/python/catbot/redpandapics"
    elif aniType is "cat":
        folder = "/home/ubuntu/python/catbot/catpics"
    animal = [f for f in listdir(folder) if isfile(join(folder, f))]
    await ctx.channel.send(file=discord.File(folder + '/' + random.choice(animal)))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    guild = message.guild.id

    async def picLoad(msg, type):
        if guild != 284063993155551232:
            from os import listdir
            from os.path import isfile, join
            if type is "panda":
                folder = "/home/ubuntu/python/catbot/redpandapics"
            elif type is "cat":
                folder = "/home/ubuntu/python/catbot/catpics"
            animal = [f for f in listdir(folder) if isfile(join(folder, f))]
            await msg.channel.send(file=discord.File(folder + '/' + random.choice(animal)))
        else:
            channel = client.get_channel(int(748501274944602214))
            await channel.send(file=discord.File('/home/ubuntu/python/catbot/pics/cat1.jpg'))

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
