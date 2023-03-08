import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    random_lowercase = [random.choice(string.ascii_lowercase)
                        for _ in range(number_of_small_letters)]
    random_uppercase = [random.choice(string.ascii_uppercase)
                        for _ in range(number_of_capital_letters)]
    random_digits = [str(random.randint(0, 9))
                     for _ in range(number_of_digits)]
    random_chars = [random.choice(allowed_special_chars)
                    for _ in range(number_of_special_chars)]
    id = random_lowercase + random_uppercase + random_digits + random_chars
    random.shuffle(id)
    return ''.join(id)


print(generate_id())
