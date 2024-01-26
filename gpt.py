from con1 import Con

# mode_available_now："gpt-3.5-turbo"，
if __name__ == '__main__':
    newCon = Con("dall-e-2", "You are a helpful assistant")
    print(newCon.textToImage("a little black cat",1))
