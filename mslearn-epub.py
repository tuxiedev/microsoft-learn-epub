#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from typing import List
import os


class Book:
    def __init__(self, title: str, description: str, articles: List[str], index: int):
        self.title = title
        self.description = description
        self.articles = articles
        self.index = index
        self.epubpress_id = None

    def set_epubpress_id(self, id: str):
        self.epubpress_id = id


def download_ebook(book, destination_directory, epubpress_url):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    with open('{}/{}-{}.epub'.format(destination_directory, book.index, book.title), 'wb+') as f:
        book = requests.get(
            ('{}/api/v1/books/{}/download'.format(epubpress_url, book.epubpress_id))).content
        f.write(book)


def generate_ebook_with_epubpress(book: Book, destination_directory, epubpress_url):
    print('Generating ebook for title {}'.format(book.title))
    r = requests.post(('{}/api/v1/books'.format(epubpress_url)), json={'title': book.title,
                                                                       'description': book.description,
                                                                       'sections': [{'url': article} for article in book.articles]})
    book.set_epubpress_id(r.json()['id'])
    completed = False
    print('Waiting ebook to finish for title {}'.format(book.title))
    while not completed:
        status = requests.get(
            ('{}/api/v1/books/{}/status'.format(epubpress_url, book.epubpress_id))).json()
        if status['progress'] > 99:
            completed = True
    print('Downloading ebook for title {}'.format(book.title))
    download_ebook(book, destination_directory, epubpress_url)


def download_lesson_ebook(url_lesson, index, destination_directory, epubpress_url):
    unit_content = requests.get(url_lesson).text
    soup = BeautifulSoup(unit_content, features='html.parser')
    title = soup.find('h1', 'title').text.strip()
    summary = soup.find('div', 'summary').text.strip()
    unit_titles = soup.find_all('a', 'unit-title')
    articles = []
    for unit_title in unit_titles:
        articles.append('{0}/{1}'.format(url_lesson, unit_title['href']))
    return generate_ebook_with_epubpress(
        Book(title, summary, articles, index),
        destination_directory,
        epubpress_url
    )


def scrape_lessons_from_learning_path(learning_path_url, destination_directory, epubpress_url):
    base_path = 'https://docs.microsoft.com/en-us/learn'
    r = requests.get(learning_path_url)
    bs = BeautifulSoup(r.text, features="html.parser")
    links = bs.find_all('a', 'is-block text-decoration-none')
    for i in range(len(links)):
        download_lesson_ebook(
            '{}/{}'.format(base_path, links[i]['href'].strip('../../')),
            i,
            destination_directory,
            epubpress_url
        )


if __name__ == '__main__':
    from argparse import ArgumentParser
    argparser = ArgumentParser()
    argparser.add_argument('--url', '-u', type=str, required=True,
                           help='Path to Microsoft Learn Learning Path')
    argparser.add_argument('--destination-dir', '-d', type=str,
                           required=True,  help='Local Path where ebooks will be stored')
    argparser.add_argument('--epubpress-url', '-e',
                           type=str, default='https://epub.press')
    args = argparser.parse_args()
    scrape_lessons_from_learning_path(
        learning_path_url=args.url,
        destination_directory=args.destination_dir,
        epubpress_url=args.epubpress_url
    )
