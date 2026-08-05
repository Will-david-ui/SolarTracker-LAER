import numpy as np
import customtkinter as ctk

ctk.set_appearance_mode("dark")

# Configuração da janela principal
app = ctk.CTk()
app.title("Solar Track")
app.geometry("450x400")

# Função para calcular e atualizar a tela
def posicionamento_solar():
    entrada = campo_usuario.get().strip()
    
    try:
        lat = float(entrada)
        
        # Validação do intervalo da latitude
        if not (-90 <= lat <= 90):
            resultado_label.configure(
                text="Latitude inválida!\nDigite um valor entre -90° e +90°.",
                text_color="#FF5555"
            )
            return

        # Cálculo dos ângulos
        lat_abs = np.abs(lat)
        inclinacao = np.where(lat_abs <= 10, 10.0, 3.7 + (0.69 * lat_abs))
        azimute = np.where(lat >= 0, 180.0, 0.0)

        if (lat >= 0):
            direcao = "Sul"
        else:
            direcao = "Norte"

        # Atualização da Label com os resultados
        texto_resultado = (
            f"• Inclinação ideal: {float(inclinacao):.2f}°\n"
            f"• Ângulo de azimute: {float(azimute):.0f}° (Orientado ao {direcao})"
        )
        resultado_label.configure(text=texto_resultado, text_color="#50FA7B")

    except ValueError:
        resultado_label.configure(
            text="Entrada inválida!\nPor favor, digite um número (ex: -23.55).",
            text_color="#FF5555"
        )

# Título e Subtítulo
titulo = ctk.CTkLabel(app, text="Posicionamento Solar", font=ctk.CTkFont(size=22, weight="bold"))
titulo.pack(pady=20)

subtitulo = ctk.CTkLabel(app, text="Digite a latitude para obter a inclinação e o azimute ideais.",font=ctk.CTkFont(size=14))
subtitulo.pack(pady=5)

# Campo de entrada
campo_usuario = ctk.CTkEntry(app, placeholder_text="Ex: -23.55", width=150, height=35)
campo_usuario.pack(pady=10)

# Botão
botao = ctk.CTkButton(app, text="Calcular Ângulos", command=posicionamento_solar, height=35)
botao.pack(pady=10)

# Quadro para destacar o resultado na tela
frame_resultado = ctk.CTkFrame(app, width=380, height=100)
frame_resultado.pack(pady=20, padx=20, fill="x")

resultado_label = ctk.CTkLabel(frame_resultado, text="Aguardando dados...", font=ctk.CTkFont(size=14, weight="bold"))
resultado_label.pack(expand=True, pady=15)

# Iniciar a aplicação
app.mainloop()