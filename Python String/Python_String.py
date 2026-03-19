# Multiline strings
A = """Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
yyyyyyyyyyyyyyyyyyyyyyyy"""

print(A)

#String are Arrays
A = "heyy , Dirk"
print(A[3]) #count all the char in A starting from 0

#len() used to get lenght of the string
A = "heyy , Dirk"
print(len(A))
# in to check if a certain phrase or character is present in a string
A = "heyy , Dirk"
print("Dirk" in A) #put not in to check if a certain phrase or character is not present in a string

# Remove Whitespace
A = "   heyy , Dirk   "
print(A.strip()) # removes whitespace from the beginning or end of a string


pasta_type = "pasta"

# Update pasta type to be more specific
pasta_type = pasta_type.replace("pasta", "fusilli pasta")

ingredient_one = "BASIL"

# Standardize ingredient_one to lowercase
ingredient_one = ingredient_one.lower()

print(pasta_type)
print(ingredient_one)