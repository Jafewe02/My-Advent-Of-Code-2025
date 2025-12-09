dialPosition = int(50)
result = int(0)

with open("./input.txt", "rt", encoding="UTF-8") as infos:
  for i in infos:
    oldPosition = dialPosition
    i = i.strip()
    direction = i[0]
    dialTurningRange = int(i[1:])
    while(dialTurningRange >= 100):
      result += 1
      dialTurningRange -= 100
    match direction:
      case "L":
        dialPosition -= dialTurningRange
      case "R":
        dialPosition += dialTurningRange
      case _:
        print("Error")
    if (dialPosition < 0 or dialPosition > 100) and oldPosition != 0:
      result += 1
    dialPosition = dialPosition % 100
    if dialPosition == 0:
      result += 1
      
print(result)