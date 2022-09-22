def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence


def main():
    sentence = input()
    sentence = convert(sentence)
    print(sentence, end="")


main()
