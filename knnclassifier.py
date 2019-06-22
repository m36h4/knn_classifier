import csv
import random
import math
import operator
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score
from pandas import *
 
#def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	
 
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((int(instance1[x]) - int(instance2[x])), 2)
	return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors
 
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	cm = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	# prepare data
	trainingSet=[]
	testSet=[]
        with open('/root/MeghaInternship/Assignment1/data/train.data', 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        trainingSet.append(dataset[x])
        with open('/root/MeghaInternship/Assignment1/data/test.data', 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	       testSet.append(dataset[x])
	print 'Train set: ' + repr(len(trainingSet))
	print 'Test set: ' + repr(len(testSet))
	# generate predictions
	predictions=[]
	k = input("Enter value of k: ") 
	print(k) 
	for x in range(len(testSet)):
		neighbors = getNeighbors(trainingSet, testSet[x], k)
		result = getResponse(neighbors)
		predictions.append(result)
		if testSet[x][-1] =='atrium_public':
			if result == 'atrium_public':
				cm[0][0] += 1
			elif result == 'general_store_outdoor':
				cm[0][1] += 1
			elif result == 'observatory_outdoor':
				cm[0][2] += 1
		if testSet[x][-1] =='general_store_outdoor':
			if result == 'atrium_public':
				cm[1][0] += 1
			elif result == 'general_store_outdoor':
				cm[1][1] += 1
			elif result == 'observatory_outdoor':
				cm[1][2] += 1
		if testSet[x][-1] =='observatory_outdoor':
			if result == 'atrium_public':
				cm[2][0] += 1
			elif result == 'general_store_outdoor':
				cm[2][1] += 1
			elif result == 'observatory_outdoor':
				cm[2][2] += 1
		#print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')
	print 'Confusion Matrix:'
	print DataFrame(cm, columns=['atrium_public', 'general_store_outdoor', 'observatory_outdoor'], index=['atrium_public', 'general_store_outdoor', 'observatory_outdoor'])
	
	
main()
