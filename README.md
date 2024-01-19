# Estudo de Dicionário em Python

Este é um simples script Python criado com o propósito de explorar o conceito de dicionários na linguagem. O código solicita informações básicas do usuário, como nome, idade, cidade e profissão, realiza verificações e armazena os dados em um dicionário. Além disso, ele realiza uma análise, verificando se os valores fornecidos para as chaves 'Nome', 'Cidade' e 'Profissão' são compostos apenas por letras.

## Funcionalidades:

- **Entrada de Dados**: Utiliza a função `input()` para coletar informações do usuário, incluindo nome, idade, cidade e profissão.

- **Verificação de Inteiro**: Utiliza um bloco `try...except` para verificar se a idade fornecida é um valor inteiro.

- **Limpeza do Console**: Utiliza a função `os.system('cls')` para limpar a tela do console entre as entradas de dados.

- **Armazenamento em Dicionário**: Armazena as informações do usuário em um dicionário chamado `dados_usuario`.

- **Verificação de Letras**: Itera sobre as chaves 'Nome', 'Cidade' e 'Profissão', verificando se os valores contêm apenas letras usando o método `isalpha()`.

## Como Executar:

1. Execute o script Python.
2. Forneça as informações solicitadas (nome, idade, cidade, profissão).
3. O script verificará se a idade é um valor inteiro e analisará se as chaves específicas contêm apenas letras.

## Objetivo do Código:

Este código foi desenvolvido como parte de um estudo sobre o uso de dicionários em Python. Ele serve como uma introdução prática ao armazenamento e manipulação de dados em dicionários, além de explorar a verificação de tipos de dados específicos.

---

**Observação:** Caso você tenha alguma dúvida ou queira contribuir, sinta-se à vontade para abrir uma issue ou um pull request neste repositório.
