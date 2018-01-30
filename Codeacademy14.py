def remove_duplicates(list):
    if list == []:
        return []   
    list = sorted(list)
    list = [list[0]]
  
    for i in list:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist
