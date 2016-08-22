'''
ANOVA - Randomized Block Design
    Note that the data must be a 'tuple of lists,' where each list must
    be of equal element count.
    
Author: up2572
'''

############################## Test Dummy Data ################################
# tupleOfLists = ([470, 530, 560, 590], [510, 540, 570, 610], [520, 550, 580, 620])
# This next dataset is on page 428 of the Devore book.
tupleOfLists = ([685,722,733,811,828],[792,806,802,888,920],[838,893,880,952,978],[875,953,941,1005,1023])
###############################################################################

# Function Definitions:
def numOfTreatments(tupleOfLists):
    return len(tupleOfLists)
    
def numOfBlocks(listOfValues):
    return len(listOfValues)

def sumRow(tupleOfLists, trmt_Num):
    theSum = 0
    for a in tupleOfLists:
        theSum += a[trmt_Num]
    return theSum
    
def sumColumn(desiredList):
    runningTotal = 0
    for listItem in range(len(desiredList)):
        runningTotal += desiredList[listItem]
    return runningTotal

def meanOfBlock(tupleOfLists, trmt_Num):
    return sumRow(tupleOfLists, trmt_Num)/numOfTreatments(tupleOfLists)
    
def meanOfTreatment(desiredList):
    return sumColumn(desiredList)/numOfBlocks(desiredList)
    
def grandMean(tupleOfLists):
    itemCounter = 0
    theSum = 0
    for tupleItem in tupleOfLists:
        for listItem in tupleItem:
            theSum += listItem
            itemCounter += 1
    return theSum/itemCounter
    
def numOfBlocksFromTuple(tupleOfLists):
    return numOfBlocks(tupleOfLists[0])

def sumOfSquaresTreatments(tupleOfLists):
    theSum = 0
    for treatment in tupleOfLists:
        theSum += (meanOfTreatment(treatment) - grandMean(tupleOfLists))**2
    return theSum * numOfBlocksFromTuple(tupleOfLists)

def sumOfSquaresBlocks(tupleOfLists):
    theSum = 0
    for block in range(len(tupleOfLists[0])):
        theSum += (meanOfBlock(tupleOfLists, block) - grandMean(tupleOfLists))**2
    return theSum * numOfTreatments(tupleOfLists)
    
def sumOfSquaresTotal(tupleOfLists):
    theSum = 0
    for treatment in tupleOfLists:
        for observation in treatment:
            theSum += (observation - grandMean(tupleOfLists))**2
    return theSum

def sumOfSquaresErrors(tupleOfLists):
    return sumOfSquaresTotal(tupleOfLists) - sumOfSquaresTreatments(tupleOfLists) - sumOfSquaresBlocks(tupleOfLists)

def meanSquareTreatment(tupleOfLists):
    return sumOfSquaresTreatments(tupleOfLists)/(numOfTreatments(tupleOfLists) - 1)
    
def numOfElements(tupleOfLists):
    count = 0
    for treatment in tupleOfLists:
        for element in treatment:
            count += 1
    return count

def meanSquareError(tupleOfLists):
    denom = numOfElements(tupleOfLists)-numOfBlocksFromTuple(tupleOfLists)-numOfTreatments(tupleOfLists)+1
    return sumOfSquaresErrors(tupleOfLists)/denom

def compute_F_Statistic(tupleOfLists):
    return meanSquareTreatment(tupleOfLists)/meanSquareError(tupleOfLists)

###############################################################################
############################### Test Code Below ###############################
########## This test code gives an example of how to use this package. ########
###############################################################################
    
print('SST: ', sumOfSquaresTreatments(tupleOfLists))
print('SSB: ', sumOfSquaresBlocks(tupleOfLists))
print('SStot: ', sumOfSquaresTotal(tupleOfLists))
print('SSE: ', sumOfSquaresErrors(tupleOfLists))
print('MST: ', meanSquareTreatment(tupleOfLists))
print('MSE: ', meanSquareError(tupleOfLists))
# compute_F_Statistic(tupleOfLists) is the only function which needs to be run.
print('F-Statistic: ', compute_F_Statistic(tupleOfLists))
