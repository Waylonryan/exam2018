def get_value(name):
    let_value = {}
    let_value["a"] = 1
    let_value["A"] = 1
    let_value["b"] = 2
    let_value["B"] = 2
    let_value["c"] = 3
    let_value["C"] = 3
    let_value["d"] = 4
    let_value["D"] = 4
    let_value["e"] = 5
    let_value["E"] = 5
    let_value["f"] = 6
    let_value["F"] = 6
    let_value["g"] = 7
    let_value["G"] = 7
    let_value["h"] = 8
    let_value["H"] = 8
    let_value["I"] = 9
    let_value["i"] = 9
    let_value["J"] = 10
    let_value["j"] = 10
    let_value["K"] = 11
    let_value["k"] = 11
    let_value["L"] = 12
    let_value["l"] = 12
    let_value["M"] = 13
    let_value["m"] = 13
    let_value["N"] = 14
    let_value["n"] = 14
    let_value["O"] = 15
    let_value["o"] = 15
    let_value["P"] = 16
    let_value["p"] = 16
    let_value["Q"] = 17
    let_value["q"] = 17
    let_value["r"] = 18
    let_value["R"] = 18
    let_value["s"] = 19
    let_value["S"] = 19
    let_value["t"] = 20
    let_value["T"] = 20
    let_value["u"] = 21
    let_value["U"] = 21
    let_value["v"] = 22
    let_value["V"] = 22
    let_value["w"] = 23
    let_value["W"] = 23
    let_value["x"] = 24
    let_value["X"] = 24
    let_value["y"] = 25
    let_value["Y"] = 25
    let_value["z"] = 26
    let_value["Z"] = 26
    let_value[" "] = 0
    let_value["-"] = 0
    value = 0
    counter = 0
    for letter in name:
        counter = let_value[letter]
        value = value + counter
    return value

def get_name_list(file_name):
    name_list = []
    fin = open(file_name)
    for line in fin:
        name = line.strip()
        name = name.split(" ")
        name_list.append(name[0]) 
    return name_list

def who_has_highest_value(name_list):
    # return the name with highest value among the given name_list
    highest = 0
    top_name = []
    for name in name_list:
        if get_value(name) > highest:
            highest = get_value(name)
            top_name = name
    return top_name 
    # pass

def get_words(file_name):
    # return a list of words
    word_list = []
    fyle = open(file_name)
    for line in fyle:
        word = line.strip()
        word_list.append(word)
    return word_list

def get_words_with_same_value(word_list, value):
    # return a list of matched words
    matched_words = []
    for word in word_list:
        if get_value(word) == value:
            matched_words.append(word)
    return matched_words


def main():
    print("Class member with the largest value:", who_has_highest_value(get_name_list('roster.txt')))
    print("Words with the same value as Waylon:", get_words_with_same_value(get_words("positive-words.txt"), get_value("waylon")))
    pass


if __name__ == '__main__':
    main()