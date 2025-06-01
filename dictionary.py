student_data = {' id' :
{'name': ['Sara'],
'class':['V'],
'subject_intergration': ['english, math, science']
},
'id1':
{'name': ['Marry'],
'class':['V'],
'subject_intergration': ['english, math, science']
},
'id2':
{'name': ['David'],
'class':['V'],
'subject_intergration': ['english, math, science']
},
'id3':
{'name': ['John'],
'class':['V'],
'subject_intergration': ['english, math, science']
},
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)