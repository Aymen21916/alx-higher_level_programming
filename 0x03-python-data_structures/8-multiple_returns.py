#!/usr/bin/python3
if __name__ == '__main__':
    def multiple_returns(sentence):
        if len(sentence) == 0:
            return (len(sentence), None)
        return (len(sentence), sentence[0])