import pyautogui as spam
import time

limite_msg = input("Enter n de msg: ")
msg = input("Coloque a mensagem: ")

i = 0

time.sleep(2)

while i<int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")
    i+=1 


