import tkinter as tk 
from tkinter import messagebox 

def verificar_nota () : 
     nota_texto = entry_nota.get() #Vai pegar a informação 

     if nota_texto.replace(".","",1).isdigit():
        nota = float(nota_texto)
        if nota > 7 and nota < 9:
           resultado = "Aprovado!!"
        elif nota >= 9 and nota <=9.9:
            resultado = 'Quase perfeito..!'
        elif nota == 10 :
         resultado = 'Parabéns,nota máxima !!'
        elif nota >=5: 
            resultado = "média"
        elif nota >=0 and nota <= 4.9:
           resultado= 'Reprovado com baixa nota.'
        else: 
            resultado = "recuperação"
        messagebox.showinfo("Resultado🥶", f"situação : {resultado}")
     else: 
       messagebox.showerror("Erro🙁☠️","Digite um número válido")
root = tk.Tk () 
root.title("Verificador de nota👌🧻")
root.geometry("300x200")
root.configure(bg="#53534f")


tk.Label(root,text="Digite a nota do Aluno:",bg = "#fffffc",fg = "black",font = ("Arial",16,"bold")).pack(pady=20)
entry_nota = tk.Entry(root)
entry_nota.pack(pady= 5)

tk.Button(root,text = "Verificar🤬",command= verificar_nota,bg = "blue",fg = "black",font = ("Arial",18,"bold")).pack(pady=20)

root.mainloop()


