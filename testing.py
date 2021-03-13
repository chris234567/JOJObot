import requests

try:
    ImgRequest = requests.get(
        'https://images-na.ssl-images-amazon.com/images/I/51XF7E8VT4L._SY445_.jpg'
    )

    if ImgRequest.status_code == requests.codes.ok:
        img = open("test.jpg", "wb")
        #img.write(ImgRequest.content)
        print(img)
        print(type(img))
        img.close()
    else:
        # print(ImgRequest.status_code)
        pass

except Exception as e:
    # print(str(e))
    pass
