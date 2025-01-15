def single_root_words(root_word: str, *other_words: str):
    same_words = []
    for word in other_words:
        if word.lower() in root_word.lower() or root_word.lower() in word.lower():
            same_words.append(word)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies', 'gjjkjkk', 'iytrichot'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel', 'ement'))
