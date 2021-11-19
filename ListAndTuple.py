# list
# to add items to a list, we use the append function

listoftext = ["one", "two", "three"]
listofnumbers = [1, 2, 3]
listmixed = listoftext + listofnumbers 
listempty = []
print(listoftext)
print(listofnumbers)
print(listmixed)
print(listempty)
print(listmixed[2:4]) # gets index 2 and 3
print(listmixed[-2]) # [-1] = last item, [-2] = second to last item, [0] = first item
print(listempty)
print()

listoftext.append("four")
print(listoftext)

listoftext.insert(1, "oneandahalf")
print(listoftext)

del listoftext[4] # del(ete) = stand-alone command
print(listoftext)

print("Removed:", listoftext.pop(0)) 
print(listoftext)

for i in range(len(listoftext)) : # identation and : instead of curly brackets for FOR LOOP
    if i > 0 :
        print(" | ", end = "") # condition
    print(listoftext[i], end = "") # end = "" means NO NEW line 
print()
print()


# tuple
# a list that uses parentheses

GRADES = (-3, 0, 2, 4, 7, 10, 12)
print(GRADES)
print()