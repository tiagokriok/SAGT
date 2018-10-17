from tkinter import messagebox

from Connection.Conexao import Conexao
from Controller.Controle import Controle


class ProdutorDao:

    # Método Salvar Produtor **********************************LINHAS VAZIAS***************************
    @staticmethod
    def salvar_pro(pro_cpf, pro_rg, pro_nome, pro_fone, tela_cad_pro):

        pro_cpf = pro_cpf.get().strip()
        pro_rg = pro_rg.get().strip()
        pro_nome = pro_nome.get().strip()
        pro_fone = pro_fone.get().strip()
        try:
            # Validar CPF
            if len(pro_cpf) == 14 and Controle.validar_cpf(pro_cpf):
                if 11 <= len(pro_rg) <= 12 and not pro_rg.isspace():
                    if len(pro_nome) <= 80 and not pro_nome.isspace():
                        if 11 <= len(pro_fone) <= 12 and not pro_fone.isspace():
                            # Insert
                            Conexao.c.execute("INSERT INTO produtor (procpf, prorg, pronome, profone)"
                                              "VALUES ('%s','%s','%s','%s')"
                                              % (pro_cpf, pro_rg, pro_nome, pro_fone))

                            Conexao.conn.commit()

                            # Mensagem de Aviso
                            messagebox.showinfo('AGT - Cadastro Produtor', 'Produtor cadastrado com sucesso.')
                            tela_cad_pro.destroy()
                        else:
                            messagebox.showwarning('AGT - Cadastrar Produtor', 'Digite o Telefone Corretamente!.')
                            tela_cad_pro.lift()
                    else:
                        messagebox.showwarning('AGT - Cadastrar Produtor', 'Abrevie o nome.')
                        tela_cad_pro.lift()
                else:
                    messagebox.showwarning('AGT - Cadastrar Produtor', 'Digite o RG corretamente!')
                    tela_cad_pro.lift()
            else:
                messagebox.showwarning('AGT - Cadastrar Produtor', 'CPF inválido!')
                tela_cad_pro.lift()
        except TypeError:
            messagebox.showwarning('AGT - Cadastrar Produtor', 'Preencha os campos corretamente!')

    @staticmethod
    def pesquisar(pesq_ent, pro_tree, telapesq, btalt, btex):
        try:
            # Select
            Conexao.c.execute("SELECT procpf, prorg, pronome, profone FROM produtor "
                              "WHERE pronome LIKE '%s%%'" % pesq_ent.get())

            # Apagar última pesquisa
            for n in pro_tree.get_children():
                pro_tree.delete(n)

            # Inserindo o retorno na Tree
            i = 0
            for row in Conexao.c.fetchall():
                pro_tree.insert('', str(i), values=(row[0], row[1], row[2], row[3]))
                i += 1

            telapesq.lift()
            btalt.config(state='normal')
            btex.config(state='normal')
            pesq_ent.delete(0, 'end')

        except TypeError:
            # Mensagem de Aviso
            messagebox.showwarning('AGT', 'Produtor não cadastrado')
            telapesq.lift()

    # Método Alterar Produtor ***************************LINHAS VAZIAS***************************
    @staticmethod
    def alterar(pro_cpf, pro_rg, pro_nome, pro_fone, pro_tree, telaalt, lista_pro, telapesq, btalt, btex):

        # Armazena o CPF antigo
        ant_cpf = lista_pro[0]

        # CPF
        pro_cpf = pro_cpf.get()

        try:
            # Validar CPF
            if len(pro_cpf) == 14 and Controle.validar_cpf(pro_cpf):

                # Mensagem de Confirmação
                if messagebox.askyesno('AGT - Alterar Produtor', 'Tem certeza que deseja alterar?'):

                    # Update
                    Conexao.c.execute("UPDATE produtor SET procpf = '%s', prorg = '%s', pronome = '%s', profone = '%s'"
                                      "WHERE procpf= '%s'"
                                      % (pro_cpf, pro_rg.get(), pro_nome.get(), pro_fone.get(), ant_cpf))

                    Conexao.conn.commit()

                    # Mensagem de Aviso
                    messagebox.showinfo('AGT - Alterar Produtor', 'Alterado com sucesso!')

                    for n in pro_tree.get_children():
                        pro_tree.delete(n)

                    telapesq.lift()
                    btalt.config(state='disabled')
                    btex.config(state='disabled')
                    telaalt.destroy()
                else:
                    pass
            else:
                messagebox.showwarning('AGT - Alterar Produtor', 'CPF inválido.')
                telaalt.lift()
        except TypeError:
            messagebox.showwarning('AGT - Alterar Produtor', 'Preencha os campos corretamente!')

    # Método Excluir Produtor
    @staticmethod
    def excluir_pro(pro_tree, telapesq, btalt, btex):

        # Recebe o CPF do item selecionado
        produtor_cpf = pro_tree.item(pro_tree.selection())['values'][0]

        # Mensagem de Confirmação
        if messagebox.askyesno('AGT - Excluir Produtor', 'Tem certeza que deseja excluir?'):

            # Delete
            Conexao.c.execute("DELETE FROM produtor where procpf = '%s'" % produtor_cpf)
            Conexao.conn.commit()

            # Mensagem de Aviso
            messagebox.showinfo('AGT - Excluir Produtor', 'Produtor excluído.')

            for n in pro_tree.get_children():
                pro_tree.delete(n)

            telapesq.lift()
            btalt.config(state='disabled')
            btex.config(state='disabled')

        else:
            pass

    @staticmethod
    def cbox_pro():
        Conexao.c.execute("SELECT pronome FROM produtor")

        produtores = []

        for linha_pro in Conexao.c.fetchall():
            produtores.append(linha_pro[0])

        return produtores
