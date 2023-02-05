# Insurance-Cross-Sell

# Problema de Negócio
  
<img src="img/batida.png" width="300px" align='right'>

<p align = 'left'>
  
A All Insurance é uma empresa fictícia que oferece serviços de seguro de saúde a seus clientes há mais de 10 anos em todo o mundo. Buscando ampliar seu espectro de atuação, a empresa deseja agora oferecer à sua base de clientes um **seguro de automóveis.** 

Para isso, foi realizada uma pesquisa com aproximadamente 381 mil clientes à fim de entender quais apresentavam interesse ou não em adquirir o novo seguro e então armazenou essas informações em um banco de dados. Agora, a empresa possui uma base de 127 mil novos clientes aos quais deseja ofertar o novo seguro.

<br>
  
<img src="img/sales team.jpg" width="300px" align='left'>
  
<p align = 'right'>
  
O plano é alocar parte do time de vendas para **contactar esses clientes via telefone** ofertando o seguro. Dado a número de vendedores e ao orçamento destinado ao projeto, a equipe tem a capacidade de realizar até 20 mil ligações para a base de potenciais clientes.

Com essa restrição de projeto, a All Insurance gostaria de **atingir o maior número possível de interessados** no seguro dentro do limite de ligações possíveis.

<br>
  
Para isso, ela contratou um time de cientistas de dados para que estes pudessem acionar os melhores clientes dentre a base potencial para o oferecimento do seguro.
  
<br>

# Estratégia de Solução

Tendo como base a pesquisa de interesse realizada pela empresa à respeito do novo seguro, que reuniu diversos dados dos potenciais clientes, o modelo proposto neste projeto será capaz de **calcular a probabilidade (score) de um determinado indivíduo aderir um seguro ou não** 

Por exemplo, entre um cliente A com probabilidade de aderir ao seguro de 20% , outro cliente B com probabilidade de 70%, o **time de vendas deveria optar por acionar primeiramente o cliente B**. Com a probabilidade de aderência do seguro de todos os clientes da base potencial calculada, é possível ordenar a lista pela probabilidade, da maior para a menor, e acionar primeiramente os clientes com maior probabilidade, aumentando assim a conversão da operação.

A imagem a seguir procura ilustrar esse processo:
 
<div align="center">
<img src="img/Apresentação-Health-Insuranse.gif" width="700px">
</div>
</br>

 # Planejamento da Solução

Em uma visão geral, o processo de solução deste problema foi elaborado da seguinte forma

1. Primeiro os dados da pesquisa de interesse realizado pela empresa foram dividos em duas parcelas, uma com 80% dos dados e outra com 20%. Esses dados utilizados para treinar e avaliar o algoritmo em um processo de cross validation, treinando-se o algortmo com a parcela maior e avaliando suas métricas com a menor
2. Após essa avaliação é feita a escolha do algoritmo a ser utilizado no projeto 
3. Com o modelo escolhido e os hiperparametros ajustados, a base de novos clientes e aplicada ao modelo para a obtenção das probabilidades e o ordenamento da lista para o time de vendas
4. Assumindo que as bases sejam homogênas, podemos generalizar as métricas obtidas na validação do modelo para a nova base de clientes, mensurando-se assim a performance da operação com essa nova base

Esse processo pode ser ilustrado pela imagem a seguir:
  
<div align="center">
<img src="img/planejamento_solucao.gif" width="700px">
</div>
</br>

# Desenvolvimento

## 1. Coleta de Dados

Foi realizada uma consulta no banco de dados para coletar os dados referentes à pesquisa feita pela empresa com sua base de potenciais clientes.

O banco possui 3 tabelas com informações dos clientes, veículos e seguros, respectivamente. Foi feito o cruzamento dessas 3 tabelas pela chave única existente, sendo o resultado desse cruzamento a fonte principal dos estudos desse projeto

<img src="img/tables.jpg" width="300px" align='left'>
