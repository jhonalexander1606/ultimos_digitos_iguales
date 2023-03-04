# programa que identifica si los dos ultimos digitos de un numeros son iguales

print("-------------------------------")
print("-----ultimos digitos iguales---")
print("-------------------------------")

# input 

n = int(input("inserte un numero: "))

# processing



if (n > 0):
    ud = n%10
    pd = (n%100)//10
    if (ud == pd):
        rta = "sus dos ultimos numeros son iguales"
    else:
        printrta = "sus dos ultimos numero no son iguales"

else :
    udN = -(n % 10)
    pdN = -(n % 100)//10
    if (udN == pdN):
        rta = "sus dos ultimos numeros son iguales"
    else:
        rta= " sus dos ultimos numeros no son iguales"

# output

print(str(rta))