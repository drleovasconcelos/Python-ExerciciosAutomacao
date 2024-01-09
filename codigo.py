#passo a passo do meu código

#clicar -> pyautogui.click
#escrever -> pyautogui.write
#apertar -> pyautogui.press
#apertar -> pyautogui.hotkey
#scroll (rolar a página) -> pyautogui.sroll
# --------------------------
#passo 1 : entrar no sistema da empresa
#passo 2 : fazer login
#passo 3 : quais produtos cadastrar
#passo 4 : cadastrar um produto
#passo 5 : repetir até acabar a base de dados
import pyautogui
import time
pyautogui.PAUSE = 1             ## A CADA COMANDO ESPERA 1 SEGUNDOminha senha
pyautogui.press("win")          ##clic na janela do windons
pyautogui.write("chrome")      ##apertar o nome do programa / aperta 
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"        ##digita link e aperta enter
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(5) ## vai esperar 5 segundos APENAS NESSE LOCAL
pyautogui.click(x=1090, y=509) #localizei o local onde ia clicar através do arquivo auxiliar
pyautogui.write("pythonimpressionador@gmail.com") #digitar o e-mail 
pyautogui.press("tab") #passar para o campo de senha
pyautogui.write("minha senha") #Digitar a senha
pyautogui.click(x=980, y=718)  ## DIRECIONEI PARA O BOTÃO LOGAR

## pip install pandas numpy openpyxl - instalar panda para importar base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:   ##tabela.index = linhas da tabela / tabela.columns = colunas da tabela
    pyautogui.click(x=764, y=362)
    #codigoLogitech 
    codigo = tabela.loc[linha, "codigo"] #ele pega a linha e a coluna em sequencia
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) #1
    pyautogui.press("tab")
    #preço
    pyautogui.write(str(tabela.loc[linha, "preço_unitario"]))
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    pyautogui.write(tabela.loc[linha, "obs"])
    if not pandas.isna("obs"): #verifica se esta vazio = isna
        pyautogui.write("obs")
    #enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)
    # repetir até acabar a base de dados