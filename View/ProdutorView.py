import tkinter as tk
from tkinter import ttk

from Dao.ProdutorDao import ProdutorDao


class ProdutorView:
    # *********************************************** View Cad Produtor ***********************************************
    @staticmethod
    def cad_pro():
        # Nova Janela, filha da Principal
        telacadpro = tk.Toplevel()

        # CPF
        registro_cpf = (telacadpro.register(entrada_cpf_rg), '%S')
        pro_cpf_lb = ttk.Label(telacadpro, text='CPF:')
        pro_cpf_lb.place(x=10, y=10)
        pro_cpf_ent = ttk.Entry(telacadpro, width=25, validate='key', validatecommand=registro_cpf)
        pro_cpf_ent.place(x=40, y=10)

        # RG
        registro_rg = (telacadpro.register(entrada_cpf_rg), '%S')
        pro_rg_lb = ttk.Label(telacadpro, text='RG:')
        pro_rg_lb.place(x=200, y=10)
        pro_rg_ent = ttk.Entry(telacadpro, width=25, validate='key', validatecommand=registro_rg)
        pro_rg_ent.place(x=225, y=10)

        # NOME
        registro_nome = (telacadpro.register(entrada_letra), '%S')
        pro_nome_lb = ttk.Label(telacadpro, text='Nome:')
        pro_nome_lb.place(x=10, y=50)
        pro_nome_ent = ttk.Entry(telacadpro, width=54, validate='key', validatecommand=registro_nome)
        pro_nome_ent.place(x=50, y=50)

        # TELEFONE
        registro_fone = (telacadpro.register(entrada_fone), '%S')
        pro_fone_lb = ttk.Label(telacadpro, text='Telefone:')
        pro_fone_lb.place(x=10, y=100)
        pro_fone_ent = ttk.Entry(telacadpro, width=20, validate='key', validatecommand=registro_fone)
        pro_fone_ent.place(x=65, y=100)
        pro_fone_ent.insert(0, '92')

        # Botão Cadastrar
        pro_cad_bt = ttk.Button(telacadpro, text='Cadastrar', command=lambda: ProdutorDao.salvar_pro(pro_cpf_ent,
                                                                                                     pro_rg_ent,
                                                                                                     pro_nome_ent,
                                                                                                     pro_fone_ent,
                                                                                                     telacadpro))
        pro_cad_bt.place(x=250, y=100)

        # Configurações Janela Cadastrar Produtor
        telacadpro.title('Cadastrar Produtor')
        telacadpro.geometry('400x150')
        telacadpro.resizable(False, False)
        telacadpro.mainloop()

    # ******************************************** View Pesq Produtor ************************************************
    @staticmethod
    def pesq_pro():
        # Nova Janela, filha da Principal
        tela_pesq_pro = tk.Toplevel()

        # Pesquisar
        pro_pesq_lb = ttk.Label(tela_pesq_pro, text='Pesquisar:')
        pro_pesq_lb.place(x=10, y=10)
        pro_pesq_ent = ttk.Entry(tela_pesq_pro, width=57)
        pro_pesq_ent.place(x=70, y=10)

        # Produtor Tree
        pro_tree = ttk.Treeview(tela_pesq_pro, columns=(
            'cpf', 'rg', 'nome', 'fone'), height=10, selectmode='browse')

        # Tree Heading
        pro_tree.heading('cpf', text='CPF')
        pro_tree.heading('rg', text='RG')
        pro_tree.heading('nome', text='NOME')
        pro_tree.heading('fone', text='TELEFONE')
        pro_tree['show'] = 'headings'

        # Tree Colunas
        pro_tree.column('cpf', width=90)
        pro_tree.column('rg', width=90)
        pro_tree.column('nome', width=150)
        pro_tree.column('fone', width=90)

        # Posicionar Tree
        pro_tree.place(x=0, y=40)

        # Botão Alterar
        pro_pesq_btalt = ttk.Button(tela_pesq_pro, text='Alterar', command=lambda: alt_pro())
        pro_pesq_btalt.place(x=75, y=280)
        pro_pesq_btalt.config(state='disabled')

        # Botão Excluir
        pro_pesq_btex = ttk.Button(tela_pesq_pro, text='Excluir',
                                   command=lambda: ProdutorDao.excluir_pro(pro_tree, tela_pesq_pro, pro_pesq_btalt,
                                                                           pro_pesq_btex)
                                   )
        pro_pesq_btex.place(x=175, y=280)
        pro_pesq_btex.config(state='disabled')

        # Botão Pesquisar
        pro_pesq_btpes = ttk.Button(tela_pesq_pro, text='Pesquisar',
                                    command=lambda: ProdutorDao.pesquisar(pro_pesq_ent, pro_tree, tela_pesq_pro,
                                                                          pro_pesq_btalt, pro_pesq_btex))
        pro_pesq_btpes.place(x=275, y=280)

        # ********************************************* View Alt Produtor ********************************************
        def alt_pro():
            # Retorna a lista do item selecionado
            lista_pro = pro_tree.item(pro_tree.selection())['values']

            # Nova Janela, filha da Tela Pesquisar Produtor
            tela_alt_pro = tk.Toplevel()

            # CPF
            registro_cpf = (tela_alt_pro.register(entrada_cpf_rg), '%S')
            pro_cpf_lb = ttk.Label(tela_alt_pro, text='CPF:')
            pro_cpf_lb.place(x=10, y=10)
            pro_cpf_ent = ttk.Entry(tela_alt_pro)
            pro_cpf_ent.place(x=40, y=10)
            pro_cpf_ent.insert(0, lista_pro[0])
            pro_cpf_ent.config(validate='key', validatecommand=registro_cpf)

            # RG
            registro_rg = (tela_alt_pro.register(entrada_cpf_rg), '%S')
            pro_rg_lb = ttk.Label(tela_alt_pro, text='RG:')
            pro_rg_lb.place(x=200, y=10)
            pro_rg_ent = ttk.Entry(tela_alt_pro, width=25)
            pro_rg_ent.place(x=225, y=10)
            pro_rg_ent.insert(0, lista_pro[1])
            pro_rg_ent.config(validate='key', validatecommand=registro_rg)

            # NOME
            registro_nome = (tela_alt_pro.register(entrada_letra), '%S')
            pro_nome_lb = ttk.Label(tela_alt_pro, text='Nome:')
            pro_nome_lb.place(x=10, y=50)
            pro_nome_ent = ttk.Entry(tela_alt_pro, width=54)
            pro_nome_ent.place(x=50, y=50)
            pro_nome_ent.insert(0, lista_pro[2])
            pro_nome_ent.config(validate='key', validatecommand=registro_nome)

            # TELEFONE
            registro_fone = (tela_alt_pro.register(entrada_fone), '%S')
            pro_fone_lb = ttk.Label(tela_alt_pro, text='Telefone:')
            pro_fone_lb.place(x=10, y=100)
            pro_fone_ent = ttk.Entry(tela_alt_pro, width=20)
            pro_fone_ent.place(x=65, y=100)
            pro_fone_ent.insert(0, lista_pro[3])
            pro_fone_ent.config(validate='key', validatecommand=registro_fone)

            # Botão Alterar
            pro_cad_bt = ttk.Button(tela_alt_pro, text='Alterar', command=lambda: ProdutorDao.alterar(pro_cpf_ent,
                                                                                                      pro_rg_ent,
                                                                                                      pro_nome_ent,
                                                                                                      pro_fone_ent,
                                                                                                      pro_tree,
                                                                                                      tela_alt_pro,
                                                                                                      lista_pro,
                                                                                                      tela_pesq_pro,
                                                                                                      pro_pesq_btalt,
                                                                                                      pro_pesq_btex)
                                    )
            pro_cad_bt.place(x=250, y=100)

            # Configurações Janela Alterar Produtor
            tela_alt_pro.title('Alterar Produtor')
            tela_alt_pro.geometry('400x150')
            tela_alt_pro.resizable(False, False)
            tela_alt_pro.mainloop()

        # Configurações Janela Pesquisar Produtor
        tela_pesq_pro.title('Pesquisar Produtor')
        tela_pesq_pro.geometry('423x320')
        tela_pesq_pro.resizable(False, False)
        tela_pesq_pro.mainloop()


# Entrada CPF
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
