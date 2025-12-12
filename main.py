f = open("input.txt")
fileContent = f.read()
f.close()
fileContent = fileContent.strip()
idRanges = fileContent.split(',')
for ids in idRanges:
  id1 = int(ids.split('-')[0])
  id2 = int(ids.split('-')[1])
  while(id1 <= id2):
    id1 += 1
    print(id1)