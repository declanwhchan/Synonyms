# Semantic Similarity Analyzer (Python)

## Overview
This project implements a simple **semantic similarity system** using Python. The program analyzes text files to build **semantic descriptors** for words and then uses **cosine similarity** to determine how similar words are to each other.

The system can be used to answer **multiple-choice synonym questions** by selecting the word most similar in meaning to a given target word.

## Features
- Builds semantic descriptors from text files
- Uses **cosine similarity** to compare word meaning
- Answers synonym multiple-choice questions
- Evaluates accuracy using a test file
- Processes large text files automatically

## How It Works

### Semantic Descriptors
Each word is represented as a **dictionary vector** containing counts of other words that appear in the same sentence.

Example concept:

```
word → {context_word: frequency}
```

Words that appear in similar contexts will have similar vectors.

### Cosine Similarity
To measure similarity between two word vectors, the program computes **cosine similarity**:

```
similarity = (A · B) / (||A|| ||B||)
```

Where:
- `A · B` is the dot product of the vectors
- `||A||` and `||B||` are vector norms

Higher values mean the words are more similar.

## Main Functions

### `norm(vec)`
Computes the **Euclidean norm (magnitude)** of a vector stored as a dictionary.

### `cosine_similarity(vec1, vec2)`
Computes similarity between two word vectors using cosine similarity.

### `build_semantic_descriptors(sentences)`
Creates semantic descriptors from a list of sentences.

Each word stores how often other words appear in the same sentence.

### `build_semantic_descriptors_from_files(filenames)`
Reads text files, processes punctuation, splits them into sentences, and builds semantic descriptors.

### `most_similar_word(word, choices, semantic_descriptors, similarity_fn)`
Selects the word from a list of choices that is **most similar** to the given word.

### `run_similarity_test(filename, semantic_descriptors, similarity_fn)`
Runs a synonym test file and calculates the **percentage of correct answers**.

## Running the Program

Run the program using Python:

```
python semantic_similarity.py
```

The script builds semantic descriptors from text files and then runs a similarity test.

Example code used:

```
sem_descriptors = build_semantic_descriptors_from_files(["2600-0.txt", "pg7178.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")
```

## Input Files

### Training Text Files
Large text files used to build semantic descriptors.

Example:

```
2600-0.txt
pg7178.txt
```

### Test File
A file containing synonym questions.

Example format:

```
word correct_answer option1 option2 option3 option4
```

Example line:

```
happy joyful sad angry tired
```

## Output
The program prints the **percentage of correct guesses** on the test set.

Example output:

```
78.0 of the guesses were correct
```
