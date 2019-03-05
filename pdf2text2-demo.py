import PyPDF2

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

# Salida del archivo *.txt
text_file = open("Output.txt", "w")
text_file.write(text)
text_file.close()