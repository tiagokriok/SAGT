from tkinter import messagebox
from Connection.Conexao import Conexao
from Controller.Controle import Controle


class ClienteDao:

    # Método Salvar Cliente ******************* VALIDAR CPF/ LINHAS VAZIAS **********************************
    @staticmethod
    def salvar_cli(cli_cpf, cli_rg, cli_nome, cli_ramo, cli_fone, cli_bai, tela_cad_cli):

        # CPF
        cli_cpf = cli_cpf.get()

        # Validar CPF
        if len(cli_cpf) == 14 and Controle.validar_cpf(cli_cpf):
            # Procura o código do bairro
            Conexao.c.execute("SELECT baicodigo FROM BAIRRO WHERE bainome = '%s'" % cli_bai.get())
            bai_id = Conexao.c.fetchone()[0]

            # Insert
            Conexao.c.execute("INSERT INTO cliente(clicpf, clirg, clinome, cliramo, clifone, clibaicodigo)"
                              "VALUES ('%s','%s','%s','%s','%s','%i')" % (cli_cpf, cli_rg.get(), cli_nome.get(),
                                                                          cli_ramo.get(), cli_fone.get(), int(bai_id)))
            Conexao.conn.commit()

            # Mensagem de Aviso
            messagebox.showinfo('AGT - Cadastro', 'Cliente cadastrado com sucesso.')
            tela_cad_cli.destroy()
        else:
            messagebox.showwarning('AGT - Cadastrar Cliente', 'CPF inválido.')
            tela_cad_cli.lift()

    @staticmethod
    def pesquisar(pesq_ent, cli_tree, tela_pesq_cli, btalt, btex):
        try:
            Conexao.c.execute("SELECT clicpf, clirg, clinome, cliramo, clifone, bainome FROM cliente "
                              "JOIN bairro ON baicodigo = clibaicodigo "
                              "WHERE clinome LIKE '%s%%'" % pesq_ent.get())

            # Apagar última pesquisa
            for n in cli_tree.get_children():
                cli_tree.delete(n)

            # Inserindo o retorno na Tree
            i = 0
            for row in Conexao.c.fetchall():
                cli_tree.insert('', str(i), values=(row[0], row[1], row[2], row[3], row[4], row[5]))
                i += 1

            btalt.config(state='normal')
            btex.config(state='normal')
            pesq_ent.delete(0, 'end')

        except TypeError:
            # Mensagem de Aviso
            messagebox.showwarning('AGT', 'Cliente não cadastrado.')
            tela_pesq_cli.lift()

    @staticmethod  # ********************* Validar CPF / Linhas Vazias
    def alterar(cli_cpf, cli_rg, cli_nome, cli_ramo, cli_fone, cli_bai, cli_tree, tela_alt_cli, lista_cli,
                tela_pesq_cli, btalt, btex):

        # CPF
        cli_cpf = cli_cpf.get()

        # Armazena o CPF antigo
        ant_cpf = lista_cli[0]

        # Validar CPF
        if len(cli_cpf) == 14 and Controle.validar_cpf(cli_cpf):
            # Mensagem de Confirmação
            if messagebox.askyesno('AGT - Alterar Cliente', 'Tem certeza que deseja alterar?'):

                # Busca o código do Bairro
                Conexao.c.execute("SELECT baicodigo FROM bairro WHERE bainome = '%s'" % cli_bai.get())
                id_bai = int(Conexao.c.fetchone()[0])

                # Update
                Conexao.c.execute("UPDATE cliente SET clicpf = '%s', clirg = '%s', clinome = '%s', cliramo = '%s',"
                                  "clifone = '%s', clibaicodigo = '%i' WHERE clicpf = '%s'"
                                  % (cli_cpf, cli_rg.get(), cli_nome.get(), cli_ramo.get(), cli_fone.get(),
                                     id_bai, ant_cpf))
                Conexao.conn.commit()

                # Mensagem de Aviso
                messagebox.showinfo('AGT - Alterar', 'Alterado com sucesso!')

                for n in cli_tree.get_children():
                    cli_tree.delete(n)

                tela_pesq_cli.lift()
                btalt.config(state='disabled')
                btex.config(state='disabled')
                tela_alt_cli.destroy()
            else:
                pass
        else:
            messagebox.showwarning('AGT - Alterar Cliente', 'CPF inválido.')
            tela_alt_cli.lift()

    @staticmethod
    def excluir_cli(cli_tree, tela_pesq_cli, btalt, btex):

        # Recebe o cpf do item selecionado
        cliente_cpf = cli_tree.item(cli_tree.selection())['values'][0]

        # Mensagem de Confirmação
        if messagebox.askyesno('AGT - Excluir Cliente', 'Tem certeza que deseja excluir?'):

            # Delete
            Conexao.c.execute("DELETE FROM cliente WHERE clicpf = '%s'" % cliente_cpf)
            Conexao.conn.commit()

            # Mensagem de Aviso
            messagebox.showinfo('AGT - Excluir Cliente', 'Cliente excluído.')

            for n in cli_tree.get_children():
                cli_tree.delete(n)

            tela_pesq_cli.lift()
            btalt.config(state='disabled')
            btex.config(state='disabled')
        else:
            pass

    @staticmethod
    def buscar_rg(cli_cpf):

        Conexao.c.execute("SELECT clirg FROM cliente WHERE clicpf='%s'" % cli_cpf.get())
        cli_rg = Conexao.c.fetchone()[0]
        return cli_rg

    @staticmethod
    def buscar_cli(cli_cpf, cli_nome, tela_con, btgecon):
        try:

            Conexao.c.execute("SELECT clinome FROM cliente WHERE clicpf='%s'" % cli_cpf.get())

            nome = Conexao.c.fetchone()[0]

            cli_nome.config(state='normal')
            cli_nome.insert(0, nome)
            cli_nome.config(state='disabled')
            btgecon.config(state='normal')
            cli_cpf.config(state='disabled')

        except TypeError:
            # Mensagem de Aviso
            messagebox.showwarning('AGT', 'Cliente não cadastrado.')
            tela_con.lift()
