import re
def read_template(file):
    with open(file,'r') as file:
        content=file.readlines()
    str=''
    content=str.join(content)
    content=content.strip()
    return content    
content=read_template('assets/template.txt')

stringArr=['Adjective','A First Name','Past Tense Verb','Plural Noun','Large Animal','Small Animal','A Girl\'s Name','First Name\'s','Number',' 1-50']

def parse(string,stringArr):
    arr=[]
    for keyword in stringArr:
        arr.append(re.findall(keyword,string))
        string=string.replace(keyword,'')
    mergedList=[]
    for i in arr:
        mergedList += i   
    return string

def merge(string,arr):
    for i in arr:
        string=string.replace('{}', i)   
    return string

def game():
    print('Welcome to madlib, you will be prompted with questions and you need to answer them so that you can have a complete sentence at the end.')
    inputArr=[]
    print('\nPlease Enter an Adjective')
    inputArr.append(input("> "))

    print('\nPlease Enter an Adjective')
    inputArr.append(input("> "))

    print('\nPlease Enter a first name')
    inputArr.append(input("> "))

    print('\nPlease Enter a past tense verb')
    inputArr.append(input("> "))

    print('\nPlease Enter a First Name')
    inputArr.append(input("> "))

    print('\nPlease Enter an Adjective')
    inputArr.append(input("> "))

    print('\nPlease Enter an Adjective')
    inputArr.append(input("> "))

    print('\nPlease Enter a plural noun')
    inputArr.append(input("> "))

    print('\nPlease Enter a large animal')
    inputArr.append(input("> "))

    print('\nPlease Enter a small animal')
    inputArr.append(input("> "))

    print('\nPlease Enter a Girl\'s Name')
    inputArr.append(input("> "))

    print('\nPlease Enter an Adjective')
    inputArr.append(input("> "))

    print('\nPlease Enter a plural noun')
    inputArr.append(input("> "))

    print('\nPlease Enter an Adjective')
    inputArr.append(input("> "))

    print('\nPlease Enter a plural noun')
    inputArr.append(input("> "))

    print('\nPlease Enter a Number (1-50)')
    inputArr.append(input("> "))

    print('\nPlease Enter a first name')
    inputArr.append(input("> "))

    print('\nPlease Enter a number')
    inputArr.append(input("> "))

    print('\nPlease Enter a plural noun')
    inputArr.append(input("> "))

    print('\nPlease Enter a number')
    inputArr.append(input("> "))

    print('\nPlease Enter a plural noun')
    inputArr.append(input("> "))
    
    string=parse(content,stringArr)
    print('Here is the result:\n ',merge(string,inputArr))

game()

       