#PlagioMol -- Para edición de tabs en archivos pdb
# esto lee los archivos y separa las líneas en datos
#si quieres pasar una línea del archivo A al archivo B
with open('2hyy_flex1.pdb', 'r') as file: #XXXout.txt sería el archivo B
    # read a list of lines into data
    data_b = file.readlines()
with open('2hyy.pdb', 'r') as file: #XXXtest.txt sería el archivo A
    # read a list of lines into data
    data_a = file.readlines()  

data_b2 = data_b
indx = (1,2,3,4)
print("A continuación, se procederá con las comparaciones")

for i in range(0 , (len(data_b)-2)):
	print("Archivo B en línea", i)
	#Esto separa en elementos las líneas del archivo B
	b_splt = data_b[i].split()
	b_targ = [b_splt[x] for x in indx]
	for j in range(0 , (len(data_a))-2):
		#Esto separa en elementos las líneas del archivo A
		a_splt = data_a[j].split()
		a_targ = [a_splt[y] for y in indx]
		if a_targ == b_targ:
			print("Sí, similitud en B en ", i, " y A en ", j)
			print("Se procede a reemplazar...")
			data_b[i] = data_a[j]
			print("Listo...")
		else:
			data_b2[i] = data_b[i]

# Esto permite que se vuelva a copiar todo en el archivo B
with open('2hyy_flex1.pdb', 'w') as file: #XXXEsto vendría a ser el archivo B
	file.writelines( data_b )
print("¡¡Gracias por volar con este script!!")
