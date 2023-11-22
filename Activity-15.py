#Q)15.	Write a Python program to create a dictionary and perform functional operations 

dic1 = {'name':'jitesh','age':23,'city':'bhubaneswar'}
print(dic1['city'])
dic1['pin'] = 754160
print(dic1)
dic1.update({'city':'cuttuck'})
print(dic1)
del dic1['age']
print(dic1)
dic1.pop('city')
print(dic1)
dic1.clear()
print(dic1)