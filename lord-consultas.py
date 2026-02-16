"""
Lord Consultas - Painel de Consultas para Termux
Autor: [Lord]
Repositório: https://github.com/seuusuario/lord-consultas
"""

import os
import sys
import json
import requests
import re
from time import sleep

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def banner():
    print(f"""{Colors.CYAN}{Colors.BOLD}
    ██╗      ██████╗ ██████╗ ██████╗     ██████╗ ██████╗ ███╗   ██╗███████╗██╗   ██╗██╗  ████████╗ █████╗ ███████╗
    ██║     ██╔═══██╗██╔══██╗██╔══██╗   ██╔════╝██╔═══██╗████╗  ██║██╔════╝██║   ██║██║  ╚══██╔══╝██╔══██╗██╔════╝
    ██║     ██║   ██║██████╔╝██║  ██║   ██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     ██║   ███████║███████╗
    ██║     ██║   ██║██╔══██╗██║  ██║   ██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██║   ██╔══██║╚════██║
    ███████╗╚██████╔╝██║  ██║██████╔╝   ╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██║   ██║  ██║███████║
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚══════╝
    {Colors.END}{Colors.YELLOW}
                                    [ Painel de Consultas v1.0 ]
                                    [ Desenvolvido para Termux ]
    {Colors.END}""")

def menu():
    print(f"""
{Colors.GREEN}{Colors.BOLD}[+] MÓDULOS DISPONÍVEIS:{Colors.END}

{Colors.CYAN}[1]{Colors.END} Consulta por NOME
{Colors.CYAN}[2]{Colors.END} Consulta por CPF
{Colors.CYAN}[3]{Colors.END} Consulta por E-MAIL
{Colors.CYAN}[4]{Colors.END} Consulta por TELEFONE
{Colors.CYAN}[5]{Colors.END} Consulta por CNPJ
{Colors.CYAN}[6]{Colors.END} Consulta por PLACA
{Colors.CYAN}[7]{Colors.END} Consulta por CEP
{Colors.CYAN}[8]{Colors.END} Consulta por IP
{Colors.CYAN}[9]{Colors.END} Consulta por BIN (Cartão)
{Colors.CYAN}[10]{Colors.END} Consulta por DOMÍNIO/WHOIS

{Colors.RED}[0]{Colors.END} Sair
{Colors.YELLOW}[99]{Colors.END} Atualizar Sistema
    """)


def consulta_nome():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA POR NOME{Colors.END}")
    nome = input(f"{Colors.YELLOW}Digite o nome completo: {Colors.END}").strip()
    
    if len(nome) < 3:
        print(f"{Colors.RED}[!] Nome muito curto!{Colors.END}")
        sleep(2)
        return
    
    print(f"{Colors.GREEN}[*] Consultando...{Colors.END}")
    
    
    try:
        
        resultado = {
            "nome": nome,
            "status": "Consulta realizada",
            "observacao": "Configure uma API real para obter resultados"
        }
        print(f"\n{Colors.GREEN}{json.dumps(resultado, indent=2, ensure_ascii=False)}{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}[!] Erro: {e}{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def consulta_cpf():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA POR CPF{Colors.END}")
    cpf = input(f"{Colors.YELLOW}Digite o CPF (somente números): {Colors.END}").strip()
    
    if len(cpf) != 11 or not cpf.isdigit():
        print(f"{Colors.RED}[!] CPF inválido!{Colors.END}")
        sleep(2)
        return
    
    print(f"{Colors.GREEN}[*] Validando CPF...{Colors.END}")
    
    def valida_cpf(cpf):
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = 11 - (soma % 11)
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[9]):
            return False
        
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = 11 - (soma % 11)
        if resto == 10 or resto == 11:
            resto = 0
        return resto == int(cpf[10])
    
    if valida_cpf(cpf):
        print(f"{Colors.GREEN}[✓] CPF válido matematicamente!{Colors.END}")
        print(f"{Colors.YELLOW}[!] Para dados completos, é necessário API paga (ReceitaWS, etc){Colors.END}")
    else:
        print(f"{Colors.RED}[✗] CPF inválido!{Colors.END}")
     
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    print(f"\n{Colors.CYAN}CPF Formatado: {cpf_formatado}{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def consulta_email():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA POR E-MAIL{Colors.END}")
    email = input(f"{Colors.YELLOW}Digite o e-mail: {Colors.END}").strip().lower()
    
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(padrao, email):
        print(f"{Colors.RED}[!] E-mail inválido!{Colors.END}")
        sleep(2)
        return
    
    print(f"{Colors.GREEN}[*] Analisando e-mail...{Colors.END}")
    
    dominio = email.split('@')[1]
    
    try:
        import socket
        socket.gethostbyname(dominio)
        print(f"{Colors.GREEN}[✓] Domínio {dominio} está ativo!{Colors.END}")
    except:
        print(f"{Colors.RED}[!] Domínio {dominio} não responde ou não existe{Colors.END}")
    
    
    print(f"\n{Colors.YELLOW}[i] APIs recomendadas:{Colors.END}")
    print(f"  - Hunter.io (hunter.io/api)")
    print(f"  - HaveIBeenPwned (haveibeenpwned.com/API)")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def consulta_telefone():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA POR TELEFONE{Colors.END}")
    telefone = input(f"{Colors.YELLOW}Digite o telefone (com DDD): {Colors.END}").strip()
    
    telefone = re.sub(r'\D', '', telefone)
    
    if len(telefone) < 10:
        print(f"{Colors.RED}[!] Número muito curto!{Colors.END}")
        sleep(2)
        return
    
    ddd = telefone[:2] if len(telefone) >= 11 else telefone[:2]
    numero = telefone[2:] if len(telefone) >= 11 else telefone[2:]
    
    print(f"{Colors.GREEN}[*] Analisando número...{Colors.END}")
    print(f"{Colors.CYAN}DDD: {ddd}{Colors.END}")
    print(f"{Colors.CYAN}Número: {numero}{Colors.END}")
    
    ddds = {
        '11': 'SP', '12': 'SP', '13': 'SP', '14': 'SP', '15': 'SP', '16': 'SP', '17': 'SP', '18': 'SP', '19': 'SP',
        '21': 'RJ', '22': 'RJ', '24': 'RJ',
        '31': 'MG', '32': 'MG', '33': 'MG', '34': 'MG', '35': 'MG', '37': 'MG', '38': 'MG',
        '41': 'PR', '42': 'PR', '43': 'PR', '44': 'PR', '45': 'PR', '46': 'PR',
        '47': 'SC', '48': 'SC', '49': 'SC',
        '51': 'RS', '53': 'RS', '54': 'RS', '55': 'RS',
        '61': 'DF',
        '62': 'GO', '64': 'GO',
        '63': 'TO',
        '65': 'MT', '66': 'MT',
        '67': 'MS',
        '68': 'AC',
        '69': 'RO',
        '71': 'BA', '73': 'BA', '74': 'BA', '75': 'BA', '77': 'BA',
        '79': 'SE',
        '81': 'PE', '87': 'PE',
        '82': 'AL',
        '83': 'PB',
        '84': 'RN',
        '85': 'CE', '88': 'CE',
        '86': 'PI', '89': 'PI',
        '91': 'PA', '93': 'PA', '94': 'PA',
        '92': 'AM', '97': 'AM',
        '95': 'RR',
        '96': 'AP',
        '98': 'MA', '99': 'MA'
    }
    
    estado = ddds.get(ddd, 'Desconhecido')
    print(f"{Colors.CYAN}Estado: {estado}{Colors.END}")
    
    print(f"\n{Colors.YELLOW}[i] Para consulta completa de operadora, use:{Colors.END}")
    print(f"  - API MNP (portabilidade) - geralmente paga")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def consulta_cnpj():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA POR CNPJ{Colors.END}")
    cnpj = input(f"{Colors.YELLOW}Digite o CNPJ (somente números): {Colors.END}").strip()
    
    if len(cnpj) != 14 or not cnpj.isdigit():
        print(f"{Colors.RED}[!] CNPJ inválido!{Colors.END}")
        sleep(2)
        return
    
    print(f"{Colors.GREEN}[*] Consultando na ReceitaWS (API pública)...{Colors.END}")
    
    try:
        url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('status') == 'OK':
                print(f"\n{Colors.GREEN}{Colors.BOLD}✓ DADOS ENCONTRADOS:{Colors.END}\n")
                print(f"{Colors.CYAN}Razão Social:{Colors.END} {data.get('nome', 'N/A')}")
                print(f"{Colors.CYAN}Nome Fantasia:{Colors.END} {data.get('fantasia', 'N/A')}")
                print(f"{Colors.CYAN}CNPJ:{Colors.END} {data.get('cnpj', 'N/A')}")
                print(f"{Colors.CYAN}Status:{Colors.END} {data.get('situacao', 'N/A')}")
                print(f"{Colors.CYAN}Atividade Principal:{Colors.END} {data.get('atividade_principal', [{}])[0].get('text', 'N/A')}")
                print(f"{Colors.CYAN}Endereço:{Colors.END} {data.get('logradouro', '')}, {data.get('numero', '')}")
                print(f"{Colors.CYAN}Bairro:{Colors.END} {data.get('bairro', 'N/A')}")
                print(f"{Colors.CYAN}Cidade/UF:{Colors.END} {data.get('municipio', 'N/A')}/{data.get('uf', 'N/A')}")
                print(f"{Colors.CYAN}CEP:{Colors.END} {data.get('cep', 'N/A')}")
                print(f"{Colors.CYAN}Telefone:{Colors.END} {data.get('telefone', 'N/A')}")
                print(f"{Colors.CYAN}E-mail:{Colors.END} {data.get('email', 'N/A')}")
                print(f"{Colors.CYAN}Capital Social:{Colors.END} R$ {data.get('capital_social', 'N/A')}")
            else:
                print(f"{Colors.RED}[!] {data.get('message', 'Erro na consulta')}{Colors.END}")
        else:
            print(f"{Colors.RED}[!] Erro na API (Status: {response.status_code}){Colors.END}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Erro: {e}{Colors.END}")
        print(f"{Colors.YELLOW}[i] Verifique sua conexão com a internet{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def consulta_placa():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA POR PLACA{Colors.END}")
    placa = input(f"{Colors.YELLOW}Digite a placa (ex: ABC1D23 ou ABC1234): {Colors.END}").strip().upper()
    
    padrao_mercosul = r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$'
    padrao_antigo = r'^[A-Z]{3}[0-9]{4}$'
    
    if not (re.match(padrao_mercosul, placa) or re.match(padrao_antigo, placa)):
        print(f"{Colors.RED}[!] Formato de placa inválido!{Colors.END}")
        sleep(2)
        return
    
    print(f"{Colors.GREEN}[*] Analisando placa...{Colors.END}")
    
    
    try:
        url = f"https://placafipeapi.com/placa/{placa}" 
        
        print(f"\n{Colors.YELLOW}[i] APIs recomendadas para consulta real:{Colors.END}")
        print(f"  - placafipeapi.com")
        print(f"  - apiplaca.com.br")
        print(f"  - fipeapi.com.br (tabela FIPE)")
        
        print(f"\n{Colors.CYAN}Placa: {placa}{Colors.END}")
        print(f"{Colors.CYAN}Formato: {'Mercosul' if re.match(padrao_mercosul, placa) else 'Antigo'}{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}[!] Erro: {e}{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def consulta_cep():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA POR CEP{Colors.END}")
    cep = input(f"{Colors.YELLOW}Digite o CEP (somente números): {Colors.END}").strip()
    
    if len(cep) != 8 or not cep.isdigit():
        print(f"{Colors.RED}[!] CEP inválido!{Colors.END}")
        sleep(2)
        return
    
    print(f"{Colors.GREEN}[*] Consultando ViaCEP (API gratuita)...{Colors.END}")
    
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if 'erro' not in data:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✓ DADOS ENCONTRADOS:{Colors.END}\n")
            print(f"{Colors.CYAN}CEP:{Colors.END} {data.get('cep', 'N/A')}")
            print(f"{Colors.CYAN}Logradouro:{Colors.END} {data.get('logradouro', 'N/A')}")
            print(f"{Colors.CYAN}Complemento:{Colors.END} {data.get('complemento', 'N/A')}")
            print(f"{Colors.CYAN}Bairro:{Colors.END} {data.get('bairro', 'N/A')}")
            print(f"{Colors.CYAN}Cidade:{Colors.END} {data.get('localidade', 'N/A')}")
            print(f"{Colors.CYAN}Estado:{Colors.END} {data.get('uf', 'N/A')}")
            print(f"{Colors.CYAN}IBGE:{Colors.END} {data.get('ibge', 'N/A')}")
            print(f"{Colors.CYAN}DDD:{Colors.END} {data.get('ddd', 'N/A')}")
        else:
            print(f"{Colors.RED}[!] CEP não encontrado!{Colors.END}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Erro: {e}{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def consulta_ip():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA POR IP{Colors.END}")
    ip = input(f"{Colors.YELLOW}Digite o IP (ou deixe em branco para seu IP): {Colors.END}").strip()
    
    if not ip:
        ip = 'check'  
    
    print(f"{Colors.GREEN}[*] Consultando...{Colors.END}")
    
    try:
        if ip == 'check':
            url = "https://ipapi.co/json/"
        else:
            url = f"https://ipapi.co/{ip}/json/"
        
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if 'error' not in data:
            print(f"\n{Colors.GREEN}{Colors.BOLD}✓ DADOS ENCONTRADOS:{Colors.END}\n")
            print(f"{Colors.CYAN}IP:{Colors.END} {data.get('ip', 'N/A')}")
            print(f"{Colors.CYAN}Tipo:{Colors.END} {data.get('version', 'N/A')}")
            print(f"{Colors.CYAN}Cidade:{Colors.END} {data.get('city', 'N/A')}")
            print(f"{Colors.CYAN}Região:{Colors.END} {data.get('region', 'N/A')}")
            print(f"{Colors.CYAN}País:{Colors.END} {data.get('country_name', 'N/A')} ({data.get('country', 'N/A')})")
            print(f"{Colors.CYAN}CEP:{Colors.END} {data.get('postal', 'N/A')}")
            print(f"{Colors.CYAN}Latitude:{Colors.END} {data.get('latitude', 'N/A')}")
            print(f"{Colors.CYAN}Longitude:{Colors.END} {data.get('longitude', 'N/A')}")
            print(f"{Colors.CYAN}Timezone:{Colors.END} {data.get('timezone', 'N/A')}")
            print(f"{Colors.CYAN}ISP:{Colors.END} {data.get('org', 'N/A')}")
            print(f"{Colors.CYAN}ASN:{Colors.END} {data.get('asn', 'N/A')}")
        else:
            print(f"{Colors.RED}[!] IP inválido ou não encontrado!{Colors.END}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Erro: {e}{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def consulta_bin():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA POR BIN (Cartão){Colors.END}")
    bin_num = input(f"{Colors.YELLOW}Digite os 6 primeiros dígitos do cartão: {Colors.END}").strip()
    
    if len(bin_num) != 6 or not bin_num.isdigit():
        print(f"{Colors.RED}[!] BIN inválido! Digite exatamente 6 números.{Colors.END}")
        sleep(2)
        return
    
    print(f"{Colors.GREEN}[*] Consultando...{Colors.END}")
    
    try:
        
        url = f"https://lookup.binlist.net/{bin_num}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n{Colors.GREEN}{Colors.BOLD}✓ DADOS ENCONTRADOS:{Colors.END}\n")
            print(f"{Colors.CYAN}BIN:{Colors.END} {bin_num}")
            print(f"{Colors.CYAN}Bandeira:{Colors.END} {data.get('scheme', 'N/A').upper()}")
            print(f"{Colors.CYAN}Tipo:{Colors.END} {data.get('type', 'N/A')}")
            print(f"{Colors.CYAN}Nível:{Colors.END} {data.get('brand', 'N/A')}")
            print(f"{Colors.CYAN}País:{Colors.END} {data.get('country', {}).get('name', 'N/A')}")
            print(f"{Colors.CYAN}Moeda:{Colors.END} {data.get('country', {}).get('currency', 'N/A')}")
            print(f"{Colors.CYAN}Banco:{Colors.END} {data.get('bank', {}).get('name', 'N/A')}")
        else:
            print(f"{Colors.RED}[!] BIN não encontrado ou API indisponível{Colors.END}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Erro: {e}{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def consulta_dominio():
    clear()
    print(f"{Colors.CYAN}[+] CONSULTA WHOIS/DOMÍNIO{Colors.END}")
    dominio = input(f"{Colors.YELLOW}Digite o domínio (ex: google.com): {Colors.END}").strip().lower()
    
    print(f"{Colors.GREEN}[*] Consultando...{Colors.END}")
    
    try:
        url = f"https://whoisjson.com/api/whoisjson?domain={dominio}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data.get('status') == 'success':
            whois = data.get('data', {})
            print(f"\n{Colors.GREEN}{Colors.BOLD}✓ DADOS ENCONTRADOS:{Colors.END}\n")
            print(f"{Colors.CYAN}Domínio:{Colors.END} {whois.get('domain', 'N/A')}")
            print(f"{Colors.CYAN}Registrante:{Colors.END} {whois.get('registrant_name', 'N/A')}")
            print(f"{Colors.CYAN}Organização:{Colors.END} {whois.get('registrant_organization', 'N/A')}")
            print(f"{Colors.CYAN}Criação:{Colors.END} {whois.get('created', 'N/A')}")
            print(f"{Colors.CYAN}Expiração:{Colors.END} {whois.get('expires', 'N/A')}")
            print(f"{Colors.CYAN}Registrador:{Colors.END} {whois.get('registrar', 'N/A')}")
            print(f"{Colors.CYAN}Nameservers:{Colors.END} {', '.join(whois.get('nameservers', []))}")
        else:
            print(f"{Colors.RED}[!] Domínio não encontrado ou API indisponível{Colors.END}")
            
    except Exception as e:
        print(f"{Colors.RED}[!] Erro: {e}{Colors.END}")
        print(f"{Colors.YELLOW}[i] Alternativa: use 'whois {dominio}' no terminal{Colors.END}")
    
    input(f"\n{Colors.YELLOW}Pressione ENTER para voltar...{Colors.END}")

def atualizar():
    clear()
    print(f"{Colors.GREEN}[*] Atualizando sistema...{Colors.END}")
    os.system("pkg update && pkg upgrade -y")
    os.system("pip install --upgrade requests")
    print(f"{Colors.GREEN}[✓] Sistema atualizado!{Colors.END}")
    sleep(2)

def main():
    while True:
        clear()
        banner()
        menu()
        
        opcao = input(f"{Colors.CYAN}{Colors.BOLD}[?] Escolha uma opção: {Colors.END}").strip()
        
        if opcao == '1':
            consulta_nome()
        elif opcao == '2':
            consulta_cpf()
        elif opcao == '3':
            consulta_email()
        elif opcao == '4':
            consulta_telefone()
        elif opcao == '5':
            consulta_cnpj()
        elif opcao == '6':
            consulta_placa()
        elif opcao == '7':
            consulta_cep()
        elif opcao == '8':
            consulta_ip()
        elif opcao == '9':
            consulta_bin()
        elif opcao == '10':
            consulta_dominio()
        elif opcao == '99':
            atualizar()
        elif opcao == '0':
            print(f"\n{Colors.GREEN}[+] Saindo...{Colors.END}")
            sleep(1)
            sys.exit(0)
        else:
            print(f"{Colors.RED}[!] Opção inválida!{Colors.END}")
            sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!] Interrompido pelo usuário{Colors.END}")
        sys.exit(0)
(0)
