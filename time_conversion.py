def timeConversion(t):
    if int(t[:2])==12:
        t='00'+t[2:]
    if t[8]=='A':
        return t[:8]
    else:
        return str(int(t[:2])+12)+t[2:8]

time = input()
print(timeConversion(time))