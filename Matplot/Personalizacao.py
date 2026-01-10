import matplotlib.pyplot as plt
year = [1950, 1951, 1952, 2100]
pop = [2.538, 2.57, 2.62, 10.85]
year = year + [1800, 1850, 1900] 
pop = pop + [1.0, 1.262, 1.650]
plt.title("Word Populatrion Projetions")
plt.xlabel("Year")
plt.ylabel("Population")
plt.yticks([0, 2 ,4 ,6 ,8 ,10],
    ['0', '2B', '4B', '6B', '8B',  '10B']
)
plt.plot(year, pop)
plt.show()