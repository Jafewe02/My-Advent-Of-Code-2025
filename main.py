dialPosition = int(50)
result = int(0)
lineCount = int(0)

with open("./input.txt", "rt", encoding="UTF-8") as infos:
  for i in infos:
    lineCount = lineCount + 1
    i = i.strip()
    direction = i[0]
    dialTurningRange = int(i[1:])
    match direction:
      case "L":
        dialPosition = dialPosition - dialTurningRange
      case "R":
        dialPosition = dialPosition + dialTurningRange
      case _:
        print("Error")
    dialPosition = dialPosition % 100
    if dialPosition == 0:
      result = result + 1
      
print(lineCount)
print(result)