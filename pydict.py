coun = {
    "India":"Delhi",
    "UK":"Londin"
}
#print(coun["India"])

#adding elements
#coun["Italy"]="Rome"
#print(coun)

#remove dictionary items
#del coun["UK"]
#print(coun)

# clear the dictionary
#coun.clear()
#print(coun)

#dictionary length
#numbers = {10: "ten", 20: "twenty", 30: "thirty"}
#print(len(numbers))

my_dict={}
print(len(my_dict))

file={
    ".txt": "Text File",
    ".pdf" : "PDF Document",
    ".jpg" : "JPEG Image" 
}

#use of in and not in operators
print(".pdf" in file)
print(".mp3" in file)
print(".mp3" not in file)

#Python Dictionary pop()
#The pop() method removes and returns an element from a dictionary having the given key.
Marks={ "Maths" : 48,"English":48,"Physics" : 45}
element=Marks.pop("Physics")
print("poped element=",element)
print("marks after pop=",Marks)

#Dictionary keys()
#The keys() method extracts the keys of the dictionary and returns the list of keys as a view object.
numbers = {1: 'one', 2: 'two', 3: 'three'}
# extracts the keys of the dictionary
#dictionaryKeys=numbers.keys()
#print(dictionaryKeys)

#Python Dictionary values()
#The values() method returns a view object that displays a list of all the values in the dictionary.
dictvalues=numbers.values()
print(dictvalues)

#Python Dictionary get()
scores = {
    'Physics': 67, 
    'Maths': 87,
    'History': 75
}
#result = scores.get('Physics')
#print(result)

#Python Dictionary popitem()
Person={
"Name":"shriya",
"age":"21",
"salary":20000
}
result=Person.popitem()
print("popped item:",result)
print(Person)

#dictionary copy
original_copy={'Physics':67, 'Maths':87}
copied_marks = original_copy.copy()
print('Original Marks:', original_copy)
print('Copied Marks:',copied_marks)
