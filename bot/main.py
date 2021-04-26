# bot driver file
import os
import random
import time

import discord
import requests
from discord.ext import commands
import urllib.request
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix="!")
TOKEN1 = os.getenv('DISCORD_TOKEN')
TOKEN2 = os.getenv('W2G_TOKEN')


# function to get(temporarily create) file located in the cloud, referenced by a public url
def getFile(url: str, fileType: str):
    myFile = 'temp' + fileType
    try:
        ImgRequest = requests.get(url)
        if ImgRequest.status_code == requests.codes.ok:
            img = open(myFile, 'wb')
            img.write(ImgRequest.content)
            img.close()
        else:
            # print(ImgRequest.status_code)
            pass
    except Exception as e:
        # print(str(e))
        pass
    return myFile


@client.event
async def on_ready():
    print('{0.user} has logged in.'.format(client))


@client.command()
async def commands(ctx):
    try:
        fileRequest = requests.get(
            'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/commands.txt'
        )
        if fileRequest.status_code == requests.codes.ok:
            file = open('temp.txt', 'wb')
            file.write(fileRequest.content)
            file.close()
        else:
            # print(ImgRequest.status_code)
            pass
    except Exception as e:
        # print(str(e))
        pass
    with open('temp.txt') as f:
        file = f.readlines()
    f.close()
    for command in file:
        await ctx.channel.send(command)
    os.remove('temp.txt')


@client.command()
async def hello(ctx):
    await ctx.channel.send('peep poop, im a bot:]')


# random short quote
@client.command()
async def jojo_light(ctx):
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


# random long quote
@client.command()
async def jojo_elaborate(ctx):
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


# # random meme
# @client.command()
# async def jojo_meme(ctx):
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


# stops time
@client.command()
async def zawarudo(ctx):
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
    voice.play(discord.FFmpegPCMAudio(executable='ffmpeg\\ffmpeg.exe', source=file))
    while ctx.voice_client.is_playing():
        time.sleep(1)
    await ctx.voice_client.disconnect()
    os.remove('temp.gif')
    os.remove('temp.mp3')


# cranks dat boi
@client.command()
async def soulja(ctx):
    file = getFile(
        'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/Its+ya+boi+soulja+boy+in+dubai.mp3',
        '.mp3'
    )
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(executable='./ffmpeg/ffmpeg.exe',
                                      source=file))
    while ctx.voice_client.is_playing():
        time.sleep(1)
    await ctx.voice_client.disconnect()


# creates a watch2gether room
@client.command()
async def w2g(ctx):
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
async def döner(ctx):
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
