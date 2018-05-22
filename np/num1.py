import numpy as np

#a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([1,2,3,4,5,6], dtype=np.float64)

#print(np.empty_like(x))
#print(np.tile(y, (4,1)))
print(np.shape(y))
print(y.reshape((2,3)))
#print(np.sum(x))
#print(np.sum(x, axis=0))
#print(np.sum(x, axis=1))
#print(np.subtract(x, y))
#print(np.add(x, y))
#print(np.multiply(x,y))

#print(np.sqrt(x))
#print(np.dot(x,y))
'''b = np.ones((4,5))
print(b)
print(np.random.random((2,3)))
c = np.full((2,3), 8)
print(c)

print( np.eye(3))

a = np.array([[1,2,3],[2,3,4],[5,6,7]])

t = a.shape
print(t)
length = t[0]
width = t[1]
for i in range(length):
	if width>0:
		for j in range(width):
			print( a[i][j])
		print('-'*8)
	else:
		print(a[i])
'''