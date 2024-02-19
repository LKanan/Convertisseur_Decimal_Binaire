nombre_dec = int(input("Saisissez le nombre => "))
val_binaire = []
if nombre_dec == 0:
    print("La valeur binaire est ", 0)
else:
    while nombre_dec > 0:
        val_binaire.append(nombre_dec%2)
        nombre_dec = int(nombre_dec/2)
    print("La valeur binaire est ", str(val_binaire[::-1]).replace("[","").replace("]","").replace(", ",""))