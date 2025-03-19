def generate_random_bits(count):
    import random
    return [random.randint(0, 1) for _ in range(count)]