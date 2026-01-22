passlen = "Arv@12345fgs"

if len(passlen) < 6:
    password ="Week"
elif len(passlen) <=10:
    password="Medium"
else:
    password = "Strong"

print("Your password strength is check here : ", password)
