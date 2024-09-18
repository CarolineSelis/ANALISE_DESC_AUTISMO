import requests
import pandas as pd

# Função para chamar a API e obter os dados de uma classe CNAE específica
def get_cnae_data(classe):
    url = f"https://servicodados.ibge.gov.br/api/v2/cnae/classes/{classe}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Dados da classe {classe} obtidos com sucesso!")
        return data
    else:
        print(f"Erro ao acessar os dados da classe {classe}: {response.status_code}")
        return None

# Exemplo: Consultar a classe 6201-5/00 (Desenvolvimento de software sob encomenda)
classe = "6201500"
cnae_data = get_cnae_data(classe)

# Se quiser organizar os dados em um DataFrame do pandas
if cnae_data:
    df = pd.json_normalize(cnae_data)
    print(df.head())  # Exibe os primeiros registros
