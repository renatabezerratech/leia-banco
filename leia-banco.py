import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

# Carregar as variáveis do arquivo .env
load_dotenv()

# Carregar as variáveis de ambiente
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')

# Debug: Verificar se as variáveis estão sendo carregadas corretamente
print(f"User: {user}, Password: {password}, Host: {host}, Database: {database}")

# Criar a URL de conexão
connection_string = f'mysql+mysqldb://{user}:{password}@{host}/{database}'
engine = create_engine(connection_string)

# Especificar a tabela que você quer ler (ex: 'categorias')
categorias = 'categorias'

# Ler a tabela do MySQL para um DataFrame
df = pd.read_sql(f'SELECT * FROM {categorias}', con=engine)

# Imprimir o conteúdo do DataFrame no terminal
print(df)



# pd.read_sql(): Utiliza uma query SQL (SELECT * FROM {nome_tabela}) para buscar todos os dados da tabela especificada e os armazena em um DataFrame.
# engine: Conecta ao banco de dados MySQL usando SQLAlchemy.
# print(df): Exibe o DataFrame no terminal com o conteúdo da tabela do banco de dados.
# Intalação de arq.env no bash: /c/Users/rsbez/banco/.venv/Scripts/python.exe -m pip install python-dotenv
# O arquivo de variáveis de ambiente não é nomeável, se coloca apenas .env

