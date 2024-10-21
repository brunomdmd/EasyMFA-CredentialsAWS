import subprocess
import json
import os

def get_aws_details():
    account_id = input("Informe o ID da conta AWS (12 dígitos): ")
    if len(account_id) == 12 and account_id.isdigit():
        mfa_name = input("Informe o nome do MFA (Ex.: arn:aws:iam::123456789009:mfa/'NOME-DO-MFA') - CASE SENSITIVE): ")
        return account_id, mfa_name
    else:
        print("ID da conta inválido. Tente novamente.")
        return get_aws_details()

def get_mfa_token():
    token = input("Informe seu código MFA (6 dígitos): ")
    if len(token) == 6 and token.isdigit():
        return token
    else:
        print("Token inválido. Tente novamente.")
        return get_mfa_token()

def get_profile():
    profile = input("Informe o nome do profile definido no arquivo 'credencials' (deixe em branco para usar o 'default'): ")
    if profile.strip() == "":
        profile = 'default'
        return profile
    else:
        return profile

def get_aws_session_token(account_id, mfa_name, mfa_token, profile):
    arn_mfa = f"arn:aws:iam::{account_id}:mfa/{mfa_name}"
    
    command = [
        "aws", "sts", "get-session-token",
        "--serial-number", arn_mfa,
        "--token-code", mfa_token,
        "--profile", profile,
        "--duration-seconds", "28800"
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        return json.loads(result.stdout)
    else:
        print("Erro ao executar o comando AWS CLI:", result.stderr)
        return None

def set_aws_credentials(credentials):
    os.environ['AWS_ACCESS_KEY_ID'] = credentials['AccessKeyId']
    os.environ['AWS_SECRET_ACCESS_KEY'] = credentials['SecretAccessKey']
    os.environ['AWS_SESSION_TOKEN'] = credentials['SessionToken']

    print("------------------------------------------------")

    print("Credenciais AWS definidas com sucesso! Expira em 8 horas!")

def main():
    account_id, mfa_name = get_aws_details()

    mfa_token = get_mfa_token()

    profile = get_profile()

    response = get_aws_session_token(account_id, mfa_name, mfa_token, profile)

    if response and "Credentials" in response:
        credentials = response["Credentials"]
        set_aws_credentials(credentials)
    else:
        print("Ops, algo deu errado! Valide as informações!")

if __name__ == "__main__":
    main()
