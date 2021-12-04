from bs4 import BeautifulSoup
import requests
import re

url = "http://192.168.0.38/"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

word = "Apache2"

def count_appearance_of_a_word(word):
    find_word = soup.body.find_all(string=re.compile('{0}'.format(word)))
    print('Found the word "{0}" {1} time\n'.format(word, len(find_word)))

if __name__ == "__main__":
    count_appearance_of_a_word(word)
