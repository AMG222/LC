#EJERCICIO 1
import nltk
nltk.download('cess_esp')
from nltk.corpus import cess_esp
from nltk.tag import hmm
from nltk.tag import tnt
from random import shuffle
from copy import copy
cess_sents = cess_esp.tagged_sents()
number_sentences=len(cess_sents)
nw=0
np=0
x = []
cadena = cess_sents
for item in cadena:
  aux=[]
  np+=1
  for word in item:
    palabra = word[0]
    etiqueta = word[1]
    if len(etiqueta) > 2:
      if palabra != '*0*':
        nw+=1
        if etiqueta.startswith('v') or etiqueta.startswith('F'):
          aux.append((palabra, etiqueta[:3]))
        else:
          aux.append((palabra, etiqueta[:2]))
  if len(aux)!=0:
    x.append(aux)
index=int(0.9*np)
Train = x[:index]
eval = x[index:]

#EJERCICIO 2
tagger_hmm = hmm.HiddenMarkovModelTagger.train(Train)
ej2_hmm=tagger_hmm.evaluate(eval)
print("Hmm value: ",ej2_hmm)
tagger_tnt = tnt.TnT()
tagger_tnt.train(Train)
ej2_tnt=tagger_tnt.evaluate(eval)
print("tnt value: ",ej2_tnt)

#EJERCICIO 3
ej3_hmm=[]
ej3_tnt=[]
z=0
y=1
aux = 0.0
while z<10:
  print("Haciendo la particiÃƒÂ³n:", y, "...")
  index0=int((z/10)*np)
  index1=int((y/10)*np)
  eval = x[index0:index1]
  Train = x[:index0] + x[index1:]
  tagger_hmm = hmm.HiddenMarkovModelTagger.train(Train)
  aux = tagger_hmm.evaluate(eval)
  print("aÃƒÂ±adiendo: a hmm")
  ej3_hmm.append(aux)
  tagger_tnt = tnt.TnT()
  tagger_tnt.train(Train)
  aux = tagger_tnt.evaluate(eval)
  print("aÃƒÂ±adiendo: a tnt")
  ej3_tnt.append(aux)
  z+=1
  y+=1
print("hmm value: ", ej3_hmm)
print("tnt value: ", ej3_tnt)

#EJERCICIO 4
import matplotlib.pyplot as plt
print("hmm")
plt.plot(ej3_hmm)
plt.ylabel('prestaciones')
plt.xlabel('particiones')
print("tnt")
plt.plot(ej3_tnt)
plt.ylabel('prestaciones')
plt.xlabel('particiones')

#BARAJADO

#EJERCICIO 3
ej3_hmm=[]
ej3_tnt=[]
z=0
y=1
aux = 0.0
barajado = copy(x)
barajar = shuffle(barajado)
while z<10:
  print("Haciendo la particiÃ³n:", y, "...")
  index0=int((z/10)*np)
  index1=int((y/10)*np)
  eval = barajado[index0:index1]
  Train = barajado[:index0] + x[index1:]
  tagger_hmm = hmm.HiddenMarkovModelTagger.train(Train)
  aux = tagger_hmm.evaluate(eval)
  print("aÃ±adiendo: a hmm")
  ej3_hmm.append(aux)
  tagger_tnt = tnt.TnT()
  tagger_tnt.train(Train)
  aux = tagger_tnt.evaluate(eval)
  print("aÃ±adiendo: a tnt")
  ej3_tnt.append(aux)
  z+=1
  y+=1

print("hmm value: ", ej3_hmm)
print("tnt value: ", ej3_tnt)

#EJERCICIO 4
import matplotlib.pyplot as plt
print("hmm")
plt.plot(ej3_hmm)
plt.ylabel('prestaciones')
plt.xlabel('particiones')
print("tnt")
plt.plot(ej3_tnt)
plt.ylabel('prestaciones')
plt.xlabel('particiones')