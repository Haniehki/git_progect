# Nested lists
numbers=[1,2,3,4,5,6]
print(numbers)
newnumbers=[[1,2,3],[4,5,6]]
index_0=newnumbers[0]
print(index_0)
index_1=newnumbers[1]
print(index_1)
number_6=index_1[2]
print(number_6)

print("********************************")

for li in newnumbers:
     for num in li:
          print(num)

print("********************************")
# be ravesh coprehension list:

#copylist=[li for li in newnumbers]
#print(copylist) => [[1, 2, 3], [4, 5, 6]]
#copylist=[print(li) for li in newnumbers]  [1, 2, 3] [4, 5, 6]

copylist=[[print(l)for l in li] for li in newnumbers]

print("***********************************")

generatedNestedlist=[num for num in range(1,4)] # [1, 2, 3]
print(generatedNestedlist)
NewgeneratedNestedlis=[[newnum for newnum in range(1,5)] for num in range(1,5)]
print(NewgeneratedNestedlis)

print("_____________________________________________")

