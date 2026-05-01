import tkinter as tk
import math
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw

class VentiladorPremium:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventilador muito foda")
        self.root.geometry("450x680") 
        self.root.configure(bg="#f4f4f4")

        self.angulo = 0
        self.velocidade = 0
        self.limite_seguranca = 130
        self.modo_constante = False 

        self.foto_centro = self.carregar_imagem_circular("Wypher _3.jpg", (40, 40))

        self.canvas = tk.Canvas(root, width=450, height=500, bg="#f4f4f4", highlightthickness=0)
        self.canvas.pack()

        self.controles = tk.Frame(root, bg="#2c3e50", pady=15)
        self.controles.pack(fill=tk.X, side=tk.BOTTOM)

        estilo_btn = {"font": ("Arial", 10, "bold"), "fg": "white", "width": 8, "bd": 1, "relief": "raised", "cursor": "hand2"}
        btn_frame = tk.Frame(self.controles, bg="#2c3e50")
        btn_frame.pack()

        tk.Button(btn_frame, text="- 5", bg="#e67e22", command=lambda: self.ajustar_velocidade(-5), **estilo_btn).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="OFF", bg="#c0392b", command=lambda: self.set_vel(0), **estilo_btn).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="+ 5", bg="#27ae60", command=lambda: self.ajustar_velocidade(5), **estilo_btn).pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="Constante", bg="#8e44ad", command=self.alternar_constante, **estilo_btn).pack(side=tk.LEFT, padx=5)

        self.label_velocidade = tk.Label(self.controles, text="VELOCIDADE: 0.0", font=("Consolas", 14, "bold"), 
                                         bg="#1a252f", fg="#ff00dd", width=22, pady=5)
        self.label_velocidade.pack(pady=10)

        self.animar()

    def alternar_constante(self):
        self.modo_constante = not self.modo_constante
        cor = "#00ffff" if self.modo_constante else "#ff00dd"
        self.label_velocidade.config(fg=cor)

    def carregar_imagem_circular(self, caminho, tamanho):
        try:
            img = Image.open(caminho).convert("RGBA")
            img = img.resize(tamanho, Image.LANCZOS)
            mascara = Image.new("L", tamanho, 0)
            draw = ImageDraw.Draw(mascara)
            draw.ellipse((0, 0) + tamanho, fill=255)
            img_circular = Image.new("RGBA", tamanho, (0, 0, 0, 0))
            img_circular.paste(img, (0, 0), mask=mascara)
            return ImageTk.PhotoImage(img_circular)
        except:
            return None

    def set_vel(self, v):
        self.velocidade = float(v)
        self.atualizar_label()

    def ajustar_velocidade(self, delta):
        nova_vel = self.velocidade + delta
        if nova_vel >= self.limite_seguranca:
            self.velocidade = 0
            messagebox.showwarning("SEGURANÇA", "PARE!! O VENTILADOR IRÁ SUPERAQUECER!\nMotor desligado.")
        else:
            self.velocidade = max(0.0, nova_vel)
        self.atualizar_label()

    def atualizar_label(self):
        self.label_velocidade.config(text=f"VELOCIDADE: {self.velocidade:.1f}")

    def animar(self):
        if not self.modo_constante:
            self.velocidade *= 0.99
            if self.velocidade < 0.1:
                self.velocidade = 0
        
        self.atualizar_label()
        self.canvas.delete("all")

        cx, cy, raio_grade = 225, 180, 160
        
        self.canvas.create_oval(140, 445, 310, 475, fill="#d1d1d1", outline="")
        self.canvas.create_oval(140, 430, 310, 470, fill="#273e5f", outline="#191d21", width=2)
        self.canvas.create_oval(145, 435, 305, 460, fill="#34495e", outline="") 
        self.canvas.create_rectangle(215, 190, 235, 450, fill="#718093", outline="#2f3640")
        
        for i in range(0, 360, 15):
            rad = math.radians(i)
            self.canvas.create_line(cx, cy, cx+raio_grade*math.cos(rad), cy+raio_grade*math.sin(rad), fill="#dcdde1")
        
        self.canvas.create_oval(cx-45, cy-45, cx+45, cy+45, fill="#8b1884", outline="black")

        self.angulo = (self.angulo + self.velocidade) % 360
        for i in range(3):
            ang = math.radians(self.angulo + (i * 120))
            pts_geo = [(5, 0), (25, 40), (45, 80), (50, 110), (35, 135), (0, 145), (-20, 110), (-5, 40)]
            finais = []
            for larg, dist in pts_geo:
                px = cx + dist * math.cos(ang) - larg * math.sin(ang)
                py = cy + dist * math.sin(ang) + larg * math.cos(ang)
                finais.extend([px, py])
            self.canvas.create_polygon(finais, fill="#1e3799", outline="#4a69bd", width=2, smooth=True)
        
        for r in[40, 80, 120, 160]:
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="#bdc3c7")
        
        if self.foto_centro:
            self.canvas.create_oval(cx-21, cy-21, cx+21, cy+21, fill="white", outline="white")
            self.canvas.create_image(cx, cy, image=self.foto_centro)
        else:
            self.canvas.create_oval(cx-18, cy-18, cx+18, cy+18, fill="#2f3640", outline="white")

        self.root.after(20, self.animar)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentiladorPremium(root)
    root.mainloop()
