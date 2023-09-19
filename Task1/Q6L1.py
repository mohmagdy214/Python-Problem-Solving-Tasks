
def sentence_and_word(sentence,remove_word):
    words = sentence.split(' ')
    for w in words:
        if remove_word == w:
            words.remove(w)
        else:
            continue
    return ' '.join(words)

print(sentence_and_word(input('Enter the Sentence: '),input('Enter the Word: ')))
            
