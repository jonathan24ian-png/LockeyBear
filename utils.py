import io

def save_password(entity_name, password):
    f=io.open(entity_name + ".passwd", "w")
    print(f"File '{f}' created successfully.")
    f.write(password)
    f.close()
    print(f"Password '{password}' added successfully.")



