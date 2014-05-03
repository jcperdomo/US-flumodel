#import libraries
import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import odeint
from connections import c, h, hash


beta = [.02] * 50
gamma = 1

#c is created in connections, includes strengths 

#function that returns the derivative of all 150 equations
def deriv(x, t):
    
    #initialize an array of 150 elements to 0
    y = np.zeros((150))
    
    #loop over first 50 elements and update S values
    for i in range(50):
        
        #update the first term
        y[i] += -x[i] * beta[i] * x[i + 50]
        
        #include all of the connections
        for j in range(len(c[i])):
            y[i] += - x[i] * beta[i] * c[i][j][1] *x[c[i][j][0] + 50]
            
    
    #loop over last 50 and update R values
    for i in range(100,150):
        
        #update recovered 
        y[i] += gamma  * y[i - 50]
            
    #loop over middle 50 elements and update I values
    for i in range(50,100):
        
        #change in I is equal to - change in S - change in R
        y[i] += -y[i - 50] - y[i + 50]
    
    #return updated array
    return y


#solve set of differential equations

#time interval of the disease
time = np.linspace(0, 1.2, 100) 

S = [90] * 50
I = [0] * 50
I[30] = 3
R = [0] * 50

SIR = S + I + R
#initial values
xinit = np.array(SIR)


#resulting values
res = odeint(deriv ,xinit ,time)

#Plot of the values
plt.figure()

#for i in range(50):
#    plt.plot(time, res[:,i])
plt.plot(time, res[:,i])
plt.plot(time, res[:,i + 50])
plt.plot(time, res[:,i + 100])

plt.show()
    









