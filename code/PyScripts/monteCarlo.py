import random
import numpy as np
import matplotlib.pyplot as plt

#Define mean and standard deviation parameters
means = [1.5298,1.6541,3.1493]
sds = [0.4486,0.3355,1.1349]

#Define other parameters
n = 20
overs = 50
state = 1

runrates = []

#Function for gaining the monte-carlo estimate

def MCE(n,state):
    t = 0 if (state<=10) else 1 if (state>10 and state<=35) else 2
    return(np.mean([random.normalvariate(means[t],sds[t]) for x in range(1,n)]))

#Perform Monte-Carlo Simmulation
while state <= overs:
    runrates.append(np.mean(MCE(n,state)))
    state+=1

plt.plot(runrates)
plt.xlabel("Over")
plt.ylabel("Runrate")
plt.title(str("Monte-Carlo Runrate Simmulation with n="+str(n)))
plt.show()