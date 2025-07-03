#Exemplo 1 - fazert treinamento onde se um composto é solvem e agua o não
#a partir dodos daodos treinados identifiqe se é solvel o não
# 1 - pip install scikit-learn

from sklearn.svm import LinearSVC

composto1 = [1, 1, 1]
composto2 = [0, 0, 0]
composto3 = [1, 0, 1]
composto4 = [0, 1, 0]
composto5 = [1, 1, 0]
composto6 = [0, 0, 1]

dados_treino = [composto1, composto2, composto3, composto4, composto5, composto6]
rotulos_treino = ['S', 'N', 'S', 'N', 'S', 'S']

modelo = LinearSVC()
modelo.fit(dados_treino, rotulos_treino)

#repara que nesse teste nehum deles é igual ao compostos, pq disso que a ideia é treinar o modelo e atarves de um padrão ele encontre sozinho o resultado
teste1 = [1,0,0]
teste2 = [0,1,1]
teste3 = [1,0,1]

dados_teste = [teste1, teste2, teste3]

previsoes = modelo.predict(dados_teste)
mapeamento_previsoes = {'S': 'Soluvel', 'N': 'Não soluvel'}

print('Previsões do modelo para os composts testado: ', previsoes)

for i, previsoes in enumerate(previsoes):
    print(f'O composto {i+1} pode ser considerado {mapeamento_previsoes[previsoes]}')
