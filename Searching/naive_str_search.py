text = input()
patt = input()
def search(patt, text): 
    len_patt = len(patt) 
    len_text = len(text)  
    for i in range(len_text - len_patt + 1): 
        j = 0 
        while(j < len_patt): 
            if (text[i + j] != patt[j]): 
                break
            j += 1
        if (j == len_patt):  
            print("Pattern found at index ", i) 
search(patt, text) 