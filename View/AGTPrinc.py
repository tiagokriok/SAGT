from Dao.ContrataDao import ContrataDao
import tkinter as tk
from tkinter import ttk
from View.AgenciadoView import AgenciadoView
from View.ClienteView import ClienteView
from View.ProdutorView import ProdutorView

TelaPrinc = tk.Tk()


class Agencia:
    # ********************************************** View Principal***************************************************
    def __init__(self, telaprinc):
        # Cria Tela Principal
        self.TelaPrinc = telaprinc

        # Menu
        menu = tk.Menu(self.TelaPrinc)
        self.TelaPrinc.config(menu=menu)

        # Menu Cliente
        cliente = tk.Menu(menu)
        cliente.add_command(label='Cadastrar', command=ClienteView.cad_cli)
        cliente.add_command(label='Pesquisar', command=ClienteView.pesq_cli)
        menu.add_cascade(label='Cliente', menu=cliente)

        # Menu Agenciado
        agenciado = tk.Menu(menu)
        agenciado.add_command(label='Cadastrar', command=AgenciadoView.cad_age)
        agenciado.add_command(label='Pesquisar', command=AgenciadoView.pesq_age)
        menu.add_cascade(label='Agenciado', menu=agenciado)

        # Menu Produtor
        produtor = tk.Menu(menu)
        produtor.add_command(label='Cadastrar', command=ProdutorView.cad_pro)
        produtor.add_command(label='Pesquisar', command=ProdutorView.pesq_pro)
        menu.add_cascade(label='Produtor', menu=produtor)

        # Menu Agenda
        agenda = tk.Menu(menu)
        agenda.add_command(label='Agenda', command=self.agendaview)
        agenda.add_command(label='Listar Contratos', command=self.listview)
        menu.add_cascade(label='Agenda', menu=agenda)

        # Configurações da Janela Principal
        self.TelaPrinc.title('AGT')
        self.TelaPrinc.geometry('800x600')
        self.TelaPrinc.mainloop()

# ****************************************** Tela Agenda *******************************************************
    @staticmethod
    def agendaview():
        # Nova janela, filha da Principal
        view_agenda = tk.Toplevel()

        # Pesquisar
        agenda_pesq_lb = ttk.Label(view_agenda, text='Pesquisar:')
        agenda_pesq_lb.place(x=10, y=10)
        agenda_pesq_ent = ttk.Entry(view_agenda, width=57)
        agenda_pesq_ent.place(x=70, y=10)

        # Agenda Tree
        agenda_tree = ttk.Treeview(view_agenda, columns=('dt_ini', 'dt_fin', 'hora_tot', 'valor', 'nome_age'),
                                   selectmode='browse')

        # Tree Heading
        agenda_tree.heading('dt_ini', text='DATA INICIAL')
        agenda_tree.heading('dt_fin', text='DATA FINAL')
        agenda_tree.heading('hora_tot', text='HORA TOTAL')
        agenda_tree.heading('valor', text='VALOR')
        agenda_tree.heading('nome_age', text='NOME')
        agenda_tree['show'] = 'headings'

        # Tree Colunas
        agenda_tree.column('dt_ini', width=90)
        agenda_tree.column('dt_fin', width=90)
        agenda_tree.column('hora_tot', width=90)
        agenda_tree.column('valor', width=90)
        agenda_tree.column('nome_age', width=150)

        # Posicionar Tree
        agenda_tree.place(x=0, y=40)

        # Botão Ver Agenda
        busc_bt = ttk.Button(view_agenda, text='Ver Agenda',
                             command=lambda: ContrataDao.buscar_agenda(agenda_pesq_ent, agenda_tree))
        busc_bt.place(x=215, y=275)

        # Configurações Janela
        view_agenda.title('AGT - Agenda')
        view_agenda.geometry('513x313')
        view_agenda.resizable(False, False)
        view_agenda.mainloop()

# ****************************************** Tela Relatório *****************************************************
    @staticmethod
    def listview():
        # Nova janela, filha da Principal
        view_list = tk.Toplevel()

        # Pesquisar
        list_pesq_lb = ttk.Label(view_list, text='Pesquisar:')
        list_pesq_lb.place(x=10, y=10)
        list_pesq_ent = ttk.Entry(view_list, width=57)
        list_pesq_ent.place(x=70, y=10)

        # Agenda Tree
        list_tree = ttk.Treeview(view_list, columns=('dt_ini', 'dt_fin', 'hora_tot', 'valor', 'nome_age'),
                                 selectmode='browse')

        # Tree Heading
        list_tree.heading('dt_ini', text='DATA INICIAL')
        list_tree.heading('dt_fin', text='DATA FINAL')
        list_tree.heading('hora_tot', text='HORA TOTAL')
        list_tree.heading('valor', text='VALOR')
        list_tree.heading('nome_age', text='NOME')
        list_tree['show'] = 'headings'

        # Tree Colunas
        list_tree.column('dt_ini', width=90)
        list_tree.column('dt_fin', width=90)
        list_tree.column('hora_tot', width=90)
        list_tree.column('valor', width=90)
        list_tree.column('nome_age', width=150)

        # Posicionar Tree
        list_tree.place(x=0, y=40)

        # Botão Lista Contratos
        busc_bt = ttk.Button(view_list, text='Listar Contratos',
                             command=lambda: ContrataDao.lista_contratos(list_pesq_ent, list_tree))
        busc_bt.place(x=215, y=275)

        # Configurações Janela
        view_list.title('AGT - Listar Contratos')
        view_list.geometry('513x313')
        view_list.resizable(False, False)
        view_list.mainloop()


if __name__ == '__main__':
    main = Agencia
    main(TelaPrinc)
