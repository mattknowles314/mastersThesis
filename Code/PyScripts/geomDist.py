import matplotlib.pyplot as plt

def pdf(k,p,q):
    return p/(q**(k-1))

p = 0.5
q = 1-p

plt.ion

i = 0
while i<=50:
    plt.scatter(i,pdf(i,p,q),color="blue")
    plt.pause(0.01)
    i+=1