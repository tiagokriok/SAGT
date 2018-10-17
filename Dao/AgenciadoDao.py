from tkinter import messagebox

from Connection.Conexao import Conexao
from Controller.Controle import Controle


class AgenciadoDao:

    # Método Salvar Agenciado *******************VALIDAR CPF/ LINHAS VAZIAS**********************************
    @staticmethod
    def salvar_age(age_cpf, age_nome, age_ida, age_sex, age_tal, age_fone, age_val, age_bai, age_pro, tela_cad_age):

        # CPF
        age_cpf = age_cpf.get()

        # Validar CPF
        if len(age_cpf) == 14 and Controle.validar_cpf(age_cpf):
            # Busca código do bairro
            Conexao.c.execute("SELECT baicodigo FROM bairro WHERE bainome = '%s'" % age_bai.get())
            age_bai_id = Conexao.c.fetchone()[0]

            # Busca cpf do produtor
            Conexao.c.execute("SELECT procpf FROM produtor WHERE pronome = '%s'" % age_pro.get())
            age_pro_cpf = Conexao.c.fetchone()[0]

            # Insert
            Conexao.c.execute("INSERT INTO agenciado (agecpf, agenome, ageidade, agesexo, agetalento, agefone,"
                              "agevalor, agebaicodigo, ageprocpf) VALUES"
                              "('%s','%s','%i','%s','%s','%s','%.2f','%i','%s')" % (age_cpf, age_nome.get(),
                                                                                    int(age_ida.get()), age_sex.get(),
                                                                                    age_tal.get(), age_fone.get(),
                                                                                    float(age_val.get()), age_bai_id,
                                                                                    age_pro_cpf))

            Conexao.conn.commit()

            # Mensagem de Informação
            messagebox.showinfo('AGT - Cadastro Agenciado', 'Agenciado cadastrado com sucesso')
            tela_cad_age.destroy()
        else:
            messagebox.showwarning('AGT - Cadastrar Agenciado', 'CPF inválido.')
            tela_cad_age.lift()

    # Método Pesquisar e colocar na Tree
    @staticmethod
    def pesquisar(pesq_ent, age_tree, tela_pesq_age, btalt, btex, btcon):
        try:
            # Select
            Conexao.c.execute(
                "SELECT agecpf, agenome, ageidade, agesexo, agetalento, agefone, agevalor, bainome, pronome FROM "
                "agenciado "
                "JOIN bairro ON baicodigo = agebaicodigo "
                "JOIN produtor ON procpf = ageprocpf "
                "WHERE agenome LIKE '%s%%'" % pesq_ent.get())

            # Apagar última pesquisa
            for n in age_tree.get_children():
                age_tree.delete(n)

            # Inserindo o retorno na Tree
            i = 0
            for row in Conexao.c.fetchall():
                age_tree.insert('', str(i), values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                    row[8]))
                i += 1

            btalt.config(state='normal')
            btex.config(state='normal')
            btcon.config(state='normal')
            pesq_ent.delete(0, 'end')

        except TypeError:

            # Mensagem de Aviso
            messagebox.showwarning('AGT', 'Agenciado não cadastrado.')
            tela_pesq_age.lift()

    # Método Alterar Agenciado ******************VERIFICAR CPF/LINHAS VAZIAS*********************************
    @staticmethod
    def alterar(age_cpf, age_nome, age_ida, age_sex, age_tal, age_fone, age_val, age_bai, pro_age, age_tree,
                tela_alt_age, lista_age, tela_pesq_age, btalt, btex, btcon):

        # CPF
        age_cpf = age_cpf.get()

        # Armazena o CPF antigo
        ant_cpf = lista_age[0]

        # Validar CPF
        if len(age_cpf) == 14 and Controle.validar_cpf(age_cpf):

            # Mensagem de Confirmação
            if messagebox.askyesno('AGT - Alterar Cliente', 'Tem certeza que deseja alterar?'):

                # Procura código Bairro
                Conexao.c.execute("SELECT baicodigo FROM bairro WHERE bainome = '%s'" % age_bai.get())
                cod_bai_age = int(Conexao.c.fetchone()[0])

                # Procura cpf Produtor
                Conexao.c.execute("SELECT procpf FROM produtor WHERE pronome = '%s'" % pro_age.get())
                cpf_pro_age = Conexao.c.fetchone()[0]

                # Update
                Conexao.c.execute("UPDATE agenciado SET agecpf = '%s', agenome = '%s', ageidade = '%i',"
                                  "agesexo = '%s', agetalento = '%s', agefone = '%s', agevalor = '%.2f',"
                                  "agebaicodigo = '%i', ageprocpf = '%s' WHERE agecpf = '%s'"
                                  % (age_cpf, age_nome.get(), int(age_ida.get()), age_sex.get(),
                                     age_tal.get(), age_fone.get(), float(age_val.get()), cod_bai_age,
                                     cpf_pro_age, ant_cpf))
                Conexao.conn.commit()
                # Mensagem de Aviso
                messagebox.showinfo('AGT - Alterar Agenciado', 'Alterado com sucesso.')

                for n in age_tree.get_children():
                    age_tree.delete(n)

                tela_alt_age.destroy()
                tela_pesq_age.lift()
                btalt.config(state='disabled')
                btex.config(state='disabled')
                btcon.config(state='disabled')
            else:
                pass
        else:
            messagebox.showwarning('AGT - Alterar Agenciado', 'CPF inválido.')
            tela_alt_age.lift()

    # Método Excluir Agenciado
    @staticmethod
    def excluir_age(age_tree, tela_pesq_age, btalt, btex, btcon):

        # Recebe o cpf do agenciado
        agenciado_cpf = age_tree.item(age_tree.selection())['values'][0]

        # Mensagem de confirmação
        if messagebox.askyesno('AGT - Excluir Agenciado', 'Tem certeza que deseja excluir?'):

            # Delete
            Conexao.c.execute("DELETE FROM agenciado WHERE agecpf= '%s'" % agenciado_cpf)
            Conexao.conn.commit()

            # Mensagem de Aviso
            messagebox.showinfo('AGT - Excluir Agenciado', 'Agenciado excluído.')

            for n in age_tree.get_children():
                age_tree.delete(n)

            tela_pesq_age.lift()
            btalt.config(state='disabled')
            btex.config(state='disabled')
            btcon.config(state='disabled')
        else:
            pass
