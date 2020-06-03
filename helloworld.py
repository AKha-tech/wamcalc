Guys = ['Ayden', 'Sohan', 'Kris', 'Sam']
Girls = ['Rishika', 'Shenali', 'Banisha', 'Chhavi']
Rents = ['Dad', 'Mom']


print("".join(
    [f'{Guys[i]} is with {Girls[i]} and her {Rents[0]} does not approve\n' for i in range(len(Guys))]))

aydens_personality = ['annoying', 'stupid', 'beta', 'always losing']
for i in aydens_personality:
    print(f'Ayden are {i}')
