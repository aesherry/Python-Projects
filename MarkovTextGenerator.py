# coding: utf-8

# Name: Ava Sherry
# Date: 11/10/17
# Problem 3: Markov Text Generation

def createDictionary(filename):
    """ input: .txt file 
    output: dictionary (keys: first words of sentences in .txt file, 
    values: list of words written directly after key throughout 
    .txt file)"""
    f = open(filename)
    text = f.read()
    f.close()

    d = {}
    pw = '$'
    LoW = text.split()

    for nw in LoW:
        if pw[-1] in '.?!':
            pw = '$'
        if pw not in d:
            d[pw] = [nw]
        else: 
            d[pw] += [nw]
        pw = nw
    return d


def generateText(filename,N):
    """input: .txt file, integer number of words
    output: string N words long in phrase styling of .txt file"""
    import random
    d=createDictionary(filename)
    first_word = random.choice(d['$'])
    text = first_word
    
    for i in range (N-1):
        if first_word not in d:
            second_word = random.choice(d['$'])
        else:
            second_word = random.choice(d[first_word])
        text += " " + second_word
        first_word = second_word
    return text
        
       