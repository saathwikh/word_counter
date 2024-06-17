def count_words(text):
  #This function counts the number of words and characters in a text string.
  words = text.split()
  character_count = len(text)
  return len(words), character_count

def count_specific_word(text, word):
   #This function counts the occurrences of a specific word in a text string.
  word_count = 0
  for w in text.split():
    if w.lower() == word.lower():
      word_count += 1
  return word_count

def main():
  while True:
    # Offer options for user input or file reading
    print("Choose an option:")
    print("1. Enter text directly")
    print("2. Read text from a file")
    choice = input("Enter your choice (1 or 2): ")
    if choice not in ("1", "2"):
      print("Invalid choice. Please enter 1 or 2.")
      continue

    # Handle user input
    if choice == "1":
      user_input = input("Enter a sentence or paragraph: ")
      text = user_input
    else:
      # Read text from file
      filename = input("Enter the file name: ")
      try:
        with open(filename, 'r') as file:
          text = file.read()
      except FileNotFoundError:
        print("Error: File not found. Please try again.")
        continue

    # Count words and characters
    word_count, character_count = count_words(text)
    print("Number of words:", word_count)
    print("Number of characters:", character_count)

    # Ask about specific word counting (optional)
    count_specific = input("Do you want to count a specific word? (y/n): ")
    if count_specific.lower() == "y":
      specific_word = input("Enter the word to count: ")
      specific_count = count_specific_word(text, specific_word)
      print("Count of '{}': {}".format(specific_word, specific_count))

    # Ask if user wants to continue
    cont = input("Do you want to continue? (y/n): ")
    if cont.lower() != "y":
      break

if __name__ == "__main__":
  main()
