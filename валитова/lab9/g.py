import itertools

def generate_combinations(*args):
    for combination in itertools.product(*args):
                yield combination
seq1 = [1, 2, 3]
seq2 = ['a', 'b', 'c', 'd']
seq3 = ('x','y')
combinations = generate_combinations(seq1,seq2, seq3)
for combo in combinations:
    print(combo)