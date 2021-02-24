# import urllib.request
#
# with urllib.request.urlopen('https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/myGif.gif') as url:
#     file = url.read()
#     print(type(file))
#
# from PIL import Image
# from urllib.request import urlopen
# from io import BytesIO
# url = 'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/myGif.gif'
#
# img = Image.open(BytesIO(urlopen(url).read()))
#
# # Start with first frame
# img.seek(0)
# img.show()
#
# while True:
#     img.seek(img.tell() + 1)
#     img.show()
#

import urllib.request

with urllib.request.urlopen('https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/quotes1.txt') as url:
    quotes = str(url.read())
    quotes = quotes.replace('b\'', '')
    quotes += '\\r\\n'
    quotes = quotes.replace('\\r\\n', '$')
    quotesList = []
    temp = ''
    for c in quotes:
        if c == '$':
            quotesList.append(temp)
            temp = ''  # reset
        elif ord(c) >= 65 and ord(c) <= 90 or ord(c) >= 97 and ord(c) <= 122 \
                or ord(c) == 42 or ord(c) == 44 or ord(c) == 45 or ord(c) == 46 or ord(c) == 32: # cuts every special character except * , . - SP
            temp += c
    for quote in quotesList:
        print(quote)