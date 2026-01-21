
#  Understanding with tuples.....

# >>> tea_types = ("Black", "Green", "Oolong")
# >>> tea_types
# ('Black', 'Green', 'Oolong')
# >>> 
# >>> tea_types[0]
# 'Black'
# >>> tea_types[2]
# 'Oolong'
# >>> 
# >>> 
# >>> tea_types[1:]
# ('Green', 'Oolong')
# >>> 
# >>> tea_types[:1]
# ('Black',)
# >>> tea_types[0]
# 'Black'
# >>> 
# >>> tea_types[0]= "lemon"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^^
# TypeError: 'tuple' object does not support item assignment
# >>>
# >>> 
# >>> print(len(tea_types))
# 3
# >>>
# >>> more_tea = ("Herbal","Earl Grey")
# >>> more_tea
# ('Herbal', 'Earl Grey')
# >>>  all_teas = tea_types + more_tea
#   File "<stdin>", line 1
#     all_teas = tea_types + more_tea
# IndentationError: unexpected indent
# >>> all_teas = more_tea + tea_types
# >>> all_teas 
# ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
# >>>
# >>> all_tea= tea_types + more_tea
# >>> all_tea
# ('Black', 'Green', 'Oolong', 'Herbal', 'Earl Grey')
# >>>
# >>> 
# >>> if "Green" in all_tea:
# ...     print("i have green tea")
# ... 
# i have green tea
# >>> 
# >>> more_tea
# ('Herbal', 'Earl Grey')
# >>> more_tea = ("Herbal", "Earl Grey","Herbal")
# >>> more_tea
# ('Herbal', 'Earl Grey', 'Herbal')
# >>>
# >>> more_tea.count("herbal")
# 0
# >>> more_tea.count("Herbal")
# 2
# >>>  
# >>> tea_types
# ('Black', 'Green', 'Oolong')
# >>> (black, green, Oolong) = tea_types
# >>> black
# 'Black'
# >>> Oolong
# 'Oolong'
# >>>
# >>> 
# >>> type(tea_types)
# <class 'tuple'>
# >>>