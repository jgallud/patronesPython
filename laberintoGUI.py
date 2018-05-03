import os
from Tkinter import *
import Tkinter,Tkconstants,tkFileDialog

from laberintoBuilder import *

class App:
    def __init__(self, master):
        #wx.Frame.__init__(self, parent, title="LaberintoGUI", size=(800,600))
        #self.frame=Frame(master)
        #self.window.geometry("800x600")
        #self.frame.pack()
        self.origen=Point(350,14)
        self.ancho=None
        self.alto=None
        self.puedeDibujar=False
        self.dc=None
        #panel = wx.Panel(self)
        #self.quote = wx.StaticText(panel, label="Archivo: ", pos=(20, 30))
        self.lbl1=Label(master,text="Archivo: ")
        self.lbl1.pack()
        #self.lbl1.grid(column=0,row=1)
        self.lbl2 = Label(master, text="")
        self.lbl2.pack()
        #self.lbl2.grid(column=1, row=1)
        self.btn1=Button(master,text="Seleccionar y procesar",command=self.OnClick)
        self.btn1.pack()
        #self.btn1.grid(column=0,row=2)

        self.dc=Canvas(master,width=900,height=700)
        #self.dc.grid(column=0,row=0)
        self.dc.pack()

        #self.archivo = wx.TextCtrl(panel, value="Localiza el archivo", pos=(20,50),size=(150,20),style=wx.TE_READONLY)
        #self.button =wx.Button(panel, label="Seleccionar y procesar", pos=(20, 80))
        #self.bichos = wx.TextCtrl(panel, value="", pos=(20,150),size=(150,20),style=wx.TE_READONLY)
        #self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)
        #self.Bind(wx.EVT_PAINT,self.on_paint)
        #self.Show()
        #self.button=Button(self.frame,text="Seleccionar y procesar",command=self.OnClick)
        #self.button.pack()

    def on_paint(self,event=None):
        #self.dc=wx.PaintDC(self)
        #self.dc.Clear()
        #self.dc.SetPen(wx.Pen("BLACK",3))
        #self.dc.DrawLine(300,0,350,50)
        if (self.puedeDibujar):
            self.dibujarLaberinto()

    def OnClick(self):
        self.dirname = ""
        # dlg = wx.FileDialog(self, "Selecciona un archivo", self.dirname, "", "*.json", wx.FD_OPEN)
        # if dlg.ShowModal() == wx.ID_OK:
        #     self.filename = dlg.GetFilename()
        #     self.dirname = dlg.GetDirectory()
        #     #f = open(os.path.join(self.dirname, self.filename), 'r')
        #     #self.control.SetValue(f.read())
        #     self.archivo.SetValue(self.filename)
        #     #f.close()
        #     director=Director()
        #     director.procesar(os.path.join(self.dirname, self.filename))
        #     self.juego=director.builder.juego
        #     self.bichos.SetValue(str(len(self.juego.bichos)))
        #     self.mostrarLaberinto()
        # dlg.Destroy()

        self.filename=tkFileDialog.askopenfilename(initialdir="./",title="Selecciona archivo",filetypes=[("JSON","*.json")])
        if (self.filename!=""):
            print(self.filename)
            self.lbl2.configure(text=self.filename)
            director=Director()
            director.procesar(self.filename)
            self.juego=director.builder.juego
            #self.bichos.SetValue(str(len(self.juego.bichos)))
            self.mostrarLaberinto()

    def mostrarLaberinto(self):
        self.calcularPosiciones()
        self.normalizar()
        self.calcularDimensiones()
        self.asignarPuntosReales()
        self.puedeDibujar=True
        #self.Refresh()
        #self.Update()
        self.dibujarLaberinto()

    def calcularPosiciones(self):
        if (self.juego!=None):
            h=self.juego.obtenerHabitacion(1)
            h.punto=Point(0,0)
            h.calcularPosicion()

    def normalizar(self):
        minX=0
        minY=0
        for h in self.juego.laberinto.hijos:
            if (h.punto.x<minX):
                minX=h.punto.x
            if (h.punto.y<minY):
                minY=h.punto.y
        for h in self.juego.laberinto.hijos:
            punto=h.punto
            h.punto.x=punto.x+abs(minX)
            h.punto.y=punto.y+abs(minY)

    def calcularDimensiones(self):
        maxX=0
        maxY=0
        self.origen=Point(5,5)
        for h in self.juego.laberinto.hijos:
            if (h.punto.x>maxX):
                maxX=h.punto.x
            if (h.punto.y>maxY):
                maxY=h.punto.y
        maxX=maxX+1
        maxY=maxY+1
        self.ancho=850/maxX
        self.alto=650/maxY

    def asignarPuntosReales(self):
        for h in self.juego.laberinto.hijos:
            x=self.origen.x+(h.punto.x * self.ancho)
            y=self.origen.y+(h.punto.y * self.alto)
            h.punto=Point(x,y)
            h.extent=Point(self.ancho,self.alto)
            for ho in h.hijos:
                ho.asignarPuntosReales(h)

    def dibujarLaberinto(self):
        for h in self.juego.laberinto.hijos:
            h.dibujar(self)

    def dibujarContenedorRectangular(self,unCont):
        x1=unCont.punto.x
        y1=unCont.punto.y
        x2=unCont.extent.x
        y2=unCont.extent.y
        #print(x1,y1,x2,y2)
        self.dc.create_rectangle(x1,y1,x1+x2,y1+y2)

root=Tk()
app = App(root)
#frame = MainWindow(None, "Sample editor")
root.title("LaberintoGUI")
root.geometry("1000x800")
root.minsize(width=1000,height=800)
root.mainloop()
#root.destroy()