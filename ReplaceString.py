RootStra = "40(01 & ( (4 & 5) | 555) & 4 & 14 & 16)4"

def ReplaceStr( rootStr, oldStr,  newStr):  
    sizeRootstr = len(rootStr)
    ReplaceStr = list(rootStr)
    for index in range(len(rootStr)):
        if rootStr[index] == oldStr and index == 0:
            if not rootStr[index + 1].isnumeric(): 
                ReplaceStr[index] = newStr   
        elif rootStr[index] == oldStr and index == sizeRootstr - 1:
            if not rootStr[index - 1].isnumeric():
               ReplaceStr[len(rootStr) - 1] = newStr
        elif rootStr[index] == oldStr:
            if not rootStr[index - 1].isnumeric() and not rootStr[index + 1].isnumeric():
                ReplaceStr[index] = newStr
    newstr = "".join(ReplaceStr)
    return newstr

test = ReplaceStr(RootStra,"1","001")
print(test)
