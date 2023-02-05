# Insurance-Cross-Sell

<img src="img/batida.png" width="400px" align='center'>

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
<img src="img/planejamento_solucao.gif" width="500px">
</div>
</br>
