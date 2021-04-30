import requests

def getFile(url: str, fileType: str):
    """function to get(temporarily create) file located in the cloud, referenced by a public url"""
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


