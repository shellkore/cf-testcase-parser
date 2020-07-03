#!/usr/bin/env python

# the_shellkore_awakens

import requests
from bs4 import BeautifulSoup
import os

BASE_URL = "https://codeforces.com/contest"

def testCaseExtracter(contestNum,level):
    print(contestNum,level)
    problemPageUrl = f"{BASE_URL}/{contestNum}/problem/{level}"
    print(problemPageUrl)
    page = requests.get(problemPageUrl)
    soup = BeautifulSoup(page.text, 'html.parser')
    sampleTests = soup.find(class_='sample-test')
    inputsElement = sampleTests.find_all(class_='input')
    inputList = [elem.find('pre').text for elem in inputsElement]
    outputsElement = sampleTests.find_all(class_='output')
    outputList = [elem.find('pre').text for elem in outputsElement]
    return(inputList,outputList)
    
def getQuestionCount(contestNum):
    contestPageUrl = f"{BASE_URL}/{contestNum}"
    print(contestPageUrl)
    contestPage = requests.get(contestPageUrl)
    soupContest = BeautifulSoup(contestPage.text,'html.parser')
    dataTable = soupContest.find_all(class_='datatable')[0]
    numberOfQuestion = len(dataTable.find_all("td",class_='id'))
    return(numberOfQuestion)

def parser(contestNumber):
    current_dir = (os.getcwd())
    folderName = os.path.join(current_dir,'temp',contestNumber)
    if os.path.exists(folderName):
        print('Requested item already exists!!')
        return
    quesCount = getQuestionCount(contestNumber)
    print(f"Total number of questions are {quesCount}")
    os.mkdir(folderName)
    for i in range(quesCount):
        problemLevel = chr(ord('A')+i)
        try: 
            inputs,outputs = testCaseExtracter(contestNumber,problemLevel)
            # print(inputs,outputs)
            numOfInputs = len(inputs)
            problemFolder = os.path.join(current_dir,'temp',contestNumber,problemLevel)
            os.mkdir(problemFolder)
            for inp in range(numOfInputs):
                with open(f'{problemFolder}/input{inp}.txt','w') as f:
                    f.write(inputs[inp])
        except:
            print(f"No inputs in {problemLevel}")
    print(f"Request for contest number {contestNumber} completed. Wish you all the best!!!")

if __name__ == '__main__':
    contestNumber = input('Enter contest number: ')
    parser(contestNumber)