# Trump's speeches here: https://github.com/ryanmcdermott/trump-speeches
trump = open('/home/roy/Downloads/Kaggle_Data/markovchains/speeches.txt', encoding='utf8').read()

corpus = trump.split()
# Cut it
corpus = corpus[:1000]

# Generator and yield
def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
        
pairs = make_pairs(corpus)
for w1, w2 in pairs:
    print(str(w1) + ' : ' + str(w2))

from collections import defaultdict
from collections import Counter
# Trump tweets
cnt = Counter()
for word in corpus:
    cnt[word] += 1
cnt
cnt.most_common(2)
'''
if counting and sorting single list elements, use counter
if counting dictionary keys, use defaultdict
if counting dictionary values within keys, use both
'''

# Complete Example
city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'), ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
cities_by_state = defaultdict(list) # Group cities by state
state_count = defaultdict(int) # Count state occurances
state_common = defaultdict(Counter) # Count city occurances within a state
for state, city in city_list:
    cities_by_state[state].append(city)
    state_count[state] += 1
    state_common[state][city] += 1
    
# Counter expands the dictionary count created above

c = Counter(state_count)
list(c.elements())

c.items()
c.values()

from operator import itemgetter
itemgetter(1,3,5)('ABCDEFG') 

# How to sort it   
inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
getcount = itemgetter(1) # define op to always take the element at index 1
sorted(inventory, key=getcount)
[('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]


# Sort dictionary
mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key in sorted(mydict.iterkeys()):
    print("%s: %s" % (key, mydict[key]))