def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here  
    targetList = []
    
    for key in aDict:
        if aDict[key] == target:
            targetList.append(key)
    
    return targetList
