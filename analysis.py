from correlation import correl
from connections import s, hash, h
from model import res, st1, st2
from numpy import corrcoef


a = res[51:,st1 + 51]
b = res[51:,st2 + 51]

#Compare correlations between states
print "Correlation according to google flu : ",correl(s[st1 + 2],s[st2 + 2])
print "Correlation according to the model : ",corrcoef([a,b])