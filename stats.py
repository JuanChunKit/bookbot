import re

def count_words(text):
    return len(text.split())

def count_characters(text):
    count = dict()
    
    text = text.lower()
    text = re.sub(r"\s+", "", text)

    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    return count

def sort_on_num( dict ):
    return dict["num"]


def sort_dic( dic ):
    sorted_list = list()
    
    for k in dic:
        sorted_list.append({"char": k, "num": dic[k]})
    
    sorted_list.sort( reverse=True, key=sort_on_num)
    return sorted_list