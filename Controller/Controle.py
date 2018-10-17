from datetime import datetime
import os
from time import strftime
from tkinter import messagebox

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


class Controle:
    # Validar CPF
    @staticmethod
    def validar_cpf(cpf):

        lista_cpf = []
        for i in range(0, len(cpf)):
            if cpf[i] == '.' or cpf[i] == '-':
                pass
            else:
                lista_cpf.append(int(cpf[i]))

        peso_veri1 = 10
        soma_veri1 = 0

        for j in range(0, 9):
            soma_veri1 += lista_cpf[j] * peso_veri1
            peso_veri1 -= 1

        rest_veri1 = soma_veri1 % 11

        if rest_veri1 < 2:
            veri1 = 0
        else:
            veri1 = 11 - rest_veri1

        if veri1 == lista_cpf[9]:

            # Verificador do segundo dígito
            peso_veri2 = 11
            soma_veri2 = 0
            for n in range(0, 10):
                soma_veri2 += lista_cpf[n] * peso_veri2
                peso_veri2 -= 1

            rest_veri2 = soma_veri2 % 11

            if rest_veri2 < 2:
                veri2 = 0
            else:
                veri2 = 11 - rest_veri2

            if veri1 == lista_cpf[9] and veri2 == lista_cpf[10]:
                return True
            else:
                return False
        else:
            return False

    # Diferença entre duas Datas
    @staticmethod
    def difer_data(data_ini, data_fin):
        if data_ini == data_fin:
            difer = 0
            return difer
        else:
            data_ini = datetime.strptime(data_ini, '%Y-%m-%d')
            data_fin = datetime.strptime(data_fin, '%Y-%m-%d')

            difer = str(data_fin - data_ini)
            difer = difer.split()
            difer = int(difer[0])

            return difer

    # Calcular Hora total por dia
    @staticmethod
    def calc_hora(hora_ini, hora_fin):

        hora_ini = hora_ini.split(':')
        hora_fin = hora_fin.split(':')
        hora_ini = hora_ini[0]
        hora_fin = hora_fin[0]

        hora_total = float(hora_fin) - float(hora_ini)

        return hora_total

    # Calcular Valor Total do Contrato
    @staticmethod
    def calc_contrato(difedt, hora_dia, age_valor):
        if difedt == 1:
            valor_total = (difedt*hora_dia)*(age_valor*2)
        elif difedt != 0:
            valor_total = (difedt*hora_dia)*age_valor
        else:
            valor_total = hora_dia * age_valor
        return float(valor_total)

    # Gerar PDF
    @staticmethod
    def gerar_pdf(cli_nome, cli_cpf, cli_rg, age_nome, age_cpf, desc, data_ini, hora_ini, hora_fin, data_fin,
                  valor_total):
        # Nome Agenciado
        age_nome = age_nome.get()
        lista_nome = age_nome.split()

        # Fonte
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))

        # Nome Arquivo
        nome_pdf = 'Contrato' + ' ' + age_cpf.get() + ' ' + str(strftime('%d-%m-%Y %H-%M')) + '.pdf'

        # Canvas
        c = canvas.Canvas(nome_pdf)

        # Fonte a ser utilizada e tamanho
        c.setFont('Arial', 12, leading=None)

        # CONTRATO DE PRESTAÇÃ O DE SERVIÇOS ARTÍSTICOS
        c.drawCentredString(290, 800, 'CONTRATO DE PRESTAÇÃO DE SERVIÇOS ARTÍSTICOS')

        # CONTRATANTE
        c.drawString(30, 750, 'CONTRATANTE:')

        # CLIENTE
        c.drawString(130, 750, cli_nome.get() + ', portador da cédula de Identidade R.G. n°')
        c.drawString(30, 730, cli_rg + ', e CPF n° ' + cli_cpf.get() + '.')

        # CONTRATADO
        c.drawString(30, 710, 'CONTRATADO:')

        # AGENCIADO
        c.drawString(130, 710, age_nome + ', portador do CPF n° ' + age_cpf.get() + '.')

        c.drawString(30, 670, 'Pelo presente contrato de serviço, as partes, têm justo e contratado o seguinte:')

        # DO OBJETO DO CONTRATO
        c.drawCentredString(290, 640, 'DO OBJETO DO CONTRATO')

        # Cláusula 1ª
        c.drawString(30, 620, 'Cláusula 1ª. O presente contrato tem como OBJETO, a realização, pelo o '
                     + lista_nome[0] + ' ' + lista_nome[-1])
        c.drawString(30, 600, 'DESCREVER: ' + desc + ' no dia ' + data_ini)
        c.drawString(30, 580, 'iniciado-se às ' + hora_ini + ' e terminando às ' + hora_fin + ' do dia ' + data_fin +
                     '.')

        # DAS OBRIGAÇÕES
        c.drawCentredString(290, 550, 'DAS OBRIGAÇÕES')

        # Cláusula 2ª
        c.drawString(30, 530,
                     'Cláusula 2ª. Será responsável a CONTRATADA pela presença do artista no dia, local e hora')
        c.drawString(30, 510,
                     'combinados, para a realização do trabalho requerido, excluído-se os casos em que não der')
        c.drawString(30, 490, ' motivo que impossibilitem a presença do artista.')

        # DA MULTAS
        c.drawCentredString(290, 460, 'DAS MULTAS')

        # Cláusula 3ª
        c.drawString(30, 440,
                     'Cláusula 3ª. Será ressarcida a parte que não violar qualquer das cláusulas dispostas neste')
        c.drawString(30, 420, 'instrumento, pela parte que der causa, aplicando-se multa de 50% do valor estipulado na '
                              'cláusula 4ª.')

        # DA RENUMERAÇÃO
        c.drawCentredString(290, 390, 'DA RENUMERAÇÃO')

        # Cláusula 4ª
        c.drawString(30, 370, 'Cláusula 4ª. O CONTRATANTE pagará o valor de R$ {:.2f} pela presentação do artista '
                     .format(valor_total))
        c.drawString(30, 350, 'contratado, efetuando o pagamento em parcela única e diretamente ao CONTRATADO.')

        # DATA E ASSINATURAS
        c.drawString(60, 305, 'de')
        c.drawString(150, 305, 'de')
        c.line(30, 300, 200, 300)  # Linha

        c.line(30, 270, 200, 270)  # Linha
        c.drawString(40, 250, '(Assinatura do Contratante)')

        c.line(30, 220, 200, 220)  # Linha
        c.drawString(40, 200, '(Assinatura do Contratado)')

        c.line(30, 170, 200, 170)  # Linha
        c.drawString(40, 150, '(Nome, RG, Testemunha)')

        # Salvar
        c.showPage()
        print('Gerando PDF....')
        c.save()

        if messagebox.askyesno('AGT - Contrato', 'PDF do Contrato gerado, Deseja abrir?'):
            os.startfile('C:/Users/Tiago/Desktop/Faculdade/6P/Analise Modelo Sistema/Cont Trabalho/Projeto AGT/'
                         + nome_pdf)
        else:
            pass
