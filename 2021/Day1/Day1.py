def getDepthMeasurements():
    measurements = []
    f = open("D1Input.txt")
    for line in f.readlines():
        num = line.split('\n')
        measurements.append(int(num[0]))
    f.close()
    return measurements


def measureDepthv1():
    depthIn = getDepthMeasurements()
    print("##INPUT##")
    print(depthIn)
    print("##INPUT##")

    num1, num2, counter = 0, 0, 0

    for i in depthIn:
        num2 = i
        if num2 > num1:
            if num1 == 0:
                print(f"{i} N/A - no previous")
                num1 = i
                continue
            print(f"{i} increased num2 {num2} > num1 {num1}")
            num1 = i
            counter += 1
        else:
            num1 = i
            print(f"{i} decreased num2 {num2} < num1 {num1}")

    print(f"\n$$$$FINAL_ANSWER$$$$\n{counter}\n$$$$FINAL_ANSWER$$$$")


def measureDepthv2():
    depthIn = getDepthMeasurements()
    print("##INPUT##")
    print(depthIn)
    print("##INPUT##")

    sumDepths = []
    num1, num2, counter = 0, 0, 0

    for i, d in enumerate(depthIn):
        if i + 2 < len(depthIn):
            sum1 = d
            sum2 = depthIn[i + 1]
            sum3 = depthIn[i + 2]
            sumFinal = sum1 + sum2 + sum3
            print(f"{sumFinal} ## {sum1} + {sum2} + {sum3}")
            sumDepths.append(sumFinal)

    for i in sumDepths:
        num2 = i
        if num2 > num1:
            if num1 == 0:
                print(f"{i} N/A - no previous")
                num1 = i
                continue
            print(f"{i} increased num2 {num2} > num1 {num1}")
            num1 = i
            counter += 1
        elif num2 == num1:
            num1 = i
            print(f"{i} no change num2 {num2} = num1 {num1}")
        else:
            num1 = i
            print(f"{i} decreased num2 {num2} < num1 {num1}")

    print(f"\n$$$$FINAL_ANSWER$$$$\n{counter}\n$$$$FINAL_ANSWER$$$$")



measureDepthv2()
