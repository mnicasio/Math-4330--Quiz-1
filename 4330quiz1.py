def inner_prod(v1, v2):
  y = 0
  for i in range(len(v1)):
    y += v1[i] * v2[i]
  return y

def matmult3(m, v):
  'matrix multiply vector by inner production.'
  return [inner_prod(r, v) for r in m]

# These are test variables being initialized to test the function matVec. Only one of these will give a correct answer the other ones should give error due to dimensions not matching up and due to wrong type of arg being used. 
testMatrix01 = [[1,2],[3,4]]
testMatrix02 = [5, 6]
testMatrix03 = 'this is a test'

testVector01 = [1, 2]
testVector02 = [[5,6],[7,8]]
testVector03 = 3

# These are test cases for the function matVec. All but two of the tests should be commented out at a time so that we can see how each pair of inputs effects the output. 
print(matmult3(testMatrix01,testVector01))
#print(matVec(testMatrix02,testVector02))
#print(matVec(testMatrix03,testVector03))
#Added comment