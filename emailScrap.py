"""
A. Input
    Get 50% off on every purchase. contact marketing team at market@qq.com. Find all your linkedin
    contacts for free, jeff.peterson@b2bsearch.com. qq.com partnership program apply at
    market@qq.com
B. Expected Output
    { "market@qq.com" : {"Occurance":2, "EmailType": "Non-Human"} ,
    "jeff.peterson@b2bsearch.com" : {"Occurance":1, "EmailType": "Human"}
    }
C. Explanation:
    The output must be in a nested json format.
    "Occurance" : No of times the email is repeated in the text.
    "EmailType" : Type of the email. You can have more complex logic to identify human and non-
    human emails but in this exercise, Just try the logic given below:
    Finding human emails: If the email is of format firstname.lastname@email.com then you can
    assume that the email is human.
    Finding non-human emails: If the email format is text@email.com where text is less than 8
    characters, then you can assume that the email is likely to be non-human.

Note: During extraction of email I found 'REALTORS®;realtors@bbn.com' from the txt file. 
So, it is treated as email beacause email accept special character also. 
I have set new 'EmailType' as Null if such mail arise i.e neither 'Human' nor 'Non-Human'
as per the description mention.
"""

import json
import re

# Email filter using split and loop
def filterEmail(data):
    strings = data.replace("\n"," ").split(" ")
    emailList = [string for string in strings if "@" in string and len(string)>7]
    jsonifyOutput(emailList)

# Email filter using regex
def filterEmailWithRegex(data):
    emailList = re.findall('\S+@\S+', data) # \S -> Matches any non-whitespace character
    jsonifyOutput(emailList)

# create nested dictionary for the output result as per description
def jsonifyOutput(emailList):
    mainDict = {}
    for email in set(emailList):
        subDict = {}
        occurance = emailList.count(email)
        subDict["Occurance"] = occurance
        emailSplit = email.split('@')[0]
        if '.' in emailSplit: 
            subDict["EmailType"] = "Human"
        elif '.' not in emailSplit and len(emailSplit)<8:
            subDict["EmailType"] = "Non-Human"
        else:
            subDict["EmailType"] = "Null"
        mainDict[email] = subDict
    exportJsonResult(mainDict)
    
# Export nested dictionary output into json     
def exportJsonResult(outputResult):
    with open("result.json","w") as resultFile:
        json.dump(outputResult,resultFile)

# Read the test file given "websiteData.txt"
def readFile():
    with open("websiteData.txt","r") as file:
        text_data = file.read()
        filterEmail(text_data)
        # uncomment below code for email filteration using regex
        # filterEmailWithRegex(text_data)

if __name__ == "__main__":
    readFile()
