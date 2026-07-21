# Modelagem do TSP com Clustering para a Fase 1 (Subgrupo G1-análogo)

## Introdução

No contexto da Proposta 2 de TCC, a Fase 1 do algoritmo de duas fases, inspirada no Algoritmo de Kociemba para o Cubo Mágico, visa transformar o problema de otimização de permutação de um estado inicial para um estado que pertença a um "subgrupo" com propriedades mais gerenciáveis. Para o Problema do Caixeiro Viajante (TSP), essa transição pode ser alcançada através da aplicação de técnicas de clustering geográfico ou espacial.

## Conceito de Subgrupo G1-análogo para o TSP

No Cubo Mágico, o subgrupo G1 é caracterizado por ter todas as peças de canto e borda orientadas corretamente, e as bordas da fatia central posicionadas em sua fatia correta. Para o TSP, um estado "G1-análogo" pode ser definido como uma permutação onde as cidades são agrupadas em clusters geograficamente coesos, e a ordem de visita entre esses clusters é estabelecida, mas a ordem exata das cidades *dentro* de cada cluster ainda não está otimizada. [^1]

### Definição Formal do Estado G1-análogo:

Um estado de permutação para o TSP é considerado G1-análogo se:
1.  **Particionamento em Clusters:** O conjunto de `N` cidades é particionado em `k` clusters disjuntos `C_1, C_2, ..., C_k`.
2.  **Ordem Inter-Cluster Definida:** Existe uma ordem de visita pré-determinada ou otimizada entre os `k` clusters (e.g., `C_1 -> C_3 -> C_2 -> ... -> C_k -> C_1`).
3.  **Ordem Intra-Cluster Não Otimizada:** A ordem das cidades dentro de cada cluster `C_i` ainda não está otimizada para minimizar a distância interna ou a conexão com o próximo cluster na rota geral.

## Metodologia de Clustering para a Fase 1

Para atingir esse estado G1-análogo, a Fase 1 envolveria os seguintes passos:

1.  **Coleta de Coordenadas:** Para cada cidade no problema TSP, obter suas coordenadas geográficas (latitude, longitude).
2.  **Aplicação de Algoritmo de Clustering:** Utilizar um algoritmo de clustering (e.g., K-Means, DBSCAN, Hierarchical Clustering) para agrupar as cidades com base em sua proximidade geográfica. A escolha do algoritmo e do número de clusters (`k`) pode ser um parâmetro a ser explorado.
3.  **Definição da Ordem Inter-Cluster:** Uma vez que os clusters são formados, o problema TSP é reduzido a um TSP menor, onde cada "cidade" é agora um cluster. Algoritmos heurísticos ou exatos podem ser usados para encontrar a ordem ótima de visita entre esses `k` clusters. Isso define a estrutura de "alta ordem" da solução.
4.  **Representação do Estado Intermediário:** O estado resultante da Fase 1 seria uma permutação onde as cidades de cada cluster aparecem consecutivamente, na ordem definida pela rota inter-cluster, mas a ordem interna de cada cluster é arbitrária (ou uma permutação inicial).

### Exemplo Visual:

Imagine um mapa com 20 cidades. A Fase 1 poderia agrupá-las em 4 clusters (Norte, Sul, Leste, Oeste). A ordem inter-cluster poderia ser Norte -> Leste -> Sul -> Oeste -> Norte. O estado G1-análogo seria uma rota que visita todas as cidades do Norte, depois todas do Leste, e assim por diante, mas a sequência exata dentro de cada região ainda não está otimizada.

## Operadores de Movimento para a Fase 1

Os "movimentos" na Fase 1 seriam operações que alteram a atribuição de cidades a clusters ou a ordem dos clusters. Por exemplo:

*   **Reatribuição de Cidade:** Mover uma cidade de um cluster para outro.
*   **Troca de Ordem de Clusters:** Trocar a posição de dois clusters na rota inter-cluster.

Esses movimentos seriam guiados por uma função de custo que avalia o quão "próximo" o estado atual está do subgrupo G1-análogo, ou seja, o quão bem as cidades estão agrupadas e a rota inter-cluster está definida.

## Próximos Passos

A implementação prática envolverá a integração de bibliotecas de clustering (e.g., `scikit-learn`) e a adaptação da classe `TSPProblem` para incorporar a noção de clusters e a avaliação de custos baseada em rotas inter-cluster e intra-cluster.

## Referências

[^1]: Kociemba, H. (n.d.). *The Two-Phase Algorithm*. Retrieved from [https://kociemba.org/math/twophase.htm](https://kociemba.org/math/twophase.htm)
