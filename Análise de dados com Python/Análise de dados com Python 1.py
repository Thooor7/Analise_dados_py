#!/usr/bin/env python
# coding: utf-8
Análise de Dados com Python

Desafio:
Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.

O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.

Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?
# In[4]:


import pandas as pd

# Passo 1: Importaria a base de dados
tabela = pd.read_csv("telecom_users.csv")



# Passo 2: Visualizar a base de dados
# - Entender as informações que você tem disponível
# - Descobrir as cagadas da base de dados

# axis -> 0 = linha; axis -> 1 = coluna

tabela = tabela.drop("Unnamed: 0", axis=1 )
display(tabela) 


# In[9]:


# Passo 3: Tratamento de dados
# resolver os valores que estão sendo reconhecidos de forma errada


#tabela TotalGasto, o ypo de dado deveria ser float ao invés de object

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors = "coerce")

# "errors" faz com que substitua o erro por algo. "coerce" força o dado virar outro tipo, como no caso vai transformar campo com letras em branco, já que não é número.

# resolver valores vazios // colunas em que TODOS os valores são vazios, eu vou exckuir // Linhas que tem PELO MENOS 1 VALOR VAZIO (que possuem ALGUM valor vazio)
# axis -> 0 = linha; axis -> 1 = coluna
# ".dropna()" para excluir valores vazios de acordo com as regras que vc passar. Duas informações para ele funcionar -> "how=" e "axis=". "how" significa se quer que apague todos (all) ou algumas (any)
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)



print(tabela.info())




# In[17]:


# Passo 4: Análise inicial

#Proporção das informações. Contar valores "sim/não".

#como estão nossos cancelamentos
#contando valores
print(tabela["Churn"].value_counts())

#valores em porcentagem
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# .map("{:.1%}".format) serve para formatar casa decimal da porcentagem.


# In[23]:


# Passo 5: Análise detalhada - descobrir as causas do cancelamento

# comparar cada coluna da base de dados com a coluna Churn
import plotly.express as px

#criar gráfico 

# para coluna da minha tabela, eu quero criar um gráfico //

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)

    #exibir gráfico 
    grafico.show()


# In[ ]:





# # Conclusões e Ações
- CLientes q tem famílias maiores tendem a cancelar menos
    - Promoções diferenciadas para mais péssoas da mesma família
- Os clientes nos primeiros meses tem uma tendência MUITO maiora cancelar
    - Pode ser algum marketing  agressivo
    - Pode ser q a experiência nos primeiros meses seja ruim
    - Pode fazer uma promoção de no primeiro ano ser mais barato


Clientes com contrato mensal tem MUITO mais chance de cancelar:

Podemos fazer promoções para o cliente ir para o contrato anual
Familias maiores tendem a cancelar menos do que famílias menores

Podemos fazer promoções pra pessoa pegar uma linha adicional de telefone
Meses Com Cliente baixos tem MUITO cancelamento. Clientes com pouco tempo como cliente tendem a cancelar muito

A primeira experiência do cliente na operadora pode ser ruim
Talvez a captação de clientes tá trazendo clientes desqualificados
Ideia: a gente pode criar incentivo pro cara ficar mais tempo como cliente
Quanto mais serviços o cara tem, menos chance dele cancelar

podemos fazer promoções com mais serviços pro cliente
Tem alguma coisa no nosso serviço de Fibra que tá fazendo os clientes cancelarem

Agir sobre a fibra
Clientes no boleto tem MUITO mais chance de cancelar, então temos que fazer alguma ação para eles irem para as outras formas de pagamento