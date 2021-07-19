from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self , master=None) :
        self.fontDefault = ("Ariel" , "10")
        
        self.primContainer = Frame(master)
        self.primContainer["pady"] = 10
        self.primContainer.pack()

        self.segContainer = Frame(master)
        self.segContainer["padx"] = 20
        self.segContainer.pack()

        self.terContainer = Frame(master)
        self.terContainer["padx"] = 20
        self.terContainer.pack()

        self.quaContainer = Frame(master)
        self.quaContainer["padx"] = 20
        self.quaContainer.pack()

        self.quiContainer = Frame(master)
        self.quiContainer["padx"] = 20
        self.quiContainer.pack()


        # Primeiro Container #
        self.Title = Label(self.primContainer, text="Calculo de aprovação ou reprovação do aluno.")
        self.Title["font"] = ("Arial" , "10" , "bold")
        self.Title.pack()

        # Conteudo de Nota 1 #
        self.inputN1 = Entry(self.segContainer)
        self.inputN1.pack(side=RIGHT)

        self.nota1Label = Label(self.segContainer , text= "Nota 1: " , font = self.fontDefault)          
        self.nota1Label.pack(side=LEFT)

        # Conteudo de Nota 2 #
        self.inputN2 = Entry(self.terContainer)
        self.inputN2.pack(side=RIGHT)

        self.nota2Label = Label(self.terContainer , text= "Nota 2: " , font = self.fontDefault)     
        self.nota2Label.pack(side=LEFT)

        # Conteudo para Logica do Botão #
        self.Button = Button(self.quaContainer , bg="red" , fg="White")
        self.Button["text"] = "Calcular Media"
        self.Button["font"] = ("Arial" , "10" , "bold")
        self.Button["width"] = 12
        self.Button["command"] = self.calc_med      
        self.Button.pack()

        # Conteudo para a Resuldado #
        #self.tela = Label(self.quiContainer , text = "" , font = self.fontDefault)
        #messagebox.showinfo("Resultado" , self.calc_med)
        
    # Função para calcular e dizer se tá aprovado ou reprovado #
    def calc_med(self):
        nota_1 = self.inputN1.get()
        nota_2 = self.inputN2.get()
        
        med = ( int(nota_1) + int(nota_2) ) / 2

        if med >= 7:            
            print("Media: ",med)
            print("Aprovado")            
        else:            
            print("Media: ",med)
            print("Reprovado")                    
            
root = Tk()
App(root)
root.mainloop()

