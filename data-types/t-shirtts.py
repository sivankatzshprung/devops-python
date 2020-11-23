## T-shirts with list comprehension

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for color in colors:
        for size in sizes:
            print((color,size)) 
print ("Let's create now list of tuples:")

tshirts = [(color, size) for color in colors for size in sizes]

print ("List of tuples:")
print (tshirts)
print (type(tshirts))

for tshirt in ('%s %s' %(c,s) for c in colors for s in sizes):
    print(tshirt)