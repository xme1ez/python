# Function will clear text from string separators and return list of words
# Input is (string) text
# Output is a list of split words


def text_converting_to_list_of_words(input_text):

	input_text = input_text.replace('.', '')
	input_text = input_text.replace(',', '')
	input_text = input_text.replace(';', '')
	input_text = input_text.replace(':', '')
	input_text = input_text.replace('!', '')
	input_text = input_text.replace('?', '')
	input_text = input_text.replace('-', '')
	input_text = input_text.replace('  ', ' ')

	words_list = input_text.split(' ')

	return words_list
