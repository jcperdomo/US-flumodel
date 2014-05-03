#this code has been taken from the lecture notes, I did not write any of it 
from math import *
from operator import itemgetter
import sys

# Function to calculate the correlation coefficient
def correl(x,y):
    n=len(x)
    if(len(x)!=len(y)):
        sys.exit("Lists must have the same length\n")

    # Set counters to zero
    sx=0
    sy=0
    sxx=0
    sxy=0
    syy=0

    # Loop over each week of the data
    for a in range(n):

        # Convert the data to floating point, and
        # skip if it's a blank entry
        xx=x[a].strip()
        yy=y[a].strip()
        if xx=='' or yy=='':
            continue
        xx=float(xx)
        yy=float(yy)

        # Add this data to the counters
        sx+=xx
        sy+=yy
        sxx+=xx*xx
        sxy+=xx*yy
        syy+=yy*yy

    # Calculate variance and covariance
    ni=1.0/n;
    sx*=ni
    sy*=ni
    varx=sxx*ni-sx*sx
    covxy=sxy*ni-sx*sy
    vary=syy*ni-sy*sy

    # Calculate correlation
    return covxy/sqrt(varx*vary)

