# **python strings**
surrounded by quotation marks   
assigning a string to a variable is done with the variable name followed by an equal sign and string    
- a="hello"
- print(a)
### **multiline strings**
be a done bt using three quotes
### **strings are arrays**
arrays of bytes representing unicode characters 
but there are no character data types so a single character with a string is length of 1    
square brackets can be used to access elements of the string    
#### get the character at position 1 (first character has position 0)
- a="hello world"
- print(a[1])
- it would print e
### **looping through a string**
we can loop through the characters with a *for* loop    
#### loop through the letters in the word banana
- for x in "banana":
-  print(x) 
- b
- a
- n
- a
- n
- a
### **string length**
- len()
- print(len(a))
### **check strings**
- chekc certain phrase or character in the string 
- use *in*
#### check if it is present
- txt= "the best things in life are free"
- print( "free" in txt)
#### print only if it is present 
- if "free" in txt:
- print("yes, 'free' is present")
#### check if NOT
- use *not in*
- print("candy" not in txt)