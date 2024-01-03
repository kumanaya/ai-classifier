# Image Classifier

## Descrição
Este projeto implementa um classificador de imagens. Ele usa aprendizado de máquina e processamento de imagens com TensorFlow e Keras para treinar um modelo de rede neural convolucional (CNN).

## Pré-requisitos
Antes de começar, certifique-se de que você tem Python instalado em seu sistema. Este projeto foi desenvolvido usando Python 3.11.

## Configuração do Ambiente
Siga estas etapas para configurar o ambiente de desenvolvimento:

1. Clone o repositório para o seu sistema local.
2. Navegue até a pasta do projeto e crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - Linux/MacOS:
     ```bash
     source venv/bin/activate
     ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Estrutura do Projeto
```
ai-classifier/
│
├── data/                     # Pasta para armazenar os conjuntos de dados
│   ├── train/                # Dados de treinamento
│   ├── validation/           # Dados de validação
│   └── test/                 # Dados de teste
│
├── models/                   # Modelos treinados
│   └── model.h5   # Modelo treinado
│
├── notebooks/                # Jupyter notebooks para exploração de dados
│
├── scripts/                  # Scripts de código fonte
│   ├── train.py              # Script para treinamento do modelo
│   └── evaluate.py           # Script para avaliação do modelo
│
└── README.md                 # Documentação do projeto
```

## Uso
Para treinar o modelo, execute:
```bash
python scripts/train.py
```

Para avaliar o modelo, execute:
```bash
python scripts/evaluate.py
```

## Contribuições
Contribuições são bem-vindas. Se você encontrar um bug ou tem uma sugestão, por favor, abra uma issue ou envie um pull request.

## Licença
[MIT](https://choosealicense.com/licenses/mit/)
