# matVec takes a matrix and a vector and returns the corresponding matrix-vector multiply.
def matVec(matrix,vector):
  #these variables are used as indices for matrix and vector multiplication
  row = len(matrix)
  col = len(vector)
  #this is the empty vector where we will store our results
  x =[] 
  for i in range(row):
    y=0
    for j in range(col):
      y += matrix[i][j]*vector[j]
    x.append(y)
  return x

# These are test variables being initialized to test the function matVec. Only one of these will give a correct answer the other ones should give error due to dimensions not matching up and due to wrong type of arg being used. 
testMatrix01 = [[1,2],[3,4]]
testMatrix02 = [5, 6]
testMatrix03 = 'this is a test'

testVector01 = [1, 2]
testVector02 = [[5,6],[7,8]]
testVector03 = 3

# These are test cases for the function matVec. All but two of the tests should be commented out at a time so that we can see how each pair of inputs effects the output. 
print(matVec(testMatrix01,testVector01))
#print(matVec(testMatrix02,testVector02))
#print(matVec(testMatrix03,testVector03))
#Added comment

