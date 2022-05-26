from email import charset
import firebirdsql
import pandas as pd

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

df = pd.read_sql("SISTB002_PARAMETRO",con)
print(df.head())