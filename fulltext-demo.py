#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import fulltext
text=""
text=fulltext.get('Resolución 0934.pdf', None)
print(text)
text_file = open("Output2.txt", "w")
text_file.write(text.encode('utf-8'))
text_file.close()