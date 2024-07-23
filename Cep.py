import requests
import os

os.system("clear")

def consultar_cep(cep):
    url = f'https://brasilapi.com.br/api/cep/v1/{cep}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Erro na requisição: {response.status_code}')
            return None
    except requests.exceptions.RequestException as e:
        print(f'Erro na conexão: {e}')
        return None

def main():
    cep = input("Digite o CEP (apenas números): ")    
    resultado = consultar_cep(cep)
    if resultado:
        print("======Consulta realizada com sucesso!=====")
        
        os.system("clear")
        
        print(f"CEP: {resultado['cep']}")
        print('==================================')
        print(f"Logradouro: {resultado['street']}")
        print('==================================')
        print(f"Bairro: {resultado['neighborhood']}")
        print('==================================')
        print('==================================')
        print(f"Cidade: {resultado['city']}")
        print('==================================')
        print('==================================')
        print(f"Estado: {resultado['state']}")
        print('==================================')
    else:
        print("Consulta falhou. Verifique o CEP e tente novamente.")

if __name__ == "__main__":
    main()
