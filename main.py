import tkinter as tk 
import math 

class ventiladorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("controle principal")
        self.root.geometry("200x100")
        
        self.btn_abrir = tk.Button(root, text="abrir ventilador", command=self.abrir_janela_ventilador)
        self.btn_abrir.pack(expand=True)
        
    def abrir_janela_ventilador(self):
        self.janela_fan = tk.Toplevel(self.root)
        self.janela_fan.title("ventilador")
        
        self.Canvas = tk.Canvas(self.janela_fan, width=300, height=300, bg="white")
        self.Canvas.pack()
        
        self.angulo = 0
        self.velocidade = 10
        self.animar()
        
    def animar(self):
        if not self.janela_fan.winfo_exists():
                return
        
        self.Canvas.delete("pas")
        
        cx, cy = 150, 150
        raio = 100
        
        for i in range(3):
            rad = math.radians(self.angulo + (i * 120))
                
            x = cx + raio * math.cos(rad)
            y = cx + raio * math.sin(rad)
                
            self.Canvas.create_line(cx, cy, x, y, width=15, fill="red", tags="pas", capstyle="round")
            
            
        self.Canvas.create_oval(cx-10, cy-10, cx+10, cy+10, fill="black", tags="pas")
        
        self.angulo += self.velocidade
        
        self.janela_fan.after(20, self.animar)
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = ventiladorApp(root)
    root.mainloop()