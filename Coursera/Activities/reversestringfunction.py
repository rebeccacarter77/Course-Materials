stringss=input("Please enter words: ")

def reverso(a):
    list=a.split()
    list.reverse()
    answer=" ".join(list)
    print(answer)

reverso(stringss)
