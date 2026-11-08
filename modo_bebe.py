import keyboard
import webview

# URL do YouTube focada em desenhos e músicas infantis
LINK_YOUTUBE = "https://youtube.com"

def bloquear_teclas(evento):
    """
    Função que intercepta as teclas. Se for ESC, fecha o programa.
    Se for qualquer outra tecla, o código 'engole' o comando e não deixa o Windows executar.
    """
    if evento.name == 'esc':
        print("Saindo do Modo Bebê...")
        # Fecha a janela do programa quando ESC é pressionado
        janela.destroy()
    else:
        # Bloqueia qualquer outra tecla (Windows, Alt+F4, Tab, etc)
        return False 

print("Iniciando o Modo Bebê... Pressione ESC para sair a qualquer momento.")

# 1. Ativa o gancho de bloqueio de teclado global
keyboard.hook(bloquear_teclas, suppress=True)

# 2. Cria uma janela de navegador própria que abre direto em tela cheia (fullscreen)
janela = webview.create_window(
    'Modo Bebê - YouTube', 
    LINK_YOUTUBE, 
    fullscreen=True, # Garante que vai cobrir a tela inteira e sumir com a barra do Windows
    text_select=False # Impede que o bebê selecione textos ou arraste coisas na tela
)

# 3. Inicia o navegador travado na tela
webview.start()

# 4. Quando o programa fechar (via ESC), libera o teclado do computador de volta
keyboard.unhook_all()
print("Teclado liberado com sucesso!")
