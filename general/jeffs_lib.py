'''
Reference: http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm
'''

import ast
import collections
import math
import random
from datetime import datetime
from dateutil.parser import *

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        #self.dob = parse(dob)
        
    def __dateObj(self, date_str, date_format):
        return datetime.strptime(date_str, date_format)
        
    def age(self):
        self.date_format = "%m/%d/%Y"
        date_obj_now = datetime.today()
        date_obj_then = self.__dateObj(self.dob, self.date_format)
        ageIs = date_obj_now - date_obj_then
        return str(int(ageIs.days/365))
        
'''

The Problem:
Calculate the price of a bond with a par value of $1,000 to be paid in ten
years, a coupon rate of 10%, and a required yield of 12%. In our example
we'll assume that coupon payments are made semi-annually to bond holders
and that the next coupon payment is expected in six months.

The Answer:
$885.32

Reference: http://www.investopedia.com/university/advancedbond/advancedbond2.asp
Bookmark: Pricing Zero-Coupon Bonds

'''
'''
We will assume C=$50
We will assume n=20
we will assume r=5%
We will assume M=$1,000
'''

class Bond:
    def __init__(self):
        pass
    
    def price(self, parValue, interestRate, yieldRate, ytm, periodsPerYear):
        compoundingPeriods = ytm * periodsPerYear
        coupon = self.__couponAmount(parValue, interestRate, periodsPerYear)
        pvAnnuity = self.__annuityPV(yieldRate/periodsPerYear, compoundingPeriods)
        principlePymtPV = self.__principlePV(parValue, yieldRate/periodsPerYear, compoundingPeriods)
        return coupon*pvAnnuity+principlePymtPV
        
    def __couponAmount(self, parValue, interestRate, periodsPerYear):
        c = parValue*interestRate/periodsPerYear
        return c
        
    def __annuityPV(self, interestRate, compoundingPeriods):
        return (1-(1/(1+interestRate)**compoundingPeriods))/interestRate
        
    def __principlePV(self, parValue, interestRate, compoundingPeriods):
        return parValue/(1+interestRate)**compoundingPeriods
        
'''
Odds and ends; some base classes I may use later.
'''

class StatUtilities:
    def __init__(self):
        pass
    
    def convertStrListToList(self, strList):
        return ast.literal_eval(strList)
        
    # I'm not sure this function works correctly, as correlation coefficient doesn't match Excel calculation.
    def correlationCoefficient(self, xList, yList):
        return self.coVarS(xList, yList)/self.stdDeviation(xList)*self.stdDeviation(yList)
        
    def coVarS(self, xList, yList):
        if len(xList) != len(yList):
            return
        else:
            summation = 0
            meanX = self.mean(xList)
            meanY = self.mean(yList)
            for x, y in zip(xList, yList):
                summation += (x - meanX)*(y - meanY)
                
            return summation/(len(xList)-1)
        
    def genRandStrList(self, numOfElements, rShift, percision):
        decimalScaler = 10 ** rShift
            
        s = '['
        for i in range(0, numOfElements):
            s += str(round(random.random() * decimalScaler, percision)) + ', '
            
        s = s[:-2]
        s += ']'
        
        return s
        
    def mean(self, sampleList):
        x = 0
        for datum in sampleList:
            x += datum
            
        return x/len(sampleList)
        
    def sampleVar(self, sList):
        return self.coVarS(sList, sList)
        
    def stdDeviation(self, sList):
        return math.sqrt(self.sampleVar(sList))

############################################################################DEV
##################### Raymond Hettinger Discussion: ########################DEV
#####################    Method Resolution Order ###########################DEV
############################################################################DEV
'''
This class, LoggingDict, was gleaned from:
Reference: https://rhettinger.wordpress.com/

This class has all the same capabilities as its parent, dict, but it extends
the __setitem__ method to make log entries whenever a key is updated. After
making a log entry, the method uses super() to delegate the work for actually
updating the dictionary with the key/value pair.
'''
class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Settingto %r' % (key, value))
        super().__setitem__(key, value)
        
class LoggingOD(LoggingDict, collections.OrderedDict):
    pass

############################################################################DEV
###################### End: Raymond Hettinger ##############################DEV
############################################################################DEV

class Matrices:
    def __init__(self):
        pass
     
    # Builds Rx Matrix, 3D.
    def buildRxMatrix_3D(self, deg, rotR):
        # Convert to radians
        deg *= math.pi/180
        
        # Initialize list
        rx = []
        
        # First Row
        n = []
        n.append(1)
        n.append(0)
        n.append(0)
        n.append(0)
        rx.append(n)

        # Second Row
        n = []
        n.append(0)
        n.append(math.cos(deg))
        if rotR:
            n.append(-math.sin(deg))
        else:
            n.append(math.sin(deg))
        n.append(0)
        rx.append(n)

        # Third Row
        n = []
        n.append(0)
        if rotR:
            n.append(math.sin(deg))
        else:
            n.append(-math.sin(deg))
        n.append(math.cos(deg))
        n.append(0)
        rx.append(n)

        # Fourth Row
        n = []
        n.append(0)
        n.append(0)
        n.append(0)
        n.append(1)
        rx.append(n)
        
        return rx
     
    # Builds Ry Matrix, 3D.
    def buildRyMatrix_3D(self, deg, rotR):
        # Convert to radians
        deg *= math.pi/180
        
        # Initialize list
        ry = []
        
        # First Row
        n = []
        n.append(math.cos(deg))
        n.append(0)
        if rotR:
            n.append(math.sin(deg))
        else:
            n.append(-math.sin(deg))
        n.append(0)
        ry.append(n)

        # Second Row
        n = []
        n.append(0)
        n.append(1)
        n.append(0)
        n.append(0)
        ry.append(n)

        # Third Row
        n = []
        if rotR:
            n.append(-math.sin(deg))
        else:
            n.append(math.sin(deg))
        n.append(0)
        n.append(math.cos(deg))
        n.append(0)
        ry.append(n)

        # Fourth Row
        n = []
        n.append(0)
        n.append(0)
        n.append(0)
        n.append(1)
        ry.append(n)
        
        return ry
     
    # Builds Rz Matrix, 3D.
    def buildRzMatrix_3D(self, deg, rotR):
        # Convert to radians
        deg *= math.pi/180
        
        # Initialize list
        rz = []
        
        # First Row
        n = []
        n.append(math.cos(deg))
        if rotR:
            n.append(-math.sin(deg))
        else:
            n.append(math.sin(deg))
        n.append(0)
        n.append(0)
        rz.append(n)

        # Second Row
        n = []
        if rotR:
            n.append(math.sin(deg))
        else:
            n.append(-math.sin(deg))
        n.append(math.cos(deg))
        n.append(0)
        n.append(0)
        rz.append(n)

        # Third Row
        n = []
        n.append(0)
        n.append(0)
        n.append(1)
        n.append(0)
        rz.append(n)

        # Fourth Row
        n = []
        n.append(0)
        n.append(0)
        n.append(0)
        n.append(1)
        rz.append(n)
        
        return rz
     
    # Builds an Affine Transform matrix for 2D rotations.
    def build_T_Matrix_Rot_2D(self, deg, rotR):
        # Convert to radians
        deg *= math.pi/180
        
        # Initialize lists
        x = []
        y = []
        
        # Build affine transformation matrix
        # First Row
        x.append(math.cos(deg))
        if rotR:
            x.append(math.sin(deg))
        else:
            x.append(-math.sin(deg))
        x.append(0)
        y.append(x)
        
        # Second Row
        x = []
        if rotR:
            x.append(-math.sin(deg))
        else:
            x.append(math.sin(deg))
        x.append(math.cos(deg))
        x.append(0)
        y.append(x)
        
        # Third Row
        x = []
        x.append(0)
        x.append(0)
        x.append(1)
        y.append(x)
        
        return y

    # Builds the Scale 3D Transform Matrix.
    def buildScaleTransformMatrix_3D(self, x, y, z):
        # Initialize list
        m = []
        
        # First Row
        n = []
        n.append(x)
        n.append(0)
        n.append(0)
        n.append(0)
        m.append(n)

        # Second Row
        n = []
        n.append(0)
        n.append(y)
        n.append(0)
        n.append(0)
        m.append(n)

        # Third Row
        n = []
        n.append(0)
        n.append(0)
        n.append(z)
        n.append(0)
        m.append(n)

        # Fourth Row
        n = []
        n.append(0)
        n.append(0)
        n.append(0)
        n.append(1)
        m.append(n)
        
        return m
        
    # Builds Translation 3D transformation matrix.
    def buildTranslationMatrix_3D(self, x, y, z):
        # Initialize list
        m = []
        
        # First Row
        n = []
        n.append(1)
        n.append(0)
        n.append(0)
        n.append(0)
        m.append(n)

        # Second Row
        n = []
        n.append(0)
        n.append(1)
        n.append(0)
        n.append(0)
        m.append(n)

        # Third Row
        n = []
        n.append(0)
        n.append(0)
        n.append(1)
        n.append(0)
        m.append(n)

        # Fourth Row
        n = []
        n.append(x)
        n.append(y)
        n.append(z)
        n.append(1)
        m.append(n)
        
        return m
        
    # Dev - generate a matrix with specified number of rows, columns.
    def genMatrix(self, numRows, numCols):
        matrix = []
        for i in range(numRows):
            matrix.append(self.genVector(numCols, 3, 0))
            
        return matrix
    
    # Dev - generate a vector with random numbers, specified integer and fractional parts.
    def genVector(self, size, integerPartLen, fractionalPartLen):
        vector = []
        decimalScaler = 10**integerPartLen
        for i in range(size):
            if fractionalPartLen > 0:
                vector.append(round(random.random()*decimalScaler, fractionalPartLen))
            else:
                vector.append(round(random.random()*decimalScaler))
            
        return vector
        
    # Extracts and returns a column vector of the specified column index from givin matrix.
    def __extractColumnVector(self, matrix, colIndex):
        columnVector = []
        for rowNum in range(len(matrix)):
            columnVector.append(matrix[rowNum][colIndex])
        return columnVector
        
    # Multiplies two matrices
    def multiplyMatrices(self, m1, m2):
        numOfColumns = len(m2[0])
        resultantMatrix = []
        indexCol = 0
        for rowVector in m1:
            resultantRowVector = []
            while (indexCol < numOfColumns):
                columnVector = self.__extractColumnVector(m2, indexCol)
                resultantRowVector.append(self.__sumProduct(rowVector, columnVector))
                indexCol += 1
            resultantMatrix.append(resultantRowVector)
            indexCol = 0
        return resultantMatrix
            
    # Private - internal support method for matrix multiplication.
    def __sumProduct(self, vector_1, vector_2):
        sumProd = 0
        for i in range(len(vector_1)):
            sumProd += vector_1[i] * vector_2[i]
        return sumProd
            
class PAround:
    def __init__(self):
        pass
        
    # DEV test - creating list of words from a simple string.
    def parseIt(self, string):
        return string.split()
        
    # DEV - Testing the trig function.
    # I am requiring degree input parameter because of nice integer numbers, mostly.
    def sin(self, x):
        # Convert to radians
        x *= math.pi/180
        
        return math.sin(x)
            
###############################################################################
############# Below code shows how to run this file as script. ################
###############################################################################
        
def Main():
    me = Person('Jeff', '5/23/1964')
    print(me.name + ', ' + me.age())
    
    bond = Bond()
    p = bond.price(1000, .10, .12, 10, 2)
    print(str(p))

        
if __name__ == '__main__':
    Main()