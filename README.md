Nomes: Guilherme Rafael Terres (00338785) e Arthur Lopes Sauer (00333033)
Turma: A

1) Regressão Linear
    - b, w = 0
    - alpha = 0.01
    - num_iterations = 15000
    - Melhor Erro Quadrático Médio: 0.011238634987875036

    - Extra: 
    Foi aplicada a normalização Min-Max ao dataset de entrada (alegrete.csv). O intuito do procedimento é redimensionar os dados no intervalo [0, 1] (mais comum) ou [-1, 1]. Com essa finalidade, foi implementada a função min_max_normalization, que retorna o dataset normalizado. O método foi aplicado no arquivo alegrete.ipynb, na seção de Visualização de Dados. 
    A utilização desse modelo de normalização corroborou para uma diminuição significativa do erro quadrático médio (antes: 6.487160580246779, após: 0.011238634987875036). Destaca-se também que os gráficos gerados durante a execução do notebook tiveram sua escala alterada, visando garantir uma representação coerente com a normalização.

2) 1)
    1 - MNIST (Menos complexo)
    É a mais simples, pois possui somente 10 imagens de 28px por 28px, que são digítos de 0 a 9 manuscritos. Ainda por cima é monocromático o que facilita na percepção dos padrões. Possui somente 10 classes.
    
    2 - Fashion MNIST
    Bem parecido com o MNIST, porém possui imagens de roupas e acessórios, se torna um pouco mais difícil pois essas imagens possuem texturas e formas um pouco mais complexas que somente números. Também são 28px por 28px e monocromáticas.
    
    3 - Cifar10
    Contém imagens coloridas 32px por 32px. Esse aumento na resolução e cores, já torna o dataset bem mais complexo que os anteriores. Possui também 10 classes, porém essas classes possuem características bem diferentes entre si. 
    
    4- Cifar100 (Mais complexo)
    É o mais complexo, pois possui 100 classes bem variadas e todas coloridas. Com resolução 32px por 32px.

   2)
    MNIST - Maior Acuracia = 97,54%
    Estruturado da seguinte forma - 1 rede convolucional com 32 filtros e 1 max pooling e rede neural com somente uma camada com 64 neurônios.
    Em média, esse dataset possuiu uma acuracia bem alta, devido a sua simplicidade, porém teve sua menor acuracia quando nao teve rede convolucional nem maxpooling e somente uma camada de 16 neuronios.

    Fashion MNIST - Maior Acuracia = 97,57%
    Estruturado da seguinte forma -  1 rede convolucional com 32 filtros e 1 max pooling e rede neural com somente 12 neurônios.
   Da mesma forma que o MNIST, teve uma acuracia alta quando possuia pelo menos uma rede convolucional e maxpooling. E sua pior acuracia foi com 81,77%, utilizando somente uma camada de 16 neurônios.

     Cifar10 - Maior Acuracia = 57.83% - 1 rede convolucional com 32 filtros e 1 max pooling e rede neural com 4 camadas de 32 neurônios.

   Cifar100 - Maior Acuracia = 62.62% - 3 redes convolucionais com 32 filtros e 3 max poolings e rede neural com 1 camda de 64 neurôncios.
   Teve uma acuracia maior que o Cifar10, apesar de ser um dataset bem mais complexo, devido a utilização de 3 redes de convoluções e max poolings


