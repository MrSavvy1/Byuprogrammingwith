import os
from datetime import datetime

def search_in_file(filename, search_word):
    """
    Search for a word in a text file and return the number of occurrences.

    Args:
        filename (str): The path to the text file.
        search_word (str): The word to search for in the file.

    Returns:
        int: Number of occurrences of the search word in the file.
    """
    with open(filename, 'r') as file:
        content = file.read()
        return content.count(search_word)

def replace_in_file(filename, search_word, replace_word):
    """
    Replace occurrences of a word in a text file with a new word.

    Args:
        filename (str): The path to the text file.
        search_word (str): The word to search for in the file.
        replace_word (str): The word to replace the search word with.
    """
    with open(filename, 'r') as file:
        content = file.read()
        new_content = content.replace(search_word, replace_word)

    with open(filename, 'w') as file:
        file.write(new_content)

def backup_original_file(filename):
    """
    Create a backup of the original file.

    Args:
        filename (str): The path to the text file.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_filename = f"{filename}_backup_{timestamp}"

    try:
        with open(filename, 'r') as original_file, open(backup_filename, 'w') as backup_file:
            backup_file.write(original_file.read())
        print(f"Backup created: {backup_filename}")
    except Exception as e:
        print(f"Failed to create backup: {e}")

def log_changes(filename, search_word, replace_word, occurrences):
    """
    Log the changes made in the file.

    Args:
        filename (str): The path to the text file.
        search_word (str): The word that was searched for.
        replace_word (str): The word used for replacement.
        occurrences (int): Number of occurrences replaced.
    """
    log_entry = f"{datetime.now()}: Replaced '{search_word}' with '{replace_word}' {occurrences} times."
    try:
        with open(f"{filename}_changes.log", 'a') as log_file:
            log_file.write(log_entry + "\n")
        print("Changes logged.")
    except Exception as e:
        print(f"Failed to log changes: {e}")


def perform_search_and_replace():
    # Retrieve input values
    file_path = filename_entry.get()
    search_word = search_word_entry.get()
    replace_word = replace_word_entry.get()

    # Create a backup of the original file
    backup_original_file(file_path)

    occurrences = search_in_file(file_path, search_word)

    if occurrences > 0:
        replace_in_file(file_path, search_word, replace_word)
        log_changes(file_path, search_word, replace_word, occurrences)
        result_label.config(text=f"Search word '{search_word}' found and replaced {occurrences} times.")
    else:
        result_label.config(text=f"Search word '{search_word}' not found in the file.")

# Create main Tkinter window
root = tk.Tk()
root.title("Search and Replace")

# Create and place Entry widgets for user input
filename_label = tk.Label(root, text="File Path:")
filename_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

filename_entry = tk.Entry(root, width=40)
filename_entry.grid(row=0, column=1, padx=10, pady=5)

search_word_label = tk.Label(root, text="Search Word:")
search_word_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

search_word_entry = tk.Entry(root, width=40)
search_word_entry.grid(row=1, column=1, padx=10, pady=5)

replace_word_label = tk.Label(root, text="Replace Word:")
replace_word_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

replace_word_entry = tk.Entry(root, width=40)
replace_word_entry.grid(row=2, column=1, padx=10, pady=5)

# Create a button to trigger the search and replace
search_replace_button = tk.Button(root, text="Search and Replace", command=perform_search_and_replace)
search_replace_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
