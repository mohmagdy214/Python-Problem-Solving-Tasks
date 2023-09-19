
def how_many_times_repeated(sentence,repeated_word):
    words = sentence.split(' ')
    count = 0
    for w in words:
        if repeated_word == w:
            count += 1
        else:
            continue
    return count

print(how_many_times_repeated(input('Enter your Sentence: '),input('Enter your word: ')))
    
