#bot driver file
import discord
import random
import os
import requests

client = discord.Client()

#token = open('token.txt', 'r', encoding='utf-8').readlines()
TOKEN1 = os.getenv("DISCORD_TOKEN")
TOKEN2 = os.getenv("W2G_TOKEN")
dirname = os.path.dirname(__file__)

@client.event
async def on_ready():
    print('We have logged is as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # list of commands
    if message.content.startswith('-commands'):
        commands = open('bot\commands.txt', 'r', encoding='utf-8').readlines()
        for command in commands:
            await message.channel.send(command)

    # inital greeting
    if message.content.startswith('-hello'):
        await message.channel.send('peep poop, im a bot:]')

    # random short quote
    if message.content.startswith('-jojo light'):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        filename = os.path.join(fileDir, '/Media/quotes.txt')
        quotes = open(filename, 'r', encoding='utf-8').readlines()
        i = random.randint(23, len(quotes) - 1)
        await message.channel.send(format(quotes[i].strip()))

    # random long quote
    if message.content.startswith('-jojo elaborate'):
        quotes = open('https://github.com/chris234567/JOJObot/tree/master/bot/Media/quotes.txt', 'r', encoding='utf-8').readlines()
        i = random.randint(1, 22)
        await message.channel.send(format(quotes[i].strip()))

    # random meme
    if message.content.startswith('-jojo meme'):
        path = r"https://github.com/chris234567/JOJObot/tree/master/bot/Media/Memes"
        random_filename = random.choice([
            x for x in os.listdir(path)
            if os.path.isfile(os.path.join(path, x))
        ])
        await message.channel.send(file=discord.File('Media\Memes\\' + random_filename))

    if message.content.startswith('-zawarudo'):
        await message.channel.send(file=discord.File('https://github.com/chris234567/JOJObot/tree/master/bot/Media/myGif.gif'))

    if message.content.startswith('-w2g'):
        url = 'https://w2g.tv/rooms/create.json'
        myObj = {
        'w2g_api_key' : TOKEN2,
        'share' : 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'bg_color' : '#00ff00',
        'bg_opacity' : '50',
        }
        myRequest = requests.post(url, data = myObj)

        await message.channel.send('https://w2g.tv/rooms/' + myRequest.text[29: 47: 1])

client.run(TOKEN1)