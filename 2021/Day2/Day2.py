def GetInstructions():
    instructionSet = []
    f = open("D2Input.txt")
    for line in f:
        l = line.split('\\n')
        instructionSet.append(l[0])
    f.close()
    return instructionSet

def CalculatePosition(_instructionSet):
    step = []



CalculatePosition(GetInstructions())