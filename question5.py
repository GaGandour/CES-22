# recognize palyndromes
def is_palyndromes(word:str):
    size = len(word)
    for i in range(int(size/2)):
        if word[i] != word[size-i-1]:
            return False

    return True
