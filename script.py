import requests as req
import pandas as pd

aminos = pd.read_json(dataPath + '/aminoacid.json')
proteinsList = pd.read_csv(dataPath + '/hetero_2-mer.csv')
proteinsList = proteinsList.iloc[:,0].to_list()

def extractSCIM(col, row):
  querySCIM = (aminos['SCIM'].where(aminos['Codigo1'] == row)).dropna()
  querySCIM = querySCIM[querySCIM.index[0]][col]
  return querySCIM

def extractHydro(col, row):
  queryHydro = (aminos['Hidrofobia'].where(aminos['Codigo1'] == row)).dropna()
  queryHydro = queryHydro[queryHydro.index[0]][col]
  return queryHydro

def proteinSeqHydrophobe():
  proteinsIndex = dataset.values.tolist()
  count = 0
  for protein in proteinsIndex:
    matrix = []
    for i in protein:
      vector = []
      for j in protein:
        if i == '-' or j == '-':
          vector.append(0)
        else:
          vector.append(extractHydro(i,j))
      matrix.append(vector)  
    matrixHydrophobe = pd.DataFrame(matrix) 
    matrixHydrophobe.to_csv(r'{}/hydro/hydroMatrix-{}.csv'.format(dataPath,str(count)), index = False) 
    print(count)
    count += 1

def proteinSeqSCIM():
  proteinsIndex = dataset.values.tolist()
  count = 0
  for protein in proteinsIndex:
    matrix = []
    for i in protein:
      vector = []
      for j in protein:
        if i == '-' or j == '-':
          vector.append(0)
        else:
          vector.append(extractSCIM(i,j))
      matrix.append(vector)  
    matrixSCIM = pd.DataFrame(matrix) 
    matrixSCIM.to_csv(r'{}/SCIM/SCIM-{}.csv'.format(dataPath,str(count)), index = False) 
    print(count)
    count += 1
    
proteinSeqHydrophobe()
proteinSeqSCIM()
