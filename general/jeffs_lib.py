'''
Reference: http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm
'''

import ast
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

class NumericUtilities:
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
        
    
        
###############################################################################
        
def Main():
    me = Person('Jeff', '5/23/1964')
    print(me.name + ', ' + me.age())
    
    bond = Bond()
    p = bond.price(1000, .10, .12, 10, 2)
    print(str(p))

        
if __name__ == '__main__':
    Main()