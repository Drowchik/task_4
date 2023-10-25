import sys
import time
import concurrent.futures


def search_word_in_text(word: str, file_name: str) -> str:
    """ 
        This function opens the file and searches for the specified word in it, if it finds it returns the string that it found
    """
    time.sleep(2)
    with open(file_name, 'r', encoding='utf-8') as f:
        file = f.read()
        if word in file:
            return f'Слово {word} было найдено в файле {file_name}'
        else:
            return f'Слово не найдено {word} в файле {file_name}'


def search(word: str, files: list) -> None:
    """
        This function searches sequentially for a word in each file
    """
    for i in files:
        search_word_in_text(word, i)


def praralel_search(word: str, files: list) -> None:
    """
        This function searches in parallel in several files at once for the word
    """
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        results = [executor.submit(search_word_in_text, word, file) for file in files]
        for future in concurrent.futures.as_completed(results):
            print(future.result())


def main():
    print("Время выполнения параллельного выполнения: ")
    word = sys.argv[1]
    files = sys.argv[2:]
    t0 = time.time()
    praralel_search(word, files)
    print(time.time() - t0)

    print("Время выполения обычного выполнения: ")
    t0 = time.time()
    search(word, files)
    print(time.time() - t0)
