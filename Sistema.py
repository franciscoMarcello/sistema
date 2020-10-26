from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox


janela = Tk()

#INICIO DA CLASSE DE FUNÇÕES.
class Funcs():
    def botao_limpar_clientes(self):
        self.NomeEntry.delete(0, END)
        self.CPFEntry.delete(0, END) 
        self.telefone.delete(0, END) 
        self.endereco.delete(0, END) 
        self.email.delete(0, END)

    def botao_limpar_produtos(self):
        self.produto_entry.delete(0, END)
        self.valorEntry.delete(0, END)
        self.datainclusao.delete(0, END)
        self.descricao.delete(0, END)
        self.codigo_produto.delete(0, END)

    def concluindo_venda(self):
        self.valor_copia = 0.25
        self.qaun_folha = float(self.quantidade_folha.get())
        self.resultado_venda = float(self.valor_copia * self.qaun_folha) 
        self.lresultado["text"] =  "R$ {:.2f}"  .format(self.resultado_venda) 

        self.troco_venda = float(self.troco_folha.get()) 
        self.resultado_troco = float(self.troco_venda - self.resultado_venda)
        self.total_troco["text"] = "R$ {:.2f}"  .format(self.resultado_troco) 
#FIM DA CLASSE DE FUNÇÕES.


#INICIO DA CLASSE DO SISTEMA.
class sistema(Funcs):
    def __init__(self):
        self.janela = janela
        self.tela_usuario()
        self.tela()
        self.frames()
        self.lista_frame1()
        self.lista_frame2()
        self.criarTabelas()
        self.select_lista()
        self.select_lista2()
        janela.mainloop()


    #INICIO DO BANCO DE DADOS.
    def conectar_bd(self):
        self.conn = sqlite3.connect("TESTE2.db")
        self.cursor = self.conn.cursor()
        

    def desconecta_bd(self):
        self.conn.close()

    def criarTabelas(self):
        self.conectar_bd();print("Conectado ao banco de dados")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            codigo_cliente INTEGER PRIMARY KEY,
            Nome_cliente VARCHAR(50) NOT NULL,
            CPF VARCHAR(15) NOT NULL UNIQUE,
            Email VARCHAR(50) NOT NULL,
            Endereco VARCHAR(60) NOT NULL,
            Telefone INTEGER(20) NOT NULL
        );
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos(
            codigo_produto INTEGER PRIMARY KEY,
            Nome_produto VARCHAR(100) NOT NULL,
            Valor_produto DECIMAL(10,2) NOT NULL,
            data_inclusao DATETIME NOT NULL,
            descricao_produto VARCHAR(100)
        );
        """)
        self.conn.commit(); print("Banco de dados Criado")
        self.desconecta_bd()
    def Registro_clientes(self):
        
        self.nome =self.NomeEntry.get()
        self.cpf = self.CPFEntry.get()
        self.tell = self.telefone.get()
        self.endere = self.endereco.get()
        self.mail = self.email.get()
        if self.nome != "" and self.cpf != "" and self.tell != "" and self.endere != "" and self.mail != "":
            self.conectar_bd()
            self.cursor.execute("INSERT INTO clientes(Nome_cliente, CPF, Email, Endereco, Telefone) VALUES(?,?,?,?,?)",(self.nome, self.cpf, self.mail, self.endere, self.tell))        
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            messagebox.showinfo(title="Cadastro", message="Cadrasto realizado com sucesso")
        else:
            messagebox.showerror(title="ERRO", message="Campo vazio")
    
    def Registro_produtos(self):
        
        self.nome_produto = self.produto_entry.get()
        self.valor_produto = self.valorEntry.get()
        self.data_inclusao = self.datainclusao .get()
        self.desc_produto = self.descricao.get()
        if self.nome_produto != "" and self.valor_produto != "" and self.data_inclusao != "" and self.desc_produto != "":
            self.conectar_bd()
            self.cursor.execute("INSERT INTO Produtos(Nome_produto, Valor_produto, data_inclusao, descricao_produto) VALUES(?,?,?,?)",(self.nome_produto, self.valor_produto ,self.data_inclusao, self.desc_produto))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista2()
            messagebox.showinfo(title="Cadastro", message="Cadrasto realizado com sucesso")
        else:
            messagebox.showerror(title="ERRO", message="Campo vazio")
    #FIM DO BANCO DE DADOS.



    #MOSTRA NOS TREEVEWS OS DADOS DO BANCO DE DADOS TELA DE CLIENTES.
    def select_lista(self):
        self.lista_Cli.delete(*self.lista_Cli.get_children())
        self.conectar_bd()
        lista = self.cursor.execute(""" SELECT codigo_cliente, Nome_cliente, CPF, Telefone FROM clientes ORDER BY codigo_cliente ASC;""")
        for i in lista:
            self.lista_Cli.insert("", END, values=i)
        self.desconecta_bd()
    #FIM DO TREEVEWS TELA DE CLIENTES.


    #MOSTRA NOS TREEVEWS OS DADOS DO BANCO DE DADOS TELA DE PRODUTOS.
    def select_lista2(self):
        self.lista_prod.delete(*self.lista_prod.get_children())
        self.conectar_bd()
        lista2 = self.cursor.execute(""" SELECT codigo_produto, Nome_produto, Valor_produto, data_inclusao FROM Produtos ORDER BY codigo_produto ASC;""")
        for i in lista2:
            self.lista_prod.insert("", END, values=i)
        self.desconecta_bd()
    #FIM DO TREEVEWS TELA DE PRODUTOS.


    #CONFIGURAÇÃO E DEFINIÇÃO DA TELA GERAL.
    def tela(self):
        self.janela.title("Só Copias")
        self.janela.configure(bg="#4682B4")
        self.largura_screen = self.janela.winfo_screenwidth()
        self.altura_screen = self.janela.winfo_screenheight()
        self.largura = 500
        self.altura = 300
        self.janela.iconbitmap('D:\Trabalho_python\SÓCOPIASVS1\leao.ico')

        self.posx = self.largura_screen/2 - self.largura/1.5
        self.posy = self.altura_screen/2 - self.altura/1.3
        self.janela.geometry("%dx%d+%d+%d"% (self.largura, self.altura, self.posx, self.posy))
        self.janela.resizable("true", "true")
        self.janela.maxsize(width=900, height=500)
        self.janela.minsize(width=700, height=400)
    #FIM DA TELA DE CONFIGURAÇÃO DE DEFINIÇÃO.


    #LISTA DO FRAME DA TELA DE CADASTRO DE USUARIO.
    def lista_frame1(self):
        self.lista_Cli = ttk.Treeview(self.frame_1,   column=('id','nome','cpf','telefone'), show='headings')
        
        self.lista_Cli.heading("id", text="ID")
        self.lista_Cli.heading("nome", text="Nome")
        self.lista_Cli.heading("cpf", text="CPF")
        self.lista_Cli.heading("telefone", text="Telefone")

       
        self.lista_Cli.column('id', stretch=YES, minwidth=50, width=60, anchor="center")
        self.lista_Cli.column('nome', stretch=YES, minwidth=100, width=150, anchor="center")
        self.lista_Cli.column('cpf', stretch=YES, minwidth=100, width=125, anchor="center")
        self.lista_Cli.column('telefone', stretch=YES, minwidth=100, width=125, anchor="center")

        
        self.scrooLista=Scrollbar(self.frame_1, orient='vertical')
        self.lista_Cli.configure(yscroll=self.scrooLista.set)
        self.scrooLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.90)

        self.lista_Cli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.90)
    #FIM DA LISTA DO FRAME DA TELA DE CADASTRO DE USUARIO.



    #LISTA DO FRAME DA TELA DE CADASTRO DE PRODUTOS.
    def lista_frame2(self):
        self.lista_prod = ttk.Treeview(self.frame_2, height=3, column=("codigo_produto",'nome_produto','valor_produto', 'data_inclusao'), show='headings')
        
        self.lista_prod.heading("codigo_produto", anchor='center', text="Código do produto")
        self.lista_prod.heading("nome_produto", anchor='center', text="Nome do produto")
        self.lista_prod.heading("valor_produto", anchor='center',text="Valor do produto")
        self.lista_prod.heading("data_inclusao", anchor='center',text="Data de inclusão")
       

       
        self.lista_prod.column('codigo_produto', width=100,anchor="center")
        self.lista_prod.column('nome_produto', width=160,anchor="center")
        self.lista_prod.column('valor_produto', width=125,anchor="center")
        self.lista_prod.column('data_inclusao', width=125,anchor="center")
       
        
        self.scrooLista2=Scrollbar(self.frame_2, orient='vertical')
        self.lista_prod.configure(yscroll=self.scrooLista2.set)
        self.scrooLista2.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.90)

        self.lista_prod.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.90)
    #FIM DA TELA DE LISTA DE CADASTRO DE PRODUTO.


    #DEFINIÇÃO DOS FRAMES/ABAS.
    def frames(self):
        self.abas = ttk.Notebook(self.janela)
        self.aba_inicio = Frame(self.abas)
        self.aba_vendas = Frame(self.abas)
        self.aba_cadastro_clientes = Frame(self.abas)
        self.aba_cadastro_produtos = Frame(self.abas)
        self.aba_politica = Frame(self.abas)
        self.aba_vendas.configure(bg="#363636")
        self.aba_cadastro_clientes.configure(bg="#363636")
        self.aba_inicio.configure(bg="#363636")
        self.aba_cadastro_produtos.configure(bg="#363636")
        self.aba_politica.configure(bg="#363636")
        self.abas.add(self.aba_inicio, text="Inicio")
        self.abas.add(self.aba_vendas, text="Venda Rapida")
        self.abas.add(self.aba_cadastro_clientes, text="Cadastro de cliente")
        self.abas.add(self.aba_cadastro_produtos, text="Cadastro de produto")
        self.abas.add(self.aba_politica, text="Relatorios")
        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)
    #FIM DA DEFINIÇÃO DE FRAMES/ABAS.


        #FRAME DA TELA DE INICIO
        self.txt_bem_vindo = Label(self.aba_inicio, text="Bem Vindo!", bg = "#363636", fg = "White",font='cambria 12' )
        self.txt_bem_vindo.place(relx=0.02, rely=0.02 )

        self.txt_inicio = Label(self.aba_inicio, text="Para um bom uso do sistema, leia o Manual!", bg = "#363636", fg = "White",font='cambria 12' )
        self.txt_inicio.place(relx=0.02, rely=0.08 )

        self.txt_manual = Label(self.aba_inicio, text="Manual basico <<< ", bg = "#363636", fg = "White",font='cambria 12' )
        self.txt_manual.place(relx=0.02, rely=0.14 )

        self.txt_do_manual = Label(self.aba_inicio, text="O sistema ainda está em desenvolvimento, muitas funçoes ainda não estão disponiveis. ",
                                                         bg = "#363636", fg = "#DC143C",font='cambria 12' )
        self.txt_do_manual.place(relx=0.02, rely=0.20 )

        self.txt_do_manual_01 = Label(self.aba_inicio, text="Os Botões ALTERAR e DELETAR, ainda não foram adicionados. ",
                                                         bg = "#363636", fg = "#DC143C",font='cambria 12' )
        self.txt_do_manual_01.place(relx=0.02, rely=0.26 )

        self.txt_do_manual_02 = Label(self.aba_inicio, text="A tela VENDA, não está totalmente funcional, ainda não é possivel registrar vendas. ",
                                                         bg = "#363636", fg = "#DC143C",font='cambria 12' )
        self.txt_do_manual_02.place(relx=0.02, rely=0.31 )

        self.txt_do_manual_03 = Label(self.aba_inicio, text="A tela Relatorios, ainda não está funcional.  ",
                                                         bg = "#363636", fg = "#DC143C",font='cambria 12' )
        self.txt_do_manual_03.place(relx=0.02, rely=0.36 )

        self.txt_do_manual_04 = Label(self.aba_inicio, text=" >>> ",
                                                         bg = "#363636", fg = "White",font='cambria 12' )
        self.txt_do_manual_04.place(relx=0.02, rely=0.41 )
        #FIM DA TELA DE INICIO

        #TELA VENDA
        
        self.Ltamanho_folha = Label(self.aba_vendas, text="Escolha tamanho da folha", font='cambria 12', bg = "#363636", fg="white")
        self.Ltamanho_folha.place(relx=0.02, rely=0.02)
        self.tamanho_Var = StringVar()
        self.tamnhoV = ("A4", "A3", "A5", "B5", "B5")
        self.tamanho_Var.set("A4")
        self.tamanhoMenu = OptionMenu(self.aba_vendas, self.tamanho_Var, *self.tamnhoV)
        self.tamanhoMenu.place(relx=0.02, rely=0.10)
        self.tamanhoMenu.config(bg="gray", fg="white")
        self.tamanhoMenu["menu"].config(bg="gray", fg="white")
        self.tamanho_folha = self.tamanho_Var.get()

        self.Ltipo_impressao = Label(self.aba_vendas, text="Escolha o tipo de impressão", font='cambria 12', bg = "#363636", fg="white")
        self.Ltipo_impressao.place(relx=0.02, rely=0.42)
        self.tipo_impressao = StringVar()
        self.tipoV = ("Preto é branco", "Colorido")
        self.tipo_impressao.set("Preto é branco")
        self.tipoMenu = OptionMenu(self.aba_vendas, self.tipo_impressao, *self.tipoV)
        self.tipoMenu.place(relx=0.02, rely=0.50)
        self.tipoMenu.config(bg="gray", fg="white")
        self.tipoMenu["menu"].config(bg="gray", fg="white")
        self.tipo_de_impressao = self.tipo_impressao.get()


        self.Llado_impressao = Label(self.aba_vendas, text="Escolha lado da  impressão", font='cambria 12', bg = "#363636", fg="white")
        self.Llado_impressao.place(relx=0.02, rely=0.72)
        self.lado_Var = StringVar()
        self.ladoV = ("Só frente", "Frente e verso")
        self.lado_Var.set("Só frente")
        self.ladoMenu = OptionMenu(self.aba_vendas, self.lado_Var, *self.ladoV)
        self.ladoMenu.place(relx=0.02, rely=0.80)
        self.ladoMenu.config(bg="gray", fg="white")
        self.ladoMenu["menu"].config(bg="gray", fg="white")
        self.lado_impressao = self.lado_Var.get()
        
        self.lquantidade_folha = Label(self.aba_vendas, text="Quantidade de copias:", font='cambria 12', bg = "#363636", fg="white")
        self.quantidade_folha = ttk.Entry(self.aba_vendas)
        self.lquantidade_folha.place(relx=0.75, rely=0.02)
        self.quantidade_folha.place(relx=0.76, rely=0.08, relwidth=0.21)
        
        self.lbtroco_folha = Label(self.aba_vendas, text="Valor Recebido:", font='cambria 12', bg = "#363636", fg="white")
        self.troco_folha = ttk.Entry(self.aba_vendas)
        self.lbtroco_folha.place(relx=0.75, rely=0.19)
        self.troco_folha.place(relx=0.76, rely=0.25, relwidth=0.21)
        
        self.total_troco = Label(self.aba_vendas, text="R$ 00,00", font='cambria 12', bg = "white", fg="black")
        self.total_troco.place(relx=0.82, rely=0.57)

        self.ltroco = Label(self.aba_vendas, text="Troco:", font='cambria 12', bg = "#363636", fg="white")
        self.ltroco.place(relx=0.74, rely=0.56)

        self.ltotal = Label(self.aba_vendas, text="Total:", font='cambria 12', bg = "#363636", fg="white")
        self.ltotal.place(relx=0.75, rely=0.50)

        self.lresultado = Label(self.aba_vendas, text="R$ 00,00", font='cambria 12', bg = "white", fg="black")
        self.lresultado.place(relx=0.82, rely=0.50)

        self.btn_venda = Button(self.aba_vendas, text='Concluir venda', font='cambria 10', bg = "#3CB371", fg="white", command=self.concluindo_venda)
        self.btn_venda.place(relx=0.80, rely=0.70)

        #FIM TELA VENDA
        
        #FRAME CADASTRO DE CLIENTES
        self.frame_1 = Frame(self.aba_cadastro_clientes)
        self.lb4 = Label(self.aba_cadastro_clientes, text="Nome completo:",  bg="#363636", fg = "white",font='cambria 12')    
        self.lb5 = Label(self.aba_cadastro_clientes, text="CPF:", bg="#363636", fg = "white",font='cambria 12')
        self.lb6 = Label(self.aba_cadastro_clientes, text="Telefone:", bg="#363636", fg = "white",font='cambria 12')
        self.lb7 = Label(self.aba_cadastro_clientes, text="Endereço:", bg="#363636", fg = "white",font='cambria 12')
        self.lb8 = Label(self.aba_cadastro_clientes, text="Email:", bg="#363636", fg = "white",font='cambria 12')
        self.NomeEntry = ttk.Entry(self.aba_cadastro_clientes)
        self.CPFEntry = ttk.Entry(self.aba_cadastro_clientes)
        self.telefone = ttk.Entry(self.aba_cadastro_clientes)
        self.endereco = ttk.Entry(self.aba_cadastro_clientes)
        self.email = ttk.Entry(self.aba_cadastro_clientes)

        self.bt_cadastro_c = Button(self.aba_cadastro_clientes, text='Cadastrar',command=self.Registro_clientes) 
        self.bt_cadastro_c.place(relx=0.35, rely=0.35) 

        self.bt_limpar_c = Button(self.aba_cadastro_clientes, text='Limpar', command=self.botao_limpar_clientes) 
        self.bt_limpar_c.place(relx=0.45, rely=0.35)  

        

        self.NomeEntry.place(relx=0.20, rely=0.02, relwidth=0.40)
        self.CPFEntry.place(relx=0.20, rely=0.08, relwidth=0.40)
        self.telefone.place(relx=0.20, rely=0.14, relwidth=0.40)
        self.endereco.place(relx=0.20, rely=0.20, relwidth=0.40)
        self.email.place(relx=0.20, rely=0.26, relwidth=0.40)
        self.lb4.place(relx=0.02, rely=0.02)
        self.lb5.place(relx=0.02, rely=0.08)
        self.lb6.place(relx=0.02, rely=0.14)
        self.lb7.place(relx=0.02, rely=0.20)
        self.lb8.place(relx=0.02, rely=0.26)
        self.frame_1.place(relx=0.02, rely=0.48, relwidth=0.96, relheight=0.50)
        #FIM DO FRAME CLIENTES



        #FRAME DE CADASTRO DE PRODUTOS
        self.frame_2 = Frame(self.aba_cadastro_produtos)
        self.lb_codigo_produto = Label(self.aba_cadastro_produtos, text="Codigo do Produto:", bg="#363636", fg = "white",font='cambria 12')
        self.lb4 = Label(self.aba_cadastro_produtos, text="Nome do Produdo:",  bg="#363636", fg = "white",font='cambria 12')    
        self.lb5 = Label(self.aba_cadastro_produtos, text="Valor do Produto:", bg="#363636", fg = "white",font='cambria 12')
        self.lb6 = Label(self.aba_cadastro_produtos, text="Data de Inclusão: ", bg="#363636", fg = "white",font='cambria 12')
        self.lb7 = Label(self.aba_cadastro_produtos, text="Descrição: ", bg="#363636", fg = "white",font='cambria 12')
        
        self.produto_entry = ttk.Entry(self.aba_cadastro_produtos)
        self.valorEntry = ttk.Entry(self.aba_cadastro_produtos)
        self.datainclusao = ttk.Entry(self.aba_cadastro_produtos)
        self.codigo_produto = ttk.Entry(self.aba_cadastro_produtos)
        self.descricao = ttk.Entry(self.aba_cadastro_produtos)

        self.bt_cadastro_p = Button(self.aba_cadastro_produtos, text='Cadastrar', bd=2 ,command=self.Registro_produtos) 
        self.bt_cadastro_p.place(relx=0.45, rely=0.35)          

        self.bt_limpar_p = Button(self.aba_cadastro_produtos, text='Limpar', bd=2 ,command=self.botao_limpar_produtos) 
        self.bt_limpar_p.place(relx=0.55, rely=0.35) 

       

        self.produto_entry.place(relx=0.22, rely=0.02, relwidth=0.40)
        self.valorEntry.place(relx=0.22, rely=0.08, relwidth=0.40)
        self.datainclusao.place(relx=0.22, rely=0.14, relwidth=0.40)
        self.codigo_produto.place(relx=0.22, rely=0.20, relwidth=0.40)
        self.descricao.place(relx=0.22, rely=0.26, relwidth=0.40)
        self.lb4.place(relx=0.02, rely=0.02)
        self.lb5.place(relx=0.02, rely=0.08)
        self.lb6.place(relx=0.02, rely=0.14)
        self.lb_codigo_produto.place(relx=0.02, rely=0.20)
        self.lb8.place(relx=0.02, rely=0.26)
        self.lb7.place(relx=0.02, rely=0.26)
        self.frame_2.place(relx=0.02, rely=0.48, relwidth=0.96, relheight=0.50)
        #FIM DO FRAME PRODUTOS


    #DEFINIÇÃO PARA FECHAR TELAS PARA EVITAR ERRO DE AUTENTICAÇÃO.
    def fechar_tela(self):
        self.tela_usuario.destroy()
        self.janela.destroy()
    #FIM DA TELA DE FECHAR.



    #AUTENTICAÇÃO TELA DE LOGIN.
    def login_(self):
        self.user = self.usuario.get()
        self.senh_a = self.senha.get()
        if self.user == "admin" and self.senh_a == "123":
            self.tela_usuario.destroy()
        else:
            messagebox.showerror(title = "ERROR", message = "Usuario ou senha Invalidos!")
    #FIM DA TELA DE AUTENTICAÇÃO.


    #TELA DE ENTRADA DE USUARIO.
    def tela_usuario(self):
        self.tela_usuario = Toplevel()
        self.tela_usuario.title("Login")
        self.tela_usuario.iconbitmap('D:\Trabalho_python\SÓCOPIASVS1\leao.ico')
        
        self.usuario = ttk.Entry(self.tela_usuario)
        self.senha = ttk.Entry(self.tela_usuario, show="*")
        self.usuario.place(relx=0.38, rely=0.35)
        self.senha.place(relx=0.38, rely=0.45)

        self.imag= PhotoImage(file="D:\Trabalho_python\SÓCOPIASVS1\impressora.png")
        self.limagem = Label(self.tela_usuario, image=self.imag,bg="#363636")
        self.limagem.place(relx=0.40, rely=0.10)

        self.lb_usuario = Label(self.tela_usuario, text="Usuário", bg="#363636", fg = "white",font='cambria 12')
        self.lb_senha = Label(self.tela_usuario, text="Senha", bg="#363636", fg = "white",font='cambria 12')
        self.lb_usuario.place(relx=0.17, rely=0.33)
        self.lb_senha.place(relx=0.17, rely=0.43)
        
        self.lb_texto_aviso = Label(self.tela_usuario, text="Por conta dos Protocolos de Segurança",
                                                         bg="#363636", fg = "white",font='cambria 10')
        self.lb_texto_aviso.place(relx=0.04, rely=0.79)
        self.lb_texto_aviso01 = Label(self.tela_usuario, text="Não tente minizar a tela antes de realizar o login!!",
                                                         bg="#363636", fg = "white",font='cambria 10')
        self.lb_texto_aviso01.place(relx=0.04, rely=0.85)
        self.lb_texto_aviso02 = Label(self.tela_usuario, text="Para sair do sistema use o botão sair!!",
                                                         bg="#363636", fg = "white",font='cambria 10')
        self.lb_texto_aviso02.place(relx=0.04, rely=0.91)

        self.bt_sair = Button(self.tela_usuario, text="Sair", command=self.fechar_tela, bg="#DC143C", fg = "white",font='cambria 10')
        self.bt_sair.place(relx=0.60, rely=0.60, relwidth=0.20)

        self.bt_entrar = Button(self.tela_usuario, text="Entrar", command=self.login_,  bg="#3CB371", fg = "white",font='cambria 10')
        self.bt_entrar.place(relx=0.35, rely=0.60, relwidth=0.20)


        self.tela_usuario.configure(bg="#363636")
        self.largura_screen = self.tela_usuario.winfo_screenwidth()
        self.altura_screen = self.tela_usuario.winfo_screenheight()
        self.largura = 300
        self.altura = 300

        self.posx = self.largura_screen/2 - self.largura/1.8
        self.posy = self.altura_screen/2 - self.altura/1.8
        self.tela_usuario.geometry("%dx%d+%d+%d"% (self.largura, self.altura, self.posx, self.posy))
        self.tela_usuario.resizable("false", "false") 
        self.tela_usuario.transient(self.janela)
        self.tela_usuario.focus_force()
        self.tela_usuario.grab_set()
        self.tela_usuario.protocol("WM_DELETE_WINDOW", self.janela)   
    #FIM DA TELA DE ENTRADA DE USUARIO.


        style=ttk.Style(janela)
        style.theme_use('alt') 

    

sistema()
#FIM DA CLASSE DO SISTEMA.