import tkinter as tk 
import math 

class ventiladorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("controle principal")
        self.root.geometry("250x250")
        
        self.janela_fan = None 
        self.ligado = False
        self.velocidade = 10
        self.angulo = 0 
        
        self.btn_abrir = tk.Button(root, text="abrir ventilador", command=self.abrir_janela_ventilador)
        self.btn_abrir.pack(pady=5)
        
        self.btn_ligar = tk.Button(root, text="ligar/desligar", bg="orange", command=self.alternar_energia)
        self.btn_ligar.pack(pady=5)
        
        self.btn_mais = tk.Button(root, text = "aumentar velocidade +", command=self.aumentar_velocidade)
        self.btn_mais.pack(pady=5)
        
        self.label_status = tk.Label(root,text=f"velocidade : {self.velocidade}")
        self.label_status.pack(pady=5)
                                           
    def abrir_janela_ventilador(self):
        if self.janela_fan is None or not self.janela_fan.winfo_exists():
            self.janela_fan = tk.Toplevel(self.root)
            self.janela_fan.title("ventilador")

            self.Canvas = tk.Canvas(self.janela_fan, width=300, height=300, bg="white")
            self.Canvas.pack()

            self.angulo = 0
            self.velocidade = 10
            self.animar()
        else:
            self.janela_fan.lift()
    def alternar_energia(self):
        self.ligado = not self.ligado
        cor = "green" if self.ligado else "orange"
        self.btn_ligar.config(bg=cor)
        
    def aumentar_velocidade(self):
        self.velocidade += 5
        self.label_status.config(text=f"velocidade: {self.velocidade}")
        
    def animar(self):
        if self.janela_fan is None or not self.janela_fan.winfo_exists():
                return
            
        if self.ligado:
            self.Canvas.delete("pas")
        
            cx, cy = 150, 150
            raio = 100

            for i in range(3):
                rad = math.radians(self.angulo + (i * 120))

                x = cx + raio * math.cos(rad)
                y = cy + raio * math.sin(rad)

                self.Canvas.create_line(cx, cy, x, y, width=15, fill="red", tags="pas", capstyle="round")
            
            
        self.Canvas.create_oval(cx-10, cy-10, cx+10, cy+10, fill="black", tags="pas")
        
        self.angulo += self.velocidade
        
        self.janela_fan.after(20, self.animar)
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ventiladorApp(root)
    root.mainloop()