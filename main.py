import tkinter as tk
import subprocess

# Função para chamar o script home.py com o texto inserido pelo usuário
def enviar_texto():
    texto = entrada_texto.get()  # Obtém o texto inserido pelo usuário
    with open('input.txt', 'w') as arquivo:
        arquivo.write(texto)  # Escreve o texto em um arquivo chamado input.txt
    # Chama o script home.py usando subprocess para obter a resposta
    resultado = subprocess.check_output(['python', 'home.py'], text=True)
    label_resultado.config(text="Resposta: " + resultado)  # Atualiza o rótulo com a resposta

# Configuração da interface gráfica
root = tk.Tk()
root.title("Interface de Envio de Texto")

# Rótulo e entrada para o usuário inserir o texto
label_instrucao = tk.Label(root, text="Digite o texto:")
label_instrucao.pack()
entrada_texto = tk.Entry(root)
entrada_texto.pack()

# Botão para enviar o texto
botao_enviar = tk.Button(root, text="Enviar", command=enviar_texto)
botao_enviar.pack()

# Rótulo para mostrar a resposta
label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Inicia o loop da interface gráfica
root.mainloop()
