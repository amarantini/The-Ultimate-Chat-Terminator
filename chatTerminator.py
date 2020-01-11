#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import json

data = json.loads(open("data.json",mode='r').read())

quote = data["famous"] 
before = data["before"] 
after = data['after']  
between = data['between'] 

repeat = 2

def shuffleThrough(lst):
    global repeat
    pond = list(lst) * repeat
    while True:
        random.shuffle(pond)
        for element in pond:
            yield element

nextBetween = shuffleThrough(between)
nextQuote = shuffleThrough(quote)

def chatGenerator(title, length=640):
    """
    :param title: //
    :param length: length of message
    :return: response message
    """
    global nextBetween
    global nextQuote
    body = ""
    while len(body) < length:
        num = random.randint(0, 100)
        if num < 20:
            body += next(nextQuote) \
                .replace('@', random.choice(data["before"])) \
                .replace('$', random.choice(data['after']))
        else:
            body += next(nextBetween)
        body = body.replace("*", title)

    return body


    


if __name__ == "__main__":
    xx = input("Please enter the chat:")
    tmp = chatGenerator(xx)
    print(tmp)

