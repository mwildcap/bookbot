def get_num_words(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
        file_contents = f.read()
        text = file_contents.split()
        return f"{len(text)}"

def count_letters(path_to_file):
    with open(path_to_file) as f:
        file_contents = str.lower(f.read())
        file = file_contents.lower()
        count = {}
        for letter in (file):
            if letter in count:
                count[letter] += 1
            else: 
                count[letter] = 1
        return(count)

def sorting(dictionary):
    def sort_on(dictionary):
        return dictionary["num"]
    list = []
    for dic in dictionary:
        if dic.isalpha():
            num = dictionary[dic]
            list.append({"char": dic, "num": num})
    list.sort(key=sort_on ,reverse=True)
    return list