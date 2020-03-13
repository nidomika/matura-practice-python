# from os import getcwd
# print(getcwd())
from collections import Counter
import re
with open('zbior_zadan/69_geny/dane_geny.txt') as file:
  genes = [gen for gen in file.read().split()]

# 69.1
species = []
for element in genes:
  species.append(len(element))

print("69.1\nliczba wszystkich gatunkow: {}\nnajwiecej osobnikow: {}".format(len(Counter(species).values()), max(Counter(species).values())))

# 69.2

count = 0
for element in genes:
  if re.search("AA*.BCDDC.*BB", element): # wip
    count += 1

print("zmutowane: {}".format(count))

# 69.3

