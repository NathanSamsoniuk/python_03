#### Exercício 1: Verificação de Qualidade de Dados
## Você está analisando um conjunto de dados de vendas e precisa garantir 
## que todos os registros tenham valores positivos para `quantidade` e `preço`. 
## Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
## forem positivos ou "Dados inválidos" caso contrário.
#
#def validar_dados(preco, quantidade):
#    """Valida se os valores de preço e quantidade são positivos."""
#    if preco > 0 and quantidade > 0:
#        return "Dados válidos"
#    else:
#        return "Dados inválidos"
#
## Repetir até que os dados sejam válidos
#while True:
#    try:
#        # Solicitando os dados do usuário
#        preco = float(input("Qual o preço? "))
#        quantidade = float(input("Qual a quantidade? "))
#
#        # Chamando a função e imprimindo o resultado
#        resultado = validar_dados(preco, quantidade)
#        print(resultado)
#        break  # Sai do loop se tudo estiver correto
#
#    except ValueError:
#        print("Erro: Por favor, insira números válidos.")
#    except Exception as e:
#        print(f"Ocorreu um erro inesperado: {e}")
#
#### Exercício 2: Classificação de Dados de Sensor
## Imagine que você está trabalhando com dados de sensores IoT. 
## Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
## como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
#
#def sensor_temperatura(temperatura):
#   """Retorna um resultado de acordo com a tempertura."""
#    if temperatura > 30:
#        return "Temperatura acima do normal"
#    elif 15 <= temperatura <= 30:
#        return "Temperatura normal"
#    else:
#        return "Temperatura abaixo do normal"
#    
## Repetir até que os dados sejam válidos
#while True:
#    try:
#        # Solicitando os dados do usuário
#        temperatura = float(input("Qual a temperatura? "))
#        resultado = sensor_temperatura(temperatura)
#        # Chamando a função e imprimindo o resultado
#        print (resultado)
#        # Sai do loop se tudo estiver correto
#        break
#    #Se der algum erro retorna as mensafens abaixo
#    except ValueError:
#        print("Erro: Por favor, insira números válidos.")
#    except Exception as e:
#        print(f"Ocorreu um erro inesperado: {e}")
#
#    
#
#### Exercício 3: Filtragem de Logs por Severidade
## Você está analisando logs de uma aplicação e precisa filtrar mensagens 
## com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
## como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
## escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
#
#def filtrar_logs(log):
#    """Filtra logs e imprime a mensagem se a severidade for 'ERROR'."""
#    try:
#        if log.get('level') == 'ERROR':
#            print(f"Mensagem de erro: {log.get('message')}")
#        else:
#            print("Nenhum erro encontrado.")
#    except Exception as e:
#        print(f"Ocorreu um erro ao processar o log: {e}")
#
## Exemplo de log
#log = {
#    'timestamp': '2021-06-23 10:00:00',
#    'level': 'ERROR',
#    'message': 'Falha na conexão'
#}
#
## Chamando a função
#filtrar_logs(log)
#
#
#### Exercício 4: Validação de Dados de Entrada
## Antes de processar os dados de usuários em um sistema de recomendação, 
## você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
## fornecido um email válido. Escreva um programa que valide essas condições 
## e imprima "Dados de usuário válidos" ou o erro específico encontrado.
#
#import re 
#
#def validacao_usuario(idade, email):
#    # Verificar se a idade está entre 18 e 65 anos e se o e-mail é válido
#    if 18 <= idade <= 65 and validar_email(email):
#        return "Dados de usuário válidos"
#    else:
#        return "Erro: Dados inválidos"
#
#def validar_email(email):
#    # Verificando se o email possui um formato válido usando expressão regular
#    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#    return re.match(email_regex, email) is not None
#
#while True:
#    try:
#        idade = float(input("Qual a sua idade? "))
#        email = input("Qual o seu email? ")
#
#        # Chamando a função de validação
#        resultado = validacao_usuario(idade, email)
#        print(resultado)
#
#        # Condição para sair do loop, quando os dados forem válidos
#        if resultado == "Dados de usuário válidos":
#            break
#
#    except ValueError:
#        print("Erro: A idade deve ser um número válido.")
#
#### Exercício 5: Detecção de Anomalias em Dados de Transações
## Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
## transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
## a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
## Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
#
#from datetime import datetime
#
## Função para verificar se a transação é suspeita
#def verificar_transacao_suspeita(valor, hora):
#    # Formatar a hora para o formato HH:MM:SS
#    hora_formatada = datetime.strptime(str(hora), '%H').strftime('%H:%M:%S')
#
#    # Verifica se o valor é superior a R$ 10.000 ou se a hora está fora do horário comercial (antes das 9h ou depois das 18h)
#    if valor > 10000 or hora < 9 or hora > 18:
#        return f"Transação suspeita - Hora: {hora_formatada}"
#    else:
#        return f"Transação normal - Hora: {hora_formatada}"
#
## Exemplo de transação
#transacao = {'valor': 12000, 'hora': 20}
#
## Chama a função e imprime o resultado
#resultado = verificar_transacao_suspeita(transacao['valor'], transacao['hora'])
#print(resultado)

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# Recebe o texto do usuário
texto = input("Digite seu texto: ")

# Converte o texto para minúsculas e divide em palavras
palavras = texto.lower().split()

# Cria um dicionário para armazenar as contagens
contagem = {}

# Conta a frequência de cada palavra
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

# Exibe a contagem de cada palavra
for palavra, quantidade in contagem.items():
    print(f'Palavra: "{palavra}" - Contagem: {quantidade}')


### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.