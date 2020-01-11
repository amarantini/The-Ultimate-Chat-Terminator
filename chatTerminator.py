import random
import json

data = json.load(open("data.json", encoding="utf-8"))

quote = data["famous"] # a 代表前面垫话，b代表后面垫话
before = data["before"] # 在名人名言前面弄点废话
after = data['after']  # 在名人名言后面弄点废话
between = data['between'] # 代表文章主要废话来源

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
    body = ""
    while len(body) < length:
        num = random.randint(0, 100)
        if num < 10:
            body += nextQuote \
                .replace('a', random.choice(data["before"])) \
                .replace('b', random.choice(data['after']))
        else:
            body += nextBetween
        body = body.replace("x", title)

    return body



if __name__ == "__main__":
    xx = input("Please input the the chat:")
    tmp = chatGenerator(xx)
    print(tmp)

