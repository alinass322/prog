import itertools

def generate_combinations(*args):
    for combination in itertools.product(*args):
                yield combination
