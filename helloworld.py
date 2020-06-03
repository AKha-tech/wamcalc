Guys = ['Ayden', 'Sohan', 'Kris', 'Sam']
Girls = ['Rish', 'Shenali', 'Banisha', 'Chhavi']
Rents = ['Dad', 'Mom']


print("".join([f'{Guys[i]} is with {Girls[i]}\n and her {Rents[0]} does not approve' for i in range(len(Guys))]))
