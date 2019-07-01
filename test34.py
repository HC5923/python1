# oldList = ['짜장면','탕수육','군만두']
# newList = oldList
# print(newList)
# oldList[0] ='짬뽕'
# oldList.append("깐풍기")
# print(newList)

# p.209

oldList = ['짜장면','탕수육','군만두']
newList = []
newList = oldList[:]
print(newList)
oldList[0] ='짬뽕'
oldList.append("깐풍기")
print(oldList)
print(newList)

# p.210  위에거랑 다르게 newlist에 old를 복사해서 넣음