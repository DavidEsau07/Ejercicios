def sin_vocales(text):
	vocales = ['a','A','e','E','i','I','o','O','u','U']
	res = ''
	for letter in text:
		if letter not in vocales:
			res += letter
			
	return res

x = str(input("Ingrese un texto: "))
print("Texto:", x)
print("\nTexto sin vocales: ",(sin_vocales(x)))

