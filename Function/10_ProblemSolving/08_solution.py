# def print_kwargs(name, power):
#     print("Name ", name, " Power: ", power)


# # print_kwargs(name="shaktiman", power="lazer")

# print_kwargs( power="lazer",name="shaktiman")


def print_kwargs(**kwargs):
   for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs( power="lazer",name="shaktiman", anemy ="Dr. Kaklaal")