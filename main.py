import pyautogui
import keyboard
import os
import datetime
import time
import random
import json


configFile = json.load(open('./config.json'))
assetsPath = configFile['assetsPath']


def clearPrint(text):
    os.system('cls')
    print(text)


pyautogui.PAUSE = 1

last_work = datetime.datetime.now()
last_idle_move = datetime.datetime.now()

logsPath = configFile['logsPath']
if not os.path.exists(logsPath):
    os.makedirs(logsPath)
logFilePath = logsPath + "/log-"+datetime.datetime.now().strftime("%Y-%m-%d--%H.%M.%S")+".txt"

state = 'disconnected'
lastState = state
connected = ''
loggedIn = False

restTime = int(configFile["restTime"]) * 60 + random.randint(1, 9)
idleMoveTimer = int(configFile["idleMoveTimer"]) * 60 + random.randint(1, 9)

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
    # pyautogui.click(clicks=2, interval=0.25)
    pyautogui.click()


def connectWallet(currentState):
    global loggedIn
    connect_wallet_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'connect_wallet_01.png', confidence=0.7)
    if connect_wallet_im1 != None:
        customClick(connect_wallet_im1)
        return 'to_asign'

    else:
        connect_wallet_im2 = pyautogui.locateCenterOnScreen(
            assetsPath + 'connect_wallet_02.png', confidence=0.7)
        if connect_wallet_im2 != None:
            customClick(connect_wallet_im2)
            return 'to_asign'

    return currentState


def asign(currentState):
    global loggedIn
    asign_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'assinar.png', confidence=0.8)
    if asign_im1 != None:
        customClick(asign_im1)
        loggedIn = True
        return 'to_expan'

    return currentState


def reAsign(currentState):
    global loggedIn
    global state
    menu_im = pyautogui.locateCenterOnScreen(
        assetsPath + 'menu.png', confidence=0.8)
    if menu_im != None:
        print('olhau')
        state = 'to_heroes'
        return 'to_heroes'
    asign_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'assinar.png', confidence=0.8)
    if asign_im1 != None:
        print('reasinou')
        customClick(asign_im1)
        loggedIn = True
        return 'to_heroes'

    return currentState


def expandGameWindow(currentState):
    expand_game_Window_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'expan_game.png', confidence=0.8)
    if expand_game_Window_im1 != None:
        customClick(expand_game_Window_im1)
        return 'to_heroes'
    return currentState


def openHeroesWindow(currentState):
    heroes_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'heroes.png', confidence=0.8)
    if heroes_im1 != None:
        customClick(heroes_im1)
        return 'to_all_work'
    return currentState


def closeHeroesWindow(currentState):
    close_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'close.png', confidence=0.7)
    if close_im1 != None:
        customClick(close_im1)
        return 'to_treasure_hunt'
    return currentState


def putAllHeroesToWork(currentState):
    global last_work
    if pyautogui.locateOnScreen(assetsPath + 'all_on.png') != None:
        all_on_im1 = pyautogui.locateCenterOnScreen(
            assetsPath + 'all_on.png', confidence=0.8)
        time.sleep(1)
        customClick(all_on_im1)
        last_work = datetime.datetime.now()
        return 'to_close'

    elif pyautogui.locateOnScreen(assetsPath + 'all_work_again.png') != None:
        all_work_again_im1 = pyautogui.locateCenterOnScreen(
            assetsPath + 'all_work_again.png')
        time.sleep(1)
        customClick(all_work_again_im1)
        last_work = datetime.datetime.now()
        return 'to_close'

    else:
        print('vazei')
        last_work = datetime.datetime.now()
        return 'to_close'

    return currentState


def backToMenu(currentState):
    back_menu_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'back_menu.png', confidence=0.8)
    if back_menu_im1 != None:
        customClick(back_menu_im1)
        return 'to_heroes'
    return currentState


def goTreasureHunt(currentState):
    treasure_hunt_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'treasure_hunt.png', confidence=0.8)
    if treasure_hunt_im1 != None:
        customClick(treasure_hunt_im1)
        return 'farming'
    return currentState


def idleMove1(currentState):
    global last_idle_move

    idle_target_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'chest.png', confidence=0.8)
    if idle_target_im1 != None:
        customClick(idle_target_im1)
        time.sleep(random.randint(1, 9))
        last_idle_move = datetime.datetime.now()

        return 'idle_move2'
    return currentState


def idleMove2(currentState):
    global last_idle_move

    idle_target_2_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'close_chest.png', confidence=0.8)
    if idle_target_2_im1 != None:
        customClick(idle_target_2_im1)

        last_idle_move = datetime.datetime.now()

        return 'farming'
    return currentState


def checkIfDisconnected():
    global state
    global loggedIn

    # if pyautogui.locateOnScreen(assetsPath + 'login_expired.png', confidence=0.8) != None:
    ok_im1 = pyautogui.locateCenterOnScreen(
        assetsPath + 'ok.png', confidence=0.8)
    if ok_im1 != None:
        customClick(ok_im1)
        state = 'disconnected'
        return
    
    ok_im2 = pyautogui.locateCenterOnScreen(
        assetsPath + 'ok2.png', confidence=0.8)
    
    if ok_im2 != None:
        customClick(ok_im2)
        state = 'disconnected'
    
    elif loggedIn:
        connect_wallet_02_im = pyautogui.locateCenterOnScreen(
            assetsPath + 'connect_wallet_02.png', confidence=0.8)
        if connect_wallet_02_im != None:
            print('deu ruim')
            loggedIn = False
            time.sleep(1)
            customClick(connect_wallet_02_im)
            pyautogui.click()
            time.sleep(10)
            state = 'to_re_asign'
            return


def saveLog(logText):
    logFile = open(logFilePath, "a")
    logFile.write(logText)
    logFile.write('\n')
    logFile.close()


try:
    while 1:
        log = '%s ||    %s' % (
            datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%S"), state)
        if lastState != state:
            if configFile["logMode"] == 'debug':
                print(log)
            saveLog(log)

        if configFile["logMode"] != 'debug':
            clearPrint('Atividade Atual: %s\nProximo movimento de presença: %ss\nFim do descanço em: %dm e %ds' %
                       (state,  
                       idleMoveTimer - (datetime.datetime.now() - last_idle_move).seconds, 
                       (restTime - (datetime.datetime.now() - last_work).seconds) / 60,
                       (restTime - (datetime.datetime.now() - last_work).seconds) % 60
            ))

        lastState = state

        if keyboard.is_pressed('q') and keyboard.is_pressed('ctrl'):
            break

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

        elif state == 'idle_move1':
            state = idleMove1(state)

        elif state == 'idle_move2':
            state = idleMove2(state)

        elif state == 'farming' and (datetime.datetime.now() - last_work).seconds > restTime:
            state = 'back_menu'

        elif state == 'farming' and (datetime.datetime.now() - last_idle_move).seconds > idleMoveTimer:
            state = 'idle_move1'

        checkIfDisconnected()
        time.sleep(int(configFile['cicleTime']))

except Exception as e:
    print(e)
