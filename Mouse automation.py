import pyautogui
import webbrowser
pyautogui.confirm('Make sure that your screen size is "1080 x 1990"')
link = input('Enter the you tube channel link : ')
webbrowser.open_new_tab(link)
pyautogui.sleep(5)
pyautogui.press('F11')
pyautogui.sleep(1)
pyautogui.moveTo(x= 1650, y= 376,duration=1 )
pyautogui.leftClick(x=1650, y= 376)
pyautogui.moveTo(x=1692, y= 382,duration=1 )

pyautogui.leftClick(x=1692, y= 382)
pyautogui.moveTo(x=1735, y= 424,duration=1 )

pyautogui.leftClick(x=1735, y= 424)
pyautogui.press('F11')
pyautogui.confirm('Succesfully subscribed..!!')

