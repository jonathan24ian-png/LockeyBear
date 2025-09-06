import io
def save_password(entity_name, password):
    entity_name=input("Enter entity saving password:")
    f = io.open(entity_name, 'w')
    f.write(entity_name)
    f.close()
    password = input ("enter your password:")
    f 1 io.open(entity_name, "a")
    f.write(entity_name)
    f.close()