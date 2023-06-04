def get_valide_post(arr,words):
    words = words.split()
    arr1 = []
    for post in arr:
        text = post.name.lower().split()
        for word in words:
            if not(word.lower() in text):
                break
        else:
            arr1.append(post)
    return arr1
# def get_valide_post(arr,words):
    # arr1 = []
    # for post in arr:
    #     if words.lower() in post.name.lower():
    #         arr1.append(post)
    #         #arr = arr.exclude(id=post.id)
    # return arr1
def split(a, n):
    l = []
    arr = []
    for i in a:
        if len(l)%8==0 and len(l)!=0:
            arr.append(l)
            l = []
        l.append(i)
    if len(l) % 8 != 0:
        arr.append(l)
    return (arr)
