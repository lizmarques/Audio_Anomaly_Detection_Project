<h1 align="center">Detector de Anomalias por Classificação de Áudio
</h1>
<p align="center"> <img width="100px" heigth="300px" src="DeteccaodeAnomaliasporAudio/imagens/logo_sidebar.png">
</p>

## Demonstração da Ferramenta

<p align=" center"><img alt="gif"  src="DeteccaodeAnomaliasporAudio/imagens/audio_anomaly_detection_demo.gif"/></p>

## Links

- Streamlit - [Streamlit Folder](https://github.com/lizmarques/Audio_Anomaly_Detection_Project/tree/master/DeteccaodeAnomaliasporAudio)
- Google Colab Notebook - [Detecção de Anomalias por Classificação de Áudio.ipynb]([GOOGLE_COLAB]_Detecção_de_Anomalias_por_Classificação_de_Áudio.ipynb)

## Objetivo

Inserida no contexto de Smart Factories*, a ferramenta de Detecção de Anomalias por Classificação de Áudio tem como principais objetivos:
- Reduzir os custos com manutenção
- Otimizar a produção
- Diminuir interrupções não planejadas
- Aumentar a produtividade do maquinário no setor industrial

O modelo atual foi desenvolvido com foco em identificar anomalias de ventiladores industriais. No entanto, é possível aplicá-lo em diferentes tipos de maquinários como: bombas, válvulas ou até mesmo trilhos deslizantes. Para isso, basta ter os dados correspondentes.

*Smart Factories são indústrias com um alto nível de digitalização que facilitam a coleta de dados e informações por meio dos dispositivos tecnológicos

## Fonte dos dados: MIMII Dataset

O MIMII (Malfunctioning Industrial Machine Investigation and Inspection) dataset é um conjunto de dados de áudio para investigação e inspeção de máquinas industriais com defeito. Ele contém sons gerados por quatro tipos de máquinas industriais:
- Válvulas Solenóide (solenoid valves)
- Bombas de Água (water pumps)
- Ventiladores Industriais (industrial fans)
- Trilhos Deslizantes (slide rails)

O dataset possui um total de 32.157 sons no formato wave, sendo:
- 26.092 sons normais
- 6.065 sons anômalos

Cada tipo de máquina inclui vários modelos de produtos individuais e os dados de cada modelo contêm sons normais e anômalos. Para se assemelhar a um cenário da vida real, vários sons anômalos foram gravados. Além disso, o ruído de fundo gravado em várias fábricas reais foi misturado com os sons da máquina.

Os sons anômalos contidos no dataset podem ser de diferentes naturezas como:
- Contaminação
- Vazamento
- Desbalanceamento rotativo
- Danos no trilho

Todos os arquivos de áudio utilizados podem ser encontrados no site: https://zenodo.org/record/3384388#.Y3vbs3bMLrd

O artigo referente ao dataset pode ser encontrado no site: https://arxiv.org/abs/1909.09347
