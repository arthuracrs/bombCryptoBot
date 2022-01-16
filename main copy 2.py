from sqlite3 import connect
import pyautogui
import keyboard
import os
import datetime
import time

clear = lambda: os.system('cls')
clear()

def clearPrint(text):
    clear()
    print(text)

print("It's on baby!")

working = False

last_work = datetime.datetime.now()
last_idle_move = datetime.datetime.now()

pyautogui.PAUSE = 2

state = 'to_connect'

connected = ''
while connected != 's':
    connected = input("Você já está conectado na MetaMask? (s/n): ")
    if connected == 's':
        if input('Voce já está com o jogo aberto? (s/n): ') == 's':
            state = 'to_heroes'
        else:
            os.system('start chrome https://app.bombcrypto.io/')
    else:
        clearPrint('Faça login na MetaMask!')
        input('Precione Enter para continuar')
        clear()

def connectWallet():
    connect_wallet_im1 = pyautogui.locateCenterOnScreen('connect_wal.png', confidence=0.7)
    pyautogui.click(connect_im1)
    state = 'to_asign'

while 1:
    clearPrint('Atividade Atual: %s || Proximo movimento de presença: %ds || Fim do descanço em: %dm' % (state, 1 * 60 - (datetime.datetime.now() - last_idle_move).seconds, (45 * 60 - (datetime.datetime.now() - last_work).seconds)/ 60))

    if state == 'to_connect' and pyautogui.locateOnScreen('connect.png') != None:
        connect_im1 = pyautogui.locateCenterOnScreen('connect.png')
        pyautogui.doubleClick(connect_im1)
        state = 'to_asign'

    if state == 'to_connect' and pyautogui.locateOnScreen('connect_wal.png', confidence=0.7) != None:
        connect_im1 = pyautogui.locateCenterOnScreen('connect_wal.png', confidence=0.7)
        pyautogui.doubleClick(connect_im1)
        state = 'to_asign'

    if state == 'to_asign' and pyautogui.locateOnScreen('assinar.png', confidence=0.7) != None:
        assinar_im1 = pyautogui.locateCenterOnScreen('assinar.png')
        pyautogui.doubleClick(assinar_im1)
        state = 'to_heroes'

    if state == 'to_expan' and pyautogui.locateOnScreen('expan_game.png', confidence=0.8) != None:
        expan_game_im1 = pyautogui.locateCenterOnScreen('expan_game.png', confidence=0.8)
        pyautogui.doubleClick(expan_game_im1)
        state = 'to_heroes'

    if state == 'to_heroes' and pyautogui.locateOnScreen('heroes.png') != None:
        heroes_im1 = pyautogui.locateCenterOnScreen('heroes.png')
        pyautogui.doubleClick(heroes_im1)
        state = 'to_all_work'
    
    if state == 'to_all_work':
        time.sleep(3)
        if pyautogui.locateOnScreen('all_on.png') != None:
            all_on_im1 = pyautogui.locateCenterOnScreen('all_on.png', confidence=0.8)
            pyautogui.click(all_on_im1)
            print('shazam')
            state = 'to_close'
        
        elif pyautogui.locateOnScreen('all_work_again.png') != None:
            all_work_again_im1 = pyautogui.locateCenterOnScreen('all_work_again.png')
            pyautogui.click(all_work_again_im1)
            state = 'to_close'
        
        else:
            print('vazei')
            state = 'to_close'
    
    if state == 'to_close' and pyautogui.locateOnScreen('close.png', confidence=0.8) != None:
        close_im1 = pyautogui.locateCenterOnScreen('close.png', confidence=0.8)
        pyautogui.doubleClick(close_im1)
        pyautogui.click(close_im1)
        state = 'to_treasure_hunt'
    
    if state == 'to_treasure_hunt' and pyautogui.locateOnScreen('treasure_hunt.png') != None or state == 'to_close' and pyautogui.locateOnScreen('treasure_hunt.png') != None:
        treasure_hunt_im1 = pyautogui.locateCenterOnScreen('treasure_hunt.png')
        pyautogui.doubleClick(treasure_hunt_im1)
        
        last_work = datetime.datetime.now()
        last_idle_move = datetime.datetime.now()
        
        state = 'farming'

    if state == 'back_menu' and pyautogui.locateOnScreen('back_menu.png') != None:
        back_menu_im1 = pyautogui.locateCenterOnScreen('back_menu.png')
        pyautogui.doubleClick(back_menu_im1)
        state = 'to_heroes'

    if state == 'farming' and (datetime.datetime.now() - last_work).seconds > 45 * 60:
        state = 'back_menu'

    if state == 'idle_move' and pyautogui.locateOnScreen('idle_target_2.png') != None:
        idle_target_im1 = pyautogui.locateCenterOnScreen('idle_target.png')
        pyautogui.doubleClick(idle_target_im1)
        
        idle_target_2_im1 = pyautogui.locateCenterOnScreen('idle_target_2.png')
        pyautogui.doubleClick(idle_target_2_im1)
        
        last_idle_move = datetime.datetime.now()
        
        state = 'farming'

    if state == 'farming' and (datetime.datetime.now() - last_idle_move).seconds > 1 * 60:
        state = 'idle_move'
    
    if (state == 'farming' or state == 'to_re_asign'or state == 'to_heroes') and pyautogui.locateOnScreen('connect_wal.png', confidence=0.8) != None:
        connect_wal_im1 = pyautogui.locateCenterOnScreen('connect_wal.png', confidence=0.8)
        pyautogui.doubleClick(connect_wal_im1)
        state = 'to_asign'

    if pyautogui.locateOnScreen('login_expired.png', confidence=0.8) != None:
        exp_im1 = pyautogui.locateCenterOnScreen('ok.png', confidence=0.8)
        pyautogui.doubleClick(exp_im1)
        state = 'to_connect'

    if pyautogui.locateOnScreen('ok.png', confidence=0.8) != None:
        ok_im1 = pyautogui.locateCenterOnScreen('ok.png', confidence=0.8)
        pyautogui.doubleClick(ok_im1)
        state = 'to_connect'

    if pyautogui.locateOnScreen('ok2.png', confidence=0.8) != None:
        ok2_im1 = pyautogui.locateCenterOnScreen('ok2.png', confidence=0.8)
        pyautogui.doubleClick(ok2_im1)
        state = 'to_connects'