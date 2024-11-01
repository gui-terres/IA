Nomes: Guilherme Rafael Terres (00338785) e Arthur Lopes Sauer (00XXXXXX)
Turma: A

1) Regressão Linear
    - b, w = 0
    - alpha = 0.01
    - num_iterations = 15000
    - Melhor Erro Quadrático Médio: 0.011238634987875036

    - Extra: 
    Foi aplicada a normalização Min-Max ao dataset de entrada (alegrete.csv). O intuito do procedimento é redimensionar os dados no intervalo [0, 1] (mais comum) ou [-1, 1]. Com essa finalidade, foi implementada a função min_max_normalization, que retorna o dataset normalizado. O método foi aplicado no arquivo alegrete.ipynb, na seção de Visualização de Dados. 
    A utilização desse modelo de normalização corroborou para uma diminuição significativa do erro quadrático médio (antes: 6.487160580246779, após: 0.011238634987875036). Destaca-se também que os gráficos gerados durante a execução do notebook tiveram sua escala alterada, visando garantir uma representação coerente com a normalização.