import numpy as np
import random as rm

class markovChain(object):
	def __init__(self, states, probStates,days,startPos):

		checkAux = 1
		if(len(states)==len(probStates)):
			for i in range(len(probStates)):
				if(len(probStates[i])!=len(states)):
					checkAux = 0
		else:
			checkAux = 0
		if checkAux == 1 :
			print "Dados ok!"
			self.states = states;
			self.probStates = probStates;
			self.setTranNames(self.states);
			self.Run(days,startPos)
		else:
			print "Ha algo de errado com o formato dos dados"

	def setTranNames(self,states):
		self.tranName = []
		auxArray = []
		for i in range(len(states)):
			aux = states[i][0];
			for j in range(len(states)):
				aux = aux + states[j][0]
				auxArray.append(aux);
				aux = aux[0]
			self.tranName.append(auxArray);
			auxArray = []
		print self.tranName;

	def Run(self,days,start):
		self.activity=[]
		if(start==None):
			start = rm.randint(0,len(states)-1)
		else:
			checkAux = 0
			i = 0
			while i < len(states) and checkAux == 0:
				if(states[i]==start):
					print "Encontrado!"
					checkAux = 1
					start = i
			if checkAux == 0:
				print "Estado nao encontrado"
		prob = 1
		print "Comecando por: " + str(states[start])
		self.activity.append(states[start])
		for i in range(days-1):
			change = np.random.choice(self.tranName[start],replace=True,p=self.probStates[start])
			nextStart = self.tranName[start].index(change)
			prob = prob*transitionMatrix[start][nextStart]
			start = nextStart
			self.activity.append(states[start])
		print "Estados visitados: " + str(self.activity)
		print "Estado final: " + str(states[start])
		print "Probabilidade da sequencia: " + str(prob)

states = ["Sleep","Icecream","Run"]

transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]
a = markovChain(states,transitionMatrix,3,None)