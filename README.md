# EasyMFA-CredentialsAWS

EasyMFA-CredentialsAWS é uma aplicação em Python que facilita o processo de autenticação temporária na AWS usando MFA (Multi-Factor Authentication). A ferramenta solicita três inputs do usuário: o ID da conta AWS, o nome do dispositivo MFA e o código MFA de 6 dígitos.

Após a verificação do código MFA, a aplicação utiliza a AWS CLI para gerar credenciais temporárias com uma validade de 8 horas, permitindo acesso seguro aos recursos da AWS.

### **Funcionalidades**

- Solicitação dinâmica do ID da conta AWS, nome do dispositivo MFA e token de 6 dígitos.
- Geração de credenciais temporárias (AWS Access Key, Secret Key e Session Token) com duração configurável.
- Facilidade para gerenciar sessões seguras na AWS via MFA.
- Verificação e validação de entradas para evitar erros durante o processo de autenticação.

### **Como usar**

1. Insira o ID da sua conta AWS (12 dígitos).
2. Digite o nome do dispositivo MFA registrado.
3. Insira o código MFA gerado pelo seu dispositivo autenticador.
4. O script retornará as credenciais temporárias, que serão definidas automaticamente como variáveis de ambiente.

### **Pré-requisitos**

Para usar o **MFAuthorizer**, você precisa garantir que os seguintes itens estejam configurados no seu ambiente:

1. **Python 3.x instalado**:
   - A aplicação é desenvolvida em Python, então você precisará de uma versão recente do Python instalada no seu sistema.
   - Verifique a instalação do Python com o comando:
     ```bash
     python --version
     ```

2. **AWS CLI instalado e configurado**:
   - O AWS CLI (Command Line Interface) é necessário para que a aplicação faça as requisições de sessão temporária com base no MFA.
   - Para instalar a AWS CLI, siga o guia oficial da AWS: [Instalação da AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
   - Após a instalação, configure suas credenciais usando:
     ```bash
     aws configure
     ```
     Certifique-se de já ter configurado suas **chaves de acesso** e **região padrão** corretamente.

3. **Dispositivo MFA configurado na sua conta AWS**:
   - É necessário ter um dispositivo MFA registrado e configurado na sua conta AWS para gerar o código MFA (6 dígitos) usado durante o processo de autenticação.
   - Para configurar um dispositivo MFA, siga as instruções fornecidas pela AWS: [Configurar MFA na AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html).
