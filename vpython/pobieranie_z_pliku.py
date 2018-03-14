import os

def pobierz_dane(plik):
	dane = []
	if os.path.isfile(plik):
		with open(plik,"r") as zawartosc:
			for linia in zawartosc:
				linia = linia.replace("\n","") # usuwamy znaki konca lini 
				linia = linia.replace("\r","")
				dane.append(tuple(linia.split(",")))
	else :
		print ("PLik z danymi  nie istnieje" )
			
	return tuple(dane)
	
#test = pobierz_dane('export.csv')
#for  i in test:
#	print (i)