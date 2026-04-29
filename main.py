import tkinter as tk 
import math 
 
class VentiladorApp:
     def __init__(self, root):
         self.root = root
         self.root.title("Ventilador Realista")
         self.root.geometry("700x500")
         
         self.ligado = False
         self.velocidade = 0
         self.angulo = 0 
         
         self.canvas = tk.Canvas(root, width=500, height=650, bg="#e0e0e0", highlightthickness=0)
         self.canvas.pack()
         
         self.desenhar_estrutura_estatica()
         
         self.frame_botoes = tk.frame(root, bg="#333333")
         self.canvas.create_window(250,580, window=self.frame_botoes)
         
        self.btn_ligar = tk.Button(self.frame_botoes, text="ON/OFF", bg="orange", fg="white", font=("arial", 8, "bold"), command=self.alternar_energia)
        self.btn_ligar.grid(row=0, column=0, padx=5 , pady=5)
        
        tk.Button(self.frame_botoes, "VEL +", width=5, command=self.aumentar_velocidade).grid(row=0, column=1, padx=5)
        tk.Button(self.frame_botoes, text="VEL -", width=5, command=self.diminuir_velocidade).grid(row=0, column=2, padx=5)
         
         self.animar()
 
     def alternar_energia(self):
         self.ligado = not self.ligado
         if self.ligado and self.velocidade == 0:
             self.velocidade = 30
         elif not self.ligado:
             self.velocidade = 0
         self.atualizar_label()
 
     def aumentar_velocidade(self):
         if self.ligado:
             self.velocidade += 5
             self.atualizar_label()
 
     def diminuir_velocidade(self):
         if self.ligado and self.velocidade > 5:
             self.velocidade -= 5
             self.atualizar_label()
 
     def atualizar_label(self):
         self.label_status.config(text=f"Velocidade: {self.velocidade}")
 
     def animar(self):
         self.canvas.delete("all")
         cx, cy = 250, 250 
         raio = 180  
         largura_pa = 40 
        
         self.canvas.create_oval(cx-200, cy-200, cx+200, cy+200, outline="#cccccc", width=2)
 
         for i in range(3):
             ang = self.angulo + (i * 120)
             
             p1_x = cx + 10 * math.cos(math.radians(ang - 90))
             p1_y = cy + 10 * math.sin(math.radians(ang - 90))
             
             p2_x = cx + raio * math.cos(math.radians(ang - 20))
             p2_y = cy + raio * math.sin(math.radians(ang - 20))
             
             p3_x = cx + raio * math.cos(math.radians(ang + 20))
             p3_y = cy + raio * math.sin(math.radians(ang + 20))
             
             p4_x = cx + 10 * math.cos(math.radians(ang + 90))
             p4_y = cy + 10 * math.sin(math.radians(ang + 90))
 
             self.canvas.create_polygon(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, p4_x, p4_y, 
                                        fill="gray", outline="black", smooth=True)
 
         self.canvas.create_oval(cx-20, cy-20, cx+20, cy+20, fill="#333333", outline="black")
         
         if self.ligado:
             self.angulo += self.velocidade
         
         self.root.after(20, self.animar)
 
if __name__ == "__main__":
    root = tk.Tk()
    app = VentiladorApp(root)
    root.mainloop()