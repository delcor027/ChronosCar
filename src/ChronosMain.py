import pyodbc
import streamlit as st

# Função para conectar ao banco de dados
def connect_to_db():
    server = 'DELCOR'
    database = 'CHRONOS'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    conn = pyodbc.connect(connection_string)
    return conn

# Função para inserir um novo registro na tabela
def insert_into_table(tipo, marca, modelo, cor, combustivel, ano, preco):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO STG.CadastroVeiculos (Tipo, Marca, Modelo, Cor, Combustivel, Ano, Preco)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    cursor.execute(query, (tipo, marca, modelo, cor, combustivel, ano, preco))
    conn.commit()
    cursor.close()
    conn.close()

# Interface gráfica com Streamlit
st.title('Cadastro de Veículos da Chronos Car')

# Opções para os campos
tipos = ['Carro', 'Moto', 'Caminhão']

marcas = [  'Volkswagen', 'Toyota', 'Hyundai', 'Fiat', 
            'Ford', 'Honda', 'Chevrolet', 'Renault', 
            'BMW', 'Mercedes-Benz', 'Nissan', 'Peugeot', 
            'Audi', 'Kia', 'Land Rover', 'Mitsubishi', 
            'JAC', 'GWM', 'BYD', 'RAM']

cores = [   'Preto', 'Branco', 'Vermelho', 'Prata',
            'Azul', 'Verde', 'Laranja', 'Bege',]

combustiveis = ['Gasolina', 'Diesel', 'Elétrico', 'Flex']

modelos_por_marca = {
    'Volkswagen': ['Gol', 'Polo', 'T-Cross', 'Taos', 'Amarok', 'Nivus', 'Jetta'],
    'Toyota': ['Corolla', 'Corolla Cross', 'Etios', 'Hilux', 'RAV4', 'SW4'],
    'Hyundai': ['Gol', 'Polo', 'T-Cross', 'Taos', 'Amarok', 'Nivus', 'Jetta'],
    'Fiat': ['Mobi', 'Argo', 'Cronos', 'Pulse', 'Fastback', 'Uno', 'Palio', 'Siena', 'Ducato', 'Strada', 'Toro'],
    'Ford': ['EcoSport', 'Fiesta', 'Fusion', 'Ka Hatch', 'Ka Sedan', 'Mustang', 'Ranger'],
    'Honda': ['Accord', 'City', 'Civic', 'CR-V', 'Fit', 'HR-V', 'WR-V'],
}

# Campos para inserção de dados com opções
tipo = st.selectbox('Tipo', tipos)
marca = st.selectbox('Marca', marcas)
modelos = modelos_por_marca.get(marca, [])
modelo = st.selectbox('Modelo', modelos)
cor = st.selectbox('Cor', cores)
combustivel = st.selectbox('Combustível', combustiveis)
ano = st.number_input('Ano', step=1, format="%d")
preco = st.number_input('Preço', step=0.01, format="%.2f")

# Botão para inserir os dados
if st.button('Inserir Registro'):
    insert_into_table(tipo, marca, modelo, cor, combustivel, ano, preco)
    st.success('Dados inseridos com sucesso!')
