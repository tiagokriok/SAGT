import tkinter as tk
from tkinter import ttk

from Dao.AgenciadoDao import AgenciadoDao
from Dao.Bairro import Bairro
from Dao.ProdutorDao import ProdutorDao
from View.ContrataView import ContrataView


class AgenciadoView:
    @staticmethod
    def cad_age():
        # Nova Janela, filha da Principal
        tela_cad_age = tk.Toplevel()

        # CPF
        registro_cpf = (tela_cad_age.register(entrada_cpf), '%S')
        age_cpf_lb = ttk.Label(tela_cad_age, text='CPF:')
        age_cpf_lb.place(x=10, y=10)
        age_cpf_ent = ttk.Entry(tela_cad_age, width=25, validate='key', validatecommand=registro_cpf)
        age_cpf_ent.place(x=40, y=10)

        # NOME
        registro_nome = (tela_cad_age.register(entrada_letra), '%S')
        age_nome_lb = ttk.Label(tela_cad_age, text='Nome:')
        age_nome_lb.place(x=10, y=50)
        age_nome_ent = ttk.Entry(tela_cad_age, width=54, validate='key', validatecommand=registro_nome)
        age_nome_ent.place(x=50, y=50)

        # IDADE
        registro_ida = (tela_cad_age.register(entrada_idade), '%S')
        age_ida_lb = ttk.Label(tela_cad_age, text='Idade:')
        age_ida_lb.place(x=10, y=100)
        age_ida_ent = ttk.Entry(tela_cad_age, width=5, validate='key', validatecommand=registro_ida)
        age_ida_ent.place(x=45, y=100)

        # SEXO
        age_sex_lb = ttk.Label(tela_cad_age, text='Sexo:')
        age_sex_lb.place(x=100, y=100)
        age_sex_cb = ttk.Combobox(tela_cad_age, width=2, state='readonly')
        age_sex_cb.place(x=130, y=100)
        age_sex_cb['values'] = ['M', 'F']

        # TALENTO
        registro_tal = (tela_cad_age.register(entrada_letra), '%S')
        age_tal_lb = ttk.Label(tela_cad_age, text='Talento:')
        age_tal_lb.place(x=200, y=100)
        age_tal_ent = ttk.Entry(tela_cad_age, width=21, validate='key', validatecommand=registro_tal)
        age_tal_ent.place(x=249, y=100)

        # TELEFONE
        registro_fone = (tela_cad_age.register(entrada_fone), '%S')
        age_fone_lb = ttk.Label(tela_cad_age, text='Telefone:')
        age_fone_lb.place(x=200, y=10)
        age_fone_ent = ttk.Entry(tela_cad_age, width=20, validate='key', validatecommand=registro_fone)
        age_fone_ent.place(x=255, y=10)
        age_fone_ent.insert(0, '92')

        # VALOR
        registro_val = (tela_cad_age.register(entrada_valor), '%S')
        age_val_lb = ttk.Label(tela_cad_age, text='Valor: R$')
        age_val_lb.place(x=10, y=150)
        age_val_ent = ttk.Entry(tela_cad_age, width=10, validate='key', validatecommand=registro_val)
        age_val_ent.place(x=60, y=150)
        age_val_ent.insert(0, '0.00')

        # BAIRRO
        age_bai_lb = ttk.Label(tela_cad_age, text='Bairro:')
        age_bai_lb.place(x=150, y=150)
        age_bai_cb = ttk.Combobox(tela_cad_age, state='readonly')
        age_bai_cb.place(x=190, y=150)
        age_bai_cb['values'] = Bairro.cbox_bai()

        # PRODUTOR
        age_pro_lb = ttk.Label(tela_cad_age, text='Produtor:')
        age_pro_lb.place(x=10, y=200)
        age_pro_cb = ttk.Combobox(tela_cad_age, state='readonly')
        age_pro_cb.place(x=65, y=200)
        age_pro_cb['values'] = ProdutorDao.cbox_pro()

        # Botão Cadastrar
        age_cad_bt = ttk.Button(tela_cad_age, text='Cadastrar',
                                command=lambda: AgenciadoDao.salvar_age(age_cpf_ent, age_nome_ent, age_ida_ent,
                                                                        age_sex_cb, age_tal_ent, age_fone_ent,
                                                                        age_val_ent, age_bai_cb, age_pro_cb,
                                                                        tela_cad_age))
        age_cad_bt.place(x=250, y=200)

        # Configurações Janela Cadastrar Agenciado
        tela_cad_age.geometry('400x250')
        tela_cad_age.title('Cadastrar Agenciado')
        tela_cad_age.resizable(False, False)
        tela_cad_age.mainloop()

    @staticmethod
    def pesq_age():
        # Nova Janela, filha da Principal
        tela_pesq_age = tk.Toplevel()

        # Pesquisar
        age_pesq_lb = ttk.Label(tela_pesq_age, text='Pesquisar:')
        age_pesq_lb.place(x=10, y=10)
        age_pesq_ent = ttk.Entry(tela_pesq_age, width=140)
        age_pesq_ent.place(x=70, y=10)

        # Agenciado Tree
        age_tree = ttk.Treeview(tela_pesq_age,
                                columns=('cpf', 'nome', 'idade', 'sexo', 'talento', 'fone', 'valor', 'bairro',
                                         'produtor'), height=10, selectmode='browse')

        # Tree Heading
        age_tree.heading('cpf', text='CPF')
        age_tree.heading('nome', text='NOME')
        age_tree.heading('idade', text='IDADE')
        age_tree.heading('sexo', text='SEXO')
        age_tree.heading('talento', text='TALENTO')
        age_tree.heading('fone', text='TELEFONE')
        age_tree.heading('valor', text='VALOR')
        age_tree.heading('bairro', text='BAIRRO')
        age_tree.heading('produtor', text='PRODUTOR')
        age_tree['show'] = 'headings'

        # Tree Colunas
        age_tree.column('cpf', width=90)
        age_tree.column('nome', width=150)
        age_tree.column('idade', width=90)
        age_tree.column('sexo', width=90)
        age_tree.column('talento', width=90)
        age_tree.column('fone', width=90)
        age_tree.column('valor', width=90)
        age_tree.column('bairro', width=120)
        age_tree.column('produtor', width=150)

        # Posicionar Tree
        age_tree.place(x=0, y=40)

        # Botão Alterar
        age_pesq_btalt = ttk.Button(tela_pesq_age, text='Alterar', command=lambda: alt_age())
        age_pesq_btalt.place(x=275, y=280)
        age_pesq_btalt.config(state='disabled')

        # Botão Excluir
        age_pesq_btex = ttk.Button(tela_pesq_age, text='Excluir',
                                   command=lambda: AgenciadoDao.excluir_age(age_tree, tela_pesq_age, age_pesq_btalt,
                                                                            age_pesq_btex, age_pesq_btcon))
        age_pesq_btex.place(x=375, y=280)
        age_pesq_btex.config(state='disabled')

        # Botão Contratar
        age_pesq_btcon = ttk.Button(tela_pesq_age, text='Contratar',
                                    command=lambda: ContrataView.tela_contratar(age_tree, tela_pesq_age))
        age_pesq_btcon.place(x=475, y=280)
        age_pesq_btcon.config(state='disabled')

        # Botão Pesquisar
        age_pesq_btpes = ttk.Button(tela_pesq_age, text='Pesquisar',
                                    command=lambda: AgenciadoDao.pesquisar(age_pesq_ent, age_tree, tela_pesq_age,
                                                                           age_pesq_btalt, age_pesq_btex,
                                                                           age_pesq_btcon))
        age_pesq_btpes.place(x=575, y=280)

        def alt_age():
            # Retorna a lista do item selecionado
            lista_age = age_tree.item(age_tree.selection())['values']

            # Nova Janela, filha da Tela Pesquisa Agenciado
            tela_alt_age = tk.Toplevel(tela_pesq_age)

            # CPF
            registro_cpf = (tela_alt_age.register(entrada_cpf), '%S')
            age_cpf_lb = ttk.Label(tela_alt_age, text='CPF:')
            age_cpf_lb.place(x=10, y=10)
            age_cpf_ent = ttk.Entry(tela_alt_age, width=25)
            age_cpf_ent.place(x=40, y=10)
            age_cpf_ent.insert(0, lista_age[0])
            age_cpf_ent.config(validate='key', validatecommand=registro_cpf)

            # NOME
            registro_nome = (tela_alt_age.register(entrada_letra), '%S')
            age_nome_lb = ttk.Label(tela_alt_age, text='Nome:')
            age_nome_lb.place(x=10, y=50)
            age_nome_ent = ttk.Entry(tela_alt_age, width=54)
            age_nome_ent.place(x=50, y=50)
            age_nome_ent.insert(0, lista_age[1])
            age_nome_ent.config(validate='key', validatecommand=registro_nome)

            # IDADE
            registro_ida = (tela_alt_age.register(entrada_idade), '%S')
            age_ida_lb = ttk.Label(tela_alt_age, text='Idade:')
            age_ida_lb.place(x=10, y=100)
            age_ida_ent = ttk.Entry(tela_alt_age, width=5)
            age_ida_ent.place(x=45, y=100)
            age_ida_ent.insert(0, lista_age[2])
            age_ida_ent.config(validate='key', validatecommand=registro_ida)

            # SEXO
            age_sex_lb = ttk.Label(tela_alt_age, text='Sexo:')
            age_sex_lb.place(x=100, y=100)
            age_sex_cb = ttk.Combobox(tela_alt_age, width=2, state='readonly')
            age_sex_cb.place(x=130, y=100)
            age_sex_cb['values'] = ['M', 'F']
            age_sex_cb.insert(0, lista_age[3])

            # TALENTO
            registro_tal = (tela_alt_age.register(entrada_letra), '%S')
            age_tal_lb = ttk.Label(tela_alt_age, text='Talento:')
            age_tal_lb.place(x=200, y=100)
            age_tal_ent = ttk.Entry(tela_alt_age, width=21)
            age_tal_ent.place(x=249, y=100)
            age_tal_ent.insert(0, lista_age[4])
            age_tal_ent.config(validate='key', validatecommand=registro_tal)

            # TELEFONE
            registro_fone = (tela_alt_age.register(entrada_fone), '%S')
            age_fone_lb = ttk.Label(tela_alt_age, text='Telefone:')
            age_fone_lb.place(x=200, y=10)
            age_fone_ent = ttk.Entry(tela_alt_age, width=20)
            age_fone_ent.place(x=255, y=10)
            age_fone_ent.insert(0, lista_age[5])
            age_fone_ent.config(validate='key', validatecommand=registro_fone)

            # VALOR
            registro_val = (tela_alt_age.register(entrada_valor), '%S')
            age_val_lb = ttk.Label(tela_alt_age, text='Valor: R$')
            age_val_lb.place(x=10, y=150)
            age_val_ent = ttk.Entry(tela_alt_age, width=10)
            age_val_ent.place(x=60, y=150)
            age_val_ent.insert(0, lista_age[6])
            age_val_ent.config(validate='key', validatecommand=registro_val)

            # BAIRRO
            age_bai_lb = ttk.Label(tela_alt_age, text='Bairro:')
            age_bai_lb.place(x=150, y=150)
            age_bai_cb = ttk.Combobox(tela_alt_age, state='readonly')
            age_bai_cb.place(x=190, y=150)
            age_bai_cb['values'] = Bairro.cbox_bai()

            # PRODUTOR
            age_pro_lb = ttk.Label(tela_alt_age, text='Produtor:')
            age_pro_lb.place(x=10, y=200)
            age_pro_cb = ttk.Combobox(tela_alt_age, state='readonly')
            age_pro_cb.place(x=65, y=200)
            age_pro_cb['values'] = ProdutorDao.cbox_pro()

            # Botão Alterar
            age_cad_bt = ttk.Button(tela_alt_age, text='Alterar',
                                    command=lambda: AgenciadoDao.alterar(age_cpf_ent, age_nome_ent, age_ida_ent,
                                                                         age_sex_cb, age_tal_ent, age_fone_ent,
                                                                         age_val_ent, age_bai_cb, age_pro_cb, age_tree,
                                                                         tela_alt_age, lista_age, tela_pesq_age,
                                                                         age_pesq_btalt, age_pesq_btex, age_pesq_btcon))
            age_cad_bt.place(x=250, y=200)

            # Configurações Janela Alterar Agenciado
            tela_alt_age.geometry('400x250')
            tela_alt_age.title('Alterar Agenciado')
            tela_alt_age.resizable(False, False)
            tela_alt_age.mainloop()

        # Configurações Janela Pesquisar Agenciado
        tela_pesq_age.geometry('963x320')
        tela_pesq_age.title('Pesquisar Agenciado')
        tela_pesq_age.resizable(False, False)
        tela_pesq_age.mainloop()


# Entrada CPF
def entrada_cpf(tecla):
    digitos_val = '0123456789.-'
    return tecla in digitos_val


# Entrada Letra
def entrada_letra(tecla):
    digitos_val = 'abcdefghijlmnopqrstuvxzkwy ABCDEFGHIJLMNOPQRSTUVXZWYK'
    return tecla in digitos_val


# Entrada Idade
def entrada_idade(tecla):
    digitos_val = '1234567890'
    return tecla in digitos_val


# Entrada Telefone
def entrada_fone(tecla):
    digitos_val = '0123456789-'
    return tecla in digitos_val


# Entrada Valor
def entrada_valor(tecla):
    digitos_val = '0123456789.'
    return tecla in digitos_val
