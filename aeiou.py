a = "The Zen of Python, by Tim Peters\n\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!"
c = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

def print_aeiou():
    for j in range(0,len(a)):
        if(a[j] == 'a' or a[j] == 'A'):
            c['a'] += 1
        if(a[j] == 'e' or a[j] == 'E'):
            c['e'] += 1
        if(a[j] == 'i' or a[j] == 'I'):
            c['i'] += 1
        if(a[j] == 'o' or a[j] == 'O'):
            c['o'] += 1     
        if(a[j] == 'u' or a[j] == 'U'):
            c['u'] += 1
            
    for data in c:
        print(data, ':', c[data])