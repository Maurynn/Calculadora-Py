from tkinter import *
import random

# build ui
janela = Tk()
janela.title('By Mauro')
janela.configure(background="#3e3e3e", borderwidth="3", height="200", pady="30")
janela.configure(relief="ridge", takefocus=False, width="200")
janela.geometry("235x370")
janela.resizable(False, False)

# Variável todos valores
todos_valores = ''

# Criando Função
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    # Passando valores para a tela
    valor_texto.set(todos_valores)

# Função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# Função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')

#Função Resetar Cor atual
def reset_cor_atual():
    cor_reset_corpo = ["#3e3e3e"]
    cor_reset_button = ["#b3b3ff"]
    cor_reset_button1 =["#e2e2e2"]
    reset_cor_atual = frame_corpo["bg"]= janela["bg"]= label_marca["bg"]= cor_reset_corpo
    reset_cor_button = bt4["bg"]=bt5["bg"]=bt6["bg"]=bt8["bg"]=bt9["bg"]=bt10["bg"]=bt12["bg"]=bt13["bg"]=bt14["bg"]=bt16["bg"]=bt17["bg"]= cor_reset_button
    reset_cor_button1 = bt2["bg"]=bt3["bg"]=bt7["bg"]=bt11["bg"]=bt15["bg"]= cor_reset_button1
   


#Função de cores aleatórias
def cores1():
    cor = ["#"+''.join([random.choice('0123456789abcdef')for j in range(6)])]
    cor_frame = frame_corpo["bg"]= janela["bg"] =label_marca["bg"]= cor

def cores2():
    cor1 = ["#"+''.join([random.choice('0123456789abcdef')for j in range(6)])]
    cor1_button = bt4["bg"]=bt5["bg"]=bt6["bg"]=bt8["bg"]=bt9["bg"]=bt10["bg"]=bt12["bg"]=bt13["bg"]=bt14["bg"]=bt16["bg"]=bt17["bg"]= cor1

def cores3():
    cor2 = ["#"+''.join([random.choice('0123456789abcdef')for j in range(6)])]
    cor2_button = bt2["bg"]=bt3["bg"]=bt7["bg"]=bt11["bg"]=bt15["bg"]= cor2

       
frame_tela = Frame(janela)
frame_tela.configure(background="#cbebea", borderwidth="4", height="60", relief="sunken")
frame_tela.configure(width="218")
frame_tela.pack(side="top")
frame_corpo = Frame(janela, container="false")
frame_corpo.configure(bg="#3e3e3e", height="260", width="220")
frame_corpo.place(anchor="nw", x="7", y="77")
valor_texto = StringVar()
label = Label(frame_tela, textvariable=valor_texto)
label.configure(anchor="e", background="#cbebea", font="{Ebrima} 16 {}", height="2")
label.configure(justify="right", text="0123", width="17")
label.place(anchor="nw")


bt1 = Button(frame_corpo, command = limpar_tela)
bt1.configure(
            activebackground="#fe3f44",
            background="#fe3f44",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt1.configure(
            foreground="#ffffff", height="2", overrelief="groove", text="C")
bt1.configure(width="13")
bt1.place(anchor="nw", relx="-0.00", x="1", y="0")
bt2 = Button(frame_corpo,command = lambda: entrar_valores('%'))
bt2.configure(
            activebackground="#e2e2e2",
            background="#e2e2e2",
            borderwidth="4",
            font="{Courier New CE} 9 {}")
bt2.configure(height="2", overrelief="groove", text="%", width="5")
bt2.place(relx="0.51", y="0")
bt3 = Button(frame_corpo, command = lambda: entrar_valores('/'))
bt3.configure(
            activebackground="#e2e2e2",
            background="#e2e2e2",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt3.configure(height="2", overrelief="groove", text="/", width="5")
bt3.place(anchor="nw", relx="0.75", x="3", y="0")
bt4 = Button(frame_corpo, command = lambda: entrar_valores('7'))
bt4.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt4.configure(height="2", overrelief="groove", text="7", width="5")
bt4.place(relx="0.0", rely="0.20", x="1", y="0")
bt5 = Button(frame_corpo, command = lambda: entrar_valores('8'))
bt5.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt5.configure(height="2", overrelief="groove", text="8", width="5")
bt5.place(relx="0.25", rely="0.20", x="2", y="0")
bt6 = Button(frame_corpo, command = lambda: entrar_valores('9'))
bt6.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt6.configure(height="2", overrelief="groove", text="9", width="5")
bt6.place(relx="0.5", rely="0.20", x="2", y="0")
bt7 = Button(frame_corpo, command = lambda: entrar_valores('*'))
bt7.configure(
            activebackground="#e2e2e2",
            background="#e2e2e2",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}",)
bt7.configure(height="2", overrelief="groove", text="*", width="5")
bt7.place(relx="0.75", rely="0.20", x="3", y="0")
bt8 = Button(frame_corpo, command = lambda: entrar_valores(eval('4')))
bt8.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt8.configure(height="2", overrelief="groove", text="4", width="5")
bt8.place(relx="0.0", rely="0.40", x="1", y="1")
bt12 = Button(frame_corpo, command = lambda: entrar_valores('1'))
bt12.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt12.configure(height="2", overrelief="groove", text="1", width="5")
bt12.place(relx="0.0", rely="0.60", x="1", y="1")
bt9 = Button(frame_corpo, command = lambda: entrar_valores('5'))
bt9.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}",
        )
bt9.configure(height="2", overrelief="groove", text="5", width="5")
bt9.place(relx="0.25", rely="0.40", x="2", y="0")
bt10 = Button(frame_corpo, command = lambda: entrar_valores('6'))
bt10.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt10.configure(height="2", overrelief="groove", text="6", width="5")
bt10.place(relx="0.5", rely="0.40", x="2", y="0")
bt11 = Button(frame_corpo, command = lambda: entrar_valores('-'))
bt11.configure(
            activebackground="#e2e2e2",
            background="#e2e2e2",
            borderwidth="4",
            font="{Courier New CE} 9 {}")
bt11.configure(height="2", overrelief="groove", text="-", width="5")
bt11.place(relx="0.75", rely="0.40", x="3", y="0")
bt13 = Button(frame_corpo, command = lambda: entrar_valores('2'))
bt13.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt13.configure(height="2", overrelief="groove", text="2", width="5")
bt13.place(relx="0.25", rely="0.60", x="2", y="0")
bt14 = Button(frame_corpo, command = lambda: entrar_valores('3'))
bt14.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt14.configure(height="2", overrelief="groove", text="3", width="5")
bt14.place(relx="0.5", rely="0.60", x="2", y="0")
bt15 = Button(frame_corpo, command = lambda: entrar_valores('+'))
bt15.configure(
            activebackground="#e2e2e2",
            background="#e2e2e2",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt15.configure(height="2", overrelief="groove", text="+", width="5")
bt15.place(relx="0.75", rely="0.60", x="3", y="0")
bt17 = Button(frame_corpo, command = lambda: entrar_valores('.'))
bt17.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt17.configure(foreground="#000000", height="2", overrelief="groove", text=".")
bt17.configure(width="5")
bt17.place(relx="0.5", rely="0.80", x="2", y="0")
bt18 = Button(frame_corpo, command = calcular)
bt18.configure(
            activebackground="#ff8000",
            background="#ff9224",
            borderwidth="4",
            font="{Courier New CE} 9 {italic}")
bt18.configure(height="2", overrelief="groove", text="=", width="5")
bt18.place(relx="0.75", rely="0.80", x="3", y="0")
bt16 = Button(frame_corpo, command = lambda: entrar_valores('0'))
bt16.configure(
            activebackground="#b3b3ff",
            background="#b3b3ff",
            borderwidth="4",
            font="{Courier New CE} 9 {bold}")
bt16.configure(foreground="#000000", height="2", overrelief="groove", text="0")
bt16.configure(width="13")
bt16.place(anchor="nw", rely="0.80", x="1", y="0")
cor1_button = Button(janela, command=cores1)
cor1_button.configure(foreground="#000000", activebackground="#ff9224",
            anchor="center",
            background="#ff9224",
            font="device", justify="center", overrelief="groove", relief="raised", text="C1")
cor1_button.place(
            anchor="nw", 
            height="14", 
            relx="0.0", 
            rely="-0.09", 
            width="23", 
            x="5", 
            y="5")
cor2_button = Button(janela, command=cores2)
cor2_button.configure(
            activebackground="#ff9224",
            anchor="center",
            background="#ff9224",
            font="device")
cor2_button.configure(foreground="#000000", overrelief="groove", relief="raised", text="C2")
cor2_button.place(
            anchor="nw",
            height="14",
            relx="0.13",
            rely="-0.09",
            width="23",
            x="4",
            y="5")
cor3_button = Button(janela,command= cores3)
cor3_button.configure(
            activebackground="#ff9224",
            anchor="center",
            background="#ff9224",
            font="device")
cor3_button.configure(foreground="#000000", overrelief="groove", relief="raised", text="C3")
cor3_button.place(
            anchor="nw",
            height="14",
            relx="0.26",
            rely="-0.09",
            width="23",
            x="5",
            y="5")
cor4_button = Button(janela,command= reset_cor_atual)
cor4_button.configure(
            activebackground="#ff9224",
            anchor="center",
            background="#ff9224",
            font="device")
cor4_button.configure(foreground="#000000", overrelief="groove", relief="raised", text="R")
cor4_button.place(
            anchor="nw",
            height="14",
            relx="0.39",
            rely="-0.09",
            width="23",
            x="5",
            y="5")

label_marca = Label(janela)
label_marca.configure(
            anchor="w",
            background="#3e3e3e",
            font="{Bahnschrift SemiBold SemiConden} 10 {}",
            foreground="#ffffff")
label_marca.configure(justify="left", relief="sunken", text="CALCULADORA PY")
label_marca.place(
            anchor="nw",
            relheight="0.05",
            relwidth="0.18",
            relx="0.56",
            rely="-0.07",
            width="55",
            x="1",
            y="-1")

janela.mainloop()
