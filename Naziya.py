def intfloatconverter(Naziya):
    return int(Naziya) if Naziya == int(Naziya) else Naziya

def floatstopper(Naziya):
    return float('{:.3f}'.format(Naziya))

def floatstopper2(Naziya):
    return float('{:.2f}'.format(Naziya))

def closestvalue(Naziya,Parveen):
    Variable = 0
    for items in Naziya:
        if items >= Parveen:
            Variable+=items
            break
        else:
            continue
    return Variable

def maxnum(Naziya):
    s1 = 0
    s= max(Naziya)
    for i in Naziya:
        if i == s:
            s1+=1
    return False if s1 <= 1 else True

class ErrorHandling:
    def __init__(self,Naziya):
        self.Naziya = Naziya
        self.variable : int = 0
        self.list : list = []
                    
    def Try(self) -> None:
        ci = [(i).strip().split("-") for i in self.Naziya]
        for j in ci:
            for i in j:
                self.list.append(int(i))
                
        cixitem = []
        for i in range(len(self.list)//2):
            cixitem.append(intfloatconverter((self.list[self.variable]+self.list[self.variable+1])/2))
            self.variable+=2
        return cixitem

    def Exception(self) -> None:
        for i in self.Naziya:
            if type(i) == list:
                for j in i:
                    self.list.append(j)
            else:
                self.list.append(i)
                
        li = []
        for _ in range(len(self.list)//2):
            li.append(self.list[self.variable] +"-"+ self.list[self.variable+1])
            self.variable += 2
            
        self.list.clear()
        ci = [(i).strip().split('-') for i in li]
        for j in ci:
            self.variable+=2
            for i in j:
                self.list.append(int(i))

        cixitem = []
        self.variable = 0
        for i in range(len(self.list)//2):
            xy = (self.list[self.variable]+self.list[self.variable+1])/2
            self.variable+=2
            cixitem.append(intfloatconverter(xy))
        return li,cixitem,self.list
    
    def Dash_Error(self) -> None:
        for i in self.Naziya:
            z = i.strip().split('-')
            if len(z) > 2:
                for i in z:
                    try:
                        if int(str(i)) == int(i):
                            self.list.append(i)
                    except ValueError:
                        continue
            else:
                self.list.append(z)
        return self.list
    
    def Empty_Error(self) -> None:
        for i in self.Naziya:
            if i == '':
                continue
            else:
                self.list.append(i)
        return self.list

class Indexing:
    def __init__(self,*Naziya) -> None:
        self.Naziya = Naziya
        self.IndexVariable : int = 0
            
    def Median_Indexing(self):
        if self.Naziya[0] <= int(self.Naziya[1]):
            indexing1 = self.Naziya[2].index(self.Naziya[0])
            self.IndexVariable += indexing1
        else:
            indexing1 = self.Naziya[2].index(self.Naziya[0])
            self.IndexVariable+=indexing1
        return self.IndexVariable

    def Single_Side_Indexing(self):
        for i in self.Naziya[0]:
            if i >= self.Naziya[1]:
                self.IndexVariable += self.Naziya[0].index(i)
                break
        return self.IndexVariable

    def Quartile_Indexing(self):
        for i in self.Naziya[0]:
            if i >= self.Naziya[1]:
                self.IndexVariable += self.Naziya[2][self.Naziya[0].index(i)]
                break
        return self.IndexVariable
        
    def Indexing_Function(self):
        return [i for i in range(len(self.Naziya[0])) if self.Naziya[0][i]==self.Naziya[1]]
            
    def Indicies(self):
        return [i for i, x in enumerate(self.Naziya[0]) if x == self.Naziya[1]]

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

def IP_Address(Naziya):
    x_forwarded_for = Naziya.META.get('HTTP_X_FORWARDED_FOR')
    return x_forwarded_for.split(',')[-1].strip() if x_forwarded_for else Naziya.META.get('REMOTE_ADDR')

if __name__ == "__main__":
    print('Running this from source file directly')

multiply = lambda Naziya,Parveen : [intfloatconverter(floatstopper2(Parveen[i]*Naziya[i])) for i in range(len(Naziya))]

square = lambda Naziya : [intfloatconverter(floatstopper2(i**2)) for i in Naziya]

substraction = lambda Naziya,Parveen : [intfloatconverter(floatstopper2(i-Parveen)) for i in Naziya]

intfloatconverter_list = lambda Naziya : [int(i) for i in Naziya]

intfloatconverter_list_ifelse = lambda Naziya : [int(i) if i == int(i) else i for i in Naziya]
