import sys
import math

global centroid_A, centroid_B, centroid_C

def printList(list):
  for p in list: print p

def readFile(filename):
  lines = [line.rstrip('\n') for line in open(filename)]
  return lines

def distance(a, b):
  dimension = len(a)
  theSum = 0
  for i in range (0, dimension):
    theSum += abs(a[i]**2 - b[i]**2)

  return math.sqrt(theSum)

def findCentroids(data, dimension):
  theSum = []
  for k in range (0, dimension):
    theSum.append(0)

  pointCount = len(data)
  for i in range(0, pointCount):
    point = data[i].split(' ')
    for j in range (0, len(point)):
      theSum[j] = theSum[j] + float(point[j])

  centroid = []
  for a in range (0, dimension):
    centroid.append(theSum[a] / pointCount)

  return centroid

def predict_AB(point):
  distance_A = distance(centroid_A, point)
  distance_B = distance(centroid_B, point)

  if (distance_A < distance_B):
    return 'A'
  else:
    return 'B'

def predict_BC(point):
  distance_B = distance(centroid_B, point)
  distance_C = distance(centroid_C, point)

  if (distance_B < distance_C):
    return 'B'
  else:
    return 'C'

def predict_AC(point):
  distance_A = distance(centroid_A, point)
  distance_C = distance(centroid_C, point)

  if (distance_A < distance_C):
    return 'A'
  else:
    return 'C'

#~~~~~~~~~~ Main ~~~~~~~~~~#

########## training process ##########
trainingData = readFile(sys.argv[1])
info = trainingData[0].split(' ')
trainingData = trainingData[1 :]

dimension = int(info[0])
count_A = int(info[1])
count_B = int(info[2])
count_C = int(info[3])

# print count_A, count_B,count_C

data_A = trainingData[0 : count_A]
data_B = trainingData[count_A : count_A + count_B]
data_C = trainingData[count_A + count_B : count_A + count_B + count_C]

centroid_A = findCentroids(data_A, dimension)
centroid_B = findCentroids(data_B, dimension)
centroid_C = findCentroids(data_C, dimension)

########## testing process ##########
testingData = readFile(sys.argv[2])
info_test = testingData[0].split(' ')
testingData = testingData[1 :]

dimension = int(info_test[0])
count_A_test = int(info_test[1])
count_B_test = int(info_test[2])
count_C_test = int(info_test[3])

data_A_test = testingData[0 : count_A_test]
data_B_test = testingData[count_A_test : count_A_test + count_B_test]
data_C_test = testingData[count_A_test + count_B_test : count_A_test + count_B_test + count_C_test]

### test for A
TP_A = 0.0
FP_A = 0.0
FN_A = 0.0
TN_A = 0.0
for n in range(0, len(data_A_test)):
  point = list(map(lambda x: float(x), data_A_test[n].split(' ')))
  prediction_AB = predict_AB(point)
  prediction_BC = predict_BC(point)
  prediction_AC = predict_AC(point)
  if (prediction_AB == 'A' and prediction_AC == 'A'):
    TP_A += 1
  else:
    FN_A += 1

Pos_A = TP_A + FP_A
NEG_A = float(count_A_test) - Pos_A
TPR_A = TP_A / Pos_A
FPR_A = FP_A / NEG_A
ACC_A = TP_A / count_A_test
ERR_A = 1 - ACC_A
PRE_A = TP_A / (TP_A + FP_A)

### test for B
TP_B = 0.0
FP_B = 0.0
FN_B = 0.0
TN_B = 0.0
for n in range(0, len(data_B_test)):
  point = list(map(lambda x: float(x), data_B_test[n].split(' ')))
  prediction_AB = predict_AB(point)
  prediction_BC = predict_BC(point)
  prediction_AC = predict_AC(point)
  if (prediction_AB == 'B' and prediction_BC == 'B'):
    TP_B += 1
  else:
    FN_B += 1

Pos_B = TP_B + FP_B
NEG_B = float(count_B_test) - Pos_B
TPR_B = TP_B / Pos_B
FPR_B = FP_B / NEG_B
ACC_B = TP_B / count_B_test
ERR_B = 1 - ACC_B
PRE_B = TP_B / (TP_B + FP_B)

### test for C
TP_C = 0.0
FP_C = 0.0
FN_C = 0.0
TN_C = 0.0
for n in range(0, len(data_C_test)):
  point = list(map(lambda x: float(x), data_C_test[n].split(' ')))
  prediction_AB = predict_AB(point)
  prediction_BC = predict_BC(point)
  prediction_AC = predict_AC(point)
  if (prediction_AC == 'C' and prediction_BC == 'C'):
    TP_C += 1
  else:
    FN_C += 1

Pos_C = TP_C + FP_C
NEG_C = float(count_C_test) - Pos_C
TPR_C = TP_C / Pos_C
FPR_C = FP_C / NEG_C
ACC_C = TP_C / count_C_test
ERR_C = 1 - ACC_C
PRE_C = TP_C / (TP_C + FP_C)

TPR = (TPR_A + TPR_B + TPR_C) / 3
FPR = (FPR_A + FPR_B + FPR_C) / 3
ERR = (ERR_A + ERR_B + ERR_C) / 3
ACC = (ACC_A + ACC_B + ACC_C) / 3
PRE = (PRE_A + PRE_B + PRE_C) / 3

orig_stdout = sys.stdout
f = open('output.txt', 'w')
sys.stdout = f

print 'True positive rate = {}'.format(TPR)
print 'False positive rate = {}'.format(FPR)
print 'Error rate = {}'.format(ERR)
print 'Accuracy = {}'.format(ACC)
print 'Precision = {}'.format(PRE)


# print centroid_A, centroid_B, centroid_C

# printList(data_A_test)
# printList(data_B_test)
# printList(data_C_test)









