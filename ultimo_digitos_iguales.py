# programa que identifica si los dos ultimos digitos de un numeros son iguales

print("-------------------------------")
print("-----ultimos digitos iguales---")
print("-------------------------------")

# input 

n = int(input("inserte un numero: "))

# processing

ud = n%10
pd = (n%100)//10

# output

if ud == pd:
    print("son iguales sus ultimos digitos")

else:
    print("no son iguales sus ultimos digitos")