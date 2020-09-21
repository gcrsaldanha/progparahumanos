import random


def binary_search(array, element):
    low_index = 0
    high_index = len(array) - 1
    while low_index <= high_index:  # While pointers don't cross nor "touch"
        target_index = (low_index + high_index) // 2
        guess = array[target_index]
        print(f"Looking up array[{target_index}] = {guess}")
        if guess == element:
            return True
        elif guess > element:
            high_index = target_index - 1
        else:
            low_index = target_index + 1
    return False


if __name__ == '__main__':
    array = sorted([random.randint(0, 1000) for x in range(1000)])
    element = 900
    found = binary_search(array, element)
    if found:
        print(f'O elemento {element} foi encontrado no array!')
    else:
        print(f'O elemento {element} NÃO existe no array...')
