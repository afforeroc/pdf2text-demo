import PyPDF2

# Function
def addBreakLine(text, wordStr):
	index = 0
	while(True):
		breakInx = text.find(wordStr, index)
		print("breakInx = ", breakInx)
		if breakInx == -1:
			break
		text = text[:breakInx] + '\n\n' + text[breakInx:]
		index = breakInx + len(wordStr)
		
	return text

#write a for-loop to open many files -- leave a comment if you'd #like to learn how
filename = 'Resolución 0934.pdf' 

#open allows you to read the file
pdfFileObj = open(filename,'rb')

#The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfReader.numPages
count = 0
text = ""

# Un ciclo 'while' que lee cada página
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

print(text)

# Cortador por palabras
wordList = ['FACULTAD ', 'RESOLUCION ', '(', '"Por la cual ', 
'EL DECANO ', 'En su condición ', 'CONSIDERANDO ', 'COMUNÍQUESE Y CÚMPLASE ', 'PARAGRAFO ', 'QUE ']
for wordStr in wordList:
	breakInx = text.find(wordStr)
	print("breakInx = ", breakInx)
	text = text[:breakInx] + '\n\n' + text[breakInx:]
	text = addBreakLine(text, 'QUE')

# Salida del archivo *.txt
text_file = open("Output.txt", "w")
text_file.write(text)
text_file.close()