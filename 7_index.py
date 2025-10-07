course = "python for beginners"
print(course[0]) # print the 1st character
print(course[2]) # print the 2nd character
print(course[-1]) # print the last character
print(course[-2])  # print the 2nd last character

print(course[0:3]) # print the 1st three character
print(course[0:]) # print all the string starting from 1st index or character
print(course[1:]) # print all the string starting from 2nd index or character and exclude 1st one
print(course[:6]) # print the string from 0 to 5

course = "python for beginners"
another = course[:] # : means from 0 index to end means complete string
print(another)

name = "siddhartha"
print(name[1:-1]) # print the string from 1st inndex till the second last and exclude the last index