import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 0.3

pyautogui.press("win")



pyautogui.write("chrome")



pyautogui.press("enter")



pyautogui.moveTo(759, 601, duration=0.1)

pyautogui.click()

time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("tab")
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("enter")

pyautogui.press("tab")
tabela= pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.moveTo(693, 261, duration=0.1)
    pyautogui.click()
    codigo = str(tabela.loc[linha, "codigo" ])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca" ]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo" ]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria" ]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario" ]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo" ]))
    pyautogui.press("tab")


    obs= str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    

   
    pyautogui.scroll(5000)
