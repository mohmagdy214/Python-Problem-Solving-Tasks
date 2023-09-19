
def repeated_words(sentence):
    right_sentence = []
    count = 0
    words = sentence.split(' ')
    for w in words:
        count += 1
            
    return count

print(repeated_words(input('Enter your Sentence: ')))
            
