nodes,blocks,layers= 0,int(input("Number of blocks  ")),0
while nodes < blocks: nodes,layers = (nodes+len([nodes for i in range(layers)])),(layers+1)
print(layers if nodes <=blocks else layers-1)