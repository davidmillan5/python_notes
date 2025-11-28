def strength(password):
    if len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        print("Strong Password")
    else:
        print("Weak Password")


strength('0ijiqor0UHQKF')