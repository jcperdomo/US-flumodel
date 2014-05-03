from correlation import correl
from operator import itemgetter
import sys

# Open the file in the "read" mode
f=open("googleflu.csv","r")

# Read in header line
h=f.readline().strip().split(",")

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

# Check correlations with Massachusetts score
q=[]
for i in range(2,53):
    q.append((h[i],correl(s[i],s[1])))

# Sort the list
p=sorted(q, key=itemgetter(1), reverse=True)

# Formatted output
for j in p:
    print "%20s : %7.5f" % j