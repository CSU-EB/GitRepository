import jeffs_lib

b = jeffs_lib.Bond()
p = b.price(1000, .10, .10, 10, 2)
print(str(p))
help(b)

utils = jeffs_lib.StatUtilities()
x = utils.convertStrListToList(utils.genRandStrList(13, 5, 0))

if type(x) is list:
    print ('a list')
elif type(x) is tuple:
    print ('a tuple')
elif type(x) is str:
    print ('a string')
else:
    print ('neither a tuple or a list')

x = utils.genRandStrList(13, 5, 0)

if type(x) is list:
    print ('a list')
elif type(x) is tuple:
    print ('a tuple')
elif type(x) is str:
    print ('a string')
else:
    print ('neither a tuple or a list')

print(x)

x = utils.convertStrListToList(utils.genRandStrList(13, 5, 0))
print('The mean value is: ' + str(utils.mean(x)) + '\n\n')
xList = utils.convertStrListToList(utils.genRandStrList(13, 5, 0))
yList = utils.convertStrListToList(utils.genRandStrList(13, 5, 0))
print(xList)
print(yList)
print(utils.coVarS(xList, yList))
print('ok\n\n')

print(utils.sampleVar(xList))
print(utils.stdDeviation(xList))
print('Correlation Coefficient:')
print(utils.correlationCoefficient(xList, yList)) # I'm not sure this works.

v = jeffs_lib.Matrices()
print(v.genVector(3, 3, 0))
x = v.genMatrix(1,2)
y = v.genMatrix(2, 7)
#v.multiply(x, y)
v = jeffs_lib.PAround()
print(v.parseIt('hello there.'))