import sys

def readFile(filename):
  lines = [line.rstrip('\n') for line in open(filename)]
  return lines

def findCentroids(data):
  return

def printList(list):
  for p in list: print p

#~~~~~~~~~~ Main ~~~~~~~~~~#
trainingData = readFile(sys.argv[1]);

info = trainingData[0].split(' ')
trainingData = trainingData[1 :]

dimension = int(info[0])
count_A = int(info[1])
count_B = int(info[2])
count_C = int(info[3])

print count_A, count_B,count_C

data_A = trainingData[0 : count_A]
data_B = trainingData[count_A : count_A + count_B]
data_C = trainingData[count_A + count_B : count_A + count_B + count_C]

# printList(data_A)
# printList(data_B)
# printList(data_C)