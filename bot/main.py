#bot driver file
import discord
import random
import os
import requests
import urllib.request
from bs4 import BeautifulSoup

client = discord.Client()

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

#
# TODO: - commands auf externe funktionen auslagern
#

TOKEN1 = os.getenv('DISCORD_TOKEN')
TOKEN2 = os.getenv('W2G_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # list of commands
    if message.content.startswith('-commands'):
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
            await message.channel.send(command)
        os.remove('temp.txt')

    # initial greeting
    if message.content.startswith('-hello'):
        await message.channel.send('peep poop, im a bot:]')

    # random short quote
    if message.content.startswith('-jojo light'):
        with open(getFile(
                'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/quotes.txt',
                '.txt'
        )) as f:
            file = f.readlines()
        f.close()
        quotes = []
        for command in file:
            quotes.append(command)
        await message.channel.send(quotes[random.randint(23, len(quotes) - 1)])
        os.remove('temp.txt')

    # random long quote
    if message.content.startswith('-jojo elaborate'):
        with open(getFile(
                'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/quotes.txt',
                '.txt'
        )) as f:
            file = f.readlines()
        f.close()
        quotes = []
        for command in file:
            quotes.append(command)
        await message.channel.send(quotes[random.randint(1, len(quotes) // 2)])
        os.remove('temp.txt')

    # # random meme
    # if message.content.startswith('-jojo meme'):
    #     num = random.randint(1, 17)
    #     if num < 10:
    #         num = '0' + str(num)
    #     else:
    #         num = str(num)
    #     url = 'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/Memes/Meme' + num + '.jpg'
    #     await message.channel.send(file=discord.File(getFile(
    #         url,
    #         '.jpg'
    #     )))
    #     os.remove('temp.jpg')

    if message.content.startswith('-zawarudo'):
        await message.channel.send(file=discord.File(getFile(
            'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/myGif.gif',
            '.gif'
        )))
        os.remove('temp.gif')


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

    if message.content.startswith('-döner'):
        await message.channel.send('näääääächste bidde wasdarfssein')

    if 'meme' in message.content: # '-"search word" meme
        searchWord = message.content[1:message.content.index('meme')]
        imgUrl = 'https://www.google.com/search?q=' + \
              searchWord + \
              '%20meme&hl=en&tbm=isch&sxsrf=ALeKk01TyW9TtpcXYTSz_HTTfTato8pibQ%3A1616238371043&source=hp&biw=939&bih=1010&ei=ItdVYKvpPKS2gwfliqtI&oq=dog&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCABQrjRYijdgpjhoAXAAeACAAUWIAcsBkgEBM5gBAKABAaoBC2d3cy13aXotaW1nsAEA&sclient=img&ved=0ahUKEwirgueP3b7vAhUk2-AKHWXFCgkQ4dUDCAc&uact=5'
        A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
             )
        Agent = A[random.randrange(len(A))]
        headers = {'user-agent': Agent}
        r = requests.get(imgUrl, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        myUrl = ''

        for img in soup.findAll('a'):
            myImg = img.get('href')
            if 'pinterest' in myImg:
                myUrl = myImg[7:myImg.index('/&sa=U')]
                await message.channel.send(myUrl)
                break

        r = requests.get(myUrl, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        for img in soup.findAll('img'):
            myImg = img.get('src')
            await message.channel.send(myUrl)
            break


client.run(TOKEN1)
