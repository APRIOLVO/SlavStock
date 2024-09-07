import csv, os, glob, pandas, numpy


def SlavStock(Bounds,Increments):
  
  for file in glob.glob(os.path.join("StockHistory",'*')): 
    excpectedValue = {}
    valueTracker = {}
    entriesPerCatergory = {}
    averageExpectedValue = {}
    matrixTracker = []
    matrixSize = 2*abs(Bounds)*Increments+1
    valuesBetweenInts = 1/Increments
    
    
    
    counter = 0
    while counter <= 2*abs(Bounds)*Increments:
      excpectedValue[-abs(Bounds)+counter*valuesBetweenInts] = 0
      counter += 1

    counter = 0
    while counter <= 2*abs(Bounds)*Increments:
      valueTracker[-abs(Bounds)+counter*valuesBetweenInts] = counter
      counter += 1
    
    for k in range(matrixSize):
      subset = [0]*(matrixSize)
      matrixTracker.append(subset)





    

    with open(file,"r") as f:
      reader = csv.reader(f)
      for index, row in enumerate(reader):
        
        
        if index == 0:
          for desiredHeader in range(len(row)):
            if row[desiredHeader] == "Close":
              desiredHeaderIndex = desiredHeader


        elif index == 1:
          previousClose = float(row[desiredHeaderIndex])
    

        elif index == 2:
          currentClose = float(row[desiredHeaderIndex])
          previousCloseChangePercentage = ((currentClose/previousClose)-1)*100
          
          if previousCloseChangePercentage > abs(Bounds):
            collumRef = Increments*abs(Bounds)
          elif previousCloseChangePercentage <= -abs(Bounds):
            collumRef = 0
          
          else:
            for key in valueTracker:
              if abs(previousCloseChangePercentage - key) <= valuesBetweenInts/2:     ##DOUBLE CHECK INCLUSIVE EXCLUSIVE
                collumRef = valueTracker[key]
                prevKey = key
            






        
        else:
          currentClose = float(row[desiredHeaderIndex])
          CurrentCloseChangePercentage = ((currentClose/previousClose)-1)*100
          if CurrentCloseChangePercentage > abs(Bounds):
            rowRef = Increments*abs(Bounds)
          elif CurrentCloseChangePercentage <= -abs(Bounds):
            rowRef = 0
          else:
            for key in valueTracker:
              if abs(CurrentCloseChangePercentage - key) <= valuesBetweenInts/2:
                rowRef = valueTracker[key]
                currentKey = key
  
          matrixTracker[rowRef][collumRef] += 1
          excpectedValue[prevKey] += (currentClose/previousClose)-1

          
          
          previousClose = currentClose
          previousCloseChangePercentage = CurrentCloseChangePercentage
          collumRef = rowRef
          prevKey = currentKey


    
    for row, key in zip(matrixTracker, valueTracker):
      entriesPerCatergory[key] = float(numpy.sum(row))

    for key in excpectedValue:
      if entriesPerCatergory[key] == 0:
        averageExpectedValue[key] = "N/A"
      else:
        averageExpectedValue[key] = excpectedValue[key]/entriesPerCatergory[key]
    
    
    print(file)
    print("\nTRANSITION MATRIX:")
    for key in valueTracker:
      print(f"{key: >5}: {matrixTracker[valueTracker[key]]}")
    print("\nAVERAGE EXPECTED VALUE")
    for key in averageExpectedValue:
      print(f"{key: >5}: {averageExpectedValue[key]}")
    print("\nEXPECTED VALUE")
    for key in excpectedValue:
      print(f"{key: >5}: {excpectedValue[key]}")
   


  

     
  

SlavStock(3,2)


#base expected value upon number of entries
#vertical titles
#from to labels
