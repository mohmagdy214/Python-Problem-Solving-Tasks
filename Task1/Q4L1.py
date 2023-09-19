
def sentence_without_duplicate(sentence):
    right_sentence = []
    words = sentence.split(' ')
    for p in words:
        if p not in right_sentence :
            right_sentence.append(p)
        else:
            continue
    return (' '.join(right_sentence))

print(sentence_without_duplicate(input('Enter your Sentence: ')))
