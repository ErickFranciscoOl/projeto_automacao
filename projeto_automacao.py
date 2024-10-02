import pyautogui
from time import sleep

pyautogui.click(971,541,duration=2)
pyautogui.write('erick')

pyautogui.click(970,564,duration=2)
pyautogui.write('1234')

pyautogui.click(880,593,duration=2)


with open ('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(694,521,duration=2)
        pyautogui.write(produto)

        pyautogui.click(696,555,duration=2)
        pyautogui.write(quantidade)

        pyautogui.click(688,582,duration=2)
        pyautogui.write(preco)

        pyautogui.click(605,738,duration=2)   