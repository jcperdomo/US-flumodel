#import libraries
import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from connections import c, h, hash, beta
from math import sin, pi

#recovery rate
gamma = 1.

#correlation scaling factor between populations
lmbd = .0000001

#correlation with the general population
mu = .000000000000000000002

#rate at which people become susceptible again
alpha = .1

#function to introduce seasonal variation
def svar(t):
    
    return (1. + .02 * sin(t* pi/52.) + .4 * sin(2.5* pi*t/52.) + .05 * sin(t*pi*2/52.))

#c is created in connections, includes strengths 

#function that returns the derivative of all 150 equations
def deriv(x, t):
    
    #initialize an array of 153 elements to 0
    y = np.zeros((153))
    
    #loop over first 51 elements and update S values
    for i in range(51):
        
        #update the first term
        y[i] += -x[i] * beta[i] * svar(t) * x[i + 51] + alpha * x[i + 102]
        
        #include all of the connections
        for j in range(len(c[i])):
            y[i] += - x[i] * beta[i] * svar(t) * (c[i][j][1] * lmbd) *x[c[i][j][0] + 51]
        
        #include correlation with the US as a whole
        #y[i] += -mu * sum(x[51:102])/51
            
    
    #loop over middle 50 elements and update I values
    for i in range(51,102):
        
        #change in I is equal to - change in S - change in R
        y[i] += -y[i - 51] - gamma * x[i] + alpha *x[i + 51]
    
    #loop over last 50 and update R values
    for i in range(102,153):
        
        #update recovered 
        y[i] += gamma  * x[i - 51] - alpha * x[i]
            

    #return updated array
    return y


#solve set of differential equations

#time interval of the disease
time = np.linspace(0, 300, 300) 

#initialize all of the populations
S = [100] * 51
I = [0] * 51
I[32] = 4
R = [0] * 51

#put them all together into an array
SIR = S + I + R
xinit = np.array(SIR)


#resulting values
res = odeint(deriv ,xinit ,time)

#Plot of the values
plt.figure()

#ID of New York
st1 = hash("New York",h)
#print st1

s1, = plt.plot(time, res[:,st1])
i1, = plt.plot(time, res[:,st1 + 51])
r1, = plt.plot(time, res[:,st1 + 102])

#ID of Connecticut
st2 = hash("California",h)
#print st2

s2, = plt.plot(time, res[:,st2])
i2, = plt.plot(time, res[:,st2 + 51])
r2, = plt.plot(time, res[:,st2 + 102])

plt.legend([s1, i1, r1, s2, i2, r2],["NY S", "NY I", "NY R", "CA S", "CA I", "CA R"])
plt.title("New York and California Simulation")
plt.ylabel("Number of People")
plt.xlabel("Time")

plt.show()
    









