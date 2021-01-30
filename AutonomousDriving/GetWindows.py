import pygetwindow as gw

# print(gw.getAllTitles(), len(gw.getAllTitles()))
UE4Window = gw.getWindowsWithTitle('Second_screen')[0]
print(UE4Window.size)
print(UE4Window.bottomright)
print(UE4Window.topleft)

# ['', '', '', '', '', 'CVPlayground – GetWindows.py', 'autonomousDriving - Unreal Editor', 'Netflix - Google Chrome', '#general - Discord', 'autonomousDriving (Running) - Microsoft Visual Studio', 'New Tab - Google Chrome', 'Mail', 'Calendar', 'Calendar', 'Settings', 'Settings', '', '', '', '', '', '', '', '', 'NVIDIA GeForce Overlay', 'Microsoft Text Input Application', '', 'Switch USB', 'Bean, Tyler, +3 | Microsoft Teams', 'Inbox - Ndus \u200e- Mail', '', 'Program Manager'] 32
# ['', '', '', '', '', 'CVPlayground – GetWindows.py', 'Second_screen', 'autonomousDriving - Unreal Editor', 'Netflix - Google Chrome', '#general - Discord', 'autonomousDriving (Running) - Microsoft Visual Studio', 'New Tab - Google Chrome', 'Mail', 'Calendar', 'Calendar', 'Settings', 'Settings', '', '', '', '', '', '', '', '', 'NVIDIA GeForce Overlay', 'Microsoft Text Input Application', '', 'Switch USB', 'Bean, Tyler, +3 | Microsoft Teams', 'Inbox - Ndus \u200e- Mail', '', 'Program Manager'] 33