from Dao.ContrataDao import ContrataDao
from Dao.ClienteDao import ClienteDao
import tkinter as tk
from tkinter import ttk


class ContrataView:
    # ************************************ View Con Agenciado *****************************************************
    @staticmethod
    def tela_contratar(age_tree, tela_pesq_age):
        # Retorna lista do item selecionado
        lista_age = age_tree.item(age_tree.selection())['values']

        # Nova janela, filha da tela_pesq_age
        tela_con = tk.Toplevel()

        # CPF Agenciado
        age_cpf_lb = ttk.Label(tela_con, text='CPF:')
        age_cpf_lb.place(x=10, y=10)
        age_cpf_ent = ttk.Entry(tela_con, width=25)
        age_cpf_ent.place(x=40, y=10)
        age_cpf_ent.insert(0, lista_age[0])
        age_cpf_ent.config(state='disabled')

        # NOME Agenciado
        age_nome_lb = ttk.Label(tela_con, text='Nome:')
        age_nome_lb.place(x=10, y=50)
        age_nome_ent = ttk.Entry(tela_con, width=54)
        age_nome_ent.place(x=50, y=50)
        age_nome_ent.insert(0, lista_age[1])
        age_nome_ent.config(state='disabled')

        # IDADE Agenciado
        age_ida_lb = ttk.Label(tela_con, text='Idade:')
        age_ida_lb.place(x=10, y=100)
        age_ida_ent = ttk.Entry(tela_con, width=3)
        age_ida_ent.place(x=45, y=100)
        age_ida_ent.insert(0, lista_age[2])
        age_ida_ent.config(state='disabled')

        # TALENTO Agenciado
        age_tal_lb = ttk.Label(tela_con, text='Talento:')
        age_tal_lb.place(x=100, y=100)
        age_tal_ent = ttk.Entry(tela_con, width=21)
        age_tal_ent.place(x=149, y=100)
        age_tal_ent.insert(0, lista_age[4])
        age_tal_ent.config(state='disabled')

        # TELEFONE Agenciado
        age_fone_lb = ttk.Label(tela_con, text='Telefone:')
        age_fone_lb.place(x=200, y=10)
        age_fone_ent = ttk.Entry(tela_con, width=20)
        age_fone_ent.place(x=255, y=10)
        age_fone_ent.insert(0, lista_age[5])
        age_fone_ent.config(state='disabled')

        # VALOR Agenciado
        age_val_lb = ttk.Label(tela_con, text='Valor: R$')
        age_val_lb.place(x=10, y=150)
        age_val_ent = ttk.Entry(tela_con, width=10)
        age_val_ent.place(x=60, y=150)
        age_val_ent.insert(0, lista_age[6])
        age_val_ent.config(state='disabled')

        # CPF Cliente
        registro_cpf = (tela_con.register(entrada_cpf), '%S')
        cli_cpf_lb = ttk.Label(tela_con, text='CPF Cliente:')
        cli_cpf_lb.place(x=150, y=150)
        cli_cpf_ent = ttk.Entry(tela_con, width=25, validate='key', validatecommand=registro_cpf)
        cli_cpf_ent.place(x=220, y=150)

        # NOME Cliente
        cli_nome_lb = ttk.Label(tela_con, text='Nome Cliente:')
        cli_nome_lb.place(x=10, y=200)
        cli_nome_ent = ttk.Entry(tela_con, width=48)
        cli_nome_ent.place(x=90, y=200)
        cli_nome_ent.config(state='disabled')

        # Data de Início
        registro_dt = (tela_con.register(entrada_data), '%S')
        dt_ini_lb = ttk.Label(tela_con, text='Data de Início(aaaa-mm-dd):')
        dt_ini_lb.place(x=10, y=250)
        dt_ini_ent = ttk.Entry(tela_con, width=10, validate='key', validatecommand=registro_dt)
        dt_ini_ent.place(x=170, y=250)

        # Data Final
        dt_fin_lb = ttk.Label(tela_con, text='Data Final(aaaa-mm-dd):')
        dt_fin_lb.place(x=10, y=300)
        dt_fin_ent = ttk.Entry(tela_con, width=10, validate='key', validatecommand=registro_dt)
        dt_fin_ent.place(x=150, y=300)

        # Hora de Início
        registro_hr = (tela_con.register(entrada_hora), '%S')
        hr_ini_lb = ttk.Label(tela_con, text='Hora de Início(HH:mm):')
        hr_ini_lb.place(x=10, y=350)
        hr_ini_ent = ttk.Entry(tela_con, width=5, validate='key', validatecommand=registro_hr)
        hr_ini_ent.place(x=145, y=350)

        # Hora Final
        hr_fin_lb = ttk.Label(tela_con, text='Hora Final(HH:mm):')
        hr_fin_lb.place(x=190, y=350)
        hr_fin_ent = ttk.Entry(tela_con, width=5, validate='key', validatecommand=registro_hr)
        hr_fin_ent.place(x=305, y=350)

        # Hora Total por dia
        # hrtot_lb = ttk.Label(tela_con, text='Hora Total por dia:')
        # hrtot_lb.place(x=10, y=400)
        # hrtot_ent = ttk.Entry(tela_con, width=4)
        # hrtot_ent.place(x=115, y=400)

        # Descrição
        desc_lb = ttk.Label(tela_con, text='Descrição:')
        desc_lb.place(x=10, y=400)
        desc_ent = tk.Text(tela_con, width=45, height=5)
        desc_ent.place(x=10, y=420)

        # Botão Buscar Cliente
        cli_bus_bt = ttk.Button(tela_con, text='Buscar Cliente',
                                command=lambda: ClienteDao.buscar_cli(cli_cpf_ent, cli_nome_ent, tela_con, age_con_bt))
        cli_bus_bt.place(x=200, y=550)

        # Botão Gerar Contrato
        age_con_bt = ttk.Button(tela_con, text='Gerar Contrato',
                                command=lambda: ContrataDao.gerar_contrato(age_cpf_ent, age_nome_ent, age_val_ent,
                                                                           cli_cpf_ent, cli_nome_ent, dt_ini_ent,
                                                                           dt_fin_ent, hr_ini_ent, hr_fin_ent,
                                                                           desc_ent, tela_con, tela_pesq_age))
        age_con_bt.place(x=100, y=550)
        age_con_bt.config(state='disabled')

        # Configurações da Janela Contratar
        tela_con.geometry('400x600')
        tela_con.title('Contratar Agenciado')
        tela_con.resizable(False, False)
        tela_con.mainloop()


# Entrada CPF
def entrada_cpf(tecla):
    digitos_val = '0123456789.-'
    return tecla in digitos_val


# Entrada Letra
def entrada_letra(tecla):
    digitos_val = 'abcdefghijlmnopqrstuvxzkwy ABCDEFGHIJLMNOPQRSTUVXZWYK'
    return tecla in digitos_val


# Entrada Data
def entrada_data(tecla):
    digitos_val = '0123456789-'
    return tecla in digitos_val


# Entrada Hora
def entrada_hora(tecla):
    digitos_val = '0123456789:'
    return tecla in digitos_val
