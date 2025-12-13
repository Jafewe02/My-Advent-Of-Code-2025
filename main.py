result = 0
f = open("input.txt")
fileContent = f.read()
f.close()
fileContent = fileContent.strip()
idRanges = fileContent.split(',')
for ids in idRanges:
  id1 = int(ids.split('-')[0])
  id2 = int(ids.split('-')[1])
  while(id1 <= id2):
    idString = str(id1)
    if(len(idString) % 2 == 0):
      splitingPosition = int(len(idString) / 2)
      part1 = int(idString[:splitingPosition])
      part2 = int(idString[splitingPosition:])
      if part1 == part2:
        result += id1
    id1 += 1
print(result)