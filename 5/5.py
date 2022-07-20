indexes = {
           "9": "\u2079",
           "8": "\u2078",
           "7": "\u2077",
           "6": "\u2076",
           "5": "\u2075",
           "4": "\u2074",
           "3": "\u00B3",
           "2": "\u00B2",
           "1": "\u00B9",
           "0": "\u2070",
           }

with open("5/file1.txt", 'r', encoding="utf-8") as data1:
    l = data1.read()
with open("5/file2.txt", 'r', encoding="utf-8") as data2:
    k = data2.read()
l += k
o = l.split()
p = []
print(o)
for key in indexes:
    tmp = 0    
    for value in o:
         if indexes[key] in value: tmp += int(value[:-2])
    p.append(str(value)+"x" + indexes[key])    
print(p)

        
    
