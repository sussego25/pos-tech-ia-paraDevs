
# Projeto de Análise e Predição de Dengue

Este repositório contém o código, dados e instruções para executar uma análise exploratória e modelagem preditiva sobre casos de dengue, usando Python, Jupyter Notebook e bibliotecas de Machine Learning.

---

## 📂 Estrutura do Projeto

- `notebook_dengue.ipynb` — Notebook Jupyter com todo o processo de análise, pré-processamento e modelagem.
- `dados_dengue.csv` — Dataset utilizado (ou link para download).
- `Dockerfile` — Arquivo para criação de imagem Docker e execução isolada
- `requirements.txt` — Lista de dependências Python necessárias.
- `model.pkl` — Modelo treinado salvo para uso posterior.

---

## 📊 Descrição do Projeto

O objetivo é utilizar dados epidemiológicos da dengue para:
1. Realizar análise exploratória dos dados (EDA).
2. Aplicar pré-processamento (limpeza, normalização, tratamento de valores nulos).
3. Construir modelos de Machine Learning para prever casos confirmados de dengue.
4. Avaliar e comparar diferentes algoritmos, como:
   - Regressão Logística
   - Random Forest
   - Gradient Boosting
   - KNN (melhor desempenho identificado no projeto)

---

## 📥 Obtenção do Dataset

O dataset pode ser baixado do portal oficial do [Open DataSUS](https://opendatasus.saude.gov.br/gl/dataset/arboviroses-dengue).  
Dicionário de dados: [dic_dados_dengue.pdf](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/SINAN/Dengue/dic_dados_dengue.pdf)

Coloque o arquivo `dados_dengue.csv` na raiz do projeto antes de rodar o notebook.

---

## 🛠️ Configuração do Ambiente

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```


### 2️⃣ Instalar Dependências
Se for executar localmente:
```bash
pip install -r requirements.txt
```

Se for executar via Docker:
```bash
docker build -t dengue_project .
docker run --rm -it -p 8888:8888 dengue_project
```

---

## 📦  `requirements.txt`

```txt
pandas
numpy
matplotlib
seaborn
scikit-learn
scipy
imbalanced-learn
jupyter
scikit-learn==1.3.2 imbalanced-learn
```

---

## 🚀 Execução

### 1️⃣ Rodando no Jupyter Notebook
```bash
jupyter notebook
```
Abra o arquivo `notebook_dengue.ipynb` e execute as células em ordem.

---

## 📊 Resultados

- Modelos treinados e comparados usando métricas de acurácia, precisão, recall e F1-score.
- Melhor desempenho identificado com **KNN**.
- Oversampling com **SMOTE** foi aplicado para lidar com desbalanceamento de classes.

---

## 🧪 Reproduzindo Experimentos

1. Baixar o dataset oficial.
2. Colocar `dados_dengue.csv` na pasta do projeto.
3. Instalar dependências (`pip install -r requirements.txt`).
4. Executar `notebook_dengue.ipynb` para gerar gráficos e métricas.
5. Salvar modelo com `pickle`.

---

## 📜 Licença

Este projeto é de uso acadêmico e livre para estudos. A base de dados é pública e proveniente do portal DataSUS.

---
## ▶️ youtube
**Link:** https://www.youtube.com/watch?v=vioUfTKtetk

---

✍️ **Autor:** Caio Moreira e Lucas Farailde   
📅 **Última atualização:** 2025
