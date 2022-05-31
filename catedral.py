from email import charset
#importando firebird e pandas
import firebirdsql
import pandas as pd
import matplotlib


#conexão ao banco de dados
con = firebirdsql.Connection(user='SYSDBA', 
password='Laika06', 
database='C:\\RDR\DADOS\\Catedral.FDB', 
host="localhost", charset="ansi")


cur=con.cursor()
""""
cur.execute('select * from sistb001_operador')

for c in cur.fetchall():
    print(c)
print('Finalizado')    """ 

#query no banco de dados
df = pd.read_sql_query("select * from sistb001_operador",con)
print(df.head())

df_index = pd.read_sql_query("select * from sistb001_operador", con, index_col="IC_ATIVO")
print(df_index.head())

query = '''
SELECT f.no_funcionario,
       fu.no_funcao

FROM sistb011_funcionario f
INNER JOIN sistb009_funcao fu
ON f.nu_funcao = fu.nu_funcao;

'''

df = pd.read_sql_query (query, con)
print(df.head())

query_venda_funcionario = '''
SELECT v.co_operador, count(*)FROM sistb007_venda v
GROUP BY v.co_operador
ORDER BY count(*) DESC;
'''

venda = pd.read_sql_query(query_venda_funcionario, con)
print(venda.head())

funcionarios_venda = venda.groupby('CO_OPERADOR')['COUNT'].mean()
funcionarios_venda.head().plot.bar()