#Rakshak Adhikari
from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt


NumberofEvents=100000

Lambda=60 #parameter value

#CREATES THE DISTRIBUTION

data_initial = np.random.poisson(Lambda, NumberofEvents)
print(type(data_initial))



#WE add a gamma distributed false positive
shape=3
scale=2
false_positive = np.random.gamma(shape, scale, NumberofEvents)
false_positive=false_positive.astype(int)

print(type(false_positive))

data_initial_2=data_initial+false_positive
print(len(data_initial_2))

#We add a false negative, this depends on a count we call saturation count after which
#the number of false negatives increases
false_negative_unsaturated=np.random.gamma(3, 1, NumberofEvents)
false_negative_saturated=np.random.gamma(4, 2, NumberofEvents)
false_negative_saturated=false_negative_saturated.astype(int)
false_negative_usaturated=false_negative_unsaturated.astype(int)


data_final=[]
saturation_count=1.8*Lambda
i=0
for i in range(len(data_initial_2)):
    if data_initial_2[i]<saturation_count:
        data_final.append(data_initial_2[i]-false_negative_unsaturated[i])
    if data_initial_2[i]>saturation_count:
        data_final.append(data_initial_2[i]-false_negative_saturated[i])    
        




#WRITES THE OUTPUT IN A TEXTFILE
np.savetxt("Data_"+str(Lambda)+".txt", data_final,fmt='%u')
np.savetxt("theory_Data_"+str(Lambda)+".txt", data_initial,fmt='%u')


#PLOTS THE DISTRIBUTION

plt.hist(data_initial,alpha=0.6, bins=70,label='Theoretical data')
plt.hist(data_final,alpha=0.6, bins=70,label='Data with Errors')

plt.title('Distribution of the Count')
plt.ylabel('Occurence')
plt.xlabel('Counts in  seconds')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('Normalized_Distribution.pdf')

plt.show()


