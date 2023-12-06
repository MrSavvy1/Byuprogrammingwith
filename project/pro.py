import os
import pytest
from datetime import datetime

def search_in_file(file_path, search_word):
				"""
				Search for a word in a text file and return the number of occurrences.

				Args:
								file_path (str): The path to the text file.
								search_word (str): The word to search for in the file.

				Returns:
								int: Number of occurrences of the search word in the file.
				"""
				with open(file_path, 'r') as file:
								content = file.read()
								return content.count(search_word)

def replace_in_file(file_path, search_word, replace_word):
				"""
				Replace occurrences of a word in a text file with a new word.

				Args:
								file_path (str): The path to the text file.
								search_word (str): The word to search for in the file.
								replace_word (str): The word to replace the search word with.
				"""
				with open(file_path, 'r') as file:
								content = file.read()
								new_content = content.replace(search_word, replace_word)

				with open(file_path, 'w') as file:
								file.write(new_content)

def run_search_and_replace(file_path, search_word, replace_word):
				"""
				Main function to perform search and replace in a text file.

				Args:
								file_path (str): The path to the text file.
								search_word (str): The word to search for in the file.
								replace_word (str): The word to replace the search word with.
				"""
				occurrences = search_in_file(file_path, search_word)

				if occurrences > 0:
								replace_in_file(file_path, search_word, replace_word)
								print(f"Search word '{search_word}' found and replaced {occurrences} times.")
				else:
								print(f"Search word '{search_word}' not found in the file.")

def test_search_in_file():
				"""
				Test search_in_file function.
				"""
				# Example test case
				file_path = "test_file.txt"
				search_word = "apple"
				with open(file_path, 'w') as test_file:
								test_file.write("apple orange banana apple")
				assert search_in_file(file_path, search_word) == 2

def test_replace_in_file():
				"""
				Test replace_in_file function.
				"""
				# Example test case
				file_path = "test_file.txt"
				search_word = "apple"
				replace_word = "kiwi"
				with open(file_path, 'w') as test_file:
								test_file.write("apple orange banana apple")
				replace_in_file(file_path, search_word, replace_word)
				with open(file_path, 'r') as test_file:
								assert test_file.read() == "kiwi orange banana kiwi"
