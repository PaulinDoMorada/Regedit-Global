import requests
import time
import random

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def generate_data(random_item):
    nome = random_item.get("nome")
    idade = random_item.get("idade")
    cpf = random_item.get("cpf")
    rg = random_item.get("rg")
    data_nasc = random_item.get("data_nasc")
    sexo = random_item.get("sexo")
    signo = random_item.get("signo")
    mae = random_item.get("mae")
    pai = random_item.get("pai")
    email = random_item.get("email")
    senha = random_item.get("senha")
    cep = random_item.get("cep")
    endereco = random_item.get("endereco")
    numero = random_item.get("numero")
    bairro = random_item.get("bairro")
    cidade = random_item.get("cidade")
    estado = random_item.get("estado")
    telefone_fixo = random_item.get("telefone_fixo")
    celular = random_item.get("celular")
    altura = random_item.get("altura")
    peso = random_item.get("peso")
    tipo_sanguineo = random_item.get("tipo_sanguineo")
    cor = random_item.get("cor")
    
    if nome:
        print("\n")
        print(colors.BLUE + "Nome:" + colors.ENDC, colors.WARNING + nome + colors.ENDC + " ⚠️")
        print(colors.BLUE + "Idade:" + colors.ENDC, colors.GREEN + str(idade) + colors.ENDC)
        print(colors.BLUE + "CPF:" + colors.ENDC, colors.GREEN + cpf + colors.ENDC)
        print(colors.BLUE + "RG:" + colors.ENDC, colors.GREEN + rg + colors.ENDC)
        print(colors.BLUE + "Data de Nascimento:" + colors.ENDC, colors.GREEN + data_nasc + colors.ENDC)
        print(colors.BLUE + "Sexo:" + colors.ENDC, colors.GREEN + sexo + colors.ENDC)
        print(colors.BLUE + "Signo:" + colors.ENDC, colors.GREEN + signo + colors.ENDC)
        print(colors.BLUE + "Mãe:" + colors.ENDC, colors.GREEN + mae + colors.ENDC)
        print(colors.BLUE + "Pai:" + colors.ENDC, colors.GREEN + pai + colors.ENDC)
        print(colors.BLUE + "E-mail:" + colors.ENDC, colors.GREEN + email + colors.ENDC)
        print(colors.BLUE + "Senha:" + colors.ENDC, colors.GREEN + senha + colors.ENDC)
        print(colors.BLUE + "CEP:" + colors.ENDC, colors.GREEN + cep + colors.ENDC)
        print(colors.BLUE + "Endereço:" + colors.ENDC, colors.GREEN + endereco + colors.ENDC)
        print(colors.BLUE + "Número:" + colors.ENDC, colors.GREEN + str(numero) + colors.ENDC)
        print(colors.BLUE + "Bairro:" + colors.ENDC, colors.GREEN + bairro + colors.ENDC)
        print(colors.BLUE + "Cidade:" + colors.ENDC, colors.GREEN + cidade + colors.ENDC)
        print(colors.BLUE + "Estado:" + colors.ENDC, colors.GREEN + estado + colors.ENDC)
        print(colors.BLUE + "Telefone Fixo:" + colors.ENDC, colors.GREEN + telefone_fixo + colors.ENDC)
        print(colors.BLUE + "Celular:" + colors.ENDC, colors.GREEN + celular + colors.ENDC)
        print(colors.BLUE + "Altura:" + colors.ENDC, colors.GREEN + altura + colors.ENDC)
        print(colors.BLUE + "Peso:" + colors.ENDC, colors.GREEN + str(peso) + colors.ENDC)
        print(colors.BLUE + "Tipo Sanguíneo:" + colors.ENDC, colors.GREEN + tipo_sanguineo + colors.ENDC)
        print(colors.BLUE + "Cor Favorita:" + colors.ENDC, colors.GREEN + cor + colors.ENDC)
        
    else:
        print("Nomes não encontrados")
        
    time.sleep(1)

def main():
    url = "https://pastebin.com/raw/ExYXWQ6w"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()

        while True:
            print(""" _  _____ ___ ___ _____ ___    _     _   
| |/ /_ _| _ \_ _|_   _/ _ \ _| |_ _| |_ 
| ' < | ||   /| |  | || (_) |_   _|_   _|
|_|\_\___|_|_\___| |_| \___/  |_|   |_|  
                                         
""")
            print(colors.BLUE+"1."+ colors.GREEN+ " Gerar Dados Reais")
            print(colors.BLUE+"2." + colors.GREEN +" Sair")
            
            choice = input(colors.GREEN + "Escolha a opção: ")
            
            if choice == "1":
                random_item = random.choice(json_data)
                generate_data(random_item)
            elif choice == "2":
                print("Saindo do programa..")
                break
            else:
                print("Opção inválida!")

    else:
        print(colors.FAIL + "Link incorreto. Verifique o link e tente novamente." + colors.ENDC)

if __name__ == "__main__":
    main()
