def is_prime(is_prime_input):
    count = 1
    number_of_factors = 0
    prime = False
    user_number = int(is_prime_input)
    while count < user_number:
        if user_number % count == 0:
            number_of_factors = number_of_factors+ 1
        count = count + 1
    if number_of_factors == 1:
        prime = True
        return prime
    else:
        return prime

def are_relatively_prime(relative_prime_input1,relative_prime_input2):
    user_number_1 = int(relative_prime_input1)
    user_number_2 = int(relative_prime_input2)
    count = 2
    factors = [1]
    relatively_prime = False
    while count <= user_number_1:
        if user_number_1 % count == 0:
            factors.append(count)
        count = count + 1
    count2 = 0
    common_factors = 0
    while count2 < len(factors):
        if user_number_2 % factors[count2] == 0:
            common_factors = common_factors + 1
        count2 = count2 + 1
    if common_factors == 1:
        relatively_prime = True
        return relatively_prime
    else:
        return relatively_prime

def primes(primes_input):
    user_number = int(primes_input)
    count = 1
    found_primes = []
    while count <= user_number:
        if is_prime(count) == True:
            found_primes.append(count)
        count = count + 1
    return(found_primes)

def prime_decomposition(decomposition_input):
    user_number = int(decomposition_input)
    decomposition = []
    count = 2
    while user_number > 1:
        while user_number % count == 0:
            decomposition.append(count)
            user_number = user_number // count
        count = count + 1
    return(decomposition)
