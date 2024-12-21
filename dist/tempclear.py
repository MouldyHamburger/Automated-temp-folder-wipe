import os
import pyautogui
import time
import pygame

def load_music():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("audio.mp3")
        pygame.mixer.music.play(-1)
    except pygame.error:
        print("Music failed to load")

def exit_program():
    os.system('cls')
    print("Exiting program...")
    time.sleep(1)
    pygame.mixer.music.stop()
    exit()

def clear_temp():
    os.system('start cmd')
    time.sleep(0.5)
    pyautogui.typewrite('cls')
    pyautogui.press('enter')
    pyautogui.typewrite(r"del /q /f C:\Users\<"your username">\AppData\Local\Temp\*")
    pyautogui.press('enter')

def main():
    try:
        while True:
            print("1. clear temp files in appdata")
            print("0. exit")
            usrInput = int(input("Make a selection: "))
            
            if usrInput == 1:
                confirmation = pyautogui.confirm(text='Are you sure you want to delete temp files?', title='Confirmation', buttons=['Yes','No'])
                if confirmation == "Yes":
                    clear_temp()
                    break
                elif confirmation == "No":
                    exit_program()
                else:
                    os.system('cls')
                
            elif usrInput == 0:
                break
            else:
                print(f"{usrInput} is an invalid entry...")
                time.sleep(1)
                os.system('cls')

    except ValueError:
        print('invalid entry...')

    input("Press enter to exit: ")
    exit_program()

if __name__ == "__main__":
    os.system('cls')
    load_music()
    main()
