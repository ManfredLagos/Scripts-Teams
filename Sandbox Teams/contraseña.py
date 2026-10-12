import bcrypt

# Contraseña que deseas encriptar
password = 'admin1'

# Generar el hash de la contraseña con una sal segura
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Imprimir el hash generado
print(hashed_password)
