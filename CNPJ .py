import requests
import os 

os.system("clear")

def consultar_cnpj(cnpj):
    url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f'Erro na requisição: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Erro na conexão: {e}')
        return None

def main():
    cnpj = input("Digite o CNPJ para consultar (apenas números): ")
    resultado = consultar_cnpj(cnpj)
    if resultado:
        print("\nInformações encontradas:")
        print("--------------------------------------------")
        print(f"CNPJ: {resultado['cnpj']}")
        print(f"Razão Social: {resultado['nome']}")
        print(f"Data de Abertura: {resultado['abertura']}")
        print(f"Telefone: {resultado['telefone']}")
        print(f"tipo: {resultado['tipo']}")
        print(f"bairro: {resultado['bairro']}")
        print(f"cep: {resultado['cep']}")
        print(f"email: {resultado['email']}")
        print(f"municipio: {resultado['municipio']}")
        print(f"uf: {resultado['uf']}")
        print(f"status: {resultado['status']}")
        print(f"abertura: {resultado['abertura']}")
        print(f"situacao: {resultado['situacao']}")
        print(f"logradouro: {resultado['logradouro']}")
    else:
        print("\nNão foi possível obter informações para o CNPJ informado.")

if __name__ == "__main__":
    main()

