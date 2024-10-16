import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk  # Import necessário para o Notebook (abas)
import difflib

def comparar_textos():
    texto1 = text_area1.get("1.0", tk.END).strip()
    texto2 = text_area2.get("1.0", tk.END).strip()
    diff = difflib.ndiff(texto1.splitlines(), texto2.splitlines())

    result_area.config(state=tk.NORMAL)
    result_area.delete("1.0", tk.END)

    tem_diferenca = False
    for linha in diff:
        if linha.startswith('- '):
            result_area.insert(tk.INSERT, f"Removido: {linha[2:]}\n", 'removido')
            tem_diferenca = True
        elif linha.startswith('+ '):
            result_area.insert(tk.INSERT, f"Adicionado: {linha[2:]}\n", 'adicionado')
            tem_diferenca = True
        elif linha.startswith('? '):
            result_area.insert(tk.INSERT, f"Detalhes:   {linha[2:]}\n", 'detalhes')
            tem_diferenca = True

    if not tem_diferenca:
        result_area.insert(tk.INSERT, "Os textos são iguais.")

    result_area.config(state=tk.DISABLED)

# Configuração da janela principal
root = tk.Tk()
root.title("Comparador de Textos")
root.geometry("800x600")

# Criação do Notebook para adicionar abas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Aba de Comparação de Textos
comparacao_frame = ttk.Frame(notebook)
notebook.add(comparacao_frame, text="Comparar Textos")

# Frame para o texto 1
frame1 = tk.LabelFrame(comparacao_frame, text="Texto 1", padx=10, pady=10)
frame1.pack(fill="both", expand="yes", padx=10, pady=5)

text_area1 = scrolledtext.ScrolledText(frame1, wrap=tk.WORD, width=70, height=10)
text_area1.pack()

# Frame para o texto 2
frame2 = tk.LabelFrame(comparacao_frame, text="Texto 2", padx=10, pady=10)
frame2.pack(fill="both", expand="yes", padx=10, pady=5)

text_area2 = scrolledtext.ScrolledText(frame2, wrap=tk.WORD, width=70, height=10)
text_area2.pack()

# Botão para comparar os textos
compare_button = tk.Button(comparacao_frame, text="Comparar Textos", command=comparar_textos)
compare_button.pack(pady=10)

# Área de resultado
result_frame = tk.LabelFrame(comparacao_frame, text="Resultado das Diferenças", padx=10, pady=10)
result_frame.pack(fill="both", expand="yes", padx=10, pady=5)

result_area = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, width=70, height=10, state=tk.DISABLED)
result_area.tag_config('removido', foreground='red')
result_area.tag_config('adicionado', foreground='green')
result_area.tag_config('detalhes', foreground='blue')
result_area.pack()

# Aba de Resumo
resumo_frame = ttk.Frame(notebook)
notebook.add(resumo_frame, text="Resumo")

# Conteúdo da Aba Resumo
resumo_label = tk.Label(resumo_frame, text="Esta é a aba de Resumo.\nAdicione aqui qualquer conteúdo que desejar.", padx=10, pady=10)
resumo_label.pack()

# Inicia o loop da interface gráfica
root.mainloop()
