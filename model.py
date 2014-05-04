#import libraries
import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from connections import c, h, hash, beta


gamma = 1.5

#c is created in connections, includes strengths 

#function that returns the derivative of all 150 equations
def deriv(x, t):
    
    #initialize an array of 153 elements to 0
    y = np.zeros((153))
    
    #loop over first 51 elements and update S values
    for i in range(51):
        
        #update the first term
        y[i] += -x[i] * beta[i] * x[i + 51]
        
        #include all of the connections
        for j in range(len(c[i])):
            y[i] += - x[i] * beta[i] * c[i][j][1] *x[c[i][j][0] + 51]
            
    
    #loop over middle 50 elements and update I values
    for i in range(51,102):
        
        #y[i] = x[i - 50] * beta[i - 51] 
        #change in I is equal to - change in S - change in R
        y[i] += -y[i - 51] - gamma * x[i]
    
    #loop over last 50 and update R values
    for i in range(102,153):
        
        #update recovered 
        y[i] += gamma  * x[i - 51]
            

    #return updated array
    return y


#solve set of differential equations

#time interval of the disease
time = np.linspace(0, 5, 500) 

#initialize all of the populations
S = [70] * 50
I = [0] * 50
I[32] = 15
R = [0] * 50

#put them all together into an array
SIR = S + I + R
xinit = np.array(SIR)


#resulting values
res = odeint(deriv ,xinit ,time)

#Plot of the values
plt.figure()

#ID of New York
st1 = 32

s1, = plt.plot(time, res[:,st1])
i1, = plt.plot(time, res[:,st1 + 50])
r1, = plt.plot(time, res[:,st1 + 100])

#ID of Connecticut
st2 = hash("Connecticut",h)

#s2, = plt.plot(time, res[:,st2])
#i2, = plt.plot(time, res[:,st2 + 50])
#r2, = plt.plot(time, res[:,st2 + 100])

#plt.legend([s1, i1, r1, s2, i2, r2],["NY S", "NY I", "NY R", "CT S", "CT I", "CT R"])
plt.legend([s1, i1, r1],["S","I","R"])
plt.ylabel("Number of People")
plt.xlabel("Time")

plt.show()
    









