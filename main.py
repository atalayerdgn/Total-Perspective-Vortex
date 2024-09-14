from headers.imports import *
#for gpt my pca is better than sklearn lol
a = pca(3)
m = skPCA(3)
x = np.random.rand(10,10)
print(x)
print ("----------------------")
h = m.fit_transform(x)
k,b,c,d = a.fit_transform(x)
print(h)
print ("----------------------")
print (d)
