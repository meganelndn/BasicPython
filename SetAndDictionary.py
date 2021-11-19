import hashlib   # for hash functions

# sets (--> no duplicates, no specific order)

set1 = {"red", "blue", "white"}
set2 = {"red", "white"}
list = ["red", "yellow", "green"]
set3 = set(list) # typecasting because different type of data
set4 = set() 
print("set1 : ", set1)
print("set2 : ", set2)
print("set3 : ", set3)
print("set4 : ", set4)

set4.add("yellow")
set4.add("blue")
set4.add("yellow")
print("set4 : ", set4)

set4.add("pink")
print("set4 : ", set4)

set4.discard("pink")
print("set4 : ", set4)

try : 
    set4.remove("pink")
except Exception as ex : 
    print("Exception : ", ex) # print this if there is no pink
print()


# sets are very fast due to internal use of haching
# the letter b means a byte-list 
# hash functions are sometimes using a random salt (e.g. a time & date, also saved in login database table)

print("red md5 hash = ", hashlib.md5(b"red").hexdigest())  # b = byte-list
print("white md5 hash = ", hashlib.md5(b"white").hexdigest())  
print("cat and kitten md5 hash = ", hashlib.md5(b"cat and kitten").hexdigest()) 
print("cat and kittens md5 hash = ", hashlib.md5(b"cat and kittens").hexdigest()) 
print("red sha256 hash = ", hashlib.sha256(b"red").hexdigest())
print("white sha256 hash = ", hashlib.sha256(b"white").hexdigest()) 

# encoding user input password
mypassword = input("Enter password: ")
print("mypassword md5 hash = ", hashlib.md5(str.encode(mypassword)).hexdigest())

print()



# dictionary

dict1 = {"Jack" : 1, "Jill" : 2}
dict2 = {}
print(dict1)
print(dict2)

dict2["Hugo"] = 111
print(dict2)

dict2["Hugo"] = 222
print(dict2)

dict1["Juliet"] = 3
dict1["James"] = 4
print()

for mykey in dict1 :
    print("%-10s %d" % (mykey, dict1[mykey]))
print()
print("dict1 sorted")

for mykey in sorted(dict1) :
    print("%-10s %d" % (mykey, dict1[mykey]))
print()