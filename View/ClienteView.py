import tkinter as tk
from tkinter import ttk

from Dao.Bairro import Bairro
from Dao.ClienteDao import ClienteDao


class ClienteView:
    # ******************************************** View Cad Cliente *************************************************
    @staticmethod
    def cad_cli():
        # Nova Janela, filha da Principal
        tela_cad_cli = tk.Toplevel()

        # CPF
        registro_cpf = (tela_cad_cli.register(entrada_cpf_rg), '%S')
        cli_cpf_lb = ttk.Label(tela_cad_cli, text='CPF:')
        cli_cpf_lb.place(x=10, y=10)
        cli_cpf_ent = ttk.Entry(tela_cad_cli, width=25, validate='key', validatecommand=registro_cpf)
        cli_cpf_ent.place(x=40, y=10)

        # RG
        registro_rg = (tela_cad_cli.register(entrada_cpf_rg), '%S')
        cli_rg_lb = ttk.Label(tela_cad_cli, text='RG:')
        cli_rg_lb.place(x=200, y=10)
        cli_rg_ent = ttk.Entry(tela_cad_cli, width=25, validate='key', validatecommand=registro_rg)
        cli_rg_ent.place(x=225, y=10)

        # NOME
        registro_nome = (tela_cad_cli.register(entrada_letra), '%S')
        cli_nome_lb = ttk.Label(tela_cad_cli, text='Nome:')
        cli_nome_lb.place(x=10, y=50)
        cli_nome_ent = ttk.Entry(tela_cad_cli, width=54, validate='key', validatecommand=registro_nome)
        cli_nome_ent.place(x=50, y=50)

        # RAMO
        registro_ramo = (tela_cad_cli.register(entrada_letra), '%S')
        cli_ramo_lb = ttk.Label(tela_cad_cli, text='Ramo:')
        cli_ramo_lb.place(x=10, y=100)
        cli_ramo_ent = ttk.Entry(tela_cad_cli, width=25, validate='key', validatecommand=registro_ramo)
        cli_ramo_ent.place(x=50, y=100)

        # Telefone
        registro_fone = (tela_cad_cli.register(entrada_fone), '%S')
        cli_fone_lb = ttk.Label(tela_cad_cli, text='Telefone:')
        cli_fone_lb.place(x=10, y=150)
        cli_fone_ent = ttk.Entry(tela_cad_cli, width=20, validate='key', validatecommand=registro_fone)
        cli_fone_ent.place(x=65, y=150)
        cli_fone_ent.insert(0, '92')

        # BAIRRO
        cli_bai_lb = ttk.Label(tela_cad_cli, text='Bairro:')
        cli_bai_lb.place(x=200, y=150)
        cli_bai_cb = ttk.Combobox(tela_cad_cli, state='readonly')
        cli_bai_cb.place(x=240, y=150)
        cli_bai_cb['values'] = Bairro.cbox_bai()

        # Botão Cadastrar
        cli_cad_bt = ttk.Button(tela_cad_cli, text='Cadastrar', command=lambda: ClienteDao.salvar_cli(cli_cpf_ent,
                                                                                                      cli_rg_ent,
                                                                                                      cli_nome_ent,
                                                                                                      cli_ramo_ent,
                                                                                                      cli_fone_ent,
                                                                                                      cli_bai_cb,
                                                                                                      tela_cad_cli))
        cli_cad_bt.place(x=300, y=200)

        # Configurações Janela Cadastrar Cliente
        tela_cad_cli.geometry('400x250')
        tela_cad_cli.title('Cadastrar Cliente')
        tela_cad_cli.resizable(False, False)
        tela_cad_cli.mainloop()

    # **************************************** View Pesq Cliente ************************************************
    @staticmethod
    def pesq_cli():
        # Nova janela, filha da Principal
        tela_pesq_cli = tk.Toplevel()

        # Pesquisar
        cli_pesq_lb = ttk.Label(tela_pesq_cli, text='Pesquisar:')
        cli_pesq_lb.place(x=10, y=10)
        cli_pesq_ent = ttk.Entry(tela_pesq_cli, width=90)
        cli_pesq_ent.place(x=70, y=10)

        # Cliente Tree
        cli_tree = ttk.Treeview(tela_pesq_cli, columns=('cpf', 'rg', 'nome', 'ramo', 'fone', 'bairro'), height=10,
                                selectmode='browse')

        # Tree Heading
        cli_tree.heading('cpf', text='CPF')
        cli_tree.heading('rg', text='RG')
        cli_tree.heading('nome', text='NOME')
        cli_tree.heading('ramo', text='RAMO')
        cli_tree.heading('fone', text='TELEFONE')
        cli_tree.heading('bairro', text='BAIRRO')
        cli_tree['show'] = 'headings'

        # Tree Colunas
        cli_tree.column('cpf', width=90)
        cli_tree.column('rg', width=90)
        cli_tree.column('nome', width=150)
        cli_tree.column('ramo', width=90)
        cli_tree.column('fone', width=90)
        cli_tree.column('bairro', width=120)

        # Posicionar Tree
        cli_tree.place(x=0, y=40)

        # Botão Alterar
        cli_pesq_btalt = ttk.Button(tela_pesq_cli, text='Alterar', command=lambda: alt_cli())
        cli_pesq_btalt.place(x=175, y=280)
        cli_pesq_btalt.config(state='disabled')

        # Botão Excluir
        cli_pesq_btex = ttk.Button(tela_pesq_cli, text='Excluir',
                                   command=lambda: ClienteDao.excluir_cli(cli_tree, tela_pesq_cli, cli_pesq_btalt,
                                                                          cli_pesq_btex))
        cli_pesq_btex.place(x=275, y=280)
        cli_pesq_btex.config(state='disabled')

        # Botão Pesquisar
        cli_pesq_btpes = ttk.Button(tela_pesq_cli, text='Pesquisar',
                                    command=lambda: ClienteDao.pesquisar(cli_pesq_ent, cli_tree, tela_pesq_cli,
                                                                         cli_pesq_btalt, cli_pesq_btex))
        cli_pesq_btpes.place(x=375, y=280)

        # ******************************************* View Alt Cliente ********************************************
        def alt_cli():
            # Retorna a lista do item selecionado
            lista_cli = cli_tree.item(cli_tree.selection())['values']

            # Nova Janela, filha da Tela Pesquisa Cliente
            tela_alt_cli = tk.Toplevel()

            # CPF
            registro_cpf = (tela_alt_cli.register(entrada_cpf_rg), '%S')
            cli_cpf_lb = ttk.Label(tela_alt_cli, text='CPF:')
            cli_cpf_lb.place(x=10, y=10)
            cli_cpf_ent = ttk.Entry(tela_alt_cli, width=25)
            cli_cpf_ent.place(x=40, y=10)
            cli_cpf_ent.insert(0, lista_cli[0])
            cli_cpf_ent.config(validate='key', validatecommand=registro_cpf)

            # RG
            registro_rg = (tela_alt_cli.register(entrada_cpf_rg), '%S')
            cli_rg_lb = ttk.Label(tela_alt_cli, text='RG:')
            cli_rg_lb.place(x=200, y=10)
            cli_rg_ent = ttk.Entry(tela_alt_cli, width=25)
            cli_rg_ent.place(x=225, y=10)
            cli_rg_ent.insert(0, lista_cli[1])
            cli_rg_ent.config(validate='key', validatecommand=registro_rg)

            # NOME
            registro_nome = (tela_alt_cli.register(entrada_letra), '%S')
            cli_nome_lb = ttk.Label(tela_alt_cli, text='Nome:')
            cli_nome_lb.place(x=10, y=50)
            cli_nome_ent = ttk.Entry(tela_alt_cli, width=54)
            cli_nome_ent.place(x=50, y=50)
            cli_nome_ent.insert(0, lista_cli[2])
            cli_nome_ent.config(validate='key', validatecommand=registro_nome)

            # RAMO
            registro_ramo = (tela_alt_cli.register(entrada_letra), '%S')
            cli_ramo_lb = ttk.Label(tela_alt_cli, text='Ramo:')
            cli_ramo_lb.place(x=10, y=100)
            cli_ramo_ent = ttk.Entry(tela_alt_cli, width=25)
            cli_ramo_ent.place(x=50, y=100)
            cli_ramo_ent.insert(0, lista_cli[3])
            cli_ramo_ent.config(validate='key', validatecommand=registro_ramo)

            # Telefone
            registro_fone = (tela_alt_cli.register(entrada_fone), '%S')
            cli_fone_lb = ttk.Label(tela_alt_cli, text='Telefone:')
            cli_fone_lb.place(x=10, y=150)
            cli_fone_ent = ttk.Entry(tela_alt_cli, width=20)
            cli_fone_ent.place(x=65, y=150)
            cli_fone_ent.insert(0, lista_cli[4])
            cli_fone_ent.config(validate='key', validatecommand=registro_fone)

            # BAIRRO
            cli_bai_lb = ttk.Label(tela_alt_cli, text='Bairro:')
            cli_bai_lb.place(x=200, y=150)
            cli_bai_cb = ttk.Combobox(tela_alt_cli, state='readonly')
            cli_bai_cb.place(x=240, y=150)
            cli_bai_cb['values'] = Bairro.cbox_bai()

            # Botão Alterar
            cli_cad_bt = ttk.Button(tela_alt_cli, text='Alterar',
                                    command=lambda: ClienteDao.alterar(cli_cpf_ent, cli_rg_ent, cli_nome_ent,
                                                                       cli_ramo_ent, cli_fone_ent, cli_bai_cb, cli_tree,
                                                                       tela_alt_cli, lista_cli, tela_pesq_cli,
                                                                       cli_pesq_btalt, cli_pesq_btex))
            cli_cad_bt.place(x=300, y=200)

            # Configurações Janela Alterar Cliente
            tela_alt_cli.geometry('400x250')
            tela_alt_cli.title('Alterar Cliente')
            tela_alt_cli.mainloop()

        # Configurações Janela Pesquisar Cliente
        tela_pesq_cli.title('Pesquisar Cliente')
        tela_pesq_cli.geometry('630x320')
        tela_pesq_cli.resizable(False, False)
        tela_pesq_cli.mainloop()


# Entrada CPF e RG
def entrada_cpf_rg(tecla):
    digitos_val = '0123456789.-'
    return tecla in digitos_val


# Entrada Letra
def entrada_letra(tecla):
    digitos_val = 'abcdefghijlmnopqrstuvxzkwy ABCDEFGHIJLMNOPQRSTUVXZWYK'
    return tecla in digitos_val


# Entrada Telefone
def entrada_fone(tecla):
    digitos_val = '0123456789-'
    return tecla in digitos_val
