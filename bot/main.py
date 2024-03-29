import os
import random
import time
import urllib.request

import requests
import discord
from discord.ext import commands
from bs4 import BeautifulSoup

from functionality import getFile

client = commands.Bot(command_prefix="!")
TOKEN1 = os.getenv('DISCORD_TOKEN')
TOKEN2 = os.getenv('W2G_TOKEN')


@client.event
async def on_ready():
    print('{0.user} has logged in.'.format(client))


@client.command()
async def commands(ctx):
    commands_txt = getFile('https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/commands2.txt', '.txt')
    with open(commands_txt) as f:
        file = f.readlines()
    commands_string = ""
    for command in file:
        commands_string += command
    f.close()
    await ctx.channel.send(commands_string)
    os.remove('temp.txt')
    print(commands_string)

@client.command()
async def hello(ctx):
    await ctx.channel.send('peep poop, im a bot:]')


@client.command()
async def jojo_light(ctx):
    """random short quote"""
    with open(getFile(
            'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/quotes.txt',
            '.txt'
    )) as f:
        file = f.readlines()
    f.close()
    quotes = []
    for command in file:
        quotes.append(command)
    await ctx.channel.send(quotes[random.randint(23, len(quotes) - 1)])
    os.remove('temp.txt')


@client.command()
async def jojo_elaborate(ctx):
    """random long quote"""
    with open(getFile(
            'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/quotes.txt',
            '.txt'
    )) as f:
        file = f.readlines()
    f.close()
    quotes = []
    for command in file:
        quotes.append(command)
    await ctx.channel.send(quotes[random.randint(1, len(quotes) // 2)])
    os.remove('temp.txt')


# @client.command()
# async def jojo_meme(ctx):
#     """random meme"""
#     num = random.randint(1, 17)
#     if num < 10:
#         num = '0' + str(num)
#     else:
#         num = str(num)
#     url = 'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/Memes/Meme' + num + '.jpg'
#     await ctx.channel.send(file=discord.File(getFile(
#         url,
#         '.jpg'
#     )))
#     os.remove('temp.jpg')


@client.command()
async def zawarudo(ctx):
    """stops time"""
    await ctx.channel.send(file=discord.File(getFile(
        'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/myGif.gif',
        '.gif'
    )))
    file = getFile(
        'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/ZA+WARUDO.mp3',
        '.mp3'
    )

    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(file))
    while ctx.voice_client.is_playing():
        time.sleep(1)
    await ctx.voice_client.disconnect()
    os.remove('temp.gif')
    os.remove('temp.mp3')


@client.command()
async def soulja(ctx):
    """cranks dat boi"""
    file = getFile(
        'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/Its+ya+boi+soulja+boy+in+dubai.mp3',
        '.mp3'
    )
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(file))
    while ctx.voice_client.is_playing():
        time.sleep(1)
    await ctx.voice_client.disconnect()
    os.remove('temp.mp3')


@client.command()
async def w2g(ctx):
    """sends url to newly created w2g room"""
    url = 'https://w2g.tv/rooms/create.json'
    myObj = {
        'w2g_api_key': TOKEN2,
        'share': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'bg_color': '#00ff00',
        'bg_opacity': '50',
    }
    myRequest = requests.post(url, data=myObj)

    await ctx.channel.send('https://w2g.tv/rooms/' + myRequest.text[29: 47: 1])


@client.command()
async def wecker(ctx):
    """aufstehen!!"""
    file = getFile(
        'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/MontanaWecker+Der+Monte+Wecker+2.0+MontanaBlack+Clips.mp3',
        '.mp3'
    )

    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(file))
    while ctx.voice_client.is_playing():
        time.sleep(1)
    await ctx.voice_client.disconnect()
    os.remove('temp.mp3')


@client.command()
async def juri(ctx):
    """triggerbot"""
    await ctx.channel.send(file=discord.File(getFile(
        'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/gmzogga_ist_top.gif',
        '.gif'
    )))
    file = getFile(
        'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/gmzogga_ist_top+(online-audio-converter.com).mp3',
        '.mp4'
    )

    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(file))
    while ctx.voice_client.is_playing():
        time.sleep(1)
    await ctx.voice_client.disconnect()
    os.remove('temp.gif')
    os.remove('temp.mp4')


@client.command()
async def doener(ctx):
    """aufnahme der naechsten bestellung"""
    await ctx.channel.send('näääääächste bidde wasdarfssein')


# # TODO: On Message Loesung??
# @client.command()
# async def meme(ctx):
# if 'meme' in message.content: # '-"search word" meme
#     searchWord = message.content[1:message.content.index('meme')]
#     imgUrl = 'https://www.google.com/search?q=' + \
#           searchWord + \
#           '%20meme&hl=en&tbm=isch&sxsrf=ALeKk01TyW9TtpcXYTSz_HTTfTato8pibQ%3A1616238371043&source=hp&biw=939&bih=1010&ei=ItdVYKvpPKS2gwfliqtI&oq=dog&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCABQrjRYijdgpjhoAXAAeACAAUWIAcsBkgEBM5gBAKABAaoBC2d3cy13aXotaW1nsAEA&sclient=img&ved=0ahUKEwirgueP3b7vAhUk2-AKHWXFCgkQ4dUDCAc&uact=5'
#     A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
#          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
#          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
#          )
#     Agent = A[random.randrange(len(A))]
#     headers = {'user-agent': Agent}
#     r = requests.get(imgUrl, headers=headers)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     myUrl = ''
#
#     for img in soup.findAll('a'):
#         myImg = img.get('href')
#         if 'pinterest' in myImg:
#             myUrl = myImg[7:myImg.index('/&sa=U')]
#             await message.channel.send(myUrl)
#             break
#
#     r = requests.get(myUrl, headers=headers)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     for img in soup.findAll('img'):
#         myImg = img.get('src')
#         await message.channel.send(myUrl)
#         break


# @client.command()
# async def play(ctx):
#     voice_channel = ctx.author.voice.channel
#     await voice_channel.connect()
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     voice.play(discord.FFmpegPCMAudio(executable="C:\\ProgramData\\chocolatey\\bin\\ffmpeg.exe", source="C:\\Users\\Chris\\Downloads\\ZA WARUDO.mp3"))
#
#     while ctx.voice_client.is_playing():
#         time.sleep(1)
#     await ctx.voice_client.disconnect()

#
# warum geht das nicht
# @client.command()
# async def leave(ctx):
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_connected():
#         await voice.disconnect()
#     else:
#         await ctx.send("The bot is not connected to a voice channel.")


client.run(TOKEN1)
