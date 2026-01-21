
# List in Python

# > tea_varities = ["Black","Green","Oolong","White"]
# >>> tea_varities
# ['Black', 'Green', 'Oolong', 'White']
# >>> print(tea_varities)
# ['Black', 'Green', 'Oolong', 'White']
# >>> print(tea_varities[0])
# Black
# >>> print(tea_varities[1:3])
# ['Green', 'Oolong']
# >>> print(tea_varities[:2])
# ['Black', 'Green']
# >>> tea_varities[3]="Herbal"
# >>> print(tea_varities)
# ['Black', 'Green', 'Oolong', 'Herbal']
# >>> print(tea_varities[0:])
# ['Black', 'Green', 'Oolong', 'Herbal']
# >>> print(tea_varities[1:])
# ['Green', 'Oolong', 'Herbal']
# >>> tea_varities[1:2]="Lemon"
# >>> tea_varities
# ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
# >>> tea_varities             
# ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
# >>> tea_varities = ["Black","Green","Oolong","White"]
# >>> tea_varities  
# ['Black', 'Green', 'Oolong', 'White']
# >>> tea_varities[1:2]        
# ['Green']
# >>> tea_varities[1:2]=["lemon"]
# >>> tea_varities 
# ['Black', 'lemon', 'Oolong', 'White']
# >>> tea_varities[1:3]          
# ['lemon', 'Oolong']
# >>> tea_varities[1:3]=["GreenTea","Mahsala"]
# >>> tea_varities                            
# ['Black', 'GreenTea', 'Mahsala', 'White']
# >>> tea_varities
# ['Black', 'GreenTea', 'Mahsala', 'White']
# >>> 
# >>> 
# >>> 
# >>> 
# >>> tea_varities
# ['Black', 'GreenTea', 'Mahsala', 'White']
# >>> 
# >>> 
# >>> tea_varities[1:1]
# []
# >>> tea_varities[1:1]=["test","test"]
# >>> tea_varities     
# ['Black', 'test', 'test', 'GreenTea', 'Mahsala', 'White']
# >>> tea_varities[1:3]
# ['test', 'test']
# >>> tea_varities[1:3]=[]
# >>> tea_varities
# ['Black', 'GreenTea', 'Mahsala', 'White']
# >>> tea_variteis[1:3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^
# NameError: name 'tea_variteis' is not defined. Did you mean: 'tea_varities'?
# >>> tea_varities[1:3]
# ['GreenTea', 'Mahsala']
# >>>
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> tea_varities
# ['Black', 'GreenTea', 'Mahsala', 'White']
# >>> 
# >>> 
# >>> for tea in tea_varities:
# ...     print(tea)
# ... 
# Black
# GreenTea
# Mahsala
# White
# >>>
# >>> for tea in tea_varities:
# ...     print(tea, end="-")
# ... 
# Black-GreenTea-Mahsala-White->>> 
# >>> 
# >>> if "Oolong" in tea_varities:
# ...     print("I have Oolong tea")
# ... 
# >>> tea_varities.append("Oolong")
# >>> tea_variteis
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^
# NameError: name 'tea_variteis' is not defined. Did you mean: 'tea_varities'?
# >>> tea_varities
# ['Black', 'GreenTea', 'Mahsala', 'White', 'Oolong']
# >>> if "Oolong" in tea_varities:
# ...     print("I have Oolong tea")
# ... 
# I have Oolong tea
# >>>
# >>> 
# >>> tea_varities.pop()            
# 'Oolong'
# >>> tea_varities
# ['Black', 'GreenTea', 'Mahsala', 'White']
# >>> tea_varities.remove("GreenTea")
# >>> tea_varities
# ['Black', 'Mahsala', 'White']
# >>> 
# >>> 
# >>> tea_varities.insert(1,"green")
# >>> tea_varities
# ['Black', 'green', 'Mahsala', 'White']
# >>>
# >>> 
# >>> tea_varities.copy= tea_varities.copy()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
# AttributeError: 'list' object attribute 'copy' is read-only
# >>> tea_varities_copy= tea_varities.copy()
# >>> tea_varities_copy
# ['Black', 'green', 'Mahsala', 'White']
# >>> tea_varities
# ['Black', 'green', 'Mahsala', 'White']
# >>> tea_varities_copy.append("lemon")
# >>> tea_varities 
# # Output- ['Black', 'green', 'Mahsala', 'White']
# >>> tea_varities.copy
# <built-in method copy of list object at 0x000001AABB0F7000>
# >>> tea_varities_copy
# # output- ['Black', 'green', 'Mahsala', 'White', 'lemon']
# >>>
# >>> 
# >>> 
# >>> squared_num = [x**2 for x in range(10)]
# >>> squared_num
# # output- [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# cube_num = [x**3 for x in range(6)]    
# print(cube_num)
# # output- [0, 1, 8, 27, 64, 125]