import rki
import matplotlib.pylab as plt

dates, cases = rki.get_cases_last7days()

for i in range(1, len(dates)):
    change_date = dates[i]
    delta = cases[i]-cases[i-1]
    if delta<0:
        print (f"Rückgang am {change_date}")
    
    if delta>0:
        print (f"Anstieg am {change_date}")
    

dates, cases_berlin = rki.get_cases_last7days("Berlin")

alphas = []
for i in range(len(dates)):
    change_date = dates[i]
    alphas.append(cases_berlin[i]/cases[i])

plt.figure()
plt.plot(dates, alphas)
plt.show()