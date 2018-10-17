import pymysql
from tkinter import messagebox


class Conexao:
    try:
        conn = pymysql.connect(host='localhost', user='nomedousuario', password='senha', db='nomebanco')
        c = conn.cursor()

    except TypeError:
        messagebox.showinfo('AGT', 'Não foi possível fazer conexão com o banco.')
