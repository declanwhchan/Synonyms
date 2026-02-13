import math
def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    return math.sqrt(sum_of_squares)

def cosine_similarity(vec1, vec2):
    dot_prod = 0
    for key, value in vec1.items():
        if vec2.get(key) != None:
            dot_prod += value * vec2.get(key)
    cos_similarity = dot_prod / (norm(vec1) * norm(vec2))
    return cos_similarity

def build_semantic_descriptors(sentences):
    main_dict = {}
    for sentence in sentences:
        # check for new word
        new_words = []
        for word in sentence:
            if word not in new_words:
                new_words.append(word)
        # check for frequency of each other word in sentence with new word
        for word in new_words:
            if word not in main_dict:
                main_dict[word] = {}
            for other_word in new_words:
                if other_word == word:
                    continue
                elif other_word not in main_dict[word]:
                    main_dict[word][other_word] = 0
                main_dict[word][other_word] += 1
    return main_dict

def build_semantic_descriptors_from_files(filenames):
    sentences = []
    punctuations = [",", "-", "--", ":", ";"]
    separators = ["!", "?"]
    for i in range(len(filenames)):
        file = open(filenames[i], "r", encoding = "latin1")
        file_chars = file.read().lower()
        for char in punctuations:
            file_chars = file_chars.replace(char, " ")
        for char in separators:
            file_chars = file_chars.replace(char, ".")
        # Convert to list of words and sentences
        file_sentences = file_chars.split(".")
        for file_sentence in file_sentences:
            file_words = file_sentence.split()
            sentences.append(file_words)
    return build_semantic_descriptors(sentences)

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    best_choice = choices[0]
    highest_similarity = -1
    if word in semantic_descriptors:
        vec1 = semantic_descriptors[word]
    else:
        vec1 = {}
    for choice in choices:
        if choice in semantic_descriptors:
            vec2 = semantic_descriptors[choice]
        else:
            vec2 = {}
        # if similarity of two words cannot be computed then set highest_similarity = -1
        try:
            if similarity_fn(vec1, vec2) > highest_similarity:
                highest_similarity = similarity_fn(vec1, vec2)
                best_choice = choice
        except:
            highest_similarity = -1
    return best_choice

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    num_tested = 0
    num_correct_answers = 0
    file = open(filename, "r", encoding = "latin1")
    file_lines = file.read().lower().split("\n")
    for line in file_lines:
        words = line.split()
        question = words[0]
        correct_ans = words[1]
        choices = words[2:]
        if most_similar_word(question, choices, semantic_descriptors, similarity_fn) == correct_ans:
            num_correct_answers += 1
        num_tested += 1
    if num_tested > 0:
        percentage = num_correct_answers / num_tested * 100.0
    else:
        percentage = 0.0
    return percentage

sem_descriptors = build_semantic_descriptors_from_files(["2600-0.txt", "pg7178.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")