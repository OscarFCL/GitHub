palabrasDiferentesTxt = []
diccionario = {}
textoEtiquetado = {}
palabrasEtiquetadas = 0
with open('SEL.txt','r') as l:
	for linea in l:
		diccionario.update({linea.split("	")[0] : linea.split("	")[2]})

with open('WebScraping/opiniones.txt','r') as f:
	for linea in f:
		for palabra in linea.split():
			if (palabra not in palabrasDiferentesTxt):
				palabrasDiferentesTxt.append(palabra)
				if (diccionario.get(palabra) != None):
					palabrasEtiquetadas += 1
					#print (palabra)
				textoEtiquetado.update({palabra : diccionario.get(palabra)})

#print ("Palabras diferentes =", len(palabrasDiferentesTxt))
#print (palabrasDiferentesTxt)
#print (diccionario.get('xd'))
print ("Se etiquetaron",palabrasEtiquetadas,"palabras de", len(palabrasDiferentesTxt),"palabras diferentes encontradas en el texto")
#print (textoEtiquetado)