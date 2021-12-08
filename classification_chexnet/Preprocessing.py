import os
from os.path import dirname
import random

dataset_pathway = dirname(__file__) + "/dataset/"

trainf = open(dataset_pathway+'train_1.txt','r+')
trainf.truncate(0)
testf = open(dataset_pathway+'test_1.txt','r+')
testf.truncate(0)
valf = open(dataset_pathway+'val_1.txt','r+')
valf.truncate(0)

pool1 = []
pool2 = []

for i in range(500):
    pool1.append(i+1)
    pool2.append(i+1)

random.shuffle(pool1)
random.shuffle(pool2)

normal_train = pool1[:300]
normal_test = pool1[300:400]
normal_val = pool1[400:]

tuber_train = pool2[:300]
tuber_test = pool1[300:400]
tuber_val = pool1[400:]

for i in normal_train:
    trainf.read()
    trainf.write('Normal-'+str(i)+'.png 1 0\n')

for i in tuber_train:
    trainf.read()
    trainf.write('Tuberculosis-' + str(i) + '.png 0 1\n')

for i in normal_test:
    testf.read()
    testf.write('Normal-'+str(i)+'.png 1 0\n')

for i in tuber_test:
    testf.read()
    testf.write('Tuberculosis-'+str(i)+'.png 0 1\n')

for i in normal_val:
    valf.read()
    valf.write('Normal-' + str(i) + '.png 1 0\n')

for i in tuber_val:
    valf.read()
    valf.write('Tuberculosis-' + str(i) + '.png 0 1\n')