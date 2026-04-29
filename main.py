import tkinter as tk 
import math 

class ventiladorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("controle principal")
        self.root.geometry("350x350")
        
        self.ligado = False
        self.velocidade = 10
        self.angulo = 0 
        
        self.btn_abrir = tk.Button(root, text="abrir ventilador", command=self.abrir_janela_ventilador)
        self.btn_abrir.pack(pady=5)
        
        self.btn_ligar = tk.Button(root, text="ligar/desligar", bg="orange", width=20, command=self.alternar_energia)
        self.btn_ligar.pack(pady=5)
        
        self.btn_mais = tk.Button(root, text = "aumentar velocidade +",width=20, command=self.aumentar_velocidade)
        self.btn_mais.pack(pady=5)
        
        self.label_status = tk.Label(root,text=f"velocidade : {self.velocidade}", font=("arial", 10, "bold"))
        self.label_status.pack(pady=5)
        
        self.Canvas = tk.Canvas(root, width=)
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ventiladorApp(root)
    root.mainloop()