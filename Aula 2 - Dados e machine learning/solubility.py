#Exemplo 2 - fazer com que verifique a r=taxa de acerto 
# No exemplo 1 prev.py criamos, treinamos o modelo mas não sabemes se esta correto

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

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

teste1 = [1,0,0]
teste2 = [0,1,1]
teste3 = [1,0,1]

dados_teste = [teste1, teste2, teste3]

#Resultado do teste anterior prev.py quanndo rodar o teste 
rotulo_teste = ['S', 'S', 'S']

previsoes = modelo.predict(dados_teste)

taxa_acerto = accuracy_score(rotulo_teste, previsoes)

print('A taxa de acerto %.2f%%' % (taxa_acerto * 100))
