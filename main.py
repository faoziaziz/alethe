# ini program utamanya
import matplotlib 
print "ini program utama"

import wx

app = wx.App()

frame = wx.Frame(None, title='Simple APplication')
frame.Show()

app.MainLoop()
