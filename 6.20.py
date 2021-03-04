def reverse(phonebook):
    new_phonebook=dict()
    for i in phonebook:
        new_phonebook.update({phonebook[i]:i})
    return new_phonebook
