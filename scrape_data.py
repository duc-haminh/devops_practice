import os
import requests
from bs4 import BeautifulSoup

def scrape_data(urls):
    data = []

    for url in urls:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        content_ques_list = soup.find_all('div', class_='qa__item-user-question')
        content_ans_list = soup.find_all('div', class_='qa__item-admin-answer')

        if content_ques_list and content_ans_list:
            for content_ques, content_ans in zip(content_ques_list, content_ans_list):
                excluded_elements = content_ques.find_all('p')
                content_ques_text = ''
                for p in excluded_elements:
                    lines = p.get_text(strip=True).split('\n')
                    lines = [line for line in lines if line.strip()]
                    if lines:
                        content_ques_text += ' '.join(lines) + ' '
                content_ques = content_ques_text.strip()

                paragraphs = content_ans.find_all('p')
                content_ans_text = ''
                for p in paragraphs:
                    lines = p.get_text(strip=True).split('\n')
                    lines = [line for line in lines if line.strip()]
                    if lines:
                        content_ans_text += ' '.join(lines) + ' '
                content_ans = content_ans_text.strip()

                row = {
                    'Content_question': content_ques,
                    'Answer': content_ans,
                }

                data.append(row)

    return data
