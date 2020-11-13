import discord
import random
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    guild = message.guild.id

    async def catLoad(message):
        if guild != 284063993155551232:
            from os import listdir
            from os.path import isfile, join
            folder = "/home/ubuntu/python/catbot/pics"
            cats = [f for f in listdir(folder) if isfile(join(folder, f))]
            await message.channel.send(file=discord.File(folder + '/' + random.choice(cats)))
        else:
            channel = client.get_channel(int(748501274944602214))
            await channel.send(file=discord.File('/home/ubuntu/python/catbot/pics/cat1.jpg'))

    if any(word in message.content.lower() for word in ["cat", "katt", "kat", "pussy", "neko", "macë", "kitte", "katu", "catua", "kotka", "maow", "gat", "eesa", "miu", "mau", "bushi", "kocka", "kat", "poes", "miw", "pussi", "kato", "kass", "kiisu", "domadh", "gorbe", "cat", "pusa", "kissa", "chat", "gnari", "pishyakan", "piscín", "cait", "kattikatze", "ket", "gata", "gati", "biladi", "muca", "popoki", "cha'tool", "billi", "cicamacska", "kottur", "kuching", "kutjing", "gatto", "bekku", "chma", "cattus", "felis", "katinas", "poocha", "kucing", "qattus", "miss", "miz", "fula", "shimii", "minoos", "gato", "pisica", "giat", "koshka", "kot", "marjara", "macka", "mačka", "paka", "büsi", "chatz", "poonai", "meo", "kedi", "kitska", "kit", "mèo", "cath", "kats", "ikati"]):
        await catLoad(message)

with open ("/home/ubuntu/python/catbot/token.txt", "r") as myfile:
    data=myfile.readlines()

client.run(data[0])

