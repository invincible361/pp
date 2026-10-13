mixedlist=[-12,-10,-56,23,-2354,45,67,90,-53,23,23.555]
print("our mixed list", mixedlist)

newabs=[abs(x) for x in mixedlist]
print("after using absolute function in list comprehension ",newabs)