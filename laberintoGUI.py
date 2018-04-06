import os
import wx
from laberintoBuilder import * 

class MainWindow(wx.Frame):
	def __init__(self, parent, title):
	    wx.Frame.__init__(self, parent, title="LaberintoGUI", size=(300,300))
	    panel = wx.Panel(self)
	    self.quote = wx.StaticText(panel, label="Archivo: ", pos=(20, 30))  
	    self.archivo = wx.TextCtrl(panel, value="Localiza el archivo", pos=(20,50),size=(150,20),style=wx.TE_READONLY)
	    self.button =wx.Button(panel, label="Seleccionar y procesar", pos=(20, 80))
	    wx.StaticText(panel, label="Numero de bichos: ", pos=(20, 130))
	    self.bichos = wx.TextCtrl(panel, value="", pos=(20,150),size=(150,20),style=wx.TE_READONLY)
	    self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)      
	    self.Show()
	def OnClick(self,event):        
	    self.dirname = ""
	    dlg = wx.FileDialog(self, "Selecciona un archivo", self.dirname, "", "*.json", wx.FD_OPEN)
	    if dlg.ShowModal() == wx.ID_OK:
	        self.filename = dlg.GetFilename()
	        self.dirname = dlg.GetDirectory()
	        #f = open(os.path.join(self.dirname, self.filename), 'r')
	        #self.control.SetValue(f.read())
	        self.archivo.SetValue(self.filename)
	        #f.close()
	        director=Director()	        
	        director.procesar(os.path.join(self.dirname, self.filename))
	        self.juego=director.builder.juego
	        self.bichos.SetValue(str(len(self.juego.bichos)))
	    dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()