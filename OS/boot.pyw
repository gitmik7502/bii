OS_KEY = '1.1U_XDV'
GAME_KEY='RRAT'
REC_KEY='STRA'

import os, time

def boot(GAME_KEY, REC_KEY):
    os.system('cls')

    def os_boot():
        print('booting OS...')
        time.sleep(5)
        os.system('cls')
        import ops
        ops.root()
          
    
    def os_check(REC_KEY):
        try:
            OS1 = open('C:/OS/ops.pyw', 'r')
            OS2 = open('C:/OS/ops.pyw', 'r')
            OS3 = open('C:/OS/ops.pyw', 'r')
            OS4= open('C:/OS/ops.pyw', 'r')
            #CHECK
            check = OS1.read()[1734:1747]
            check2 = OS2.read()[37:50]
            check3 = OS3.read()[2772:2785]
            check4 = OS4.read()[10:18]
            if check and check2 and check3 == 'SYS_INSTALLED':
                if check4 == OS_KEY:
                    pass
                else: raise ValueError('Not "1.0U_XDV"')
            else: raise ValueError('No OS Installed')
        except:
            print('''               OS currupt
            Please insert Recovery Disc...''')
            while 1:
                try:
                    REC_DISC = open('D:/disc.pyw', 'r')  
                    REC_DISK_KEY = REC_DISC.read()[7:11] 
                    print('                disc found')
                    if REC_DISK_KEY == REC_KEY:
                        REC_VER = open('D:/disc.pyw', 'r')
                        VER = REC_VER.read()[26:28]#[23:31]
                        if VER == 'U_':
                            REC_VER.close()
                            REC_DISC.close()
                            REC_DISC1 = open('D:/disc.pyw', 'r')
                            VER1 = REC_DISC1.read()[23:31]
                            print(f'                OS VERSION: {VER1}')
                            REC_RUN = open('d:/disc.pyw','r')
                            REC_DISC1.close()
                            exec(REC_RUN.read())
                            break
                        else:
                            REC_DISC1 = open('D:/disc.pyw', 'r')
                            VER1 = REC_DISC1.read()[23:27]
                            sure=input(F'are you sure you want to install {VER1} insted of {OS_KEY}?: ')
                            if sure == 'no' or 'n': break
                            REC_VER.close()
                            REC_DISC.close()
                            print(f'                OS VERSION: {VER1}')
                            REC_RUN = open('d:/disc.pyw','r')
                            REC_DISC1.close()
                            exec(REC_RUN.read())
                            break


                except:
                    import operator


    def disc_check(GAME_KEY, REC_KEY):
        try:
            DISC = open('D:/disc.pyw', 'r')
            #--------DISC KEY CHECKING
            DISC_KEY = DISC.read()[7:11] # initializing/finding the key from the Disc
            DISC.close()

            if DISC_KEY == GAME_KEY: # checking if the key from the Disc is the same as the Varible
                GAME = open('D:/disc.pyw', 'r')
                pass
                try:
                    exec(GAME.read())# executing the game by copying the code and pasting to the exec function
                except:
                    os.system('cls')
                    print('The Software Closed Because An Error Occurred')
                    os.system('pause')
                    pass

                GAME.close()
                pass

        except FileNotFoundError:
            print('No Disc')
            pass

    disc_check(GAME_KEY, REC_KEY)
    os_boot()
boot(GAME_KEY, REC_KEY)