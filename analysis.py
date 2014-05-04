from correlation import correl
from connections import s, hash, h
from model import res, st1, st2
from numpy import corrcoef

#calculate the indices 
CA = hash("California", h) + 2
NY = hash("New York", h) + 2


a = res[:,st1 + 102]
b = res[:,st2 + 102]

#Compare correlations between states
print "Correlation according to google flu : ",correl(s[st1 + 2],s[st2 + 2])
print "Correlation according to the model : ",corrcoef([a,b])