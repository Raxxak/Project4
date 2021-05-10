#analyzes the output from simulation
import numpy as np
import matplotlib.pyplot as plt

alpha=0.05    




#open the output files
f1 = open("Data_45.txt", "r")
f2 = open("Data_60.txt", "r")
f3 = open("theory_Data_45.txt", "r")
f4 = open("theory_Data_60.txt", "r")

a=[]
b=[]
c=[]
d=[]
for line in f1:
    a.append(int(line))
for line in f2:
    b.append(int(line))

for line in f3:
    c.append(int(line))
for line in f4:
    d.append(int(line))    


#PLOTS THE DISTRIBUTION

plt.hist(a,alpha=0.4, bins=75,label='λ=45 ,Theoretical data')
plt.hist(c,alpha=0.4, bins=75,label='λ=45 ,Data with Errors')
plt.hist(b,alpha=0.4, bins=75,label='λ=60 ,Theoretical data')
plt.hist(d,alpha=0.4, bins=75,label='λ=60 ,Data with Errors')

plt.title('Distribution of the Count')
plt.ylabel('Occurence')
plt.xlabel('Counts in  seconds')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('final_plot_Normalized_Distribution.pdf')

plt.show()

    
