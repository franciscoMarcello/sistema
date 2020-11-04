from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from datetime import date
from datetime import datetime


janela = Tk()
total = 0
cpf = ""

# INICIO DA CLASSE DE FUNÇÕES.


class Funcs():
    def botao_limpar_clientes(self):
        self.NomeEntry.delete(0, END)
        self.CPFEntry.delete(0, END)
        self.telefone.delete(0, END)
        self.endereco.delete(0, END)
        self.email.delete(0, END)

    def botao_limpar_produtos(self):
        self.codigo_produto.delete(0, END)
        self.produto_entry.delete(0, END)
        self.valorEntry.delete(0, END)
        self.tipo.delete(0, END)
        self.datainclusao.delete(0, END)
        self.descricao.delete(1.0, END)

    def botao_limpar_produtos_venda(self):
        self.codigo_produto_venda.delete(0, END)
        self.Nome_produto_venda.delete(0, END)
        self.valor_produto_venda.delete(0, END)

    def variaveis_cliente(self):
        self.nome = self.NomeEntry.get()
        self.cpf = self.CPFEntry.get()
        self.tell = self.telefone.get()
        self.endere = self.endereco.get()
        self.mail = self.email.get()

    def botao_limpar_produtos_venda(self):
        self.codigo_produto_venda.delete(0, END)
        self.Nome_produto_venda.delete(0, END)
        self.valor_produto_venda.delete(0, END)

    def botao_limpar_cliente_venda(self):
        self.cpf_cliente_venda.delete(0, END)
        self.nome_cliente_venda.delete(0, END)
        self.telefone_cliente_venda.delete(0, END)

    def variaveis_produto(self):
        self.codigo_prod = self.codigo_produto.get()
        self.nome_produto = self.produto_entry.get()
        self.valor_produto = self.valorEntry.get()
        self.data_inclusao = self.datainclusao .get()
        self.Tipo = self.tipo.get()
        self.desc_produto = self.descricao.get("1.0", END)

    def botao_duplo_click(self, event):
        self.botao_limpar_clientes()
        self.lista_Cli.selection()

        for n in self.lista_Cli.selection():
            col1, col2, col3, col4, col5 = self.lista_Cli.item(n, 'values')
            self.CPFEntry.insert(END, col1)
            self.NomeEntry.insert(END, col2)
            self.telefone.insert(END, col3)
            self.endereco.insert(END, col4)
            self.email.insert(END, col5)

    def botao_duplo_click_2(self, event):
        self.botao_limpar_produtos()
        self.lista_prod.selection()

        for n in self.lista_prod.selection():
            col1, col2, col3, col4, col5, col6 = self.lista_prod.item(
                n, 'values')
            self.codigo_produto.insert(END, col1)
            self.produto_entry.insert(END, col2)
            self.valorEntry.insert(END, col3)
            self.datainclusao.insert(END, col4)
            self.tipo.insert(END, col5)
            self.descricao.insert(END, col6)

    def botao_click_venda_produto(self, event):
        self.botao_limpar_produtos_venda()
        self.lista_produto_venda.selection()

        for n in self.lista_produto_venda.selection():
            col1, col2, col3, col4 = self.lista_produto_venda.item(n, 'values')
            self.codigo_produto_venda.insert(END, col1)
            self.Nome_produto_venda.insert(END, col2)
            self.valor_produto_venda.insert(END, col3)

    def botao_click_venda_cliente(self, event):
        self.botao_limpar_cliente_venda()
        self.lista_clientes_venda.selection()

        for n in self.lista_clientes_venda.selection():
            col1, col2, col3 = self.lista_clientes_venda.item(n, 'values')
            self.cpf_cliente_venda.insert(END, col1)
            self.nome_cliente_venda.insert(END, col2)
            self.telefone_cliente_venda.insert(END, col3)

    def deleta_lista_cliente(self):

        self.variaveis_cliente()
        self.conectar_bd()
        self.cursor.execute(
            """DELETE FROM clientes WHERE CPF= ?""", (self.cpf,))
        self.conn.commit()
        self.desconecta_bd()
        self.botao_limpar_clientes()
        self.select_lista()
        messagebox.showinfo(
            title="Registro", message="Registro deletado com sucesso")

    def deleta_lista_produto(self):
        self.variaveis_produto()
        self.conectar_bd()
        self.cursor.execute(
            """DELETE FROM Produtos WHERE codigo_produto = ?""", (self.codigo_prod,))
        self.conn.commit()
        self.desconecta_bd()
        self.botao_limpar_clientes()
        self.select_lista2()
        messagebox.showinfo(
            title="Registro", message="Registro deletado com sucesso")

    def altera_cliente(self):
        self.variaveis_cliente()
        self.conectar_bd()
        self.cursor.execute(""" UPDATE clientes SET Nome_cliente = ?,  Email = ?, Endereco = ?, Telefone = ? WHERE CPF = ?  """,
                            (self.nome, self.mail, self.endere, self.tell, self.cpf))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.select_lista_venda_clientes()
        messagebox.showinfo(
            title="Registro", message="Registro alterado com sucesso")

    def altera_produto(self):
        self.variaveis_produto()
        self.conectar_bd()
        self.cursor.execute(""" UPDATE Produtos SET Nome_produto = ?,  Valor_produto = ?, data_inclusao = ?, tipo_produto = ? ,descricao_produto = ? WHERE codigo_produto = ?  """,
                            (self.nome_produto, self.valor_produto, self.data_inclusao, self.Tipo, self.desc_produto, self.codigo_prod))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista2()
        self.select_lista_venda_produtos()
        messagebox.showinfo(
            title="Registro", message="Registro alterado com sucesso")

    def busca_cliente(self):
        self.conectar_bd()
        self.lista_Cli.delete(*self.lista_Cli.get_children())
        self.NomeEntry.insert(END, '%')
        nome = self.NomeEntry.get()
        self.cursor.execute(
            """ SELECT CPF, Nome_cliente, Email, Endereco, Telefone FROM clientes
                WHERE Nome_cliente LIKE '%s' ORDER BY Nome_cliente ASC  """ % nome)
        busca_nome_cliente = self.cursor.fetchall()
        for i in busca_nome_cliente:
            self.lista_Cli.insert("", END, values=i)

        self.botao_limpar_clientes()
        self.desconecta_bd()

    def busca_produto(self):
        self.conectar_bd()
        self.lista_prod.delete(*self.lista_prod.get_children())
        self.codigo_produto.insert(END, '%')
        codigo_produto = self.codigo_produto.get()
        self.cursor.execute(
            """ SELECT codigo_produto, Nome_produto, Valor_produto, data_inclusao,tipo_produto, descricao_produto FROM Produtos
                WHERE codigo_produto LIKE '%s' ORDER BY codigo_produto ASC  """ % codigo_produto)
        busca_nome_produto = self.cursor.fetchall()
        for i in busca_nome_produto:
            self.lista_prod.insert("", END, values=i)

        self.botao_limpar_produtos()
        self.desconecta_bd()

    def busca_produto_venda(self):
        self.conectar_bd()
        self.lista_produto_venda.delete(
            *self.lista_produto_venda.get_children())
        self.codigo_produto_venda.insert(END, '%')
        codigo_produto2 = self.codigo_produto_venda.get()
        self.cursor.execute(
            """ SELECT codigo_produto, Nome_produto, Valor_produto, data_inclusao,tipo_produto, descricao_produto FROM Produtos
                WHERE codigo_produto LIKE '%s' ORDER BY codigo_produto ASC  """ % codigo_produto2)
        busca_nome_produto = self.cursor.fetchall()
        for i in busca_nome_produto:
            self.lista_produto_venda.insert("", END, values=i)

        self.botao_limpar_produtos_venda()
        self.desconecta_bd()

    def busca_cliente_venda(self):
        self.conectar_bd()
        self.lista_clientes_venda.delete(
            *self.lista_clientes_venda.get_children())
        self.cpf_cliente_venda.insert(END, '%')
        nome_cliente_venda2 = self.cpf_cliente_venda.get()
        self.cursor.execute(
            """ SELECT CPF, Nome_cliente, Telefone, Endereco, Email FROM clientes
                WHERE CPF LIKE '%s' ORDER BY Nome_cliente ASC  """ % nome_cliente_venda2)
        busca_nome_cliente = self.cursor.fetchall()
        for i in busca_nome_cliente:
            self.lista_clientes_venda.insert("", END, values=i)

        self.botao_limpar_cliente_venda()
        self.desconecta_bd()

    def Selecionando_cliente(self):
        global cpf
        cpf = self.cpf_cliente_venda.get()
        self.lcliente_selecionado["text"] = "{}"  .format(
            self.cpf_cliente_venda.get())
        self.cpf_cliente_venda.delete(0, END)
        self.nome_cliente_venda.delete(0, END)
        self.telefone_cliente_venda.delete(0, END)

    def troco_venda2(self):
        global total
        self.valor_recebido = float(self.valor_recebido_entry.get())
        troco_resultado = self.valor_recebido - total
        self.label_troco_resultado['text'] = "R${:.2f}" .format(
            troco_resultado)

    def Concluir(self):
        global cpf
        global total
        dataToday = date.today()
        data = "{}/{}/{}" .format(dataToday.day,
                                  dataToday.month, dataToday.year)
        valor_formatado = '{:.2f}' .format(total)
        self.conectar_bd()
        self.cursor.execute(
            "INSERT INTO Vendas (CPF_cliente,Valor_da_venda, Data) VALUES(?,?,?)", (cpf, valor_formatado, data))
        self.conn.commit()
        self.desconecta_bd()
        self.troco.destroy()
        for apagar_item in self.lista_car.get_children():
            self.lista_car.delete(apagar_item)

        total = 0
        cpf = ""
        self.ltotal_resultado["text"] = ""
        self.lcliente_selecionado["text"] = ""

        messagebox.showinfo(title="Venda concluida",
                            message='Venda concluida com sucesso')
        self.lista_relatorio()

    def concluindo_venda(self):
        global cpf
        global total

        if total != 0:
            self.troco = Toplevel()
            self.troco.title("Xerox")
            self.troco.configure(bg="#363636")
            self.troco.resizable("false", "false")
            self.troco.iconbitmap('C:\ImgProjeto\leao.ico')
            self.label_total = Label(self.troco, text='Total da venda: R${:.2f}' .format(
                total), font='cambria 12', bg="#363636", fg="white")
            self.label_total.place(relx=0.01, rely=0.01)
            self.label_troco = Label(
                self.troco, text='Valor recebido:', font='cambria 12', bg="#363636", fg="white")
            self.label_troco.place(relx=0.01, rely=0.15)
            self.valor_recebido_entry = Entry(self.troco)
            self.valor_recebido_entry.place(
                relx=0.40, rely=0.17, relwidth=0.30)
            self.butao_troco = Button(self.troco, text="Troco",  bg="#3CB371",
                                      fg="white", font='cambria 10', command=self.troco_venda2)
            self.butao_troco.place(relx=0.10, rely=0.50, relwidth=0.20)
            self.butao_concluir_venda = Button(
                self.troco, text="Concluir",  bg="#f90f10", fg="white", font='cambria 10', command=self.Concluir)
            self.butao_concluir_venda.place(
                relx=0.35, rely=0.50, relwidth=0.20)
            self.troco.focus_force()
            self.troco.grab_set()
            self.label_troco_resultado = Label(
                self.troco, text="R$00.00", font='cambria 12', bg="#363636", fg="white")
            self.label_troco_resultado.place(relx=0.10, rely=0.35)
            self.largura = 300
            self.altura = 200
            self.posx = self.largura_screen/2 - self.largura/2
            self.posy = self.altura_screen/2 - self.altura/2
            self.troco.geometry("%dx%d+%d+%d" %
                                (self.largura, self.altura, self.posx, self.posy))

        else:
            messagebox.showerror(
                title="ERRO", message="Campos vazios/Inválidos")

    def busca_data(self):
        self.conectar_bd()
        self.lista_relatorio_venda.delete(
            *self.lista_relatorio_venda.get_children())
        self.data_relatorio.insert(END, '%')
        data = self.data_relatorio.get()
        self.cursor.execute(
            """ SELECT codigo_venda,CPF_cliente,Valor_da_venda, Data FROM Vendas
                WHERE Data LIKE '%s'   """ % data)
        busca_data = self.cursor.fetchall()
        for i in busca_data:
            self.lista_relatorio_venda.insert("", END, values=i)
        self.data_relatorio.delete(0, END)
        self.desconecta_bd()

    def remover_do_carrinho(self):
        global total
        x = self.lista_car.selection()[0]
        valores = self.lista_car.item(x, 'values')
        quantida_valores = float(valores[0])
        valor_valores = float(valores[3])
        total_quantidade = quantida_valores * valor_valores
        total = total - float(total_quantidade)
        self.lista_car.delete(x)
        self.ltotal_resultado["text"] = 'R${:.2f}' .format(total)

        self.lista_car.delete(x)


# FIM DA CLASSE DE FUNÇÕES.


# INICIO DA CLASSE DO SISTEMA.
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
        self.select_lista_venda_clientes()
        self.select_lista_venda_produtos()
        self.lista_crarrinho()
        self.lista_relatorio()
        janela.mainloop()

    # INICIO DO BANCO DE DADOS.

    def conectar_bd(self):
        self.conn = sqlite3.connect("Xeroz3.db")
        self.cursor = self.conn.cursor()

    def desconecta_bd(self):
        self.conn.close()

    def criarTabelas(self):
        self.conectar_bd()
        print("Conectado ao banco de dados")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            CPF VARCHAR(15) NOT NULL PRIMARY KEY,
            Nome_cliente VARCHAR(50) NOT NULL,
            Email VARCHAR(50) NOT NULL UNIQUE,
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
            tipo_produto VARCHAR(10) NOT NULL,
            descricao_produto VARCHAR(100)
        );
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Vendas(
            codigo_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            CPF_cliente VARCHAR(15) NOT NULL,
            Valor_da_venda DECIMAL(10,2) NOT NULL,
            Data DATETIME,
            Tipo VARCHAR(10)

        );
        """)
        self.conn.commit()
        print("Banco de dados Criado")
        self.desconecta_bd()

    def Registro_clientes(self):

        self.nome = self.NomeEntry.get()
        self.cpf = self.CPFEntry.get()
        self.tell = self.telefone.get()
        self.endere = self.endereco.get()
        self.mail = self.email.get()
        if self.nome != "" and self.cpf != "" and self.tell != "" and self.endere != "" and self.mail != "":
            self.conectar_bd()
            self.cursor.execute("INSERT INTO clientes(Nome_cliente, CPF, Email, Endereco, Telefone) VALUES(?,?,?,?,?)", (
                self.nome, self.cpf, self.mail, self.endere, self.tell))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.select_lista_venda_clientes()
            messagebox.showinfo(
                title="Cadastro", message="Cadrasto realizado com sucesso")

        else:
            messagebox.showerror(title="ERRO", message="Campos vazios")

    def Registro_produtos(self):
        self.variaveis_produto()
        if self.nome_produto != "" and self.valor_produto != "" and self.data_inclusao != "" and self.tipo != "" and self.desc_produto != "":
            self.conectar_bd()
            self.cursor.execute("INSERT INTO Produtos(codigo_produto, Nome_produto, Valor_produto, data_inclusao, tipo_produto, descricao_produto) VALUES(?,?,?,?,?,?)", (
                self.codigo_prod, self.nome_produto, self.valor_produto, self.data_inclusao, self.Tipo, self.desc_produto))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista2()
            self.select_lista_venda_produtos()
            messagebox.showinfo(
                title="Cadastro", message="Cadrasto realizado com sucesso")
        else:
            messagebox.showerror(title="ERRO", message="Campos vazios")
    # FIM DO BANCO DE DADOS.

    # MOSTRA NOS TREEVEWS OS DADOS DO BANCO DE DADOS TELA DE CLIENTES.

    def select_lista(self):
        self.lista_Cli.delete(*self.lista_Cli.get_children())
        self.conectar_bd()
        lista = self.cursor.execute(
            """ SELECT  CPF, Nome_cliente, Telefone, Endereco, Email FROM clientes ORDER BY Nome_cliente ASC;""")
        for i in lista:
            self.lista_Cli.insert("", END, values=i)
        self.desconecta_bd()
    # FIM DO TREEVEWS TELA DE CLIENTES.

    # TREEVIEWS TELA VENDA
    def select_lista_venda_produtos(self):
        self.lista_produto_venda.delete(
            *self.lista_produto_venda.get_children())
        self.conectar_bd()
        lista_produto_venda = self.cursor.execute(
            """ SELECT   codigo_produto, Nome_produto, Valor_produto, tipo_produto FROM Produtos ORDER BY codigo_produto ASC;""")
        for i in lista_produto_venda:
            self.lista_produto_venda.insert("", END, values=i)
        self.desconecta_bd()

    def select_lista_venda_clientes(self):
        self.lista_clientes_venda.delete(
            *self.lista_clientes_venda.get_children())
        self.conectar_bd()
        lista_clientes_venda = self.cursor.execute(
            """ SELECT CPF, Nome_cliente, Telefone  FROM clientes ORDER BY Nome_cliente ASC;""")
        for i in lista_clientes_venda:
            self.lista_clientes_venda.insert("", END, values=i)
        self.desconecta_bd()
    # FIM TREEVIEWS TELA VENDA

    # MOSTRA NOS TREEVEWS OS DADOS DO BANCO DE DADOS TELA DE PRODUTOS.
    def select_lista2(self):
        self.lista_prod.delete(*self.lista_prod.get_children())
        self.conectar_bd()
        lista2 = self.cursor.execute(
            """ SELECT codigo_produto, Nome_produto, Valor_produto, data_inclusao, tipo_produto, descricao_produto FROM Produtos ORDER BY codigo_produto ASC;""")
        for i in lista2:
            self.lista_prod.insert("", END, values=i)
        self.desconecta_bd()
    # FIM DO TREEVEWS TELA DE PRODUTOS.

    # MOSTRA NOS TREEVEWS DO CARRINHO.
    def select_lista_carrinho(self):
        global total
        if self.valor_produto_venda.get() != "" and self.quant.get() != "":
            self.lista_car.insert(parent="", index='end', text="", values=(self.quant.get(
            ), self.codigo_produto_venda.get(), self.Nome_produto_venda.get(), self.valor_produto_venda.get()))
            valor_produto = float(self.valor_produto_venda.get())
            Quantidade = float(self.quant.get())
            total = float(total) + float(valor_produto * Quantidade)
            self.ltotal_resultado["text"] = "R$ {:.2f}"  .format(total)
            self.codigo_produto_venda.delete(0, END)
            self.valor_produto_venda.delete(0, END)
            self.Nome_produto_venda.delete(0, END)
            self.quant.delete(0, END)
        else:
            messagebox.showerror(title="ERRO", message="Campo vazio")

    # FIM
    def lista_relatorio(self):
        self.lista_relatorio_venda.delete(
            *self.lista_relatorio_venda.get_children())
        self.conectar_bd()
        relatorio = self.cursor.execute(
            """ SELECT codigo_venda, CPF_cliente, valor_da_venda, Data FROM Vendas ORDER BY Data ASC;""")
        for i in relatorio:
            self.lista_relatorio_venda.insert("", END, values=i)
        self.desconecta_bd()

    # CONFIGURAÇÃO E DEFINIÇÃO DA TELA GERAL.
    def tela(self):
        self.janela.title("Xerox")
        self.janela.configure(bg="#4682B4")
        self.largura_screen = self.janela.winfo_screenwidth()
        self.altura_screen = self.janela.winfo_screenheight()
        self.janela.iconbitmap('C:\ImgProjeto\leao.ico')
        self.largura = 1100
        self.altura = 600

        self.posx = self.largura_screen/2 - self.largura/2.0
        self.posy = self.altura_screen/2 - self.altura/2.3
        self.janela.geometry("%dx%d+%d+%d" %
                             (self.largura, self.altura, self.posx, self.posy))
        self.janela.resizable("true", "true")
        self.janela.maxsize(width=1500, height=900)
        self.janela.minsize(width=700, height=400)
    # FIM DA TELA DE CONFIGURAÇÃO DE DEFINIÇÃO.

    # LISTA DO FRAME DA TELA DE CADASTRO DE USUARIO.

    def lista_frame1(self):
        self.lista_Cli = ttk.Treeview(self.frame_1,   column=(
            'cpf', 'nome', 'telefone', 'endereco', 'email'), show='headings')

        self.lista_Cli.heading("cpf", text="CPF")
        self.lista_Cli.heading("nome", text="Nome")
        self.lista_Cli.heading("telefone", text="Telefone")
        self.lista_Cli.heading("endereco", text="Endereço")
        self.lista_Cli.heading("email", text="Email")

        self.lista_Cli.column('cpf', stretch=YES,
                              minwidth=100, width=125, anchor="center")
        self.lista_Cli.column('nome', stretch=YES,
                              minwidth=100, width=133, anchor="center")
        self.lista_Cli.column('telefone', stretch=YES,
                              minwidth=100, width=125, anchor="center")
        self.lista_Cli.column('endereco', stretch=YES,
                              minwidth=100, width=125, anchor="center")
        self.lista_Cli.column('email', stretch=YES,
                              minwidth=50, width=125, anchor="center")

        self.scrooLista_cadastro_cliente = ttk.Scrollbar(
            self.lista_Cli, orient='vertical', command=self.lista_Cli.yview)
        self.lista_Cli.configure(
            yscrollcommand=self.scrooLista_cadastro_cliente.set)
        self.scrooLista_cadastro_cliente.pack(side=RIGHT, fill=Y)
        self.lista_Cli.place(relx=0.01, rely=0.1,
                             relwidth=0.97, relheight=0.90)

        self.lista_Cli.bind("<Double-1>", self.botao_duplo_click)
    # FIM DA LISTA DO FRAME DA TELA DE CADASTRO DE USUARIO.

    # LISTA DO FRAME DA TELA DE CADASTRO DE PRODUTOS.

    def lista_frame2(self):
        self.lista_prod = ttk.Treeview(self.frame_2, height=3, column=(
            "codigo_produto", 'nome_produto', 'valor_produto', 'data_inclusao', 'tipo', "descricao"), show='headings')

        self.lista_prod.heading(
            "codigo_produto", anchor='center', text="Código")
        self.lista_prod.heading(
            "nome_produto", anchor='center', text="Nome do produto")
        self.lista_prod.heading(
            "valor_produto", anchor='center', text="Valor do produto")
        self.lista_prod.heading(
            "data_inclusao", anchor='center', text="Data de inclusão")
        self.lista_prod.heading("tipo", anchor='center', text="Tipo")
        self.lista_prod.heading(
            "descricao", anchor='center', text="Descrição")

        self.lista_prod.column('codigo_produto', width=60, anchor="center")
        self.lista_prod.column('nome_produto', width=160, anchor="center")
        self.lista_prod.column('valor_produto', width=125, anchor="center")
        self.lista_prod.column('data_inclusao', width=125, anchor="center")
        self.lista_prod.column('tipo', width=125, anchor="center")
        self.lista_prod.column('descricao', width=125, anchor="center")

        self.scrooLista_cadastro_produto = ttk.Scrollbar(
            self.lista_prod, orient=VERTICAL, command=self.lista_prod.yview)
        self.lista_prod.configure(
            yscrollcommand=self.scrooLista_cadastro_produto.set)
        self.scrooLista_cadastro_produto.pack(side=RIGHT, fill=Y)
        self.lista_prod.place(relx=0.01, rely=0.02,
                              relwidth=0.96, relheight=0.90)
        self.lista_prod.bind("<Double-1>", self.botao_duplo_click_2)
    # FIM DA TELA DE LISTA DE CADASTRO DE PRODUTO.

    def lista_crarrinho(self):
        self.lista_car = ttk.Treeview(self.frame_venda, height=3, column=(
            'Quant', "codigo_produto", 'Nome produto', 'valor_produto'), show="headings")
        self.lista_car.heading("Quant", anchor='center', text="Quantidade")
        self.lista_car.heading(
            "codigo_produto", anchor='center', text="Código")
        self.lista_car.heading(
            "Nome produto", anchor='center', text="Nome produto")
        self.lista_car.heading(
            "valor_produto", anchor='center', text="Valor")

        self.lista_car.column('Quant', width=57, anchor="center")
        self.lista_car.column('codigo_produto', width=35, anchor="center")
        self.lista_car.column('Nome produto', width=83, anchor="center")
        self.lista_car.column('valor_produto', width=60, anchor="center")

        self.lista_car.place(relx=0.01, rely=0.01,
                             relwidth=0.99, relheight=0.90)

    # DEFINIÇÃO DOS FRAMES/ABAS.

    def frames(self):
        self.abas = ttk.Notebook(self.janela)
        self.aba_inicio = Frame(self.abas)
        self.aba_cadastro_clientes = Frame(self.abas)
        self.aba_cadastro_produtos = Frame(self.abas)
        self.aba_politica = Frame(self.abas)
        self.aba_cadastro_clientes.configure(bg="#363636")
        self.aba_inicio.configure(bg="#363636")
        self.aba_venda_padrao = Frame(self.abas)
        self.aba_cadastro_produtos.configure(bg="#363636")
        self.aba_venda_padrao.configure(bg="#363636")
        self.aba_politica.configure(bg="#363636")
        self.abas.add(self.aba_inicio, text="Inicio")
        self.abas.add(self.aba_cadastro_produtos, text="Cadastro de Itens")
        self.abas.add(self.aba_cadastro_clientes, text="Cadastro de cliente")
        self.abas.add(self.aba_venda_padrao, text="Venda")
        self.abas.add(self.aba_politica, text="Relatorios")
        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)
    # FIM DA DEFINIÇÃO DE FRAMES/ABAS.

        # FRAME DA TELA DE INICIO
        self.txt_bem_vindo = Label(
            self.aba_inicio, text="Bem Vindo!", bg="#363636", fg="White", font='cambria 20')
        self.txt_bem_vindo.place(relx=0.02, rely=0.02)

        hora_atual = datetime.now()
        hora = hora_atual.hour
        minuto = hora_atual.minute
        segundo = hora_atual.second

        self.txt_do_manual_01 = Label(self.aba_inicio, text="{}:{}:{}" .format(hora, minuto, segundo),
                                      bg="#363636", fg="white", font='cambria 20')
        self.txt_do_manual_01.place(relx=0.90, rely=0.02)

        self.imag_inicio = PhotoImage(file="C:\ImgProjeto\leao.png")
        self.limagem_inicio = Label(
            self.aba_inicio, image=self.imag_inicio, bg="#363636")
        self.limagem_inicio.place(relx=0.25, rely=0.05)
        # FIM DA TELA DE INICIO

        # FRAME CADASTRO DE CLIENTES
        self.frame_1 = Frame(self.aba_cadastro_clientes, bg="#363636")
        self.lb4 = Label(self.aba_cadastro_clientes, text="Nome completo:",
                         bg="#363636", fg="white", font='cambria 12')
        self.lb5 = Label(self.aba_cadastro_clientes, text="CPF:",
                         bg="#363636", fg="white", font='cambria 12')
        self.lb6 = Label(self.aba_cadastro_clientes, text="Telefone:",
                         bg="#363636", fg="white", font='cambria 12')
        self.lb7 = Label(self.aba_cadastro_clientes, text="Endereço:",
                         bg="#363636", fg="white", font='cambria 12')
        self.lb8 = Label(self.aba_cadastro_clientes, text="Email:",
                         bg="#363636", fg="white", font='cambria 12')

        self.CPFEntry = ttk.Entry(self.aba_cadastro_clientes)
        self.NomeEntry = ttk.Entry(self.aba_cadastro_clientes)
        self.telefone = ttk.Entry(self.aba_cadastro_clientes)
        self.endereco = ttk.Entry(self.aba_cadastro_clientes)
        self.email = ttk.Entry(self.aba_cadastro_clientes)

        self.bt_cadastro_c = Button(self.aba_cadastro_clientes, text='Cadastrar',
                                    bg="#3CB371", fg="white", command=self.Registro_clientes)
        self.bt_cadastro_c.place(relx=0.15, rely=0.35, relwidth=0.09)

        self.bt_limpar_c = Button(self.aba_cadastro_clientes, text='Limpar',
                                  bg="#4169E1", fg="white", command=self.botao_limpar_clientes)
        self.bt_limpar_c.place(relx=0.25, rely=0.35, relwidth=0.09)

        self.bt_apagar_c = Button(self.aba_cadastro_clientes, text='Apagar',
                                  bg="#DC143C", fg="white", command=self.deleta_lista_cliente)
        self.bt_apagar_c.place(relx=0.35, rely=0.35, relwidth=0.09)

        self.bt_alterar_c = Button(self.aba_cadastro_clientes, text='Alterar',
                                   bg="black", fg="white", command=self.altera_cliente)
        self.bt_alterar_c.place(relx=0.45, rely=0.35, relwidth=0.09)

        self.bt_buscar_c = Button(self.aba_cadastro_clientes, text='Buscar',
                                  bg="White", fg="Black", command=self.busca_cliente)
        self.bt_buscar_c.place(relx=0.55, rely=0.35, relwidth=0.09)

        self.CPFEntry.place(relx=0.15, rely=0.02, relwidth=0.40)
        self.NomeEntry.place(relx=0.15, rely=0.08, relwidth=0.40)
        self.telefone.place(relx=0.15, rely=0.14, relwidth=0.40)
        self.endereco.place(relx=0.15, rely=0.20, relwidth=0.40)
        self.email.place(relx=0.15, rely=0.26, relwidth=0.40)
        self.lb5.place(relx=0.02, rely=0.02)
        self.lb4.place(relx=0.02, rely=0.08)
        self.lb6.place(relx=0.02, rely=0.14)
        self.lb7.place(relx=0.02, rely=0.20)
        self.lb8.place(relx=0.02, rely=0.26)
        self.frame_1.place(relx=0.02, rely=0.48, relwidth=0.96, relheight=0.50)
        # FIM DO FRAME CLIENTES

        # FRAME DE CADASTRO DE PRODUTOS
        self.frame_2 = Frame(self.aba_cadastro_produtos, bg="#363636")
        self.lb10 = Label(self.aba_cadastro_produtos, text="Cod.:",
                          bg="#363636", fg="white", font='cambria 12')
        self.lb4 = Label(self.aba_cadastro_produtos, text="Nome:",
                         bg="#363636", fg="white", font='cambria 12')
        self.lb5 = Label(self.aba_cadastro_produtos, text="Valor:",
                         bg="#363636", fg="white", font='cambria 12')
        self.lb6 = Label(self.aba_cadastro_produtos, text="Data de Inclusão: ",
                         bg="#363636", fg="white", font='cambria 12')
        self.lb7 = Label(self.aba_cadastro_produtos, text="Descrição: ",
                         bg="#363636", fg="white", font='cambria 12')
        self.lb_tipo = Label(self.aba_cadastro_produtos, text="Tipo: ",
                             bg="#363636", fg="white", font='cambria 12')
        self.codigo_produto = ttk.Entry(self.aba_cadastro_produtos)
        self.produto_entry = ttk.Entry(self.aba_cadastro_produtos)
        self.valorEntry = ttk.Entry(self.aba_cadastro_produtos)
        self.datainclusao = ttk.Entry(self.aba_cadastro_produtos)
        self.tipo = ttk.Entry(self.aba_cadastro_produtos)
        self.descricao = Text(self.aba_cadastro_produtos, font="arial 10")

        self.bt_cadastro_p = Button(self.aba_cadastro_produtos, text='Cadastrar',
                                    bg="#3CB371", fg="white", command=self.Registro_produtos)
        self.bt_cadastro_p.place(relx=0.15, rely=0.35, relwidth=0.09)

        self.bt_limpar_p = Button(self.aba_cadastro_produtos, text='Limpar',
                                  bg="#4169E1", fg="white", command=self.botao_limpar_produtos)
        self.bt_limpar_p.place(relx=0.25, rely=0.35, relwidth=0.09)

        self.bt_apagar_p = Button(self.aba_cadastro_produtos, text='Apagar',
                                  bg="#DC143C", fg="white", command=self.deleta_lista_produto)
        self.bt_apagar_p.place(relx=0.35, rely=0.35, relwidth=0.09)

        self.bt_alterar_p = Button(self.aba_cadastro_produtos, text='Alterar',
                                   bg="black", fg="white", command=self.altera_produto)
        self.bt_alterar_p.place(relx=0.45, rely=0.35, relwidth=0.09)

        self.bt_buscar_p = Button(self.aba_cadastro_produtos, text='Buscar',
                                  bg="White", fg="Black", command=self.busca_produto)
        self.bt_buscar_p.place(relx=0.55, rely=0.35, relwidth=0.09)

        self.codigo_produto.place(relx=0.15, rely=0.02, relwidth=0.40)
        self.produto_entry.place(relx=0.15, rely=0.08, relwidth=0.40)
        self.valorEntry.place(relx=0.15, rely=0.14, relwidth=0.40)
        self.datainclusao.place(relx=0.15, rely=0.20, relwidth=0.40)
        self.tipo.place(relx=0.15, rely=0.26, relwidth=0.40)
        self.descricao.place(relx=0.70, rely=0.02,
                             relwidth=0.25, relheight=0.30)
        self.lb10.place(relx=0.02, rely=0.02)
        self.lb4.place(relx=0.02, rely=0.08)
        self.lb5.place(relx=0.02, rely=0.14)
        self.lb6.place(relx=0.02, rely=0.20)
        self.lb_tipo.place(relx=0.02, rely=0.25)
        self.lb7.place(relx=0.60, rely=0.02)
        self.frame_2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.50)
        # FIM DO FRAME PRODUTOS

        # FRAME DA TELA DE VENDAS
        self.produto = Frame(self.aba_venda_padrao, bg="#363636")
        self.produto.place(relx=0.02, rely=0.04, relwidth=0.50, relheight=0.45)
        self.lista_produto_venda = ttk.Treeview(self.produto, height=3, column=(
            "codigo_produto", 'nome_produto', 'valor_produto', 'tipo'), show='headings')

        self.lista_produto_venda.heading(
            "codigo_produto", anchor='center', text="Código")
        self.lista_produto_venda.heading(
            "nome_produto", anchor='center', text="Nome")
        self.lista_produto_venda.heading(
            "valor_produto", anchor='center', text="Valor")
        self.lista_produto_venda.heading("tipo", anchor='center', text="Tipo")

        self.lista_produto_venda.column(
            'codigo_produto', width=60, anchor="center")
        self.lista_produto_venda.column(
            'nome_produto', width=125, anchor="center")
        self.lista_produto_venda.column(
            'valor_produto', width=125, anchor="center")
        self.lista_produto_venda.column('tipo', width=125, anchor="center")

        self.label_produto = Label(
            self.aba_venda_padrao, text="Itens",  bg="#363636", fg="white", font='cambria 12')
        self.label_produto.place(relx=0.02, rely=0.0)

        self.label_codigo_produto = Label(
            self.aba_venda_padrao, text="Codigo",  bg="#363636", fg="white", font='cambria 12')
        self.label_codigo_produto.place(relx=0.51, rely=0.04)

        self.label_nome_produto = Label(
            self.aba_venda_padrao, text="Nome",  bg="#363636", fg="white", font='cambria 12')
        self.label_nome_produto.place(relx=0.51, rely=0.14)

        self.label_valor_produto = Label(
            self.aba_venda_padrao, text="Valor",  bg="#363636", fg="white", font='cambria 12')
        self.label_valor_produto.place(relx=0.51, rely=0.23)

        self.label_quant = Label(
            self.aba_venda_padrao, text="Quantidade",  bg="#363636", fg="white", font='cambria 12')
        self.label_quant.place(relx=0.51, rely=0.33)

        self.scrooLista_produto = ttk.Scrollbar(
            self.lista_produto_venda, orient='vertical', command=self.lista_produto_venda.yview)
        self.lista_produto_venda.configure(yscroll=self.scrooLista_produto.set)
        self.scrooLista_produto.pack(side=RIGHT, fill=Y)
        self.lista_produto_venda.place(
            relx=0.01, rely=0.02, relwidth=0.95, relheight=0.90)

        self.codigo_produto_venda = ttk.Entry(self.aba_venda_padrao)
        self.Nome_produto_venda = ttk.Entry(self.aba_venda_padrao)
        self.valor_produto_venda = ttk.Entry(self.aba_venda_padrao)
        self.quant = ttk.Entry(self.aba_venda_padrao)

        self.codigo_produto_venda.place(relx=0.51, rely=0.08, relwidth=0.20)
        self.Nome_produto_venda.place(relx=0.51, rely=0.18, relwidth=0.20)
        self.valor_produto_venda.place(relx=0.51, rely=0.27, relwidth=0.20)
        self.quant.place(relx=0.51, rely=0.37, relwidth=0.20)

        self.bt_confirmar_produto_venda = Button(
            self.aba_venda_padrao, text='Confirmar', bg="#3CB371", fg="white", command=self.select_lista_carrinho)
        self.bt_confirmar_produto_venda.place(
            relx=0.51, rely=0.44, relwidth=0.09)

        self.bt_buscar_venda = Button(
            self.aba_venda_padrao, text='Buscar', bg="White", fg="Black", command=self.busca_produto_venda)
        self.bt_buscar_venda.place(relx=0.61, rely=0.44, relwidth=0.09)
        self.lista_produto_venda.bind(
            "<Double-1>", self.botao_click_venda_produto)
        # FIM

        # FRAME DA TELA DE VENDAS, CLIENTES
        global cpf
        self.clientes = Frame(self.aba_venda_padrao, bg="#363636")
        self.clientes.place(relx=0.02, rely=0.50,
                            relwidth=0.50, relheight=0.45)
        self.lista_clientes_venda = ttk.Treeview(self.clientes, height=3, column=(
            "codigo_cliente", 'nome_cliente', "telefone_cliente"), show='headings')

        self.lista_clientes_venda.heading(
            "codigo_cliente", anchor='center', text="CPF")
        self.lista_clientes_venda.heading(
            "nome_cliente", anchor='center', text="Nome do Cliente")
        self.lista_clientes_venda.heading(
            "telefone_cliente", anchor='center', text="Telefone")

        self.lista_clientes_venda.column(
            'codigo_cliente', width=40, anchor="center")
        self.lista_clientes_venda.column(
            'nome_cliente', width=125, anchor="center")
        self.lista_clientes_venda.column(
            'telefone_cliente', width=60, anchor="center")

        self.label_cliente = Label(
            self.aba_venda_padrao, text="Clientes",  bg="#363636", fg="white", font='cambria 12')
        self.label_cliente.place(relx=0.02, rely=0.46)

        self.label_codigo_cliente = Label(
            self.aba_venda_padrao, text="CPF Cliente",  bg="#363636", fg="white", font='cambria 12')
        self.label_codigo_cliente.place(relx=0.51, rely=0.52)

        self.label_nome_cliente = Label(
            self.aba_venda_padrao, text="Nome do Cliente",  bg="#363636", fg="white", font='cambria 12')
        self.label_nome_cliente.place(relx=0.51, rely=0.62)

        self.label_telefone_cliente = Label(
            self.aba_venda_padrao, text="Telefone",  bg="#363636", fg="white", font='cambria 12')
        self.label_telefone_cliente.place(relx=0.51, rely=0.72)

        self.scrooLista_clientes = ttk.Scrollbar(
            self.lista_clientes_venda, orient='vertical', command=self.lista_clientes_venda.yview)
        self.lista_clientes_venda.configure(
            yscroll=self.scrooLista_clientes.set)
        self.scrooLista_clientes.pack(side=RIGHT, fill=Y)
        self.lista_clientes_venda.place(
            relx=0.01, rely=0.02, relwidth=0.95, relheight=0.90)

        self.cpf_cliente_venda = ttk.Entry(self.aba_venda_padrao)
        self.nome_cliente_venda = ttk.Entry(self.aba_venda_padrao)
        self.telefone_cliente_venda = ttk.Entry(self.aba_venda_padrao)

        self.cpf_cliente_venda.place(relx=0.51, rely=0.56, relwidth=0.20)
        self.nome_cliente_venda.place(relx=0.51, rely=0.66, relwidth=0.20)
        self.telefone_cliente_venda.place(relx=0.51, rely=0.76, relwidth=0.20)

        self.bt_confirmar_cliente_venda = Button(
            self.aba_venda_padrao, text='Confirmar', bg="#3CB371", fg="white", command=self.Selecionando_cliente)
        self.bt_confirmar_cliente_venda.place(
            relx=0.51, rely=0.83, relwidth=0.09)

        self.bt_buscar_cliente_venda = Button(
            self.aba_venda_padrao, text='Buscar', bg="White", fg="Black", command=self.busca_cliente_venda)
        self.bt_buscar_cliente_venda.place(relx=0.61, rely=0.83, relwidth=0.09)
        self.lista_clientes_venda.bind(
            "<Double-1>", self.botao_click_venda_cliente)

        self.imag_carrinho = PhotoImage(
            file="C:\ImgProjeto\carrinho-de-compras.png")
        self.Lcarrinho = Label(self.aba_venda_padrao, image=self.imag_carrinho,
                               bg="#363636", fg="white", font='cambria 20')
        self.Lcarrinho.place(relx=0.82, rely=0.01)

        self.frame_venda = Frame(self.aba_venda_padrao,  bg="#363636")
        self.frame_venda.place(relx=0.73, rely=0.12,
                               relwidth=0.26, relheight=0.70)

        self.ltotal_venda = Label(
            self.aba_venda_padrao, text="Total:", bg="#363636", fg="white", font='cambria 12')
        self.ltotal_venda.place(relx=0.73, rely=0.77)

        self.ltotal_resultado = Label(
            self.aba_venda_padrao, text="R$00,00", font='cambria 12', bg="#363636", fg="white")
        self.ltotal_resultado.place(relx=0.77, rely=0.77)

        self.lcliente = Label(self.aba_venda_padrao, text="CPF:",
                              bg="#363636", fg="white", font='cambria 12')
        self.lcliente.place(relx=0.73, rely=0.83)

        self.lcliente_selecionado = Label(self.aba_venda_padrao, text='{}' .format(
            cpf), font='cambria 12',  bg="#363636", fg="#fff")
        self.lcliente_selecionado.place(relx=0.77, rely=0.83)

        self.bt_confirmar_venda = Button(
            self.aba_venda_padrao, text='Concluir Venda', bg="#3CB371", fg="white", command=self.concluindo_venda)
        self.bt_confirmar_venda.place(relx=0.89, rely=0.88, relwidth=0.09)
        self.bt_remover_venda = Button(
            self.aba_venda_padrao, text='Remover item', bg="#DC143C", fg="white", command=self.remover_do_carrinho)
        self.bt_remover_venda.place(relx=0.75, rely=0.88, relwidth=0.09)
        # FIM

        # TELA RELATORIOS
        self.list_relatorios = Frame(self.aba_politica)
        self.list_relatorios.place(
            relx=0.02, rely=0.02, relwidth=0.55, relheight=0.80)
        self.lista_relatorio_venda = ttk.Treeview(self.list_relatorios, height=3, column=(
            "codigo", 'cpf', 'valor', 'data', 'tipo'), show='headings')

        self.lista_relatorio_venda.heading(
            "codigo", anchor='center', text="Código")
        self.lista_relatorio_venda.heading("cpf", anchor='center', text="CPF")
        self.lista_relatorio_venda.heading(
            "valor", anchor='center', text="Valor")
        self.lista_relatorio_venda.heading(
            "data", anchor='center', text="Data")
        self.lista_relatorio_venda.heading(
            "tipo", anchor='center', text="Tipo")

        self.lista_relatorio_venda.column('codigo', width=60, anchor="center")
        self.lista_relatorio_venda.column('cpf', width=125, anchor="center")
        self.lista_relatorio_venda.column('valor', width=125, anchor="center")
        self.lista_relatorio_venda.column('data', width=125, anchor="center")
        self.lista_relatorio_venda.column('tipo', width=125, anchor="center")

        self.lista_relatorio_venda.place(
            relx=0.01, rely=0.02, relwidth=0.99, relheight=0.98)
        self.ldata = Label(self.aba_politica, text="Insira data:",
                           bg="#363636", fg="white", font='cambria 12')
        self.ldata.place(relx=0.65, rely=0.05)
        self.data_relatorio = Entry(self.aba_politica)
        self.data_relatorio.place(relx=0.65, rely=0.10)
        self.bt_confirmar_data = Button(
            self.aba_politica, text='Confirmar', bg="#3CB371", fg="white", command=self.busca_data)
        self.bt_confirmar_data.place(relx=0.65, rely=0.15, relwidth=0.09)

        # FIM DA TELA RELATORIOS

    # DEFINIÇÃO PARA FECHAR TELAS PARA EVITAR ERRO DE AUTENTICAÇÃO.

    def fechar_tela(self):
        self.tela_usuario.destroy()
        self.janela.destroy()
    # FIM DA TELA DE FECHAR.

    # AUTENTICAÇÃO TELA DE LOGIN.

    def login_(self):
        self.user = self.usuario.get()
        self.senh_a = self.senha.get()
        if self.user == "admin" and self.senh_a == "123":
            self.tela_usuario.destroy()
        else:
            messagebox.showerror(
                title="ERROR", message="Usuario ou senha Invalidos!")
    # FIM DA TELA DE AUTENTICAÇÃO.

    # TELA DE ENTRADA DE USUARIO.

    def tela_usuario(self):
        self.tela_usuario = Toplevel()
        self.tela_usuario.title("Login")
        self.tela_usuario.iconbitmap('C:\ImgProjeto\leao.ico')

        self.usuario = ttk.Entry(self.tela_usuario)
        self.senha = ttk.Entry(self.tela_usuario, show="*")
        self.usuario.place(relx=0.38, rely=0.35)
        self.senha.place(relx=0.38, rely=0.45)

        self.imag = PhotoImage(file="C:\ImgProjeto\impressora.png")
        self.limagem = Label(self.tela_usuario, image=self.imag, bg="#363636")
        self.limagem.place(relx=0.40, rely=0.10)

        self.lb_usuario = Label(
            self.tela_usuario, text="Usuário", bg="#363636", fg="white", font='cambria 12')
        self.lb_senha = Label(self.tela_usuario, text="Senha",
                              bg="#363636", fg="white", font='cambria 12')
        self.lb_usuario.place(relx=0.17, rely=0.33)
        self.lb_senha.place(relx=0.17, rely=0.43)

        self.lb_texto_aviso01 = Label(self.tela_usuario, text="Não tente minizar a tela antes de realizar o login!!",
                                      bg="#363636", fg="white", font='cambria 10')
        self.lb_texto_aviso01.place(relx=0.04, rely=0.85)
        self.lb_texto_aviso02 = Label(self.tela_usuario, text="Para sair do sistema use o botão sair!!",
                                      bg="#363636", fg="white", font='cambria 10')
        self.lb_texto_aviso02.place(relx=0.04, rely=0.91)

        self.bt_sair = Button(self.tela_usuario, text="Sair",
                              command=self.fechar_tela, bg="#DC143C", fg="white", font='cambria 10')
        self.bt_sair.place(relx=0.60, rely=0.60, relwidth=0.20)

        self.bt_entrar = Button(self.tela_usuario, text="Entrar",
                                command=self.login_,  bg="#3CB371", fg="white", font='cambria 10')
        self.bt_entrar.place(relx=0.35, rely=0.60, relwidth=0.20)

        self.tela_usuario.configure(bg="#363636")
        self.largura_screen = self.tela_usuario.winfo_screenwidth()
        self.altura_screen = self.tela_usuario.winfo_screenheight()
        self.largura = 300
        self.altura = 300

        self.posx = self.largura_screen/2 - self.largura/1.8
        self.posy = self.altura_screen/2 - self.altura/1.8
        self.tela_usuario.geometry(
            "%dx%d+%d+%d" % (self.largura, self.altura, self.posx, self.posy))
        self.tela_usuario.resizable("false", "false")
        self.tela_usuario.transient(self.janela)
        self.tela_usuario.focus_force()
        self.tela_usuario.grab_set()
        self.tela_usuario.protocol("WM_DELETE_WINDOW", self.janela)
    # FIM DA TELA DE ENTRADA DE USUARIO.

        style = ttk.Style(janela)
        style.theme_use('alt')


sistema()
# FIM DA CLASSE DO SISTEMA.
