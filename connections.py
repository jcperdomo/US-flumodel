from correlation import correl
from operator import itemgetter
import sys
#adapted from example in class

# Open the file in the "read" mode
f = open("googleflu.csv","r")

# Read in header line
h = f.readline().strip().split(",")



def hash(s,l):
    h.index(s) - 2


# Initialize 53 empty lists
s=[]
for i in range(53):
    s.append([])


# Loop over the remaining lines
for l in f:

    # Create a list by separating the line at commas
    d=l.split(",")

    # Store the 53 entries in the line to each relevant list
    for i in range(53):
        s[i].append(d[i])

# Close the file
f.close()


c = []

#Initialize 51 empty lists
for i in range(51):
    c.append([])

#Iterate over all of the lists calculating correlations 
# between each pair of states    
for i in range(2,53):
   for j in range(2,53):
        if (i != j):
            c[i - 2].append((h[j],correl(s[i],s[j])))


# Sort the lists
for i in range(51):
    t = sorted(c[i], key=itemgetter(1), reverse=True)
    
    #for now I only want the top 3 for each state
    p = t[:3] #list of 3 tuples
    for k in range(3):
        [name, r] = p[k] 
        v = h.index(name) - 2 
        p[k] = [v , r]
    c[i] = p
    
print c
