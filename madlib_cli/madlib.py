from textwrap import dedent
import re

def read_template(file):
    with open(file,'r') as file:
        content=file.readlines()
    str=''
    content=str.join(content)
    content=content.strip()
    return content    

content=read_template('assets/template.txt')
stringArr=['Adjective','A First Name','Past Tense Verb','Plural Noun','Large Animal','Small Animal','A Girl\'s Name','Number',' 1-50']

def parse(string,stringArr):
    arr=re.findall('{(.+?)}',string)
    for keyword in stringArr:
        string=string.replace(keyword,'')   
    return string,arr

def merge(string,arr):
    string=string.format(*arr)   
    return string

def game():
    print(dedent('''
    ************************
    Welcome to madlib, you will be prompted with questions and you need to answer them so that you can have a complete sentence at the end.

    ************************

    '''))
    inputArr=[]
    partsArr=parse(content,stringArr)[1]

    for i in partsArr:
        print(f'\nPlease Enter {i}')
        inputArr.append(input("> "))
    return inputArr
    
def result():
    string=parse(content,stringArr)[0]
    inputArr=game()
    with open('assets/copy.text', 'w') as file:
        file.write(merge(string,inputArr))
    with open('assets/copy.text', 'r') as file:
        copy=file.readlines()
    string=''
    for i in copy:
        string += i   
    print(dedent(f'Here is the result:\n {string}'))

result()
       