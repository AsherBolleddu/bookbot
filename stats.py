def get_word_count(content):
    return len(content.split())

def get_num_letter_count(content):
    letter_dict = {}
    for i in content.lower():
        if i not in letter_dict:
            letter_dict[i] = content.lower().count(i)
    return letter_dict

def sort_on(dict):
    return dict["count"]

def sorted_num_letter_count(letter_dict):
    foo = []
    for item in letter_dict:
        foo.append({"char": item, "count": letter_dict[item]})
    foo.sort(key=sort_on, reverse=True)
    return foo