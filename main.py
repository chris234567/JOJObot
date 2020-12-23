#bot driver file
import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged is as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-commands.txt'):
        commands = open('commands.txt.txt', 'r', encoding='utf-8').readlines()
        for command in commands:
            await message.channel.send(command)

    if message.content.startswith('-hello'):
        await message.channel.send('peep poop, im a bot:]')

    if message.content.startswith('-jojo light'):
        quotes = open('quotes.txt', 'r', encoding='utf-8').readlines()
        i = random.randint(23, len(quotes) - 1)
        await message.channel.send(format(quotes[i].strip()))

    if message.content.startswith('-jojo elaborate'):
        quotes = open('quotes.txt', 'r', encoding='utf-8').readlines()
        i = random.randint(1, 22)
        await message.channel.send(format(quotes[i].strip()))

    if message.content.startswith('-zawarudo'):
        await message.channel.send(file=discord.File('myGif.gif'))

client.run('NzkxMzQwMTgzODE1NTg1Nzky.X-Nu-g.e5BwC2n_rKUFx-vRBi2f2V7CEpk')


