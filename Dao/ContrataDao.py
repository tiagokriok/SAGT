from time import strftime
from tkinter import messagebox, END

from Connection.Conexao import Conexao
from Controller.Controle import Controle
from Dao.ClienteDao import ClienteDao


class ContrataDao:

    @staticmethod
    def gerar_contrato(age_cpf, age_nome, age_val, cli_cpf, cli_nome, dt_ini, dt_fin, hr_ini, hr_fin, desc, tela_con,
                       tela_pesq_age):
        age_val = float(age_val.get().strip())
        data_ini = dt_ini.get().strip()
        data_fin = dt_fin.get().strip()
        hora_ini = hr_ini.get().strip()
        hora_fin = hr_fin.get().strip()
        hora_total = Controle.calc_hora(hora_ini, hora_fin)
        desc = desc.get(1.0, END).strip()
        cli_rg = ClienteDao.buscar_rg(cli_cpf)

        diferenca_dt = Controle.difer_data(data_ini, data_fin)

        valor_total = Controle.calc_contrato(diferenca_dt, hora_total, age_val)

        try:
            if messagebox.askyesno('AGT - Contrato', 'Valor Total: R$ {:.2f} Deseja Contratar?'.format(valor_total)):
                Conexao.c.execute("INSERT INTO contrata(condataini, condatafin, conhoraini, conhorafin, conhoratotal, "
                                  "convalortotal, condescricao, conclicpf, conagecpf) VALUES "
                                  "('%s', '%s', '%s', '%s', '%.2f', '%.2f', '%s', '%s', '%s')"
                                  % (data_ini, data_fin, hora_ini, hora_fin, hora_total, float(valor_total), desc,
                                     cli_cpf.get(), age_cpf.get()))

                Conexao.conn.commit()
                Controle.gerar_pdf(cli_nome, cli_cpf, cli_rg, age_nome, age_cpf, desc, data_ini, hora_ini, hora_fin,
                                   data_fin, valor_total)
                tela_con.destroy()
                tela_pesq_age.lift()
            else:
                tela_con.lift()

        except TypeError:
            messagebox.showwarning('AGT - Contratar', 'Campo em branco ou não preenchido.')

    @staticmethod
    def buscar_agenda(pesq_nome, agenda_tree):
        Conexao.c.execute("SELECT condataini, condatafin, conhoratotal, convalortotal, agenome FROM contrata "
                          "JOIN agenciado ON agecpf = conagecpf "
                          "WHERE condatafin > '%s' and agenome LIKE '%s%%'"
                          % (str(strftime('%Y-%m-%d')), pesq_nome.get()))

        for n in agenda_tree.get_children():
            agenda_tree.delete(n)

        i = 0
        for row in Conexao.c.fetchall():
            agenda_tree.insert('', str(i), values=(row[0], row[1], row[2], row[3], row[4]))
            i += 1

        pesq_nome.delete(0, 'end')

    @staticmethod
    def lista_contratos(pesq_nome, rela_tree):
        Conexao.c.execute("SELECT condataini, condatafin, conhoratotal, convalortotal, agenome FROM contrata "
                          "JOIN agenciado ON agecpf = conagecpf "
                          "WHERE agenome LIKE '%s%%'"
                          % (pesq_nome.get()))

        for n in rela_tree.get_children():
            rela_tree.delete(n)

        i = 0
        for row in Conexao.c.fetchall():
            rela_tree.insert('', str(i), values=(row[0], row[1], row[2], row[3], row[4]))
            i += 1

        pesq_nome.delete(0, 'end')
