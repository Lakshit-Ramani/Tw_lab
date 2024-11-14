def dot_product(a_vector,b_vector):
    #a1 x b1 + a2 * b2..an*bn return scalar
    return sum([an*bn for an,bn in zip(a_vector,b_vector)])

X = [2,3,5,7,11]
Y = [13,17,19,23,29]
print(dot_product(X,Y)) #652

a=[1,2,3]
b=[4,5,6]
print(dot_product(a,b)) #prints 32= 1*4 + 2*5 + 3*6 = 
a = [1, 2, 3]
b = [7, 8, 9]

z=dot_product(a,b)
print(z) #prints 50 



