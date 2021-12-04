from bs4 import BeautifulSoup
import requests
import re

url = "http://192.168.0.38/"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

word = "Apache2"
apache2_headings = []


def list_headings():
    headings = soup.find_all(class_="section_header")
    print(f'list of headings on the Apache2 Ubuntu Default Page')
    for i in headings:
        apache2_headings.append(i.get_text())
    for apache2_heading in apache2_headings:
        print(apache2_heading.strip())
    print("\n")


def count_appearance_of_a_word(word):
    find_word = soup.body.find_all(string=re.compile('{0}'.format(word)))
    print('Found the word "{0}" {1} time\n'.format(word, len(find_word)))


if __name__ == "__main__":
    '''...'''
    list_headings()
    count_appearance_of_a_word(word)

