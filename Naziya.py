def intfloatconverter(Naziya):
    return int(Naziya) if Naziya == int(Naziya) else Naziya

def floatstopper(Naziya):
    return float('{:.3f}'.format(Naziya))

def floatstopper2(Naziya):
    return float('{:.2f}'.format(Naziya))

def ErrorHandling(Naziya):
    q = []
    for i in Naziya:
        try:
            z = i.strip().split('-')
            if len(z) > 2:
                for i in z:
                    zs = str(i)
                    try:
                        if int(zs) == int(i):
                            z1 = [z[0],z[-1]]
                            q.append(i)
                    except ValueError:
                        continue
            else:
                q.append(z)
        except SyntaxError:
            print('There Is Two Comma In Your Input Please Remove That')
    return q

def closestvalue(Naziya,Parveen):
    o = 0
    for i in Naziya:
        if i>= Parveen:
            o+=i
            break
        else:
            continue
    return o

def indices(Naziya,Parveen):
    return [i for i, x in enumerate(Naziya) if x == Parveen]

def maxnum(Naziya):
    s1 = 0
    s= max(Naziya)
    for i in Naziya:
        if i == s:
            s1+=1
    return False if s1 <= 1 else True

def indexingfunction(Naziya,Parveen):
    indexlist = [i for i in range(len(Naziya)) if Naziya[i]==Parveen]
    return indexlist

def Try(Naziya):
    ci = [(i).strip().split("-") for i in Naziya]
    cilis = []
    cinaz = 0
    for i in ci:
        g = i
        cinaz+=1
        for i in g:
            we = int(i)
            cilis.append(we)

    cixitem = []
    ciy = 0
    cix = 1
    for i in range(len(cilis)//2):
        xy = (cilis[ciy]+cilis[cix])/2
        if xy == int(xy):
            z = int(xy)
            cix+=2
            ciy+=2
            cixitem.append(z)
        else:   
            cix+=2
            ciy+=2
            cixitem.append(xy)
    return cixitem

def Exception(Naziya):
    a = []
    for i in Naziya:
        if type(i) == list:
            for j in i:
                a.append(j)
        else:
            a.append(i)

    k = 0
    o = 1
    list1 = []
    for i in range(len(a)//2):
        r = a[k] +"-"+ a[o]
        k += 2
        o += 2
        list1.append(r)
    li = list1

    cishow = []
    ci = []
    for i in li:
        z = (i).strip().split("-")
        ci.append(z)
        cishow.append(i)

    cilis = []
    cinaz = 0
    for i in ci:
        g = i
        cinaz+=1
        for i in g:
            we = int(i)
            cilis.append(we)

    cixitem = []
    ciy = 0
    cix = 1
    for i in range(len(cilis)//2):
        xy = (cilis[ciy]+cilis[cix])/2
        if xy == int(xy):
            z = int(xy)
            cix+=2
            ciy+=2
            cixitem.append(z)
        else:   
            cix+=2
            ciy+=2
            cixitem.append(xy)
    return li,cixitem,cilis

def Empty_Error_Handling(Naziya):
    Parveen = []
    for i in Naziya:
        if i == '':
            continue
        else:
            Parveen.append(i)
    return Parveen

def Cumulative(Naziya):
    Parveen = []
    naz = 0
    for i in Naziya:
        Parveen.append(i+naz)
        naz+=i
    return Parveen

def Summation_Value(*Naziya):
    zs = []
    za = []
    if len(Naziya) == 4:
        if Naziya[0][Naziya[1]] == Naziya[2]:
            for i in range(Naziya[1]+1, len(Naziya[0])):
                zs.append(Naziya[3][i])
            for j in range(0,Naziya[1]):
                za.append(Naziya[3][j])
        else:
            for i in range(Naziya[1], len(Naziya[0])):
                zs.append(Naziya[3][i])
            for j in range(0,Naziya[1]):
                za.append(Naziya[3][j])
    else:
        if Naziya[0][Naziya[1]] == Naziya[2]:
            for i in range(Naziya[1]+1, len(Naziya[0])):
                zs.append(1)
            for j in range(0,Naziya[1]):
                za.append(1)
        else:
            for i in range(Naziya[1], len(Naziya[0])):
                zs.append(1)
            for j in range(0,Naziya[1]):
                za.append(1)
    return zs,za

def Indexing(*Naziya):
    indexing = 0
    if Naziya[0] <= int(Naziya[1]):
        indexing1 = Naziya[2].index(Naziya[0])
        indexing += indexing1
    else:
        indexing1 = Naziya[2].index(Naziya[0])
        indexing+=indexing1
    return indexing

def Single_Side_Indexing(*Naziya):
    indexingforcf = 0
    for i in Naziya[0]:
        if i >= Naziya[1]:
            indexingforcf += Naziya[0].index(i)
            break
    return indexingforcf

def Quartile_Indexing(*Naziya):
    fs1 = 0
    for i in Naziya[0]:
        if i >= Naziya[1]:
            fs1 += Naziya[2][Naziya[0].index(i)]
            break
    return fs1

def String_Add(*Naziya):
    dlist1 = []
    l = 0
    if len(Naziya) == 3:
        for i in Naziya[0]:
            dlist1.append(str(Naziya[1])+" "+"-"+" "+str(Naziya[0][l])+" "+"="+" "+str(intfloatconverter(Naziya[2][l])))
            l+=1
    else:
        for i in Naziya[0]:
            dlist1.append(str(Naziya[1])+" "+"-"+" "+str(Naziya[2][l])+" "+"="+" "+str(intfloatconverter(Naziya[3][l])))
            l+=1
    return dlist1

def Existing_Value(*Naziya):
    email_count = []
    for key in Naziya[0]:
        for i in key[Naziya[1]].values():
            email_count.append(i)
    return email_count

def Last_Number_Checking(*Naziya):
    j2 = []
    for i in Naziya[0]:
        for j in i.get(Naziya[1]):
            j2.append(j)
    n = ''.join(filter(lambda i: i.isdigit(), str(j2[-1])))
    return int(n)

def Database_Insertion(*Naziya):
    '''Series_Name, Firstinput, Secondinput, Collection_Name, IpAddress, Firstinput_Type'''
    Data = {Naziya[0]: {'Question1':{Naziya[5]: Naziya[1],'Frequency': Naziya[2]}}}

    checking_last_message_count = [i for i in Naziya[3].find({'User':Naziya[4]},{ 'User':1,Naziya[0]:1,'_id':0 })]

    var = [i for i in Naziya[3].find({'User': Naziya[4]}, {Naziya[0]:1, '_id':0})]

    if var[0].get(Naziya[0]) == {}:
        Naziya[3].update_one({'User':Naziya[4]},{'$set':Data})
    else:
        N_User = Last_Number_Checking(checking_last_message_count,Naziya[0])
        N_Question_Check = Existing_Value(checking_last_message_count,Naziya[0])

        z = [[i[Naziya[5]],i['Frequency']] for i in N_Question_Check]
        
        Naziya[3].update_one({'User': Naziya[4]},{'$set':{f'{Naziya[0]}.Question'+f'{N_User+1}':{Naziya[5]:Naziya[1], 'Frequency': Naziya[2]}}}) if [Naziya[1],Naziya[2]] not in z else None

def IP_Address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[-1].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR')

if __name__ == "__main__":
    print('Running this from source file directly')

multiply = lambda Naziya,Parveen : [intfloatconverter(floatstopper2(Parveen[i]*Naziya[i])) for i in range(len(Naziya))]

square = lambda Naziya : [intfloatconverter(floatstopper2(i**2)) for i in Naziya]

substraction = lambda Naziya,Parveen : [intfloatconverter(floatstopper2(i-Parveen)) for i in Naziya]

intfloatconverter_list = lambda Naziya : [int(i) for i in Naziya]

intfloatconverter_list_ifelse = lambda Naziya : [int(i) if i == int(i) else i for i in Naziya]
