import pyautogui
import keyboard
import os
import datetime
import time
import random

def clearPrint(text):
    os.system('cls')
    print(text)

pyautogui.PAUSE = 1

last_work = datetime.datetime.now()
last_idle_move = datetime.datetime.now()
state = 'disconnected'
connected = ''
loggedIn = True

clearPrint("It's on baby!")

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
        os.system('cls')

def customClick(coords):
    pyautogui.moveTo(coords.x, coords.y, 1)
    pyautogui.click(clicks=2, interval=0.25)

def connectWallet(currentState):
    global loggedIn
    connect_wallet_im1 = pyautogui.locateCenterOnScreen('connect_wallet_01.png', confidence=0.7)
    if connect_wallet_im1 != None:
        customClick(connect_wallet_im1)
        return 'to_asign'
        
    else:
     connect_wallet_im2 = pyautogui.locateCenterOnScreen('connect_wallet_02.png', confidence=0.7)
     if connect_wallet_im2 != None:
        customClick(connect_wallet_im2)
        return 'to_asign'
    
    return currentState

def asign(currentState):
    global loggedIn
    asign_im1 = pyautogui.locateCenterOnScreen('assinar.png', confidence=0.8)
    if asign_im1 != None:
        customClick(asign_im1)
        loggedIn = True
        return 'to_expan'

    return currentState

def reAsign(currentState):
    global loggedIn
    global state
    menu_im = pyautogui.locateCenterOnScreen('menu.png', confidence=0.8)
    if menu_im != None:
        print('olhau')
        state = 'to_heroes'
        return 'to_heroes'
    asign_im1 = pyautogui.locateCenterOnScreen('assinar.png', confidence=0.8)
    if asign_im1 != None:
        print('reasinou')
        customClick(asign_im1)
        loggedIn = True
        return 'to_heroes'

    return currentState

def expandGameWindow(currentState):
    expand_game_Window_im1 = pyautogui.locateCenterOnScreen('expan_game.png', confidence=0.8)
    if expand_game_Window_im1 != None:
        customClick(expand_game_Window_im1)
        return 'to_heroes'
    return currentState

def openHeroesWindow(currentState):
    heroes_im1 = pyautogui.locateCenterOnScreen('heroes.png', confidence=0.8)
    if heroes_im1 != None:
        customClick(heroes_im1)
        return 'to_all_work'
    return currentState

def closeHeroesWindow(currentState):
    close_im1 = pyautogui.locateCenterOnScreen('close.png', confidence=0.7)
    if close_im1 != None:
        customClick(close_im1)
        return 'to_treasure_hunt'
    return currentState

def putAllHeroesToWork(currentState):
    if pyautogui.locateOnScreen('all_on.png') != None:
        all_on_im1 = pyautogui.locateCenterOnScreen('all_on.png', confidence=0.8)
        customClick(all_on_im1)
        return 'to_close'

    elif pyautogui.locateOnScreen('all_work_again.png') != None:
        all_work_again_im1 = pyautogui.locateCenterOnScreen('all_work_again.png')
        customClick(all_work_again_im1)
        return 'to_close'
        
    else:
        print('vazei')
        return 'to_close'

    return currentState

def backToMenu(currentState):
    back_menu_im1 = pyautogui.locateCenterOnScreen('back_menu.png', confidence=0.8)
    if back_menu_im1 != None:
        customClick(back_menu_im1)
        return 'to_heroes'
    return currentState

def goTreasureHunt(currentState):
    treasure_hunt_im1 = pyautogui.locateCenterOnScreen('treasure_hunt.png', confidence=0.8)
    if treasure_hunt_im1 != None:
        customClick(treasure_hunt_im1)
        return 'farming'
    return currentState

def idleMovement(currentState):
    global last_idle_move
    idle_target_im1 = pyautogui.locateCenterOnScreen('chest.png')
    if idle_target_im1 != None:
        customClick(idle_target_im1)
        time.sleep(random.randint(1,9))
        idle_target_2_im1 = pyautogui.locateCenterOnScreen('close.png')
        if idle_target_2_im1 != None:
            customClick(idle_target_2_im1)
        
            last_idle_move = datetime.datetime.now()
        
            return 'farming'
    return currentState

def checkIfDisconnected():
    global state
    global loggedIn
    
    if pyautogui.locateOnScreen('login_expired.png', confidence=0.8) != None:
        ok_im1 = pyautogui.locateCenterOnScreen('ok.png', confidence=0.8)
        if ok_im1 != None:
            customClick(ok_im1)
            state = 'disconnected'
        
        ok_im2 = pyautogui.locateCenterOnScreen('ok2.png', confidence=0.8)
        if ok_im2 != None:
            customClick(ok_im2)
            state = 'disconnected'
    elif loggedIn:
        connect_wallet_02_im = pyautogui.locateCenterOnScreen('connect_wallet_02.png', confidence=0.8)
        if connect_wallet_02_im != None:
            print('deu ruim')
            loggedIn = False
            customClick(connect_wallet_02_im)
            pyautogui.click()
            time.sleep(10)
            state = 'to_re_asign'

while 1:
    print(state)
#     clearPrint('''LoggedIn: %r
# Atividade Atual: %s
# Proximo movimento de presença: %ds
# Fim do descanço em: %dm''' % (loggedIn, state, 1 * 60 - (datetime.datetime.now() - last_idle_move).seconds, (45 * 60 - (datetime.datetime.now() - last_work).seconds)/ 60))

    if state == 'disconnected':
        state = connectWallet(state)

    elif state == 'to_asign':
        state = asign(state)
    
    elif state == "to_re_asign":
        state == reAsign(state)
    
    elif state == 'to_expan':
        state = expandGameWindow(state)

    elif state == 'to_heroes':
        state = openHeroesWindow(state)
    
    elif state == 'to_all_work':
        state = putAllHeroesToWork(state)
    
    elif state == 'to_close':
        state = closeHeroesWindow(state)
    
    elif state == 'to_treasure_hunt':
        state = goTreasureHunt(state)
    
    elif state == 'back_menu':
        state = backToMenu(state)

    elif state == 'idle_move':
        state = idleMovement(state)
    
    elif state == 'farming' and (datetime.datetime.now() - last_work).seconds > 45 * 60:
        state = 'back_menu'

    elif state == 'farming' and (datetime.datetime.now() - last_idle_move).seconds > 5 * 60:
        state = 'idle_move'

    checkIfDisconnected()
    time.sleep(1)