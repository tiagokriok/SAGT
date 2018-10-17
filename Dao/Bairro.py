from Connection.Conexao import Conexao


class Bairro:
    @staticmethod
    def cbox_bai():
        Conexao.c.execute("SELECT bainome FROM bairro")

        bairros = []

        for linha_bai in Conexao.c.fetchall():
            bairros.append(linha_bai[0])
        return bairros
