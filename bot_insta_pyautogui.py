'''Criar um bot de curtidas e comentários no Instagram com PyAutoGUI

- Vamos criar um bot que define qual página quer seguir, verifica se a postagem mais atual ainda não foi curtida pelo bot. Caso 
uma nova postagem tenha sido feita, ele deve entrar na postagem, curtir e comentar algo nela
'''
"""
É NECESSÁRIO:
- ABRIR O CMD E PASSAR OS COMANDOS
- python
- from mouseinfo import mouseInfo
- mouseInfo()

"""

#PASSOS E CÓDIGO:

#1.Abrir o site do instagram
import webbrowser
import pyautogui
from time import sleep

def logout():
    pyautogui.click(1771,424,duration=2)
    pyautogui.click(90,964,duration=2)
    pyautogui.click(78,893,duration=2)
    pyautogui.hotkey('ctrl','w')

while True:
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(4)

    #2.Selecionar e digitar o usuário
    pyautogui.click(1144,358,duration=1)
    pyautogui.typewrite('usuario')

    #3.Selecionar e digitar a senha

    pyautogui.click(1105,411,duration=1)
    pyautogui.typewrite('senha')
    sleep(1)

    #4.Clicar em Log in
    pyautogui.click(1166,473)
    sleep(10)

    #5.Fechar a janela que aparece "Salvar suas informações", clicar "Agora não"
    pyautogui.click(1090,628,duration=1)
    sleep(3)

    #6.Fechar a janela que aparece "Ativar notificações"
    """ pyautogui.click(655,750,duration=1)
    sleep(1) """

    #7.Ir até a Lupa de pesquisar e pesquisar a página desejada
    pyautogui.click(51,338,duration=1)
    sleep(2)
    pyautogui.moveTo(197,254,duration=1)
    sleep(1)
    pyautogui.click()
    pyautogui.typewrite('cristiano')
    sleep(3)
    pyautogui.move(15,65,duration=2)
    sleep(2)

    #8.Entrar na página
    pyautogui.click()
    sleep(1)

    #9.Clicar na postagem mais recente
    pyautogui.click(684,644,duration=1)
    sleep(4)

    #10.Verificar se a postagem mais recente foi curtida
    try:
        coracao = pyautogui.locateCenterOnScreen('.\pyautogui\projeto_bot_instagram\coracao1.png')

    #11.Se já tiver curtido, não fazer nada e pausar o bot por 24horas
        if coracao is not None:
            logout()
            sleep(5) #segundos de 24horas
            

    #12.Se não tiver curtido, curtir a foto
    except pyautogui.ImageNotFoundException as error:
        pyautogui.click(1100,836,duration=1)
        sleep(2)

    #13.Se não tiver curtido, comentar a foto
        pyautogui.click(1154,836)
        sleep(3)
        pyautogui.typewrite('GOAT')
        sleep(3)
        pyautogui.click(1641,970)
        sleep(3)

    #15.Logout
        logout()
    #15.Após as 24 horas, repetir todo o processo
        sleep(86400)
