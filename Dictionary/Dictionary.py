

# learning with Dictionary .......

# >>> chai_types = {"Masala": "Spicy", "ginger": "Zesty", "Green": "Mild"}
# >>> 
# >>> chai_types
# {'Masala': 'Spicy', 'ginger': 'Zesty', 'Green': 'Mild'}
# >>> chai_types["Masala"]
# 'Spicy'
# >>> 
# >>> chai_types.get("Ginger")
# >>> 
# >>> chai_types.get("ginger")
# 'Zesty'
# >>> chai_types.get("Masala")
# 'Spicy'
# >>> chai_types.get("Zesty")
# >>> 
# >>> chai_types.get("Green")
# 'Mild'
# >>> 
# >>> chai_types
# {'Masala': 'Spicy', 'ginger': 'Zesty', 'Green': 'Mild'}
# >>> 
# >>> 
# >>> chai_types["Green"]="fresh" 
# >>> chai_types
# {'Masala': 'Spicy', 'ginger': 'Zesty', 'Green': 'fresh'}
# >>> 
# >>> 
# >>> 
# >>> for chai in chai_types:
# ...     print(chai)
# ... 
# Masala
# ginger
# Green
# >>>
# >>> for chai in chai_types:
# ...     print(chai, chai_types[chai])
# ... 
# Masala Spicy
# ginger Zesty
# Green fresh
# >>>
# >>> 
# >>> for key, value in chai_types.items():
# ...     print(key,  value)
# ... 
# Masala Spicy
# ginger Zesty
# Green fresh
# >>>
# >>> if "Masala" in chai_types:
# ...     print("I have a Masala chia")
# ... 
# I have a Masala chia
# >>>
# >>> 
# >>> print(len(chai_types))
# 3
# >>>
# >>> chai_types["Earl Grey"]="Citrus"
# >>> chai_types
# {'Masala': 'Spicy', 'ginger': 'Zesty', 'Green': 'fresh', 'Earl Grey': 'Citrus'}
# >>>
# >>> chai_types.pop("ginger")
# 'Zesty'
# >>> chai_types 
# {'Masala': 'Spicy', 'Green': 'fresh', 'Earl Grey': 'Citrus'}
# >>> chai_types.popitem()
# ('Earl Grey', 'Citrus')
# >>>
# >>> chai_types
# {'Masala': 'Spicy', 'Green': 'fresh'}
# >>>
# >>> del chai_types["Green"]
# >>> chai_types
# {'Masala': 'Spicy'}
# >>>
# >>> chai_types_copy = chai_types.copy()
# >>> cha_types
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^
# NameError: name 'cha_types' is not defined. Did you mean: 'chai_types'?
# >>> chai_types
# {'Masala': 'Spicy'}
# >>> chai_types_copy
# {'Masala': 'Spicy'}
# >>>
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> tea_shop={
# ... "chai":{"Masala":"Spicy", "Green":"Mild", "Ginger":"Zesty"},
# ... "Tea":{"Green":"Mild", "Black": "Strong"}
# ... }
# >>> tea_shop
# {'chai': {'Masala': 'Spicy', 'Green': 'Mild', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
# >>>
# >>> tea_shop["chai", "Tea"]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
# KeyError: ('chai', 'Tea')
# >>>
# >>> print(tea_shop)
# {'chai': {'Masala': 'Spicy', 'Green': 'Mild', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
# >>>
# >>> 
# >>> tea_shop["chai"]
# {'Masala': 'Spicy', 'Green': 'Mild', 'Ginger': 'Zesty'}
# >>> tea_shop["chai"]["Ginger"]
# 'Zesty'
# >>> tea_shop.get("chai", "Tea")
# {'Masala': 'Spicy', 'Green': 'Mild', 'Ginger': 'Zesty'}
# >>> tea_shop.get("[chai"], ["Tea"])
#   File "<stdin>", line 1
#     tea_shop.get("[chai"], ["Tea"])
#                         ^
# SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
# >>> tea_shop.get(["chai"], ["Tea"]) 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
# TypeError: unhashable type: 'list'
# >>>
# >>> 
# >>> sqared_num = {x:x**2 for x in reange(6) }
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform

# NameError: name 'reange' is not defined. Did you mean: 'range'?
# >>>
# >>> 
# >>> sqared_num = {x:x**2 for x in range(6) }}
#   File "<stdin>", line 1
#     sqared_num = {x:x**2 for x in range(6) }}
#                                             ^
# SyntaxError: unmatched '}'
# >>>
# >>> 
# >>> sqared_num = {x:x**2 for x in range(6) } 
# >>> 
# >>> squared_num
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#     ^^^^^^^^^^^
# NameError: name 'squared_num' is not defined. Did you mean: 'sqared_num'?
# >>> sqared_num
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# >>> sqared_num.clear()
# >>> sqared_num
# {}
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> keys = ["Masala","Ginger", "Green"]
# >>> keys
# ['Masala', 'Ginger', 'Green']
# >>>
# >>> default_value = "Delicious"
# >>> default_value
# 'Delicious'
# >>> 
# >>> 
# >>> new_dict= dict.fromKeys(keys, default_value)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     import platform
#               ^^^^^
# AttributeError: type object 'dict' has no attribute 'fromKeys'. Did you mean: 'fromkeys'?
# >>>
# >>> new_dict = dict.fromkeys(keys, default_value)
# >>> new_dict
# {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Green': 'Delicious'}
# >>>
# >>> 
# >>> default_val=["spicy","Mild", "fresh"]
# >>> default_val
# ['spicy', 'Mild', 'fresh']
# >>>
# >>> new-dictionary = dict.fromkeys(keys, default_val)
#   File "<stdin>", line 1
#     new-dictionary = dict.fromkeys(keys, default_val)
#     ^^^^^^^^^^^^^^
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
# >>> new-dictnry= dict.fromkeys(keys, default_val)    
#   File "<stdin>", line 1
#     new-dictnry= dict.fromkeys(keys, default_val)
#     ^^^^^^^^^^^
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
# >>> new_dictnry= dict.fromkeys(keys, default_val)
# >>> new_dictnry
# {'Masala': ['spicy', 'Mild', 'fresh'], 'Ginger': ['spicy', 'Mild', 'fresh'], 'Green': ['spicy', 'Mild', 'fresh']}
