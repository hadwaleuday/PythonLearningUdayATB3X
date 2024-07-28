letter_list = ['a', 'c', 'e', 'd', 'i', 'o', 'f', 'u']
letter_set = {'a', 'c', 'e', 'd', 'i', 'o', 'f', 'u'}
letter_tuple = ('a', 'c', 'e', 'd', 'i', 'o', 'f', 'u')


def check_vowel(alphabets):
    vowel = ['a', 'e', 'i', 'o', 'u']
    return alphabets in vowel

vowel_letter_list = filter(check_vowel, letter_list)
vowel_letter_set = filter(check_vowel, letter_set)
vowel_letter_tuple = filter(check_vowel, letter_tuple)
print("vowel list", list(vowel_letter_list))
print("vowel set", set(vowel_letter_set))
print("vowel tuple", tuple(vowel_letter_tuple))

