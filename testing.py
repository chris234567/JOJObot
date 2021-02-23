import urllib.request

with urllib.request.urlopen('https://chrisdiscordpybucket.s3.eu-central-1.amazonaws.com/commands.txt') as url:
    commands = str(url.read())
    commands = commands.replace('b\'', '')
    commands = commands.replace('\\r\\n', '$')
    temp = ''
    for command in commands:
        if command == '$':
            print(temp)
            print('')
            temp = '' #reset
        else:
            temp += command
