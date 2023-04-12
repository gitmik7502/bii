OS_KEY = "1.1U_XDV"
UI_KEY = "1.3E"
GAME_KEY = 'RRAT'
UP_KEY = 'LKIQ'

import os, time, shutil

#custom channel checking
try:
    import custom_channels.channel1 as channel1
    chan1 = channel1.title()
except:
    chan1 = ''
    pass
try:
    import custom_channels.channel2 as channel2
    chan2 = channel2.title()
except:
    chan2 = ''
    pass
try:
    import custom_channels.channel3 as channel3
    chan3 = channel3.title()
except:
    chan3 = ''
    pass
#-----------------------
def shop_channel():
    import requests
    print('Checking Apps...')
    url = 'https://codeload.github.com/gitmik7502/programshop/zip/refs/heads/main'

    # Downloading the file by sending the request to the URL
    req = requests.get(url)
 
 
    # Writing the file to the local file system
    with open('c:/OS/temp/apps.zip','wb') as output_file:
        output_file.write(req.content)
    import zipfile
    with zipfile.ZipFile('c:/OS/temp/apps.zip', 'r') as zip_ref:
        zip_ref.extractall('c:/OS/temp/')
        try:
            os.rename('c:/OS/temp/programshop-main', 'c:/OS/temp/programshop')
        except:
            shutil.rmtree('c:/OS/temp/programshop')
            os.rename('c:/OS/temp/programshop-main', 'c:/OS/temp/programshop')
        import temp.programshop as prog
        print('Avaible Channels')
        print(prog.prog_tiles())
        i = input('Download: ')
        if i in prog.prog_tiles():
            channel_num = input(f'which channel should {i} install to?(in numbers 1, 2 or 3): ')
            os.system(f'md "c:/os/custom_channels/channel{channel_num}"')
            os.system(f'copy c:\\OS\\temp\\programshop\\{i}.py "c:/OS/custom_channels/channel{channel_num}/__init__.py"')

def menu():
    while 1:
        print('Channels:')
        print('Shop channel')
        if chan1 == '':
            pass
        else:
            print(chan1)
        if chan2 == '':
            pass
        else:
            print(chan2)
        if chan3 == '':
            pass
        else:
            print(chan3)
        channel = input()
        if channel == 'shop':
            shop_channel()
        elif channel == chan1:
            if chan1 == '':
                pass
            else: channel1.run()
        elif channel == chan2:
            if chan2 == '':
                pass
            else: channel2.run()
        elif channel == chan3:
            if chan3 == '':
                pass
            else: channel3.run()
        else:
            os.system('cls')
            print('invalid channel try again.')

menu()