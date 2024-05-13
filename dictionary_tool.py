import streamlit as st

def generate_dictionary_file(dictionary):
    with open("dictionary.txt", "w") as file:
        for word, meaning in dictionary.items():
            file.write(f"{word}: {meaning}\n")

def preprocess_dictionary_file():
    dictionary = {}
    with open("dictionary.txt", "r") as file:
        for line in file:
            word, meaning = line.strip().split(": ")
            dictionary[word] = meaning
    return dictionary

def add_word(dictionary, word, meaning):
    if word.strip() == "":
        st.error("Word cannot be empty.")
        return

    dictionary[word] = meaning
    generate_dictionary_file(dictionary)
    st.success(f"Word '{word}' added successfully!")

def search_word(dictionary, word):
    if word.strip() == "":
        st.error("Please enter a word to search.")
        return

    if word in dictionary:
        return dictionary[word]
    else:
        return "Word not found in the dictionary."

def remove_word(dictionary, word):
    if word.strip() == "":
        st.error("Please enter a word to remove.")
        return

    if word in dictionary:
        del dictionary[word]
        generate_dictionary_file(dictionary)
        return f"{word} and its meaning removed from the dictionary."
    else:
        return "Word not found in the dictionary."

def main():
    st.set_page_config(page_title="Dictionary Tool", page_icon=":book:", layout="wide")

    dictionary = preprocess_dictionary_file()

    option = st.selectbox("Select an option:", ["Add Word", "Search Word", "Remove Word"])

    if option == "Add Word":
        word = st.text_input("Enter the word:")
        meaning = st.text_area("Enter the meaning:")
        if st.button("Add"):
            add_word(dictionary, word, meaning)
    
    elif option == "Search Word":
        word = st.text_input("Enter the word to search:")
        if st.button("Search"):
            meaning = search_word(dictionary, word)
            st.write(meaning)
    
    elif option == "Remove Word":
        word = st.text_input("Enter the word to remove:")
        if st.button("Remove"):
            result = remove_word(dictionary, word)
            st.success(result)

if __name__ == "__main__":
    main()
