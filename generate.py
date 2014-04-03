from summarize import Document, Summary
from matplotlib import pyplot as plt
from sklearn.externals import joblib
import logging
import sys
from os import path
import os

logging.basicConfig(level = logging.INFO)
machine = joblib.load("machine/machine.pkl")

folderName = sys.argv[1]

if path.isdir(sys.argv[1]):
    mainDoc = Document(folderName + '/doc.txt')
    sentences = mainDoc.compress(machine)


    with open(folderName + '/sum.txt', 'w') as f:
        for s in sentences :
            f.write(str(s) + '\n\n' )

else:
    print 'Folder not Found'
    
#mainDoc = Document(for'/doc.txt')
#sens = mainDoc.compress(machine)


#with open('nexus/sum.txt', 'w') as f:
#    for s in sens :
#        f.write(str(s) + '\n\n' )
