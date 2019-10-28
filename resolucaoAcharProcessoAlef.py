import nltk
import pandas as pd
import re
#le o arquivo do.txt para o python
dfDo = pd.read_fwf('D:\Python\do.txt',header=None,encoding='utf_8')
dfDo
#remove todos os \n (quebra de linha em unix/macOSX)
dfDo=dfDo.replace('\n','')
#remove todos os \r (quebra de linha em MacOS antes do X
dfDo=dfDo.replace('\r','')
dfDo
#transforma o dataframe em series
seriesDo=dfDo.iloc[:,0]
seriesDo
#transforma a series em uma unica string de texto
texto=seriesDo.str.cat()
texto
#utilizo regex com o padrao de numero do processo, que foi dado no exercicio, para encontrar todos os numeros de processos.
processos=re.findall('\d{7}-\d{2}.\d{4}.\d{1}.\d{2}.\d{4}',texto)
len(processos)
processos
#identifica todos os processos unicos do texto
processosUnicos=set(processos)
#tamanho do dataframe
len(processosUnicos)
processosUnicos
