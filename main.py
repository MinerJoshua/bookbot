

def read_book(book_path: str) -> str:
	with open(f"books/{book_path}") as file:

		file_content: str = file.read();
		return file_content;

def count_book(book: str) -> int:
	words :list[str] = book.split();
	
	return len(words);

def char_count(book: str)-> dict:
	char_count: dict = {};
	words :list[str] = book.split();

	for word in words:
		for character in word.lower():
			if character.isalpha():	
				if character in char_count:
					char_count[character] += 1;
				else:
					char_count[character] = 1;
	return char_count;

def generate_report(book: str, word_count: int, char_dict: dict):

	char_dict = dict(sorted(char_dict.items(),key = lambda x:x[1],reverse=True));

	print(f"--- Begin report of {book} ---");
	print(f"{word_count} words found in the book\n");
	for char in char_dict:
		print(f"The '{char}' character was found {char_dict[char]} times");
	print(f"--- End Report ---");
	

def main():
	book: str = "frankenstein.txt";
	book_text: str = read_book(book);
	book_words: int = count_book(book_text);
	book_char: dict = char_count(book_text)
	generate_report(book,book_words,book_char);

if __name__ == "__main__":
	main();