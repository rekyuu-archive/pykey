import ctypes
from ctypes import wintypes
import win32con, win32gui, win32process
import psutil
from keys import keydefs

# Definitions 
##################################################

# Easy mode
byref    = ctypes.byref
user32   = ctypes.windll.user32

# Padding
Bar      = 30
Pad      = Bar

# Monitors
Top      = 180    # Padding from the top of the left and right monitors
LMonW    = 1600   # Left monitor
LMonH    = 900
CMonW    = 1920   # Center monitor
CMonH    = 1080
RMonW    = 1600   # Right monitor
RMonH    = 900

# Windows 10 has strange sizes for system borders on the left, bottom, and right sides. This is defined here, as well as applications that do not use the default window borders.
Border   = 7
NiceApps = ["mpc-hc64.exe", "Steam.exe", "InDesign.exe", "Photoshop.exe", "Telegram.exe", "MusicBee.exe", "firefox.exe", "KanColleViewer.exe", "Honeyview.exe", "electron.exe"]

# Functions 
##################################################

# Main window movement function.
# ww/wh = Window width and height, pixels
# wx/wy = Window position, x and y, pixels
# s = Monitor selection
def WindowMove(ww,wh,wx,wy,s):
   pid   = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
   pname = psutil.Process(pid[1]).name()
   
   if s == "left":
      width    = ww
      height   = wh
      posx     = wx
      posy     = wy
      if pname in NiceApps:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(-LMonW + Pad + posx),
            int(Top + Pad + posy),
            int(width - (2 * Pad)),
            int(height - (2* Pad)), 1)
      else:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(-LMonW + Pad - Border + posx),
            int(Top + Pad + posy),
            int(width - (2 * Pad) + (2 * Border)),
            int(height - (2 * Pad) + Border), 1)
   
   if s == "center":
      width    = ww
      height   = wh
      posx     = wx
      posy     = wy
      if pname in NiceApps:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(Pad + posx),
            int(Bar + Pad + posy),
            int(width - (2 * Pad)),
            int(height - (2* Pad)), 1)
      else:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(Pad - Border + posx),
            int(Bar + Pad + posy),
            int(width - (2 * Pad) + (2 * Border)),
            int(height - Bar - (2 * Pad) + Border), 1)
   
   if s == "right":
      width    = ww
      height   = wh
      posx     = wx
      posy     = wy
      if pname in NiceApps:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(CMonW + Pad + posx),
            int(Top + Pad + posy),
            int(width - (2 * Pad)),
            int(height - (2* Pad)), 1)
      else:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(CMonW + Pad - Border + posx),
            int(Top + Pad + posy),
            int(width - (2 * Pad) + (2 * Border)),
            int(height - (2 * Pad) + Border), 1)
            
def WindowMovePercent(ww,wh,wx,wy,s):
   pid   = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
   pname = psutil.Process(pid[1]).name()
   
   if s == "left":
      width    = ( ww / 100 ) * LMonW
      height   = ( wh / 100 ) * LMonH
      posx     = ( wx / 100 ) * LMonW
      posy     = ( wy / 100 ) * LMonH
      if pname in NiceApps:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(-LMonW + Pad + posx),
            int(Top + Pad + posy),
            int(width - (2 * Pad)),
            int(height - (2* Pad)), 1)
      else:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(-LMonW + Pad - Border + posx),
            int(Top + Pad + posy),
            int(width - (2 * Pad) + (2 * Border)),
            int(height - (2 * Pad) + Border), 1)
   
   if s == "center":
      width    = ( ww / 100 ) * CMonW
      height   = ( wh / 100 ) * CMonH
      posx     = ( wx / 100 ) * CMonW
      posy     = ( wy / 100 ) * CMonH
      if pname in NiceApps:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(Pad + posx),
            int(Bar + Pad + posy),
            int(width - (2 * Pad)),
            int(height - (2* Pad)), 1)
      else:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(Pad - Border + posx),
            int(Bar + Pad + posy),
            int(width - (2 * Pad) + (2 * Border)),
            int(height - Bar - (2 * Pad) + Border), 1)
   
   if s == "right":
      width    = ( ww / 100 ) * RMonW
      height   = ( wh / 100 ) * RMonH
      posx     = ( wx / 100 ) * RMonW
      posy     = ( wy / 100 ) * RMonH
      if pname in NiceApps:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(CMonW + Pad + posx),
            int(Top + Pad + posy),
            int(width - (2 * Pad)),
            int(height - (2* Pad)), 1)
      else:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(CMonW + Pad - Border + posx),
            int(Top + Pad + posy),
            int(width - (2 * Pad) + (2 * Border)),
            int(height - (2 * Pad) + Border), 1)
            
def WindowMoveGrid(columns, rows, col_sel, row_sel, col_span, row_span, s):
   pid   = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
   pname = psutil.Process(pid[1]).name()
   
   if s == "left":
      win_width   = (LMonW - ((columns + 1) * Pad)) / columns
      win_height  = (LMonH - ((rows    + 1) * Pad)) / rows
      
      if col_span:
         width    = (Pad * (col_span - 1)) + (col_span * win_width)
      if row_span:
         height   = (Pad * (row_span - 1)) + (row_span * win_height)
      else:
         width    = win_width
         height   = win_height
         
      posx     = (col_sel - 1) + (Pad * (col_sel - 1)) + (win_width * (col_sel - 1))
      posy     = (row_sel - 1) + (Pad * (row_sel - 1)) + (win_height * (row_sel - 1))
      
      if pname in NiceApps:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(-LMonW + Pad + posx),
            int(Top + Pad + posy),
            int(width),
            int(height), 1)
      else:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(-LMonW + Pad - Border + posx),
            int(Top + Pad + posy),
            int(width + (2 * Border)),
            int(height + Border), 1)
   
   if s == "center":
      win_width   = (CMonW - ((columns + 1) * Pad)) / columns
      win_height  = (CMonH - ((rows    + 1) * Pad)) / rows
      
      if col_span:
         width    = (Pad * (col_span - 1)) + (col_span * win_width)
      if row_span:
         height   = (Pad * (row_span - 1)) + (row_span * win_height)
      else:
         width    = win_width
         height   = win_height
         
      posx     = (col_sel - 1) + (Pad * (col_sel - 1)) + (win_width * (col_sel - 1))
      posy     = (row_sel - 1) + (Pad * (row_sel - 1)) + (win_height * (row_sel - 1))
      
      if pname in NiceApps:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(Pad + posx),
            int(Bar + Pad + posy),
            int(width),
            int(height - Bar), 1)
      else:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(Pad - Border + posx),
            int(Bar + Pad + posy),
            int(width + (2 * Border)),
            int(height - Bar + Border), 1)
   
   if s == "right":
      win_width   = (RMonW - ((columns + 1) * Pad)) / columns
      win_height  = (RMonH - ((rows    + 1) * Pad)) / rows
      
      if col_span:
         width    = (Pad * (col_span - 1)) + (col_span * win_width)
      if row_span:
         height   = (Pad * (row_span - 1)) + (row_span * win_height)
      else:
         width    = win_width
         height   = win_height
         
      posx     = (col_sel - 1) + (Pad * (col_sel - 1)) + (win_width * (col_sel - 1))
      posy     = (row_sel - 1) + (Pad * (row_sel - 1)) + (win_height * (row_sel - 1))
      
      if pname in NiceApps:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(CMonW + Pad + posx),
            int(Top + Pad + posy),
            int(width),
            int(height), 1)
      else:
         win32gui.MoveWindow(
            win32gui.GetForegroundWindow(),
            int(CMonW + Pad - Border + posx),
            int(Top + Pad + posy),
            int(width + (2 * Border)),
            int(height + Border), 1)
            
   print("Width:", str(int(width)))
   print("Height:", str(int(height)))
   print("Position: (" + str(int(posx)) + ",", str(int(posy)) + ")")
            
def useHotKey(n,mod,key):
   HOTKEYS.update({n : (keydefs[key], keydefs[mod])})

# Hotkey defintions
##################################################

HOTKEYS = {}

# Left monitor
useHotKey(4,"super","num4")
def id_4_super_num4():
   WindowMoveGrid(
      columns  = 1, 
      rows     = 1, 
      col_sel  = 1, 
      row_sel  = 1, 
      col_span = 1, 
      row_span = 1, 
      s        = "left"
   )

id_1_var = 0
useHotKey(1,"super","num1")
def id_1_super_num1():
   global id_1_var
   if id_1_var == 0:
      WindowMoveGrid(
         columns  = 2, 
         rows     = 2, 
         col_sel  = 1, 
         row_sel  = 1, 
         col_span = 1, 
         row_span = 2, 
         s        = "left"
      )
   if id_1_var == 1:
      WindowMoveGrid(
         columns  = 2, 
         rows     = 2, 
         col_sel  = 1, 
         row_sel  = 1, 
         col_span = 1, 
         row_span = 1, 
         s        = "left"
      )
   if id_1_var == 2:
      WindowMoveGrid(
         columns  = 2, 
         rows     = 2, 
         col_sel  = 1, 
         row_sel  = 2, 
         col_span = 1, 
         row_span = 1, 
         s        = "left"
      )
   id_1_var += 1
   if id_1_var == 3:
      id_1_var = 0

id_2_var = 0
useHotKey(2,"super","num2")
def id_2_super_num2():
   global id_2_var
   if id_2_var == 0:
      WindowMoveGrid(
         columns  = 2, 
         rows     = 2, 
         col_sel  = 2, 
         row_sel  = 1, 
         col_span = 1, 
         row_span = 2, 
         s        = "left"
      )
   if id_2_var == 1:
      WindowMoveGrid(
         columns  = 2, 
         rows     = 2, 
         col_sel  = 2, 
         row_sel  = 1, 
         col_span = 1, 
         row_span = 1, 
         s        = "left"
      )
   if id_2_var == 2:
      WindowMoveGrid(
         columns  = 2, 
         rows     = 2, 
         col_sel  = 2, 
         row_sel  = 2, 
         col_span = 1, 
         row_span = 1, 
         s        = "left"
      )
   id_2_var += 1
   if id_2_var == 3:
      id_2_var = 0
   
id_3_var = 0
useHotKey(3,"super","num3")
def id_3_super_num3():
   global id_3_var
   if id_3_var == 0:
      WindowMoveGrid(
         columns  = 3, 
         rows     = 1, 
         col_sel  = 1, 
         row_sel  = 1, 
         col_span = 1, 
         row_span = 1, 
         s        = "left"
      )
   if id_3_var == 1:
      WindowMoveGrid(
         columns  = 3, 
         rows     = 1, 
         col_sel  = 2, 
         row_sel  = 1, 
         col_span = 1, 
         row_span = 1, 
         s        = "left"
      )
   if id_3_var == 2:
      WindowMoveGrid(
         columns  = 3, 
         rows     = 1, 
         col_sel  = 3, 
         row_sel  = 1, 
         col_span = 1, 
         row_span = 1, 
         s        = "left"
      )
   if id_3_var == 3:
      WindowMoveGrid(
         columns  = 3, 
         rows     = 1, 
         col_sel  = 1, 
         row_sel  = 1, 
         col_span = 2, 
         row_span = 1, 
         s        = "left"
      )
   if id_3_var == 4:
      WindowMoveGrid(
         columns  = 3, 
         rows     = 1, 
         col_sel  = 2, 
         row_sel  = 1, 
         col_span = 2, 
         row_span = 1, 
         s        = "left"
      )
   id_3_var += 1
   if id_3_var == 5:
      id_3_var = 0
   
# Center monitor
useHotKey(0,"super","num0")
def id_0_super_num0():
   WindowMoveGrid(
      columns  = 1, 
      rows     = 1, 
      col_sel  = 1, 
      row_sel  = 1, 
      col_span = 1, 
      row_span = 1, 
      s        = "center"
   )
   
id_5_var = 0
useHotKey(5,"super","num5")
def id_5_super_num5():
   global id_5_var
   if id_5_var == 0:
      WindowMove(1147,1082,387,0,"center")
   if id_5_var == 1:
      WindowMove(1376,1082,272,0,"center")
   if id_5_var == 2:
      WindowMove(1835,1082,43,0,"center")
   id_5_var += 1
   if id_5_var == 3:
      id_5_var = 0
   
# Right monitor
useHotKey(6,"super","num6")
def id_6_super_num6():
   WindowMoveGrid(
      columns  = 1, 
      rows     = 1, 
      col_sel  = 1, 
      row_sel  = 1, 
      col_span = 1, 
      row_span = 1, 
      s        = "right"
   )
   
useHotKey(7,"super","num7")
def id_7_super_num7():
   WindowMoveGrid(
      columns  = 4, 
      rows     = 1, 
      col_sel  = 1, 
      row_sel  = 1, 
      col_span = 1, 
      row_span = 1, 
      s        = "right"
   )
   
id_8_var = 0
useHotKey(8,"super","num8")
def id_8_super_num8():
   global id_8_var
   if id_8_var == 0:
      WindowMoveGrid(
         columns  = 4, 
         rows     = 1, 
         col_sel  = 2, 
         row_sel  = 1, 
         col_span = 2, 
         row_span = 1, 
         s        = "right"
      )
   if id_8_var == 1:
      WindowMoveGrid(
         columns  = 4, 
         rows     = 1, 
         col_sel  = 1, 
         row_sel  = 1, 
         col_span = 2, 
         row_span = 1, 
         s        = "right"
      )
   if id_8_var == 2:
      WindowMoveGrid(
         columns  = 4, 
         rows     = 1, 
         col_sel  = 3, 
         row_sel  = 1, 
         col_span = 2, 
         row_span = 1, 
         s        = "right"
      )
   id_8_var += 1
   if id_8_var == 3:
      id_8_var = 0
   
useHotKey(9,"super","num9")
def id_9_super_num9():
   WindowMoveGrid(
      columns  = 4, 
      rows     = 1, 
      col_sel  = 4, 
      row_sel  = 1, 
      col_span = 1, 
      row_span = 1, 
      s        = "right"
   )
   
HOTKEY_ACTIONS = {
   0 : id_0_super_num0,
   1 : id_1_super_num1,
   2 : id_2_super_num2,
   3 : id_3_super_num3,
   4 : id_4_super_num4,
   5 : id_5_super_num5,
   6 : id_6_super_num6,
   7 : id_7_super_num7,
   8 : id_8_super_num8,
   9 : id_9_super_num9
}