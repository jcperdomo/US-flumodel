from correlation import correl
from operator import itemgetter
import sys
#adapted from example in class

# Open the file in the "read" mode
f = open("googleflu.csv","r")

# Read in header line
h = f.readline().strip().split(",")



def hash(s,l):
    return l.index(s) - 2

#print hash("California", h)
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
    
# http://www.cdc.gov/flu/fluvaxview/reports/reporti1213/reporti/index.htm
# Percentage of people vaccinated per state, used to determine infection rate
vacc = [45.7,39.7,38.3,47.0,44.2,48.3,46.5,51.3,47.4,34.1,41.1,54.3,
    37.8,43.1,42.2,50.4,40.7,46.6,47.1,50.0,53.1,57.5,40.8,52.5,40.8,46.4,41.7,50.3,39.6,48.9,
    45.3,48.1,46.6,50.1,48.9,44.8,46.1,40.1,46.2,56.7,44.8,56.7,50.8,43.7,42.9,49.6,49.4,47.5,
    48.8,40.6,39.2]

beta = []
ibeta = 58
for i in range(51):
     beta.append((vacc[i] * .01 * ibeta) ** -1)

print hash("District of Columbia",h)
