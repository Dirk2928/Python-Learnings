#Creating Variables
x = "Dirk"
y = 29
print(x)
print(y)

# Casting it is process of putting data type to the variable
x = int(29)
y = str("Dirk")

print(x)
print(y)

#type() to get the data type of the variable
x = 29
y = "Dirk"
print(type(x))
print(type(y))

#many values to multiple variables
x, y, z = "Dirk", 29, "Python"
print(x)
print(y)
print(z)

#one value to multiple variables
x = y = z = "Dirk"
print(x)    
print(y)
print(z)

#unpack a collection
CCS = ["IT", "CS"]
x,y = CCS
print(x)
print(y)