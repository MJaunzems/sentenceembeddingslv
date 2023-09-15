import re
def normalize_sentence(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.lower()
    sentence = sentence.strip()
    return sentence
def normalize_files(uncompressed_file_path, compressed_file_path, normalized_uncompressed_path, normalized_compressed_path):
    with open(uncompressed_file_path, 'r', encoding='utf-8') as uncompressed_file, \
         open(compressed_file_path, 'r', encoding='utf-8') as compressed_file, \
         open(normalized_uncompressed_path, 'w', encoding='utf-8') as normalized_uncompressed_file, \
         open(normalized_compressed_path, 'w', encoding='utf-8') as normalized_compressed_file:
        for uncompressed_sentence, compressed_sentence in zip(uncompressed_file, compressed_file):
            normalized_uncompressed_sentence = normalize_sentence(uncompressed_sentence)
            normalized_compressed_sentence = normalize_sentence(compressed_sentence)
            
            normalized_uncompressed_file.write(normalized_uncompressed_sentence + '\n')
            normalized_compressed_file.write(normalized_compressed_sentence + '\n')

uncompressed_file_path = 'Compression_1.txt'
compressed_file_path = 'Compression_2.txt'
normalized_uncompressed_path = 'normalized_uncompressed.txt'
normalized_compressed_path = 'normalized_compressed.txt'

normalize_files(uncompressed_file_path, compressed_file_path, normalized_uncompressed_path, normalized_compressed_path)
