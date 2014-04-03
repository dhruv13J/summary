from summarize import Document, Summary
from matplotlib import pyplot as plt
from sklearn.externals import joblib

import logging

logging.basicConfig(level = logging.INFO)

mainDoc = Document('train/doc.txt')
#summDoc = Summary('train/abs.txt', mainDoc)


for s in mainDoc.sentences():
    print s
    print '\n\n\n'


#machine = mainDoc.trainMachine(summDoc)
#joblib.dump(machine,"machine/machine.pkl")



