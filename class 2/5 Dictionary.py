# Dictionary
# 'Key':'Value'
#   |        |
# 'String':dynamic
person={
    "name":"Bill",
    "age":60,
    "height":5.9,
    "weight":"80KG",
    "mobile":178538891,
    "shirt-color":"black",
    "hire-color":"black and white"
}

course={
    "title":"Web Development with Python, Django & React",
    "fee":8000,
    "rating":4.7,
    "batch-no":13,
    "lessons":40,
    "students": 50,
    "instructor":["Hasin","Rabbil","Setu","Tajnur"],
    "details":{#Nested dictionary
        "hours":70,
        "lessons":58,
        "students":500,
    }
}
print(person)

#Onek gula dictionary mile akta list korle JSON array bole
IC=[course,course,course,course,course]
print(IC)

print(course["title"])
print(course["details"]["hours"])
print(course["details"]["lessons"])