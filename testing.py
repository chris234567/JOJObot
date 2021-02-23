import urllib.request

with urllib.request.urlopen('https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/myGif.gif') as url:
    file = url.read()
    print(type(file))

from PIL import Image
from urllib.request import urlopen
from io import BytesIO
url = 'https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/Media/myGif.gif'

img = Image.open(BytesIO(urlopen(url).read()))

# Start with first frame
img.seek(0)
img.show()

while True:
    img.seek(img.tell() + 1)
    img.show()

