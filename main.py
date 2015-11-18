import ctypes
from ctypes import wintypes
import win32con
from importlib import reload

import hotkey

byref = ctypes.byref
user32 = ctypes.windll.user32

HOTKEYS = {}
HOTKEYS.update(hotkey.HOTKEYS)   
HOTKEY_ACTIONS = {}
HOTKEY_ACTIONS.update(hotkey.HOTKEY_ACTIONS)

for id, (vk, modifiers) in HOTKEYS.items():
   print("Registering ID", id, "for key", vk)
   if not user32.RegisterHotKey(None, id, modifiers, vk):
      print("Unable to register ID!")
      
try:
   msg = wintypes.MSG()
   while user32.GetMessageA(byref(msg), None, 0, 0) != 0:
      if msg.message == win32con.WM_HOTKEY:
         action_to_take = HOTKEY_ACTIONS.get(msg.wParam)
         if action_to_take:
            action_to_take()   
      user32.TranslateMessage (byref (msg))
      user32.DispatchMessageA (byref (msg))

finally:
   for id in HOTKEYS.keys():
      user32.UnregisterHotKey(None, id)