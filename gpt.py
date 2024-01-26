from con1 import Con
if __name__ == '__main__':
    newCon = Con("gpt-3.5-turbo", "You are a helpful assistant")
    print(newCon.textToText("describe yourself please"))
    print(newCon.textToText("recite 10 digits of PI for me, please"))
    print(newCon.textToText("Did you remember the last question i ask you?"))
