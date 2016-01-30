import math
import nltk

def add_to_classification(occurrences, new_words):
    for word in new_words:
        if word in occurrences:
            occurrences[word] += 1
        else:
            occurrences[word] = 1

def compute_prob_evil(evil, good, words):
    total_evil_words = float(sum(evil.values()))
    total_good_words = float(sum(good.values()))

    ratio_evil_to_not = ((proportion_evil) / (1.0 - proportion_evil))

    for word in words:
        evil_times = evil[word] if word in evil else 1
        good_times = good[word] if word in good else 1
        ratio_evil_to_not *= (float(evil_times) / total_evil_words)
        ratio_evil_to_not /= (float(good_times) / total_good_words)

    return ratio_evil_to_not / (1 + ratio_evil_to_not)

proportion_evil = 0.3

evil_occurrences = { }
good_occurrences = { }

# Evil
for i in range(1, 7):
    tokens = nltk.word_tokenize(open('data/bad/' + str(i), 'r').read().decode('utf-8'))
    add_to_classification(evil_occurrences, tokens)

# Good
for i in range(1, 7):
    tokens = nltk.word_tokenize(open('data/good/' + str(i), 'r').read().decode('utf-8'))
    add_to_classification(good_occurrences, tokens)

# Now let's take it for a spin
for i in range(1, 9):
    tokens = nltk.word_tokenize(open('data/test/' + str(i), 'r').read().decode('utf-8'))
    print compute_prob_evil(evil_occurrences, good_occurrences, tokens)

while True:
    user_story = raw_input("Write something: ")
    tokens = nltk.word_tokenize(user_story.decode('utf-8'))
    prob = compute_prob_evil(evil_occurrences, good_occurrences, tokens)
    print prob
    if prob > 0.7:
        print "This is probably inappropriate"
    elif prob < 0.3:
        print "This is probably fine"
    else:
        print "Could be inappropriate. Who knows?"
