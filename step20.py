with open('preproinsulin-seq-clean.txt', 'r') as file:
    content = file.read()
length = len (content)
print(length)
if length == 110:
    print(True)
else: 
    print(False)