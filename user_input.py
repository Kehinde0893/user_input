name = input("Enter your name: ")
age = int(input("Enter your age:"))
location = input("Enter your location: ")

# first approach
print ("Hello ", name, "you are ", age, "year old and live in ", location)

#second approach %
print ("second approach")
print ("Hello %s your are %d years old and you live in %s "%(name, age, location))

