import sys

def readFile(filename):
  lines = [line.rstrip('\n') for line in open(filename)]
  return lines

def findCentroids(data):
  return


trainingData = readFile(sys.argv[1]);

info = trainingData[0].split(' ')
trainingData = trainingData[1 :]
for p in trainingData: print p

dimension = int(info[0])
count_A = int(info[1])
count_B = int(info[2])
count_C = int(info[3])

data_A = trainingData[1 : count_A]
data_B = trainingData[count_A + 1 : count_B]
data_C = trainingData[count_C + 1 : count_C]