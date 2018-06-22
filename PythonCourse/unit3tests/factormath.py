

def get_hcf(first,second):
    list1=[]
    if first==[] or second==[]:
        return list1
    else:
        i=0;j=0
        while i<len(first)and j<len(second):
            if first[i][0]==second[j][0]:
                list1.append((first[i][0],min(first[i][1],second[j][1])))
                i=i+1;j=j+1
            elif first[i][0] > second[j][0]:
                j=j+1
            else:
                i=i+1
        return list1



def get_lcm(first,second):
    list1=[]
    if first!=[] and second!=[]:
        i=0;j=0
        while i<len(first) and j<len(second):
            if first[i][0]==second[j][0]:
                list1.append((first[i][0],max(first[i][1],second[j][1])))
                i=i+1;j=j+1
            elif first[i][0] < second[j][0]:
                list1.append(first[i])
                i=i+1
            else:
                list1.append(second[j])
                j=j+1
        while i<len(first):
            list1.append(first[i])
            i=i+1
        while j<len(second):
            list1.append(second[j])
            j=j+1
    else:
        if first!=[]:
            list1=first
        elif second!=[]:
            list1=second
    return list1




def multiply(first,second):
    list1=[]
    if first!=[] or second!=[]:
        i=0;j=0
        while i<len(first)and j<len(second):
            if first[i][0]==second[j][0]:
                list1.append((first[i][0],first[i][1]+second[j][1]))
                i=i+1;j=j+1
            elif first[i][0] < second[j][0]:
                list1.append(first[i])
                i=i+1
            else:
                list1.append(second[j])
                j=j+1
        while i<len(first):
            list1.append(first[i])
            i=i+1
        while j<len(second):
            list1.append(second[j])
            j=j+1
    return list1

