# Sample string 
RootStr = "((True & not (False | False) & not (True | False )) | not True | not False| (False & True))"

def Str_FormatEvalStr(_rootStr_):
    #print("Format String: " + _rootStr_)
    listStr = list(_rootStr_)
    for index in range(len(_rootStr_)):
        cntBracketOpen = 0
        cntBracketClose = 0
        flgSingleCon = 0
        if (index < len(_rootStr_) - 3) and _rootStr_[index] == 'n' and _rootStr_[index + 1] == 'o' and _rootStr_[index + 2] == 't':
            listStr[index] = "(" + listStr[index]
            cntBracketOpen = 1
            for index2 in range(index,len(_rootStr_) - 2):
                # Count Brackets
                if _rootStr_[index2] == "(":
                    cntBracketOpen = cntBracketOpen + 1
                elif _rootStr_[index2] == ")":
                    cntBracketClose = cntBracketClose + 1
                elif cntBracketOpen == 1 and ( _rootStr_[index2] == "T" or _rootStr_[index2] == "F"): # check is it single condition
                    flgSingleCon = 1
                # Add one more Brackets
                if cntBracketOpen > 1 and cntBracketClose > 0 and (cntBracketOpen - cntBracketClose) == 1 and flgSingleCon == 0:
                    listStr[index2] = listStr[index2] + ")"
                    break
                elif flgSingleCon == 1 and  _rootStr_[index2] == "e":
                    listStr[index2] = listStr[index2] + ")"
                    break

    resultStr = "".join(listStr)
    #print("Result String: " + resultStr)
    return resultStr

print(eval(Str_FormatEvalStr(RootStr)))

