# Fort Business Data Engineering

## Week1 

#### Test Question
Write a python code to extract emails found within the website content with their relevance. See
the input and output format.

#### Test Input
Get 50% off on every purchase. contact marketing team at market@qq.com. Find all your linkedin
contacts for free, jeff.peterson@b2bsearch.com. qq.com partnership program apply at
market@qq.com

---
**NOTE**

Use file websiteData.txt for program execution

---

#### Expected Output
{ "market@qq.com" : {"Occurance":2, "EmailType": "Non-Human"} ,
"jeff.peterson@b2bsearch.com" : {"Occurance":1, "EmailType": "Human"}
}

#### Description
The output must be in a nested json format.
"Occurance" : No of times the email is repeated in the text.
"EmailType" : Type of the email. You can have more complex logic to identify human and non-
human emails but in this exercise, Just try the logic given below:
Finding human emails: If the email is of format firstname.lastname@email.com then you can
assume that the email is human.
Finding non-human emails: If the email format is text@email.com where text is less than 8
characters, then you can assume that the email is likely to be non-human.