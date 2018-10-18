# Sistema para Agência de Talentos
O sistema foi criado para aprensentação acadêmica no ano de 2017. Criado totalmente em Python 3.
# Descrição
Uma Agência de Talentos deseja criar um sistema para gerenciar seu funcionamento de forma mais eficiente. Para os seus Clientes é mantido um cadastro com: nome, telefone e endereço (nome do bairro, nome da rua e número). Os clientes podem contratar junto aos produtores, os agenciados por uma data, hora, valor e uma descrição sobre o tipo de trabalho que será realizado pelos agenciados. Os agenciados são mantidos um cadastro com nome, sexo, talento, telefone e endereço. Os agenciados são gerenciados por produtores que estão à frente do contrato com o cliente. Será mantido um cadastro de cada produtor, como, nome e telefone. Nota-se que um cliente pode contratar mais de um agenciado para um determinado serviço. E os produtores podem gerenciar mais de um agenciado. Já os agenciados possuem um único produtor gerenciado sua carreira.
# Pacotes necessários
Os pacotes podem ser baixados através do comando pip install.
    
    pymysql
    tkinter
    reportlab
    
### Reportlab
O Reportlab foi usado para criação de PDFs, toda vez que era realizada a contratação de um agenciado, era emitido o Contrato em PDF, com o nome do arquivo sendo Contrato CPF do Agenciado Data e Hora.
- Exemplo: [Contrato.pdf](https://github.com/tiagokriok/SAGT/blob/master/Contrato%20404.019.302-46%2020-11-2017%2022-50.pdf)
### Tkinter
Utilizado para a criação das telas do sistema.
### Pymysql
Realiza a comunicação com o banco de dados MySQL.
