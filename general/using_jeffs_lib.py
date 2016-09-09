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

# Testing Matix Multiplication
v = jeffs_lib.Matrices()
m1 = [[6,7,33,28], [23,9,23,9],[65,28,11,3]]
m2 = [[87,65,7,5,4,3,2,9,3], [7,6,4,3,9,4,33,44,2],[5,6,7,8,2,33,2,11,13],[7,6,54,3,8,9,4,3,22]]
m = v.multiplyMatrices(m1, m2)
print('This is what happens when you multiply two matrices:')
print(m)

v = jeffs_lib.PAround()

print('\n')
print('Sin 0:')
print(v.sin(0))
print('\n')

print('Sin pi/6:')
print(v.sin(30))
print('\n')

print('Sin pi/4:')
print(v.sin(45))
print('\n')

print('Sin pi/3:')
print(v.sin(60))
print('\n')

print('Sin pi/2:')
print(v.sin(90))
print('\n')

v = jeffs_lib.Matrices()
print(v.build_T_Matrix_Rot_2D(90, True))
print(v.build_T_Matrix_Rot_2D(90, False))

print(v.buildScaleTransformMatrix_3D(5,5,5))
print(v.buildTranslationMatrix_3D(5,5,5))

print(v.buildRxMatrix_3D(45, True))
print(v.buildRyMatrix_3D(45, True))
print(v.buildRzMatrix_3D(45, True))
# help(v)
