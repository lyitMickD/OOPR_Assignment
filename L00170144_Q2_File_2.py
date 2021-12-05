from bs4 import BeautifulSoup
import requests
import re

url = "http://192.168.0.38/"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

word = "Apache2"
apache2_headings = []


# Displays the title of the webpage
def apache2_title():
    title = soup.span
    print(title.string)


# finds the heading of the webpage
def list_headings():
    headings = soup.find_all(class_="section_header")
    print("-" * 60)
    apache2_title()
    print(f'list of headings:')
    print("-" * 60)
    for i in headings:
        apache2_headings.append(i.get_text())
    for apache2_heading in apache2_headings:
        print(apache2_heading.strip())
    print("-" * 60, "\n")


# counts the number of times a word appears on the webpage
def count_appearance_of_a_word(word):
    find_word = soup.body.find_all(string=re.compile('{0}'.format(word)))
    print('The appearance of the word "{0}" was found {1} times\n'.format(word, len(find_word)))
    print("-" * 60, "\n")


if __name__ == "__main__":
    '''...'''
    list_headings()
    count_appearance_of_a_word(word)
