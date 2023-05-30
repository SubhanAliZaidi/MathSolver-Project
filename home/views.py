Naziya = "naziya"
import Naziya as NAZIYA
import math,random,pymongo
from django.shortcuts import render
from home.models import *
from collections import Counter
from dotenv import load_dotenv
import os

load_dotenv()


Database_Link = pymongo.MongoClient("mongodb+srv://" + os.environ.get('DB_USER') + ':' + os.environ.get('DB_PASS')+"@cluster0.n2bv4fb.mongodb.net/")
Database_Name = Database_Link[os.environ.get('DB_NAME')]

# Database_Link = ''
# Database_Name = ''

def homepage(Naziya):
    return render(Naziya, 'index.html')

def mathsolver(request):
    Naziya= {'info':'Please Choose From what you want to solve',
        'question':'Maths Solver',
        'cando':'Here You Can solve all your Business Statistic Questions'}
    return render(request, "Mathsolver.html",Naziya)

def html(request):
    return render(request, "index(Second).html")

def contactform(request):
    Naziya = {}
    if request.method == "POST":
        name = request.POST.get('name').lower()
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        message = request.POST.get('message')

        Collection_Name = Database_Name["ContactForm"]
        Data = { 'Name': name, 'Email': {'Email1': email} , 'Phone_Number':{'Phone_Number1': phonenumber} ,'Message':{'Message1': message} }

        var = [i for i in Collection_Name.find({'Name': name}, {'Name':1, '_id':0})]

        checking_last_message_count = [i for i in Collection_Name.find({ 'Name':name},{'Email':1,'Message':1,'Phone_Number':1,'history': -1,'_id':0 })]
        
        if var == []:
            Collection_Name.insert_one(Data)
            Naziya['submitstatus'] = 'sucessful'
        else:
            N_Email = NAZIYA.Last_Number_Checking(checking_last_message_count,'Email')
            N_PhoneNumber = NAZIYA.Last_Number_Checking(checking_last_message_count,'Phone_Number')
            N_Message = NAZIYA.Last_Number_Checking(checking_last_message_count,'Message')

            email_count = NAZIYA.Existing_Value(checking_last_message_count,'Email')
            phone_count = NAZIYA.Existing_Value(checking_last_message_count,'Phone_Number')
            message_count = NAZIYA.Existing_Value(checking_last_message_count,'Message')

            Collection_Name.update_one({"Name": name},{'$set':{'Email.Email'+f'{N_Email+1}':email}}) if email not in email_count else None

            Collection_Name.update_one({"Name": name},{'$set':{'Phone_Number.Phone_Number'+f'{N_PhoneNumber+1}':phonenumber}}) if phonenumber not in phone_count else None
            
            Collection_Name.update_one({"Name": name},{'$set':{'Message.Message'+f'{N_Message+1}':message}}) if message not in message_count else None
            Naziya['submitstatus'] = 'sucessful'
    return render(request, "NewSignUp.html", Naziya)

def about(request):
    return render(request, "About.html")

def heartlink(request):
    return render(request,'Heartlink.html')

def standarddev(request):
    Naziya = {'root':[],
        'parveen':'Click Below To Solve Standard Deviation (Actual And Assumed Mean Method), Variance, Coefficient of Standard Deviation and Coefficient of Variation',
        'cando':'Please enter your question with comma seperated in textbox',
        'question':'Standard Deviation',
        'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
        'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',
        'match':[],
        'classinterval':[],}
    
    if request.method == "POST":

        firstinput = request.POST.get('firstinput')
        secondinput = request.POST.get('secondinput')

        # DATABASE FUNCTION GLOBAL INFO 
        Collection_Name = Database_Name["StandardDeviation"]
        IpAddress = NAZIYA.IP_Address(request)

        Checking_Existence = [i for i in Collection_Name.find({'User': IpAddress}, {'User':1, '_id':0})]

        Collection_Name.insert_one({'User' : IpAddress,'Continuous_Series': {}, 'Discrete_Series':{}, 'Individual_Series': {}, 'Errors':{}}) if Checking_Existence == [] else None

        if firstinput == '' and secondinput == '':
            Naziya['seriesname1'] = 'Please Enter Your Question First'
            Naziya['emp'] = 0
        else:
            if firstinput == '':
                Naziya['seriesname1'] = 'Please Enter X (No. of items) or C.I. (Class Interval)'
                Naziya['emp'] = 0
            else:
                try:
                    if secondinput == '':
                        secondinput = '0'
                    Naziya['match'] = secondinput

                    # SEPERATING WITH COMMA
                    list12 = (firstinput).strip().split(',')
                    listnaz = (secondinput).strip().split(',')

                    list2 = NAZIYA.ErrorHandling(listnaz).Empty_Error()
                    list1 = list12
                    li = list12

                    try:
                        cixitem = NAZIYA.ErrorHandling(li).Try()
                    except ValueError:
                        q = NAZIYA.ErrorHandling(list12).Dash_Error()
                        colo = NAZIYA.ErrorHandling(q).Exception()
                        li = colo[0]
                        cixitem = colo[1]

                    if len(cixitem) == len(list2):
                        Naziya['seriesname'] = "CONTINUOUS SERIES"
                        Naziya['classinterval'] = li

                        firstlist = [i for i in cixitem]
                        Naziya['x'] = firstlist

                        # # SECOND LIST
                        secondlist = [int(i) for i in list2]
                        Naziya['f'] = secondlist

                        # SUM OF X FIRST LIST
                        sumof_x = sum(cixitem)
                        Naziya["sumx"]= sumof_x

                        # SUM OF F SECOND LIST
                        sumof_f = sum(secondlist)
                        Naziya["sumf"]= sumof_f

                        # # TAKING ASSUME MEAN
                        assumed_mean = random.choice(firstlist)
                        Naziya["assumedmean"]= assumed_mean

                        # CALCULATING DEVIATION
                        deviation = NAZIYA.substraction(firstlist,assumed_mean)
                        Naziya['d'] = deviation
                        Naziya["sumd"]= sum(deviation)

                        # DEVIATION SQUARE
                        deviation2 = NAZIYA.square(deviation)
                        Naziya['d2'] = deviation2
                        Naziya["sumd2"]= sum(deviation2)

                        # FREQUENCY AND DEVIATION MULTIPLY
                        fdeviation = NAZIYA.multiply(secondlist,deviation)
                        Naziya['fd'] = fdeviation
                        Naziya["sumfd"]= sum(fdeviation)

                        # FREQUENCY AND DEVIATION SQUARE MULTIPLY   
                        fdeviation2 = NAZIYA.multiply(secondlist,deviation2)
                        Naziya['fd2'] = fdeviation2
                        Naziya["sumfd2"]= sum(fdeviation2)

                        # DIVINDING SUMMATION FD2 WITH SUMMATIOM F
                        divide1 = NAZIYA.floatstopper2(sum(fdeviation2)/sumof_f)
                        Naziya['divide1']= divide1

                        divide2 = NAZIYA.floatstopper2(sum(fdeviation)/sumof_f)
                        Naziya['divide2']= divide2

                        square2 = divide2*divide2
                        g = NAZIYA.floatstopper(square2)
                        Naziya['square2'] = g

                        subs = divide1 - g
                        g1 = NAZIYA.floatstopper(subs)
                        Naziya['subs'] = g1

                        sqrroot = NAZIYA.floatstopper(math.sqrt(g1))
                        Naziya['sqrroot'] = sqrroot

                        # ACTUAL MEAN METHOD
                        parveen = NAZIYA.multiply(firstlist,secondlist)
                        Naziya['fx'] = parveen
                        Naziya['sumfx']=sum(parveen)

                        # TAKING ACTUAL MEAN
                        actualmean = sum(parveen)/sumof_f
                        Naziya['actualmean'] = NAZIYA.floatstopper(actualmean)

                        # CALCULATION DEVIATION OF ACTUAL MEAN METHOD
                        acdeviation = NAZIYA.substraction(firstlist,actualmean)
                        Naziya['acd'] = acdeviation
                        
                        nazpar= sum(acdeviation)
                        nazpar1 = NAZIYA.floatstopper2(nazpar)
                        Naziya["sumacd"]= nazpar1

                        # ACTUAL MEAN DEVIATION SQUARE
                        acdeviation2 = NAZIYA.square(acdeviation)
                        Naziya['acd2'] = acdeviation2
                        varacd2 = sum(acdeviation2)
                        nazpar21 = NAZIYA.floatstopper2(varacd2)
                        Naziya["sumacd2"]= nazpar21

                        # ACTUAL MEAN FREQUENCY AND DEVIATION SQUARE MULTIPLY

                        acfdeviation2 = NAZIYA.multiply(secondlist,acdeviation2)
                        Naziya['acfd2'] = acfdeviation2
                        
                        varac= NAZIYA.floatstopper2(sum(acfdeviation2))

                        varac1 = NAZIYA.intfloatconverter(varac)
                        Naziya["sumacfd2"]= varac1

                        divide3 = sum(acfdeviation2)/sumof_f
                        Naziya['divide3'] = NAZIYA.floatstopper2(divide3)

                        acsqr = NAZIYA.floatstopper(math.sqrt(divide3))
                        Naziya['acsqrroot'] = acsqr

                        # COEFFICIENT OF STANDARD DEVIATION
                        cosd = NAZIYA.floatstopper(acsqr/actualmean)
                        Naziya['coefficientofsd'] = cosd
                        Naziya['coefficientofvar'] = cosd*100
                        Naziya['variance'] = acsqr**2

                        # DATABASE
                        NAZIYA.Database_Insertion('Continuous_Series',firstinput,secondinput,Collection_Name,IpAddress,'Class_Interval')

                    else:
                        # FOR DISCRETE SERIES
                        if len(list1) == len(list2):
                            Naziya['seriesname'] = "DISCRETE SERIES"

                            # FIRST LIST
                            firstlist = [int(i) for i in list1]
                            Naziya['x'] = firstlist

                            # # SECOND LIST
                            secondlist = [int(i) for i in list2]
                            Naziya['f'] = secondlist

                            # SUM OF X FIRST LIST
                            sumof_x = sum(firstlist)
                            Naziya["sumx"]= sumof_x

                            # SUM OF F SECOND LIST
                            sumof_f = sum(secondlist)
                            Naziya["sumf"]= sumof_f

                            # # TAKING ASSUME MEAN
                            assumed_mean = 25
                            Naziya["assumedmean"]= assumed_mean

                            # CALCULATING DEVIATION
                            deviation = NAZIYA.substraction(firstlist,assumed_mean)
                            Naziya['d'] = deviation
                            Naziya["sumd"]= sum(deviation)

                            # DEVIATION SQUARE
                            deviation2 = NAZIYA.square(deviation)
                            Naziya['d2'] = deviation2
                            Naziya["sumd2"]= sum(deviation2)

                            # FREQUENCY AND DEVIATION MULTIPLY
                            fdeviation = NAZIYA.multiply(secondlist,deviation)
                            Naziya['fd'] = fdeviation
                            Naziya["sumfd"]= sum(fdeviation)

                            # FREQUENCY AND DEVIATION SQUARE MULTIPLY   
                            fdeviation2 = NAZIYA.multiply(secondlist,deviation2)
                            Naziya['fd2'] = fdeviation2
                            Naziya["sumfd2"]= sum(fdeviation2)

                            # DIVINDING SUMMATION FD2 WITH SUMMATIOM F
                            divide1 = sum(fdeviation2)/sumof_f
                            Naziya['divide1']= divide1

                            divide2 = sum(fdeviation)/sumof_f
                            Naziya['divide2']= divide2

                            square2 = divide2*divide2
                            g = NAZIYA.floatstopper2(square2)
                            Naziya['square2'] = g

                            subs = divide1 - g
                            g1 = NAZIYA.floatstopper2(subs)
                            Naziya['subs'] = g1

                            sqrroot = math.sqrt(g1)
                            Naziya['sqrroot'] = sqrroot

                            # ACTUAL MEAN METHOD
                            parveen = NAZIYA.multiply(firstlist,secondlist)
                            Naziya['fx'] = parveen
                            Naziya['sumfx']=sum(parveen)

                            # TAKING ACTUAL MEAN
                            actualmean = sum(parveen)/sumof_f
                            Naziya['actualmean'] = actualmean

                            # CALCULATION DEVIATION OF ACTUAL MEAN METHOD
                            acdeviation = NAZIYA.substraction(firstlist,actualmean)
                            Naziya['acd'] = acdeviation
                            nazpar= sum(acdeviation)
                            nazpar1 = NAZIYA.intfloatconverter(NAZIYA.floatstopper((nazpar)))
                            Naziya["sumacd"]= nazpar1

                            # ACTUAL MEAN DEVIATION SQUARE
                            acdeviation2 = NAZIYA.square(acdeviation)
                            Naziya['acd2'] = acdeviation2
                            varacd2 = sum(acdeviation2)
                            nazpar21 = NAZIYA.intfloatconverter(NAZIYA.floatstopper((varacd2)))
                            Naziya["sumacd2"]= nazpar21

                            # ACTUAL MEAN FREQUENCY AND DEVIATION SQUARE MULTIPLY
                            acfdeviation2 = NAZIYA.multiply(secondlist,acdeviation2)
                            Naziya['acfd2'] = acfdeviation2
                            
                            varac= NAZIYA.floatstopper2(sum(acfdeviation2))
                            Naziya["sumacfd2"]= varac

                            divide3 = sum(acfdeviation2)/sumof_f
                            Naziya['divide3'] = NAZIYA.floatstopper2(divide3)

                            acsqr = NAZIYA.floatstopper(math.sqrt(divide3))
                            Naziya['acsqrroot'] = acsqr

                            # COEFFICIENT OF STANDARD DEVIATION
                            cosd = NAZIYA.floatstopper(acsqr/actualmean)
                            Naziya['coefficientofsd'] = cosd
                            Naziya['coefficientofvar'] = NAZIYA.floatstopper(cosd*100)
                            Naziya['variance'] = NAZIYA.floatstopper(acsqr**2)

                            # DATABASE
                            NAZIYA.Database_Insertion('Discrete_Series', firstinput, secondinput, Collection_Name, IpAddress, 'Items')
                        else:
                            if secondinput == '0':
                                Naziya['seriesname'] = "INDIVIDUAL SERIES"

                                firstlist = NAZIYA.intfloatconverter_list(list1)
                                Naziya['x'] = firstlist
                                Naziya['f1'] = 0
            
                                indmean = random.choice(firstlist)
                                Naziya['assumedmean'] = indmean

                                indd = NAZIYA.substraction(firstlist,indmean)
                                Naziya['d'] = indd
                                Naziya['sumd'] = sum(indd)

                                indd2 = NAZIYA.square(indd)
                                Naziya['d2'] = indd2
                                Naziya['sumd2'] = sum(indd2)
                                Naziya['len'] = len(firstlist)
                        
                                div = NAZIYA.floatstopper2(sum(indd2)/len(firstlist))
                                Naziya['divide1'] = NAZIYA.intfloatconverter(div)

                                vaq = NAZIYA.floatstopper2(sum(indd)/len(firstlist))
                                Naziya['divide2'] = NAZIYA.intfloatconverter(vaq)

                                va = NAZIYA.floatstopper2(sum(indd)/len(firstlist))

                                va1 = NAZIYA.floatstopper(va**2)
                                Naziya['square2'] = NAZIYA.intfloatconverter(va1)

                                min = NAZIYA.floatstopper2(div - va1)
                                Naziya['min'] = NAZIYA.intfloatconverter(min)

                                sqr = math.sqrt(min)
                                Naziya['sqrroot'] = sqr

                                # ACTUAL MEAN METHOD FOR INDIVIDUAL SERIES
                                mean = sum(firstlist)/len(firstlist)
                                Naziya['actualmean'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper2(mean))
                
                                Naziya['sumx'] = sum(firstlist)
                                Naziya['len'] = len(firstlist)
                                
                                acd = NAZIYA.substraction(firstlist,mean)
                                Naziya['acd'] = acd
                                
                                acd2 = NAZIYA.square(acd)
                                Naziya['acd2'] = acd2

                                Naziya['sumacd2'] = sum(acd2)

                                parveen1 = NAZIYA.floatstopper2(sum(acd2)/len(firstlist))
                                Naziya['divide3'] = NAZIYA.intfloatconverter(parveen1)

                                srt = NAZIYA.floatstopper2(math.sqrt(parveen1))
                                Naziya['acsqrroot'] = srt

                                # COEFFICIENT OF STANDARD DEVIATION
                                cosd = srt/mean
                                Naziya['coefficientofsd'] = cosd
                                Naziya['coefficientofvar'] = cosd*100
                                Naziya['variance'] = srt**2   

                                #DATABASE
                                NAZIYA.Database_Insertion('Individual_Series', firstinput,secondinput,Collection_Name,IpAddress,'Items')
                            else:
                                if len(list1) != len(list2):
                                    Naziya['x2'] = len(list1)
                                    Naziya['f2'] = len(list2)
                                    Naziya['seriesname1'] = "Please Check that lenght of both( X/C.I. and frequency is equal or may be you entered Two (,,) Commas )"
                                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
                except:
                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
                    Naziya['allerror'] = 'Handle'
                    Naziya['seriesname1'] = 'Please Enter Your Question Correctly'
    return render(request, "Mathstandardev.html",Naziya)  

def mean(request):

    Naziya = {'root':[],
        'parveen':'Click Below To Solve Mean',
        'cando':'Please enter your question with comma seperated in textbox',
        'question':'Mean',
        'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
        'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',}

    if request.method == "POST":

        firstinput = request.POST.get('firstinput')
        secondinput = request.POST.get('secondinput')

        # DATABASE FUNCTION GLOBAL INFO 
        Collection_Name = Database_Name["Mean"]
        IpAddress = NAZIYA.IP_Address(request)

        Checking_Existence = [i for i in Collection_Name.find({'User': IpAddress}, {'User':1, '_id':0})]

        Collection_Name.insert_one({'User' : IpAddress,'Continuous_Series': {}, 'Discrete_Series':{}, 'Individual_Series': {}, 'Errors':{}}) if Checking_Existence == [] else None

        if firstinput == '' and secondinput == '':
            Naziya['seriesname1'] = 'Please Enter Your Question First'
            Naziya['emp'] = 0
        else:
            if firstinput == '':
                Naziya['seriesname1'] = 'Please Enter X (No. of items) or C.I. (Class Interval)'
                Naziya['emp'] = 0
            else:
                try:
                    if secondinput == '':
                        secondinput = '0'
                    Naziya['match'] = secondinput

                    list12 = (firstinput).strip().split(',')
                    listnaz = (secondinput).strip().split(',')

                    list2 = NAZIYA.ErrorHandling(listnaz).Empty_Error()
                    list1 = list12
                    li = list12

                    try:
                        cixitem = NAZIYA.ErrorHandling(li).Try()
                    except ValueError:
                        q = NAZIYA.ErrorHandling(list12).Dash_Error()
                        colo = NAZIYA.ErrorHandling(q).Exception()
                        li = colo[0]
                        cixitem = colo[1]

                    if len(cixitem) == len(list2):
                        Naziya['seriesname'] = "CONTINUOUS SERIES"
                        Naziya['classinterval'] = li

                        firstlist = NAZIYA.intfloatconverter_list_ifelse(cixitem)
                        Naziya['x'] = firstlist

                        # # SECOND LIST
                        secondlist = NAZIYA.intfloatconverter_list(list2)
                        Naziya['f'] = secondlist

                        # SUM OF X FIRST LIST
                        sumof_x = sum(cixitem)
                        Naziya["sumx"]= sumof_x

                        # SUM OF F SECOND LIST
                        sumof_f = sum(secondlist)
                        Naziya["sumf"]= sumof_f

                        par = NAZIYA.intfloatconverter_list_ifelse(NAZIYA.multiply(firstlist,secondlist))
                        Naziya['fx'] = par

                        Naziya['sumfx'] = NAZIYA.intfloatconverter(sum(par))

                        acm = NAZIYA.intfloatconverter(sum(par)/sum(secondlist))
                        Naziya['actualmean'] = acm
                        #DATABASE
                        NAZIYA.Database_Insertion('Continuous_Series',firstinput,secondinput,Collection_Name,IpAddress,'Class_Interval')
                    else:
                        if len(list1) == len(list2):
                            Naziya['seriesname'] = "DISCRETE SERIES"

                            firstlist = NAZIYA.intfloatconverter_list(list1)
                            Naziya['x'] = firstlist

                            secondlist = NAZIYA.intfloatconverter_list(list2)
                            Naziya['f'] = secondlist
                            Naziya['sumf'] = sum(secondlist)

                            par = NAZIYA.multiply(firstlist,secondlist)
                            Naziya['fx'] = par

                            Naziya['sumfx'] = sum(par)
                            acm = NAZIYA.intfloatconverter(sum(par)/sum(secondlist))
                            Naziya['actualmean'] = acm
                            #DATABASE
                            NAZIYA.Database_Insertion('Discrete_Series',firstinput,secondinput,Collection_Name,IpAddress,'Items')
                        else:
                            if secondinput == '0':
                                Naziya['seriesname'] = "INDIVIDUAL SERIES"
                                firstlist = NAZIYA.intfloatconverter_list(list1)
                                Naziya['x'] = firstlist
                                Naziya['f1'] = 0

                                su = sum(firstlist)
                                Naziya['sumx'] = su
                                Naziya['len'] = len(firstlist)
                                Naziya['actualmean'] = NAZIYA.intfloatconverter(sum(firstlist)/len(firstlist)) 
                                #DATABASE
                                NAZIYA.Database_Insertion('Individual_Series',firstinput,secondinput,Collection_Name,IpAddress,'Items')
                            else:
                                if len(list1) != len(list2):
                                    Naziya['x2'] = len(list1)
                                    Naziya['f2'] = len(list2)
                                    Naziya['seriesname1'] = "Please Check that lenght of both( X/C.I. and frequency is equal or may be you entered Two (,,) Commas )"
                                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
                except:
                    Naziya['allerror'] = 'Handle'
                    Naziya['seriesname1'] = 'Please Enter Your Question Correctly'
                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
    return render(request, "Mathsmean.html",Naziya)

def median(request):

    Naziya = {'root':[],
        'parveen':'Click Below To Solve Median',
        'cando':'Please enter your question with comma seperated in textbox',
        'question':'Median',
        'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
        'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',}

    if request.method == "POST":

        firstinput = request.POST.get('firstinput')
        secondinput = request.POST.get('secondinput')

        Collection_Name = Database_Name["Median"]
        IpAddress = NAZIYA.IP_Address(request)

        Checking_Existence = [i for i in Collection_Name.find({'User': IpAddress}, {'User':1, '_id':0})]

        Collection_Name.insert_one({'User' : IpAddress,'Continuous_Series': {}, 'Discrete_Series':{}, 'Individual_Series': {}, 'Errors':{}}) if Checking_Existence == [] else None

        if firstinput == '' and secondinput == '':
            Naziya['seriesname1'] = 'Please Enter Your Question First'
            Naziya['emp'] = 0
        else:
            if firstinput == '':
                Naziya['seriesname1'] = 'Please Enter X (No. of items) or C.I. (Class Interval)'
                Naziya['emp'] = 0
            else:
                try:
                    if secondinput == '':
                        secondinput = '0'
                    Naziya['match'] = secondinput

                    # SEPERATING WITH COMMA
                    list12 = (firstinput).strip().split(',')
                    listnaz = (secondinput).strip().split(',')
                    
                    list2 = NAZIYA.ErrorHandling(listnaz).Empty_Error()
                    list1 = list12
                    li = list12

                    try:
                        cixitem = NAZIYA.ErrorHandling(li).Try()
                    except ValueError:
                        q = NAZIYA.ErrorHandling(list12).Dash_Error()
                        colo = NAZIYA.ErrorHandling(q).Exception()
                        li = colo[0]
                        cixitem = colo[1]

                    if len(cixitem) == len(list2):
                        # FOR CONTINUOUS SERIES
                        Naziya['seriesname'] = "CONTINUOUS SERIES"
                        Naziya['len1'] = len(list1)
                        Naziya['dislen'] = len(list1)
                        Naziya['len'] = len(list1)

                        Naziya['classinterval'] = li
                        f = NAZIYA.intfloatconverter_list(list2)
                        Naziya['f'] = f

                        # TAKING SUM OF F
                        Naziya['sumf'] = sum(f)

                        # TAKING N/2
                        sum_f = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(f)/2))
                        Naziya['n2'] = sum_f

                        # TAKING CUMULATIVE FREQUENCY
                        cf = NAZIYA.Cumulative(f)
                        Naziya['cf'] = cf

                        # CHOOSING CLOSEST VALUE IN LIST
                        val= NAZIYA.closestvalue(cf,sum_f)
                        indexing = NAZIYA.Indexing(val,sum_f,cf).Median_Indexing()

                        # TAKING POSITION IN LIST
                        cfp = cf[indexing-1]
                        Naziya['cfp'] = cfp

                        # TAKING F1 AND L1
                        f1 = f[indexing] #F1
                        Naziya['f1'] = f1
                        
                        l = (li[indexing]).strip().split('-')
                        l1 = int(l[0]) #L1
                        Naziya['L1'] = l1

                        Naziya['i'] = int(l[1]) - int(l[0]) if int(l[0]) > int(l[1]) else int(l[1]) - int(l[0])

                        divide1 = NAZIYA.intfloatconverter(sum_f/1)
                        Naziya['divide1'] = divide1

                        calc = (divide1 - cfp) * Naziya['i']
                        calc1 = NAZIYA.intfloatconverter(calc)
                        Naziya['multiply1'] = calc1

                        med = calc1 / f1
                        med1 = l1 + med
                        Naziya['divide2'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(med))
                        Naziya['median'] = NAZIYA.intfloatconverter(med1)

                        #DATABASE
                        NAZIYA.Database_Insertion('Continuous_Series',firstinput,secondinput,Collection_Name,IpAddress,'Class_Interval')
                    else:
                        if len(list1) == len(list2):
                            Naziya['seriesname'] = "DISCRETE SERIES"
                            naziya = {}
                            Naziya['len1'] = len(list1)
                            Naziya['lenf1'] = 0
                            Naziya['dislen'] = len(list1)
                            
                            firstlist = NAZIYA.intfloatconverter_list(list1)
                            firstlistcopy = firstlist.copy()
                            Naziya['x'] = firstlist
                            
                            firstlistcopy.sort()
                            Naziya['sortx'] = firstlistcopy
                            Naziya['discretex'] = 1

                            f12 = NAZIYA.intfloatconverter_list(list2)
                            fcopy = f12.copy()

                            for key,value in zip(firstlist,fcopy):
                                naziya[key] = value
                            
                            f = [naziya[i] for i in firstlistcopy]
                            Naziya['f'] = f
                            sumf = sum(f)
                            Naziya['sumf'] = sumf

                            cf = NAZIYA.Cumulative(f)
                            Naziya['cf'] = cf

                            if sum(f)%2 == 0 :
                                print('this is even series')
                                Naziya['len3'] = sumf

                                findincf = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sumf/2))
                                Naziya['divide1'] = NAZIYA.intfloatconverter(findincf)
                                
                                divi = findincf+1
                                Naziya['add1'] = NAZIYA.intfloatconverter(divi)

                                indexingforcf = NAZIYA.Indexing(cf,findincf).Single_Side_Indexing()

                                te = firstlistcopy[indexingforcf]
                                Naziya['term1'] = te

                                indexingforcf2 = NAZIYA.Indexing(cf,divi).Single_Side_Indexing()

                                te2 = firstlistcopy[indexingforcf2]
                                Naziya['term2'] = te2

                                la = NAZIYA.intfloatconverter(NAZIYA.floatstopper(te + te2))
                                Naziya['la'] = la

                                me = NAZIYA.intfloatconverter(NAZIYA.floatstopper(la/2))
                                Naziya['median'] = me
                            else:
                                print('this is odd series')
                                Naziya['odd'] = 1
                                Naziya['len3'] = sumf
                                
                                zu = sumf + 1
                                Naziya['n'] = zu
                                zu1 = zu/2
                                Naziya['divide1'] = NAZIYA.intfloatconverter(zu1)
                                a = NAZIYA.Indexing(cf,zu1).Single_Side_Indexing()
                                firstli = firstlistcopy[a]
                                Naziya['term'] = firstli
                            # DATABASE
                            NAZIYA.Database_Insertion('Discrete_Series', firstinput, secondinput, Collection_Name, IpAddress, 'Items')
                        else:
                            if secondinput == '0':
                                # print('this is individual series')
                                Naziya['lenf1'] = 0
                                Naziya['lensumx'] = 1
                                
                                if len(list1)%2:
                                    # FOR ODD SERIES
                                    Naziya['seriesname'] = "INDIVIDUAL SERIES"

                                    firstlist = NAZIYA.intfloatconverter_list(list1)
                                    firstlistcopy = firstlist.copy()
                                    Naziya['x'] = firstlist

                                    if len(firstlist)%2 :
                                        Naziya['odd'] = 1

                                    Naziya['len1'] = len(list1)
                                    firstlistcopy.sort()
                                    Naziya['sortx'] = firstlistcopy

                                    zu = len(list1) + 1
                                    Naziya['n'] = zu
                                    zu1 = zu/2
                                    Naziya['divide1'] = NAZIYA.intfloatconverter(zu1)
                                    term = firstlistcopy[int(zu1)-1]
                                    Naziya['term'] = term
                                else:
                                    Naziya['seriesname'] = "INDIVIDUAL SERIES"
                                    firstlist = NAZIYA.intfloatconverter_list(list1)
                                    firstlistcopy = firstlist.copy()
                                    Naziya['x'] = firstlist

                                    Naziya['len1'] = len(list1)
                                    firstlistcopy.sort()
                                    Naziya['sortx'] = firstlistcopy
                                    
                                    length = len(list1)/2
                                    Naziya['divide1'] = NAZIYA.intfloatconverter(length)

                                    Naziya['add1'] = NAZIYA.intfloatconverter(length +1)

                                    term1 = firstlistcopy[int(length)-1]
                                    Naziya['term1'] = term1
                                    term2 = firstlistcopy[int(length+1)-1]
                                    Naziya['term2'] = term2

                                    la = term1 + term2
                                    Naziya['la'] = la
                                    median = la/2
                                    Naziya['median']= NAZIYA.intfloatconverter(median)
                                #DATABASE
                                NAZIYA.Database_Insertion('Individual_Series', firstinput,secondinput,Collection_Name,IpAddress,'Items')
                            else:
                                if len(list1) != len(list2):
                                    Naziya['x2'] = len(list1)
                                    Naziya['f2'] = len(list2)
                                    Naziya['seriesname1'] = "Please Check that lenght of both( X/C.I. and frequency is equal or may be you entered Two (,,) Commas )"
                                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
                except:
                    Naziya['allerror'] = 'Handle'
                    Naziya['seriesname1'] = 'Please Enter Your Question Correctly'
                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
    return render(request, "Mathsmedian.html", Naziya)

def mode(request):

    Naziya = {'root':[],
        'parveen':'Click Below To Solve Mode',
        'cando':'Please enter your question with comma seperated in textbox',
        'question':'Mode',
        'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
        'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',
        'x':[],}
    
    if request.method == "POST":

        firstinput = request.POST.get('firstinput')
        secondinput = request.POST.get('secondinput')

        Collection_Name = Database_Name["Mode"]
        IpAddress = NAZIYA.IP_Address(request)

        Checking_Existence = [i for i in Collection_Name.find({'User': IpAddress}, {'User':1, '_id':0})]

        Collection_Name.insert_one({'User' : IpAddress,'Continuous_Series': {}, 'Discrete_Series':{}, 'Individual_Series': {}, 'Errors':{}}) if Checking_Existence == [] else None

        if firstinput == '' and secondinput == '':
            Naziya['seriesname1'] = 'Please Enter Your Question First'
            Naziya['emp'] = 0
        else:
            if firstinput == '':
                Naziya['seriesname1'] = 'Please Enter X (No. of items) or C.I. (Class Interval)'
                Naziya['emp'] = 0
            else:
                try:
                    if secondinput == '':
                        secondinput = '0'
                    Naziya['match'] = secondinput

                    # SEPERATING WITH COMMA
                    list12 = (firstinput).strip().split(',')
                    listnaz = (secondinput).strip().split(',')
                    
                    list2 = NAZIYA.ErrorHandling(listnaz).Empty_Error()
                    list1 = list12
                    li = list12

                    try:
                        cixitem = NAZIYA.ErrorHandling(li).Try()
                    except ValueError:
                        q = NAZIYA.ErrorHandling(list12).Dash_Error()
                        colo = NAZIYA.ErrorHandling(q).Exception()
                        li = colo[0]
                        cixitem = colo[1]

                    if len(cixitem) == len(list2):
                        Naziya['seriesname'] = "CONTINUOUS SERIES"
                        Naziya['classinterval'] = li

                        firstlist = NAZIYA.intfloatconverter_list_ifelse(cixitem)
                        Naziya['x'] = firstlist

                        # # SECOND LIST
                        secondlist = NAZIYA.intfloatconverter_list(list2)
                        Naziya['f'] = secondlist
                        checklist = NAZIYA.maxnum(secondlist)

                        if checklist == True:
                            # IF THERE IS MAX NUMBER REPEATING(GROUPING METHOD)
                            Naziya['seriesname'] = "CONTINUOUS SERIES"
                            Naziya['method1'] = "Tally Method (Grouping Table)"
                            
                            Naziya['tallymatch'] = "NaziyaParveen"
                            Naziya['heightfire'] = "off"

                            dash1 =[]
                            dash2 =[]
                            dash3 =[]
                            dash4 =[]
                            dash5 =[]
                            dash6 =[]
                            dash7 =[]
                            for i in range(len(secondlist)):
                                dash1.append('-')
                                dash2.append('-')
                                dash3.append('-')
                                dash4.append('-')
                                dash5.append('-')
                                dash6.append('-')
                                dash7.append('-')

                            zero = 0
                            one = 1
                            g2_2 = []
                            for i in range(len(secondlist)//2):
                                z = secondlist[zero] + secondlist[one]
                                zero+= 2
                                one+= 2 
                                g2_2.append(z)
                            Naziya['g2_2'] = g2_2          
                            Naziya['leng2_2'] = len(g2_2)  

                            zer = 1
                            on = 2
                            g1_2_2 = []
                            for i in range((len(secondlist)-1)//2):
                                z = secondlist[zer] + secondlist[on]
                                zer+=2
                                on+=2
                                g1_2_2.append(z)
                            g1_2_2.insert(0,1)
                            Naziya['g1_2_2'] = g1_2_2

                            ze = 0
                            onze = 1
                            two = 2
                            g3_3 = []
                            for i in range(len(secondlist)//3):
                                z = secondlist[ze] + secondlist[onze] + secondlist[two]
                                ze+=3
                                onze+=3
                                two +=3
                                g3_3.append(z)
                            Naziya['g3_3'] = g3_3
                            Naziya['leng3_3'] = len(g3_3)

                            naz1 = 1
                            naz2 = 2
                            naz3 = 3
                            g1_3_3 = []
                            for i in range((len(secondlist)-1) //3):
                                z = secondlist[naz1] + secondlist[naz2] + secondlist[naz3]
                                naz1 += 3
                                naz2 += 3
                                naz3 += 3
                                g1_3_3.append(z)
                            g1_3_3.insert(0,1)
                            Naziya['g1_3_3'] = g1_3_3
                            Naziya['leng1_3_3'] = len(g1_3_3)

                            naz23 = 2
                            naz231 = 3
                            naz232 = 4
                            g2_3_3 = []
                            for i in range((len(secondlist)-2) //3):
                                z = secondlist[naz23] + secondlist[naz231] + secondlist[naz232]
                                naz23 += 3
                                naz231 += 3
                                naz232 += 3
                                g2_3_3.append(z)
                            g2_3_3.insert(0,1)
                            Naziya['g2_3_3'] = g2_3_3
                            Naziya['leng2_3_3'] = len(g2_3_3)

                            ui = NAZIYA.Indexing(secondlist,max(secondlist)).Indexing_Function()
                            for i in ui:
                                dash7[i] = "Naziya"

                            max7 = max(g2_2)
                            Naziya['max2_2'] = 7
                            max7_index = g2_2.index(max7)
                            max7_tal1 = (max7_index + 1)*2-1
                            max7_tal2 = (max7_index + 1)*2
                            dash1[max7_tal1 - 1] = "Naziya"
                            dash1[max7_tal2 - 1] = "Naziya"

                            max1 = max(g2_2)
                            Naziya['max2_2'] = max1
                            max1_index = g2_2.index(max1)
                            max1_tal1 = (max1_index + 1)*2-1
                            max1_tal2 = (max1_index + 1)*2
                            dash1[max1_tal1 - 1] = "Naziya"
                            dash1[max1_tal2 - 1] = "Naziya"

                            max2 = max(g1_2_2)
                            Naziya['max1_2_2'] = max2
                            max2_index = g1_2_2.index(max2)
                            max2_tal1 = (max2_index)*2
                            max2_tal2 = (max2_index)*2+1
                            dash2[max2_tal1 - 1] = "Naziya"
                            dash2[max2_tal2 - 1] = "Naziya"

                            max3 = max(g3_3)
                            Naziya['max3_3'] = max3
                            max3_index = g3_3.index(max3)
                            max3_tal1 = (max3_index+1)*3-2
                            max3_tal2 = (max3_index+1)*3-1
                            max3_tal3 = (max3_index + 1)*3
                            dash3[max3_tal1 - 1] = "Naziya"
                            dash3[max3_tal2 - 1] = "Naziya"
                            dash3[max3_tal3 - 1] = "Naziya"

                            max4 = max(g1_3_3)
                            Naziya['max1_3_3'] = max4
                            max4_index = g1_3_3.index(max4)
                            max4_tal1 = (max4_index)*3+1
                            max4_tal2 = (max4_index)*3-1
                            max4_tal3 = (max4_index )*3
                            dash4[max4_tal1 - 1] = "Naziya"
                            dash4[max4_tal2 - 1] = "Naziya"
                            dash4[max4_tal3 - 1] = "Naziya"

                            max5 = max(g2_3_3)
                            Naziya['max2_3_3'] = max5
                            max5_index = g2_3_3.index(max5)
                            max5_tal1 = (max5_index)*3+1
                            max5_tal2 = (max5_index)*3
                            max5_tal3 = (max5_index)*3+2

                            dash5[max5_tal1 - 1] = "Naziya"
                            dash5[max5_tal2 - 1] = "Naziya"
                            dash5[max5_tal3 - 1] = "Naziya"

                            Naziya['dash1'] = dash1
                            Naziya['dash2'] = dash2
                            Naziya['dash3'] = dash3
                            Naziya['dash4'] = dash4
                            Naziya['dash5'] = dash5
                            Naziya['dash6'] = dash6
                            Naziya['dash7'] = dash7

                            tallydict = {}
                            for i in range(len(secondlist)+1):
                                tallydict[i] = 0

                            ex = NAZIYA.Indexing(dash1,"Naziya").Indexing_Function()
                            for i in ex:
                                tallydict[i] += 1

                            ex2 = NAZIYA.Indexing(dash2,"Naziya").Indexing_Function()
                            for i in ex2:
                                tallydict[i] += 1

                            ex3 = NAZIYA.Indexing(dash3,"Naziya").Indexing_Function()
                            for i in ex3:
                                tallydict[i] += 1
                            
                            ex4 = NAZIYA.Indexing(dash4,"Naziya").Indexing_Function()
                            for i in ex4:
                                tallydict[i] += 1

                            ex5 = NAZIYA.Indexing(dash5,"Naziya").Indexing_Function()
                            for i in ex5:
                                tallydict[i] += 1

                            ex7 = NAZIYA.Indexing(dash7,"Naziya").Indexing_Function()
                            for i in ex7:
                                tallydict[i] += 1

                            inde = []
                            for i in tallydict:
                                inde.append(tallydict[i])

                            modalclass = inde.index(max(inde))
                            dash6[modalclass] = "Naziya"

                            modalcl = li[modalclass]
                            Naziya['modeclass'] = modalcl

                            lq = modalcl.strip().split('-')
                            l1 = lq[0]
                            Naziya['l1'] = l1 

                            f1 = secondlist[modalclass]
                            Naziya['f1'] = f1
                            f0 = secondlist[modalclass - 1]
                            Naziya['f0']  = f0
                            f2 = secondlist[modalclass + 1]
                            Naziya["f21"] = f2

                            la = int(lq[0])
                            la1 = int(lq[1])
                            Naziya["i"] = la1-la

                            min1 = f1-f0
                            Naziya["min1"] = min1
                            
                            min2 = (2*f1)-f0-f2
                            Naziya['min2'] = min2

                            mult = min1*(la1-la)
                            Naziya['mult'] = mult

                            divide = mult/min2
                            divide1 = NAZIYA.intfloatconverter(NAZIYA.floatstopper(divide))
                            Naziya['divide1'] = divide1
                            Naziya['mode'] = la+divide1

                        else:
                            # IF THERE IS NO NUMBER REPEATING AND LIST IS IN ORDERED FORM (SIMPLE METHOD)
                            Naziya['simplemethod'] = 1
                            maxf = max(secondlist)
                            f1index = secondlist.index(maxf)
                            f0 = secondlist[f1index-1]
                            f1 = secondlist[f1index]
                            f2 = secondlist[f1index+1]
                            l1list = li[f1index].strip().split('-')
                            i1 = 0
                            for i in range(1):
                                z = int(l1list[1]) - int(l1list[0])
                                i1+=z
                                Naziya['i'] = z

                            Naziya['f0'] = f0
                            Naziya['f1'] = f1
                            Naziya['f21'] = f2
                            Naziya['l1'] = int(l1list[0])

                            min1 = f1-f0
                            Naziya['min1'] = min1
                            min2 = (2*f1)-f0-f2
                            Naziya['min2'] = min2

                            mult = min1*i1
                            Naziya['mult'] = mult
                            divide = mult/min2
                            divide1 = NAZIYA.intfloatconverter(NAZIYA.floatstopper(divide))
                            Naziya['divide1'] = divide1

                            Naziya['mode'] = int(l1list[0])+divide1
                        NAZIYA.Database_Insertion('Continuous_Series',firstinput,secondinput,Collection_Name,IpAddress,'Class_Interval')
                    else:
                        # FOR DISCRETE SERIES
                        if len(list1) == len(list2):

                            firstlist = NAZIYA.intfloatconverter_list(list1)
                            Naziya['x'] = firstlist

                            secondlist = NAZIYA.intfloatconverter_list(list2)
                            Naziya['f'] = secondlist
                            checklist = NAZIYA.maxnum(secondlist)

                            if checklist == True:
                                Naziya['seriesname'] = "DISCRETE SERIES"
                                Naziya['method1'] = "Tally Method (Grouping Table)"
                                Naziya['tallymatch'] = "NaziyaParveen"

                                dash1 =[]
                                dash2 =[]
                                dash3 =[]
                                dash4 =[]
                                dash5 =[]
                                dash6 =[]
                                dash7 =[]
                                for i in range(len(secondlist)):
                                    dash1.append('-')
                                    dash2.append('-')
                                    dash3.append('-')
                                    dash4.append('-')
                                    dash5.append('-')
                                    dash6.append('-')
                                    dash7.append('-')

                                zero = 0
                                one = 1
                                g2_2 = []
                                for i in range(len(secondlist)//2):
                                    z = secondlist[zero] + secondlist[one]
                                    zero+= 2
                                    one+= 2 
                                    g2_2.append(z)
                                Naziya['g2_2'] = g2_2          
                                Naziya['leng2_2'] = len(g2_2)  

                                zer = 1
                                on = 2
                                g1_2_2 = []
                                for i in range((len(secondlist)-1)//2):
                                    z = secondlist[zer] + secondlist[on]
                                    zer+=2
                                    on+=2
                                    g1_2_2.append(z)
                                g1_2_2.insert(0,1)
                                Naziya['g1_2_2'] = g1_2_2

                                ze = 0
                                onze = 1
                                two = 2
                                g3_3 = []
                                for i in range(len(secondlist)//3):
                                    z = secondlist[ze] + secondlist[onze] + secondlist[two]
                                    ze+=3
                                    onze+=3
                                    two +=3
                                    g3_3.append(z)
                                Naziya['g3_3'] = g3_3
                                Naziya['leng3_3'] = len(g3_3)

                                naz1 = 1
                                naz2 = 2
                                naz3 = 3
                                g1_3_3 = []
                                for i in range((len(secondlist)-1) //3):
                                    z = secondlist[naz1] + secondlist[naz2] + secondlist[naz3]
                                    naz1 += 3
                                    naz2 += 3
                                    naz3 += 3
                                    g1_3_3.append(z)
                                g1_3_3.insert(0,1)
                                Naziya['g1_3_3'] = g1_3_3
                                Naziya['leng1_3_3'] = len(g1_3_3)

                                naz23 = 2
                                naz231 = 3
                                naz232 = 4
                                g2_3_3 = []
                                for i in range((len(secondlist)-2) //3):
                                    z = secondlist[naz23] + secondlist[naz231] + secondlist[naz232]
                                    naz23 += 3
                                    naz231 += 3
                                    naz232 += 3
                                    g2_3_3.append(z)
                                g2_3_3.insert(0,1)
                                Naziya['g2_3_3'] = g2_3_3
                                Naziya['leng2_3_3'] = len(g2_3_3)

                                ui = NAZIYA.Indexing(secondlist,max(secondlist)).Indexing_Function()
                                for i in ui:
                                    dash7[i] = "Naziya"

                                max7 = max(g2_2)
                                Naziya['max2_2'] = 7
                                max7_index = g2_2.index(max7)
                                max7_tal1 = (max7_index + 1)*2-1
                                max7_tal2 = (max7_index + 1)*2
                                dash1[max7_tal1 - 1] = "Naziya"
                                dash1[max7_tal2 - 1] = "Naziya"

                                max1 = max(g2_2)
                                Naziya['max2_2'] = max1
                                max1_index = g2_2.index(max1)
                                max1_tal1 = (max1_index + 1)*2-1
                                max1_tal2 = (max1_index + 1)*2
                                dash1[max1_tal1 - 1] = "Naziya"
                                dash1[max1_tal2 - 1] = "Naziya"

                                max2 = max(g1_2_2)
                                Naziya['max1_2_2'] = max2
                                max2_index = g1_2_2.index(max2)
                                max2_tal1 = (max2_index)*2
                                max2_tal2 = (max2_index)*2+1
                                dash2[max2_tal1 - 1] = "Naziya"
                                dash2[max2_tal2 - 1] = "Naziya"

                                max3 = max(g3_3)
                                Naziya['max3_3'] = max3
                                max3_index = g3_3.index(max3)
                                max3_tal1 = (max3_index+1)*3-2
                                max3_tal2 = (max3_index+1)*3-1
                                max3_tal3 = (max3_index + 1)*3
                                dash3[max3_tal1 - 1] = "Naziya"
                                dash3[max3_tal2 - 1] = "Naziya"
                                dash3[max3_tal3 - 1] = "Naziya"

                                max4 = max(g1_3_3)
                                Naziya['max1_3_3'] = max4
                                max4_index = g1_3_3.index(max4)
                                max4_tal1 = (max4_index)*3+1
                                max4_tal2 = (max4_index)*3-1
                                max4_tal3 = (max4_index )*3
                                dash4[max4_tal1 - 1] = "Naziya"
                                dash4[max4_tal2 - 1] = "Naziya"
                                dash4[max4_tal3 - 1] = "Naziya"

                                max5 = max(g2_3_3)
                                Naziya['max2_3_3'] = max5
                                max5_index = g2_3_3.index(max5)
                                max5_tal1 = (max5_index)*3+1
                                max5_tal2 = (max5_index)*3
                                max5_tal3 = (max5_index)*3+2

                                dash5[max5_tal1 - 1] = "Naziya"
                                dash5[max5_tal2 - 1] = "Naziya"
                                dash5[max5_tal3 - 1] = "Naziya"

                                Naziya['dash1'] = dash1
                                Naziya['dash2'] = dash2
                                Naziya['dash3'] = dash3
                                Naziya['dash4'] = dash4
                                Naziya['dash5'] = dash5
                                Naziya['dash6'] = dash6
                                Naziya['dash7'] = dash7

                                tallydict = {}
                                for i in range(len(secondlist)+1):
                                    tallydict[i] = 0

                                ex = NAZIYA.Indexing(dash1,"Naziya").Indexing_Function()
                                for i in ex:
                                    tallydict[i] += 1

                                ex2 = NAZIYA.Indexing(dash2,"Naziya").Indexing_Function()
                                for i in ex2:
                                    tallydict[i] += 1

                                ex3 = NAZIYA.Indexing(dash3,"Naziya").Indexing_Function()
                                for i in ex3:
                                    tallydict[i] += 1
                                
                                ex4 = NAZIYA.Indexing(dash4,"Naziya").Indexing_Function()
                                for i in ex4:
                                    tallydict[i] += 1

                                ex5 = NAZIYA.Indexing(dash5,"Naziya").Indexing_Function()
                                for i in ex5:
                                    tallydict[i] += 1

                                ex6 = NAZIYA.Indexing(dash6,"Naziya").Indexing_Function()
                                for i in ex6:
                                    tallydict[i] += 1

                                ex7 = NAZIYA.Indexing(dash7,"Naziya").Indexing_Function()
                                for i in ex7:
                                    tallydict[i] += 1

                                inde = [tallydict[i] for i in tallydict]

                                modalclass = inde.index(max(inde))
                                dash6[modalclass] = "Naziya"

                                modalcl = li[modalclass]
                                Naziya['modeclass'] = modalcl
                            else:
                                Naziya['seriesname'] = "DISCRETE SERIES"
                                Naziya['method1'] = "Solved With Inspection Method"

                                Naziya['sumf'] = sum(secondlist)
                                Naziya['indiformulamatch'] = "1"

                                mo = secondlist.index(max(secondlist))
                                Naziya['mode'] = firstlist[mo]
                            # DATABASE
                            NAZIYA.Database_Insertion('Discrete_Series', firstinput, secondinput, Collection_Name, IpAddress, 'Items')
                        else:
                            if secondinput == '0':
                                Naziya['seriesname'] = "INDIVIDUAL SERIES"

                                firstlist = NAZIYA.intfloatconverter_list(list1)
                                Naziya['x'] = firstlist

                                for i in list2:
                                    y2 = int(i)
                                    Naziya['f1'] = y2
                                Naziya['len1'] = len(list1)

                                naz = dict(Counter(firstlist))
                                key = [i for i in naz]
                                value = [naz[i] for i in naz]

                                z = [1 for i in value if i == max(value)]
                                if len(z) == len(value):
                                    Naziya['mode'] = "Mode Is not possible"
                                else:
                                    maxval = max(value) 
                                    z = NAZIYA.Indexing(value, maxval).Indicies()
                                    mode = [key[i] for i in z]
                                    Naziya['mode'] = mode
                                    Naziya['lenmode'] = len(mode)
                                    #DATABASE
                                NAZIYA.Database_Insertion('Individual_Series', firstinput,secondinput,Collection_Name,IpAddress,'Items')
                            else:
                                if len(list1) != len(list2):
                                    Naziya['x2'] = len(list1)
                                    Naziya['f2'] = len(list2)
                                    Naziya['seriesname1'] = "Please Check that lenght of both( X/C.I. and frequency is equal or may be you entered Two (,,) Commas )"
                                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
                except:
                    Naziya['allerror'] = 'Handle'
                    Naziya['seriesname1'] = 'Please Enter Your Question Correctly'
                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
    return render(request, "Mathsmode.html", Naziya)

def mathsrange(request):

    Naziya = {'root':[],
        'parveen':'Click Below To Solve Range, Coefficient Of Range',
        'cando':'Please enter your question with comma seperated in textbox',
        'question':'Range',
        'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
        'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',
        'classinterval1':[],}
    
    if request.method == "POST":

        firstinput = request.POST.get('firstinput')
        secondinput = request.POST.get('secondinput')

        Collection_Name = Database_Name["Range"]
        IpAddress = NAZIYA.IP_Address(request)

        Checking_Existence = [i for i in Collection_Name.find({'User': IpAddress}, {'User':1, '_id':0})]

        Collection_Name.insert_one({'User' : IpAddress,'Continuous_Series': {}, 'Discrete_Series':{}, 'Individual_Series': {}, 'Errors':{}}) if Checking_Existence == [] else None

        if firstinput == '' and secondinput == '':
            Naziya['seriesname1'] = 'Please Enter Your Question First'
            Naziya['emp'] = 0
        else:
            if firstinput == '':
                Naziya['seriesname1'] = 'Please Enter X (No. of items) or C.I. (Class Interval)'
                Naziya['emp'] = 0
            else:
                try:
                    if secondinput == '':
                        secondinput = '0'
                    Naziya['match'] = secondinput

                    # SEPERATING WITH COMMA
                    list12 = (firstinput).strip().split(',')
                    listnaz = (secondinput).strip().split(',')

                    list2 = NAZIYA.ErrorHandling(listnaz).Empty_Error()
                    list1 = list12
                    li = list12

                    try:
                        cixitem = NAZIYA.ErrorHandling(li).Try()
                    except ValueError:
                        q = NAZIYA.ErrorHandling(list12).Dash_Error()
                        colo = NAZIYA.ErrorHandling(q).Exception()
                        li = colo[0]
                        cixitem = colo[1]
                        cilis = colo[2]

                    if len(cixitem) == len(list2):
                        Naziya['seriesname'] = "CONTINUOUS SERIES"
                        Naziya['classinterval'] = li

                        # # SECOND LIST
                        secondlist = NAZIYA.intfloatconverter_list(list2)
                        Naziya['f'] = secondlist

                        hf = int(max(cilis))
                        lf = int(min(cilis))
                        Naziya['highestf'] = hf
                        Naziya['lowestf'] = lf
                        Naziya['rang'] = hf - lf
                        Naziya['add1'] = hf + lf
                        Naziya['coefficientofrange'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(((hf-lf)/(hf+lf))))

                        NAZIYA.Database_Insertion('Continuous_Series',firstinput,secondinput,Collection_Name,IpAddress,'Class_Interval')
                    else:
                        # FOR DISCRETE SERIES
                        if len(list1) == len(list2):
                            Naziya['seriesname'] = "DISCRETE SERIES"
                            Naziya['fseries'] = 2

                            firstlist = NAZIYA.intfloatconverter_list(list1)
                            Naziya['x'] = firstlist

                            secondlist = NAZIYA.intfloatconverter_list(list2)
                            Naziya['f'] = secondlist

                            hf = max(firstlist)
                            lf = min(firstlist)

                            Naziya['highestf'] = hf
                            Naziya['lowestf'] = lf

                            Naziya['rang'] = hf - lf
                            Naziya['add1'] = hf + lf

                            Naziya['coefficientofrange'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(((hf-lf)/(hf+lf))))
                            # DATABASE
                            NAZIYA.Database_Insertion('Discrete_Series', firstinput, secondinput, Collection_Name, IpAddress, 'Items')
                        else:
                            if secondinput == '0':
                                Naziya['seriesname'] = "INDIVIDUAL SERIES"
                                try:
                                    firstlist = NAZIYA.intfloatconverter_list(list1)
                                    Naziya['x'] = firstlist

                                    for i in list2:
                                        y2 = int(i)
                                        Naziya['f1'] = y2

                                    Naziya['len1'] = len(list1)

                                    hf = max(firstlist)
                                    lf = min(firstlist)

                                    Naziya['highestf'] = hf
                                    Naziya['lowestf'] = lf

                                    Naziya['rang'] = hf - lf
                                    Naziya['add1'] = hf + lf

                                    Naziya['coefficientofrange'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(((hf-lf)/(hf+lf))))

                                except ValueError:
                                    Naziya['seriesname'] = 'Continuous Series'
                                    Naziya['classinterval1'] = li

                                    firstlist = []
                                    hf = max(cilis)
                                    lf = min(cilis)

                                    Naziya['highestf'] = hf
                                    Naziya['lowestf'] = lf
                                    Naziya['rang'] = hf - lf
                                    Naziya['add1'] = hf + lf
                                    Naziya['coefficientofrange'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(((hf-lf)/(hf+lf))))
                                #DATABASE
                                NAZIYA.Database_Insertion('Individual_Series', firstinput,secondinput,Collection_Name,IpAddress,'Items')
                            else:
                                if len(list1) != len(list2):
                                    Naziya['x2'] = len(list1)
                                    Naziya['f2'] = len(list2)
                                    Naziya['seriesname1'] = "Please Check that lenght of both( X/C.I. and frequency is equal or may be you entered Two (,,) Commas )"
                                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
                except:
                    Naziya['allerror'] = 'Handle'
                    Naziya['seriesname1'] = 'Please Enter Your Question Correctly'
                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
    return render(request, "Mathsrange.html", Naziya)
    
def quartile(request):

    Naziya = {'root':[],
        'parveen': 'Click Below To Solve Quartile Deviation (Semi Inter Quartile), Inter Quartile Range, Coefficient Of Quartile Deviation',
        'cando':'Please enter your question with comma seperated in textbox',
        'question':'Quartile',
        'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
        'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',}

    if request.method == "POST":

        firstinput = request.POST.get('firstinput')
        secondinput = request.POST.get('secondinput')

        Collection_Name = Database_Name["Quartile"]
        IpAddress = NAZIYA.IP_Address(request)

        Checking_Existence = [i for i in Collection_Name.find({'User': IpAddress}, {'User':1, '_id':0})]

        Collection_Name.insert_one({'User' : IpAddress,'Continuous_Series': {}, 'Discrete_Series':{}, 'Individual_Series': {}, 'Errors':{}}) if Checking_Existence == [] else None

        if firstinput == '' and secondinput == '':
            Naziya['seriesname1'] = 'Please Enter Your Question First'
            Naziya['emp'] = 0
        else:
            if firstinput == '':
                Naziya['seriesname1'] = 'Please Enter X (No. of items) or C.I. (Class Interval)'
                Naziya['emp'] = 0
            else:
                try:
                    if len(firstinput) in range(6):
                        Naziya['seriesname1'] = "Please enter atleast 3 comma seperated value to calculate quartile"
                        Naziya['emp'] = 0
                    else:
                        if secondinput == '':
                            secondinput = '0'
                        Naziya['match'] = secondinput

                        list12 = (firstinput).strip().split(',')
                        listnaz = (secondinput).strip().split(',')
                            
                        list2 = NAZIYA.ErrorHandling(listnaz).Empty_Error()
                        list1 = list12
                        li = list12

                        try:
                            cixitem = NAZIYA.ErrorHandling(li).Try()
                        except ValueError:
                            q = NAZIYA.ErrorHandling(list12).Dash_Error()
                            colo = NAZIYA.ErrorHandling(q).Exception()
                            li = colo[0]
                            cixitem = colo[1]

                        if len(cixitem) == 1:
                            cixitem.append(189)

                        if len(cixitem) == len(list2):
                            Naziya['seriesname'] = "CONTINUOUS SERIES"
                            Naziya['len1'] = len(list1)
                            Naziya['lencon'] = 56
                            Naziya['dislen'] = 10
                            Naziya['horrible'] = 10
                            Naziya['len'] = len(list1)

                            c_I = [i for i in li]
                            Naziya['classinterval'] = c_I
                            f = NAZIYA.intfloatconverter_list(list2)
                            Naziya['f'] = f

                            Naziya['lengthofseries'] = sum(f)
                            classfind = NAZIYA.intfloatconverter(sum(f)/4)
                            classfind1 = NAZIYA.intfloatconverter(classfind*3)
                            Naziya['classfind'] = NAZIYA.floatstopper(NAZIYA.intfloatconverter(classfind))

                            Naziya['classfind1'] = NAZIYA.floatstopper(NAZIYA.intfloatconverter(classfind1))

                            # TAKING SUM OF F
                            Naziya['sumf'] = sum(f)

                            # TAKING N/2
                            sum_f = NAZIYA.intfloatconverter(sum(f)/2)
                            Naziya['n2'] = sum_f

                            # TAKING CUMULATIVE FREQUENCY
                            cf = NAZIYA.Cumulative(f)
                            Naziya['cf'] = cf

                            indexing = 0
                            thirdstep = 0
                            for i in cf:
                                if i >= sum(f)/4:
                                    a1 = cf.index(i)
                                    cfp = cf[a1 - 1]
                                    z = c_I[a1]
                                    indexing += a1
                                    Naziya['q1class'] = z
                                    f1 = f[a1]
                                    Naziya['fforq1'] = f1

                                    lisforclass = NAZIYA.intfloatconverter_list(z.strip().split('-'))

                                    lforclass = lisforclass[0]
                                    Naziya['lforclass'] = lforclass
                                    Naziya['cfpforclass'] = cfp

                                    iforclass = lisforclass[1] - lisforclass[0]
                                    Naziya['iforclass'] = iforclass

                                    step1 = classfind - cfp
                                    Naziya['step1'] = step1

                                    step2 = step1*iforclass
                                    Naziya['step2'] = NAZIYA.intfloatconverter(step2)

                                    step3 = step2/f1
                                    Naziya['step3'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper2(step3))

                                    q1 = NAZIYA.intfloatconverter(NAZIYA.floatstopper2(step3 + lforclass))
                                    Naziya['q1'] = q1
                                    thirdstep+= q1
                                    break
                            Naziya['thirdstep'] = NAZIYA.intfloatconverter(thirdstep)
                                
                            indexing1 = 0
                            q3thirdstep = 0
                            for i in cf:
                                if i >= classfind1:
                                    a1 = cf.index(i)
                                    cfp = cf[a1 - 1]
                                    z = c_I[a1]
                                    indexing1 += a1
                                    Naziya['q3class1'] = z
                                    f1 = f[a1]
                                    Naziya['fforq11'] = f1

                                    lisforclass = NAZIYA.intfloatconverter_list(z.strip().split('-'))

                                    lforclass = lisforclass[0]
                                    Naziya['lforclass1'] = lforclass
                                    Naziya['cfpforclass1'] = cfp

                                    iforclass = lisforclass[1] - lisforclass[0]
                                    Naziya['iforclass1'] = iforclass

                                    step1 = classfind1 - cfp
                                    Naziya['step11'] = step1

                                    step2 = step1*iforclass
                                    Naziya['step21'] = NAZIYA.intfloatconverter(step2)

                                    step3 = step2/f1
                                    Naziya['step31'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper2(step3))

                                    q3 = NAZIYA.intfloatconverter(NAZIYA.floatstopper2(step3 + lforclass))
                                    Naziya['q3'] = q3
                                    q3thirdstep+=q3
                                    break

                            Naziya['q3thirdstep'] = NAZIYA.intfloatconverter(q3thirdstep)
                                
                            variab = NAZIYA.intfloatconverter(NAZIYA.floatstopper2((q3thirdstep - thirdstep)))
                            Naziya['min1'] = variab
                            variab1 = NAZIYA.intfloatconverter(NAZIYA.floatstopper2((q3thirdstep + thirdstep)))
                            Naziya['add1'] = variab1

                            Naziya['divide'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper2((variab/2)))

                            Naziya['coqd'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(variab/variab1))
                            NAZIYA.Database_Insertion('Continuous_Series',firstinput,secondinput,Collection_Name,IpAddress,'Class_Interval')
                        else:
                            if len(list1) == len(list2):
                                Naziya['seriesname'] = "DISCRETE SERIES"

                                Naziya['fseries'] = 2
                                naziya = {}
                                Naziya['len1'] = len(list1)
                                Naziya['dislen'] = len(list1)

                                firstlist = NAZIYA.intfloatconverter_list(list1)
                                firstlistcopy = firstlist.copy()
                                Naziya['x'] = firstlist

                                firstlistcopy.sort()
                                Naziya['sortx'] = firstlistcopy

                                f12 = NAZIYA.intfloatconverter_list(list2)
                                fcopy = f12.copy()

                                for key,value in zip(firstlist,fcopy):
                                    naziya[key] = value
                                
                                f = [naziya[i] for i in firstlistcopy]
                                Naziya['f'] = f
                                Naziya['sumf'] = sum(f)
                                Naziya['lengthofseries'] = sum(f)

                                cf = NAZIYA.Cumulative(f)
                                Naziya['cf'] = cf

                                n = sum(f)
                                firststep = n + 1
                                Naziya['firststep'] = firststep

                                secondstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(firststep / 4))
                                
                                Naziya['secondstep'] = secondstep

                                thirdstep = 0
                                if secondstep == int(secondstep):
                                    for i in cf:
                                        if secondstep <= i:
                                            z = cf.index(i)
                                            y = firstlist[z]
                                            thirdstep += y
                                            break
                                else:
                                    if type(secondstep) == float:

                                        Naziya['floatmethod'] = 2
                                        aa = secondstep
                                        q = str(aa)
                                        z = (q).strip().split(".")

                                        first = int(z[0])
                                        Naziya['first'] = first
                                        a = float('.'+z[1])
                                        Naziya['a'] = a
                                        
                                        roundfirst = math.floor(secondstep)
                                        roundsecond = math.ceil(secondstep)
                                        Naziya['roundfirst'] = roundfirst
                                        Naziya['roundsecond'] = roundsecond

                                        fs1 = NAZIYA.Indexing(cf,first,firstlistcopy).Quartile_Indexing()
                                        Naziya['fs1'] = fs1

                                        fs2 = NAZIYA.Indexing(cf,roundfirst,firstlistcopy).Quartile_Indexing()
                                        Naziya['fs2'] = fs2

                                        fs3 = NAZIYA.Indexing(cf,roundsecond,firstlistcopy).Quartile_Indexing()
                                        Naziya['fs3'] = fs3

                                        var = fs3 - fs2
                                        Naziya['firstsolve'] = var

                                        var1 = NAZIYA.intfloatconverter(a*var)
                                        Naziya['secondsolve'] = var1
                                        var3 = fs1 + var1
                                        thirdstep += var3

                                Naziya['thirdstep'] = NAZIYA.intfloatconverter(thirdstep)

                                q3thterm = 3*secondstep
                                Naziya['q3thterm'] = NAZIYA.intfloatconverter(q3thterm)

                                q3thirdstep = 0
                                if q3thterm == int(q3thterm):
                                    for i in cf:
                                        if q3thterm <= i:
                                            q3thirdstep += firstlistcopy[cf.index(i)]
                                            break
                                else:
                                    if type(q3thterm) == float:
                                        Naziya['floatmethod1'] = 2
                                        aa = q3thterm
                                        q = str(aa)
                                        z = (q).strip().split(".")

                                        first = int(z[0])
                                        Naziya['first1'] = first
                                        a = float('.'+z[1])
                                        Naziya['a1'] = a
                                        
                                        roundfirst = math.floor(q3thterm)
                                        roundsecond = math.ceil(q3thterm)
                                        Naziya['roundfirst1'] = roundfirst
                                        Naziya['roundsecond1'] = roundsecond
                                        
                                        fs1 = NAZIYA.Indexing(cf,first,firstlistcopy).Quartile_Indexing()
                                        Naziya['fs11'] = fs1

                                        fs2 = NAZIYA.Indexing(cf,roundfirst,firstlistcopy).Quartile_Indexing()
                                        Naziya['fs21'] = fs2

                                        fs3 = NAZIYA.Indexing(cf,roundsecond,firstlistcopy).Quartile_Indexing()
                                        Naziya['fs31'] = fs3
                                        var = fs3 - fs2
                                        Naziya['firstsolve1'] = var

                                        var1 = a*var
                                        Naziya['secondsolve1'] = var1
                                        var3 = fs1 + var1
                                        q3thirdstep += var3

                                Naziya['q3thirdstep'] = NAZIYA.intfloatconverter(q3thirdstep)
                                variab = NAZIYA.intfloatconverter(q3thirdstep - thirdstep)
                                Naziya['min1'] = variab
                                variab1 = NAZIYA.intfloatconverter(q3thirdstep + thirdstep)
                                Naziya['add1'] = variab1

                                Naziya['divide'] = NAZIYA.intfloatconverter(variab/2)
                                Naziya['coqd'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(variab/variab1))
                                # DATABASE
                                NAZIYA.Database_Insertion('Discrete_Series', firstinput, secondinput, Collection_Name, IpAddress, 'Items')
                            else:
                                if  secondinput == '0':
                                    Naziya['seriesname'] = "INDIVIDUAL SERIES"
                                    Naziya['lenf1'] = 0
                                    Naziya['len2'] = len(list1)
                                    
                                    firstlist = NAZIYA.intfloatconverter_list(list1)
                                    Naziya['x'] = firstlist
                                    copy = firstlist.copy()
                                    copy21 = set(copy)

                                    copy2 = [i for i in copy21]
                                    copy2.sort()
                                    Naziya['len1'] = len(copy2)
                                    Naziya['lengthofseries'] = len(copy2)

                                    Naziya['sortx'] = copy2
                                    for i in list2:
                                        y2 = int(i)
                                        Naziya['f1'] = y2

                                    n = len(copy2)
                                    firststep = n + 1
                                    Naziya['firststep'] = firststep
                                    secondstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(firststep / 4))
                                    
                                    Naziya['secondstep'] = secondstep
                                    thirdstep = 0
                                    if secondstep == int(secondstep):
                                        z = copy2[secondstep - 1]
                                        thirdstep += z
                                    else:
                                        if type(secondstep) == float:
                                            Naziya['floatmethod'] = 2
                                            aa = secondstep
                                            q = str(aa)
                                            z = (q).strip().split(".")

                                            first = int(z[0])
                                            Naziya['first'] = first
                                            a = float('.'+z[1])
                                            Naziya['a'] = a
                                            
                                            roundfirst = math.floor(secondstep)
                                            roundsecond = math.ceil(secondstep)
                                            Naziya['roundfirst'] = roundfirst
                                            Naziya['roundsecond'] = roundsecond

                                            one = first -1
                                            two = roundfirst -1
                                            three = roundsecond -1
                                            fs1 = copy2[one]
                                            fs2 = copy2[two]
                                            fs3 = copy2[three]
                                            Naziya['fs1'] = fs1
                                            Naziya['fs3'] = fs3
                                            Naziya['fs2'] = fs2

                                            var = fs3 - fs2
                                            Naziya['firstsolve'] = var
                                            var1 = a*var
                                            Naziya['secondsolve'] = var1
                                            var3 = fs1 + var1
                                            thirdstep += var3

                                    Naziya['thirdstep'] = thirdstep
                                    q3thterm = 3*secondstep
                                    Naziya['q3thterm'] = q3thterm

                                    q3thirdstep = 0
                                    if q3thterm == int(q3thterm):
                                        z = copy2[q3thterm - 1]
                                        q3thirdstep += z
                                    else:
                                        if type(q3thterm) == float:
                                            Naziya['floatmethod1'] = 2
                                            aa = q3thterm
                                            q = str(aa)
                                            z = (q).strip().split(".")

                                            first = int(z[0])
                                            Naziya['first1'] = first
                                            a = float('.'+z[1])
                                            Naziya['a1'] = a
                                            
                                            roundfirst = math.floor(q3thterm)
                                            roundsecond = math.ceil(q3thterm)
                                            Naziya['roundfirst1'] = roundfirst
                                            Naziya['roundsecond1'] = roundsecond

                                            one = first -1
                                            two = roundfirst -1
                                            three = roundsecond -1
                                            fs1 = copy2[one]
                                            fs2 = copy2[two]
                                            fs3 = copy2[three]
                                            Naziya['fs11'] = fs1
                                            Naziya['fs31'] = fs3
                                            Naziya['fs21'] = fs2

                                            var = fs3 - fs2
                                            Naziya['firstsolve1'] = var
                                            var1 = a*var
                                            Naziya['secondsolve1'] = var1
                                            var3 = fs1 + var1
                                            q3thirdstep += var3

                                    Naziya['q3thirdstep'] = q3thirdstep
                                    variab = NAZIYA.intfloatconverter(q3thirdstep - thirdstep)
                                    Naziya['min1'] = variab
                                    variab1 = NAZIYA.intfloatconverter(q3thirdstep + thirdstep)
                                    Naziya['add1'] = variab1
                                    Naziya['divide'] = variab/2
                                    Naziya['coqd'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(variab/variab1))
                                    #DATABASE
                                    NAZIYA.Database_Insertion('Individual_Series', firstinput,secondinput,Collection_Name,IpAddress,'Items')
                                else:
                                    if len(list1) != len(list2):
                                        Naziya['x2'] = len(list1)
                                        Naziya['f2'] = len(list2)
                                        Naziya['seriesname1'] = "Please Check that lenght of both( X/C.I. and frequency is equal or may be you entered Two (,,) Commas )"
                                        NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
                except:
                    Naziya['allerror'] = 'Handle'
                    Naziya['seriesname1'] = 'Please Enter Your Question Correctly'
                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
    return render(request, "Mathsquartile.html",Naziya)

def MeanDeviation(request):

    Naziya = {'root':[],
        'parveen':'Click Below To Solve Mean Deviation (Direct and Indirect Method with Mean/Median), Coefficient Of Mean Deviation',
        'cando':'Please enter your question with comma seperated in textbox',
        'question':'Mean Deviation',
        'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
        'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',}

    if request.method == "POST":

        firstinput = request.POST.get('firstinput')
        secondinput = request.POST.get('secondinput')

        Collection_Name = Database_Name["MeanDeviation"]
        IpAddress = NAZIYA.IP_Address(request)

        Checking_Existence = [i for i in Collection_Name.find({'User': IpAddress}, {'User':1, '_id':0})]

        Collection_Name.insert_one({'User' : IpAddress,'Continuous_Series': {}, 'Discrete_Series':{}, 'Individual_Series': {}, 'Errors':{}}) if Checking_Existence == [] else None

        if firstinput == '' and secondinput == '':
            Naziya['seriesname1'] = 'Please Enter Your Question First'
            Naziya['emp'] = 0
        else:
            if firstinput == '':
                Naziya['seriesname1'] = 'Please Enter X (No. of items) or C.I. (Class Interval)'
                Naziya['emp'] = 0
            else:
                try:
                    if secondinput == '':
                        secondinput = '0'
                    Naziya['match'] = secondinput

                    # SEPERATING WITH COMMA
                    list12 = (firstinput).strip().split(',')
                    listnaz = (secondinput).strip().split(',')

                    list2 = NAZIYA.ErrorHandling(listnaz).Empty_Error()
                    list1 = list12
                    li = list12

                    try:
                        cixitem = NAZIYA.ErrorHandling(li).Try()
                    except ValueError:
                        q = NAZIYA.ErrorHandling(list12).Dash_Error()
                        colo = NAZIYA.ErrorHandling(q).Exception()
                        li = colo[0]
                        cixitem = colo[1]

                    if len(cixitem) == len(list2):
                        Naziya['seriesname'] = "CONTINUOUS SERIES"
                        Naziya['method1'] = "Solved With Mean"
                        Naziya['classinterval'] = li

                        firstlist = NAZIYA.intfloatconverter_list_ifelse(cixitem)
                        Naziya['x'] = firstlist

                        # # SECOND LIST
                        secondlist = NAZIYA.intfloatconverter_list(list2)
                        Naziya['f'] = secondlist

                        sumof_x = sum(cixitem)
                        Naziya["sumx"]= sumof_x

                        # SUM OF F SECOND LIST
                        sumof_f = sum(secondlist)
                        Naziya["sumf"]= sumof_f
                        par = NAZIYA.multiply(firstlist,secondlist)
                        Naziya['fx'] = par
                        Naziya['sumfx'] = NAZIYA.intfloatconverter(sum(par))

                        acm = NAZIYA.intfloatconverter(NAZIYA.floatstopper((sum(par)/sum(secondlist))))
                        Naziya['actualmean'] = acm

                        d = [abs(NAZIYA.intfloatconverter(NAZIYA.floatstopper(acm-i))) for i in cixitem]
                        Naziya['d'] = d
                        dlist = NAZIYA.String_Add(cixitem,acm,firstlist,d)
                        Naziya['dlist1'] = dlist

                        o = 0
                        lk = []
                        for i in secondlist:
                            k = NAZIYA.intfloatconverter(NAZIYA.floatstopper(i*d[o]))
                            o+=1
                            lk.append((k))
                        Naziya['fd'] = lk
                        Naziya['sumfd'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(lk)))

                        va = NAZIYA.intfloatconverter(sum(lk)/sum(secondlist))
                        Naziya["meand"] = va

                        # MEDIAN METHOD FOR MEAN DEVIATION
                        Naziya['method2'] = "Solved With Median"

                        sum_f = NAZIYA.intfloatconverter(sum(secondlist)/2)
                        Naziya['n2'] = sum_f

                        # TAKING CUMULATIVE FREQUENCY
                        cf = NAZIYA.Cumulative(secondlist)
                        Naziya['cf'] = cf

                        # CHOOSING CLOSEST VALUE IN LIST
                        val= NAZIYA.closestvalue(cf,sum_f)
                        indexing = NAZIYA.Indexing(val,sum_f,cf).Median_Indexing()

                        # TAKING POSITION IN LIST
                        cfp = cf[indexing-1]
                        Naziya['cfp'] = cfp

                        # TAKING F1 AND L1
                        f1 = secondlist[indexing] #F1
                        Naziya['f1'] = f1
                        
                        l = (li[indexing]).strip().split('-')
                        l1 = int(l[0]) #L1
                        Naziya['L1'] = l1

                        Naziya['i'] = int(l[0]) - int(l[1]) if int(l[0]) > int(l[1]) else int(l[1]) - int(l[0])

                        divide1 = sum_f/1

                        Naziya['divide1'] = int(divide1) if divide1 == int(divide1) else divide1 

                        calc = (divide1 - cfp) * Naziya['i']
                        calc1 = NAZIYA.intfloatconverter(calc)
                        Naziya['multiply1'] = calc1

                        med = calc1 / f1
                        med1 = NAZIYA.intfloatconverter(NAZIYA.floatstopper(l1 + med))
                        Naziya['divide2'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(med))
                        Naziya['median'] = med1

                        dmedian = [abs(NAZIYA.intfloatconverter(NAZIYA.floatstopper(med1 - i))) for i in cixitem]
                        Naziya['dmedian'] = dmedian

                        dlist5 = NAZIYA.String_Add(cixitem,med1,firstlist,dmedian)
                        Naziya['dlist5'] = dlist5

                        o1 = 0
                        lk1 = []
                        for i in secondlist:
                            k = NAZIYA.intfloatconverter(NAZIYA.floatstopper(i*dmedian[o1]))
                            o1+=1
                            lk1.append((k))

                        Naziya['fdmedian'] = lk1
                        Naziya['sumfdmedian'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(lk1)))

                        mediand = NAZIYA.intfloatconverter(sum(lk1)/sumof_f)
                        Naziya['mediand'] = mediand

                        # SOLVED WITH MEAN SHORTCUT METHOD
                        Naziya['method3'] = "Solved With Mean (Shortcut Method)"
                        df = NAZIYA.Indexing(cixitem,acm).Single_Side_Indexing()

                        # FOR SIGMAFXA AND SIGMAFXB
                        zs_tuple = NAZIYA.Summation_Value(cixitem,df,acm,par)
                        sigmafxa = sum(zs_tuple[0])
                        sigmafxb = sum(zs_tuple[1])
                        Naziya['sigmafxa'] = sigmafxa
                        Naziya['sigmafxb'] = sigmafxb

                        # FOR SIGMAFA AND SIGMAFB
                        zq_tuple = NAZIYA.Summation_Value(cixitem,df,acm,secondlist)
                        sigmafa = sum(zq_tuple[0])
                        sigmafb = sum(zq_tuple[1])
                        Naziya['sigmafa'] = sigmafa
                        Naziya['sigmafb'] = sigmafb

                        firststep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmafxa - sigmafxb))
                        Naziya['firststep'] = firststep
                        secondstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmafa - sigmafb))
                        Naziya['secondstep'] = secondstep
                        thirdstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(secondstep*acm))
                        Naziya['thirdstep'] = thirdstep

                        if thirdstep < 0:
                            Naziya['showplus'] = 'nazpar'
                            Naziya['thirdstep1'] = abs(thirdstep)

                        fourthstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(firststep - thirdstep))
                        Naziya['fourthstep'] = fourthstep

                        fifthstep = NAZIYA.intfloatconverter(fourthstep/sumof_f)
                        Naziya['fifthstep'] = fifthstep

                        # SOLVED WITH MEDIAN (SHORTCUT METHOD)
                        Naziya['method4'] = "Solved With Median (Shortcut Method)"
                        dfm = NAZIYA.Indexing(cixitem,med1).Single_Side_Indexing()

                        # FOR SIGMAFXAM AND SIGMAFXBM
                        zsm_tuple = NAZIYA.Summation_Value(cixitem,dfm,med1,par)
                        sigmafxam = sum(zsm_tuple[0])
                        sigmafxbm = sum(zsm_tuple[1])
                        Naziya['sigmafxam'] = sigmafxam
                        Naziya['sigmafxbm'] = sigmafxbm

                        # FOR SIGMAFA AND SIGMAFB
                        zqm_tuple = NAZIYA.Summation_Value(cixitem,dfm,med1,secondlist)
                        sigmafam = sum(zqm_tuple[0])
                        sigmafbm = sum(zqm_tuple[1])
                        Naziya['sigmafam'] = sigmafam
                        Naziya['sigmafbm'] = sigmafbm

                        firststepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmafxam - sigmafxbm))
                        Naziya['firststepm'] = firststepm

                        secondstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmafam - sigmafbm))
                        Naziya['secondstepm'] = secondstepm

                        thirdstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(secondstepm*med1))
                        Naziya['thirdstepm'] = thirdstepm

                        if thirdstepm < 0:
                            Naziya['showplusm'] = 'showplusm'
                            Naziya['thirdstep1m'] = abs(thirdstepm)

                        fourthstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(firststepm - thirdstepm))
                        Naziya['fourthstepm'] = fourthstepm
                        fifthstepm = NAZIYA.intfloatconverter(fourthstepm/sumof_f)
                        Naziya['fifthstepm'] = fifthstepm

                        # CALCULATION OF COEFFICIENT OF MEAN DEVIATION
                        Naziya['coefficientmdmean'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(va))
                        Naziya['coefficientmean'] = acm

                        calcofcomd = NAZIYA.intfloatconverter(NAZIYA.floatstopper(va/acm))
                        Naziya['coefficientofmdmean'] = calcofcomd

                        Naziya['coefficientmdmedian'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(mediand))
                        Naziya['coefficientmedian'] = med1

                        calcofcomdm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(mediand/med1))
                        Naziya['coefficientofmdmedian'] = calcofcomdm
                        NAZIYA.Database_Insertion('Continuous_Series',firstinput,secondinput,Collection_Name,IpAddress,'Class_Interval')
                    else:
                        # FOR DISCRETE SERIES
                        if len(list1) == len(list2):
                            # MEAN METHOD
                            Naziya['seriesname'] = "DISCRETE SERIES"
                            Naziya['method1'] = "Solved With Mean"
                            naziya = {}
                            firstlist = NAZIYA.intfloatconverter_list(list1)
                            firstlistcopy = firstlist.copy()
                            firstlistcopy.sort()
                            Naziya['x'] = firstlistcopy

                            secondlist = NAZIYA.intfloatconverter_list(list2)
                            secondlistcopy = secondlist.copy()

                            for key,value in zip(firstlist,secondlistcopy):
                                naziya[key] = value
                                
                            f = [naziya[i] for i in firstlistcopy]
                            Naziya['f'] = f
                            sumof_x = sum(firstlist)
                            Naziya["sumx"]= sumof_x
                            # SUM OF F SECOND LIST
                            sumof_f = sum(secondlist)
                            Naziya["sumf"]= sumof_f

                            par = NAZIYA.multiply(firstlistcopy,f)
                            Naziya['fx'] = par
                            Naziya['sumfx'] = sum(par)

                            acm = NAZIYA.intfloatconverter(NAZIYA.floatstopper((sum(par)/sum(secondlist))))
                            Naziya['actualmean'] = acm

                            d = [NAZIYA.floatstopper(abs(NAZIYA.intfloatconverter(acm - i))) for i in firstlistcopy]
                            Naziya['d'] = d

                            dlist = NAZIYA.String_Add(firstlistcopy,acm,d)
                            Naziya['dlist1'] = dlist

                            o = 0
                            lk = []
                            for i in f:
                                k = NAZIYA.intfloatconverter(NAZIYA.floatstopper(i*d[o]))
                                o+=1
                                lk.append((k))

                            # TAKING MEAN DEVIATION WITH MEAN (SIMPLE)
                            Naziya['fd'] = lk
                            Naziya['sumfd'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(lk)))
                            va = NAZIYA.intfloatconverter(sum(lk)/sum(secondlist))
                            Naziya["meand"] = va
                            # END OF MEAN METHOD

                            # Solved With Median (Simple Method)
                            cf = NAZIYA.Cumulative(f)
                            Naziya['cf'] = cf
                            Naziya['method2'] = "Solved With Median"  

                            Median_Odd_Even = 0
                            if sum(f)%2 == 0 :
                                Naziya['len3'] = sum(f)
                                findincf = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(f)/2))
                                Naziya['divide1'] = NAZIYA.intfloatconverter(findincf)

                                divi = findincf+1
                                Naziya['add1'] = NAZIYA.intfloatconverter(divi)

                                indexingforcf = NAZIYA.Indexing(cf,findincf).Single_Side_Indexing()
                                te = firstlistcopy[indexingforcf]
                                Naziya['term1'] = te

                                indexingforcf2 = NAZIYA.Indexing(cf,divi).Single_Side_Indexing()
                                te2 = firstlistcopy[indexingforcf2]
                                Naziya['term2'] = te2

                                la = NAZIYA.intfloatconverter(NAZIYA.floatstopper(te + te2))
                                Naziya['la'] = la

                                me = NAZIYA.intfloatconverter(NAZIYA.floatstopper(la/2))
                                Naziya['median'] = me
                                Median_Odd_Even += me
                            else:
                                print('this is odd series')
                                Naziya['odd'] = 1
                                Naziya['len3'] = sum(f)
                                
                                zu = sum(f) + 1
                                Naziya['n'] = zu
                                zu1 = zu/2
                                Naziya['divide1'] = NAZIYA.intfloatconverter(zu1)

                                a = NAZIYA.Indexing(cf,zu1).Single_Side_Indexing()
                                firstli = firstlistcopy[a]
                                Naziya['term'] = firstli
                                Median_Odd_Even += firstli

                            dmedian = [abs(NAZIYA.intfloatconverter(NAZIYA.floatstopper(Median_Odd_Even - i))) for i in firstlistcopy]
                            Naziya['dmedian'] = dmedian

                            dlist5 = NAZIYA.String_Add(firstlistcopy,Median_Odd_Even,dmedian)
                            Naziya['dlist5'] = dlist5
                            o1 = 0
                            lk1 = []
                            for i in f:
                                k = NAZIYA.intfloatconverter(NAZIYA.floatstopper(i*dmedian[o1]))
                                o1+=1
                                lk1.append((k))

                            # TAKING MEAN DEVIATION WITH MEDIAN (SIMPLE)
                            Naziya['fdmedian'] = lk1
                            Naziya['sumfdmedian'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(lk1)))

                            mediand = NAZIYA.intfloatconverter(sum(lk1)/sumof_f)
                            Naziya['mediand'] = mediand
                            # END MEDIAN SIMPLE METHOD

                            # SOLVED WITH MEAN SHORTCUT METHOD
                            Naziya['method3'] = "Solved With Mean (Shortcut Method)"
                            df = NAZIYA.Indexing(firstlistcopy,acm).Single_Side_Indexing()

                            # FOR SIGMAFXA AND SIGMAFXB (Mean)
                            za_tuple = NAZIYA.Summation_Value(firstlistcopy,df,acm,par)
                            sigmafxa = sum(za_tuple[0])
                            sigmafxb = sum(za_tuple[1])
                            Naziya['sigmafxa'] = sigmafxa
                            Naziya['sigmafxb'] = sigmafxb

                            # FOR SIGMAFA AND SIGMAFB (Mean)
                            zq_tuple = NAZIYA.Summation_Value(firstlist,df,acm,f)
                            sigmafa = sum(zq_tuple[0])
                            sigmafb = sum(zq_tuple[1])
                            Naziya['sigmafa'] = sigmafa
                            Naziya['sigmafb'] = sigmafb

                            firststep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmafxa - sigmafxb))
                            Naziya['firststep'] = firststep

                            secondstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmafa - sigmafb))
                            Naziya['secondstep'] = secondstep

                            thirdstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(secondstep*acm))
                            Naziya['thirdstep'] = thirdstep

                            if thirdstep < 0:
                                Naziya['showplus'] = 'nazpar'
                                Naziya['thirdstep1'] = abs(thirdstep)
                            fourthstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(firststep - thirdstep))
                            Naziya['fourthstep'] = fourthstep

                            # TAKING MEAN DEVIATION OF MEAN DEVIATION (SHORTCUT METHOD)
                            fifthstep = NAZIYA.intfloatconverter(fourthstep/sumof_f)
                            Naziya['fifthstep'] = fifthstep
                            # END MEAN SHORTCUT METHOD

                            # # SOLVED WITH MEDIAN (SHORTCUT METHOD)
                            Naziya['method4'] = "Solved With Median (Shortcut Method)"
                            dfm = NAZIYA.Indexing(firstlistcopy,Median_Odd_Even).Single_Side_Indexing()

                            # FOR SIGMAFXAM AND SIGMAFXBM (Median)
                            zsm_tuple = NAZIYA.Summation_Value(firstlistcopy,dfm,Median_Odd_Even,par)
                            sigmafxam = sum(zsm_tuple[0])
                            sigmafxbm = sum(zsm_tuple[1])
                            Naziya['sigmafxam'] = sigmafxam
                            Naziya['sigmafxbm'] = sigmafxbm

                            # FOR SIGMAFA AND SIGMAFB (Median)
                            zqm_tuple = NAZIYA.Summation_Value(firstlistcopy,dfm,Median_Odd_Even,f)
                            sigmafam = sum(zqm_tuple[0])
                            sigmafbm = sum(zqm_tuple[1])
                            Naziya['sigmafam'] = sigmafam
                            Naziya['sigmafbm'] = sigmafbm

                            firststepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmafxam - sigmafxbm))
                            Naziya['firststepm'] = firststepm

                            secondstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmafam - sigmafbm))
                            Naziya['secondstepm'] = secondstepm

                            thirdstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(secondstepm*Median_Odd_Even))
                            Naziya['thirdstepm'] = thirdstepm

                            if thirdstepm < 0:
                                Naziya['showplusm'] = 'showplusm'
                                Naziya['thirdstep1m'] = abs(thirdstepm)
                            fourthstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(firststepm - thirdstepm))
                            Naziya['fourthstepm'] = fourthstepm

                            # TAKING MEAND DEVIATION WITH MEDIAN (SHORTCUT METHOD)
                            fifthstepm = NAZIYA.intfloatconverter(fourthstepm/sumof_f)
                            Naziya['fifthstepm'] = fifthstepm
                            # END OF MEDIAN (SHORTCUT METHOD)

                            # CALCULATION OF COEFFICIENT OF MEAN DEVIATION
                            Naziya['coefficientmdmean'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(va))
                            Naziya['coefficientmean'] = acm

                            calcofcomd = NAZIYA.intfloatconverter(NAZIYA.floatstopper(va/acm))
                            Naziya['coefficientofmdmean'] = calcofcomd

                            Naziya['coefficientmdmedian'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(mediand))
                            Naziya['coefficientmedian'] = Median_Odd_Even

                            calcofcomdm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(mediand/Median_Odd_Even))
                            Naziya['coefficientofmdmedian'] = calcofcomdm
                            # DATABASE
                            NAZIYA.Database_Insertion('Discrete_Series', firstinput, secondinput, Collection_Name, IpAddress, 'Items')
                        else:
                            if secondinput == '0':
                                # INDIVIDAUL SERIES 
                                Naziya['seriesname'] = "INDIVIDUAL SERIES"
                                firstlist = NAZIYA.intfloatconverter_list(list1)
                                Naziya['x'] = firstlist

                                for i in list2:
                                    y2 = int(i)
                                    Naziya['f1'] = y2
                                Naziya['len'] = len(list1)

                                # SOLVED WITH MEAN
                                Naziya['method1'] = 'Solved With Mean'
                                su = sum(firstlist)
                                Naziya['sumx'] = su
                                Naziya['len'] = len(firstlist)
                                
                                Naziya['actualmean'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(firstlist)/len(firstlist)))
                                
                                me = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(firstlist)/len(firstlist)))

                                mdm = [abs(NAZIYA.intfloatconverter(NAZIYA.floatstopper(me - i))) for i in firstlist]

                                dlist = NAZIYA.String_Add(firstlist,me,mdm)
                                Naziya['dlist1'] = dlist
                                Naziya['summd'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(mdm)))

                                va = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(mdm)/len(list1)))
                                Naziya['mdforind'] = va
                                
                                # FOR SIMPLE MEDIAN METHOD
                                Naziya['method2'] = 'Solve With Median'
                                copyformedianx = firstlist.copy()
                                copyformedianx.sort()
                                Naziya['sortx'] = copyformedianx
                                Naziya['lenf1'] = 0
                                Naziya['lensumx'] = 1
                                globalmd = 0
                                
                                if len(firstlist)%2:
                                    # FOR ODD SERIES
                                    Naziya['seriesname'] = "INDIVIDUAL SERIES"
                                    if len(firstlist)%2 :
                                        Naziya['odd'] = 1
                                    Naziya['len1'] = len(firstlist)
                                    zu = len(firstlist) + 1
                                    Naziya['n'] = zu
                                    zu1 = zu/2
                                    Naziya['divide1'] = NAZIYA.intfloatconverter(zu1)
                                    term = copyformedianx[int(zu1)-1]
                                    Naziya['term'] = term
                                    Naziya['median']= NAZIYA.intfloatconverter(term)
                                    globalmd += term
                                else:
                                    Naziya['seriesname'] = "INDIVIDUAL SERIES"
                                    Naziya['len1']= len(firstlist)
                                    length = len(firstlist)/2
                                    Naziya['divide1'] = NAZIYA.intfloatconverter(length)
                                    Naziya['add1'] = NAZIYA.intfloatconverter(length +1)

                                    term1 = copyformedianx[int(length)-1]
                                    Naziya['term1'] = term1
                                    term2 = copyformedianx[int(length+1)-1]
                                    Naziya['term2'] = term2
                                    la = term1 + term2
                                    Naziya['la'] = la

                                    median = la/2
                                    Naziya['median']= NAZIYA.intfloatconverter(median)
                                    globalmd += NAZIYA.intfloatconverter(median)

                                mdm1 = [abs(NAZIYA.intfloatconverter(NAZIYA.floatstopper(globalmd - i))) for i in copyformedianx]

                                dlist1 = NAZIYA.String_Add(copyformedianx,globalmd,mdm1)

                                Naziya['dlist2'] = dlist1
                                summd1 = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(mdm1)))
                                Naziya['summd1'] = summd1

                                mediand = NAZIYA.intfloatconverter(NAZIYA.floatstopper((summd1)/len(firstlist)))
                                Naziya['mdforind1'] = mediand

                                # SOLVING FOR INDIVIDUAL SERIES WITH MEAN SHORTCUT METHOD
                                Naziya['method3'] = 'Solve With Mean (Shortcut Method)'
                                df = NAZIYA.Indexing(copyformedianx,me).Single_Side_Indexing()

                                # FOR SIGMAXA AND SIGMAXB
                                zs_tuple = NAZIYA.Summation_Value(copyformedianx,df,me,copyformedianx)
                                sigmaxa = sum(zs_tuple[0])
                                sigmaxb = sum(zs_tuple[1])
                                Naziya['sigmaxa'] = sigmaxa
                                Naziya['sigmaxb'] = sigmaxb

                                # FOR SIGMANA AND SIGMANB
                                zq_tuple = NAZIYA.Summation_Value(copyformedianx,df,me)
                                sigmana = sum(zq_tuple[0])
                                sigmanb = sum(zq_tuple[1])
                                Naziya['sigmana'] = sigmana
                                Naziya['sigmanb'] = sigmanb

                                firststep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmaxa - sigmaxb))
                                Naziya['firststep'] = firststep

                                secondstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmana - sigmanb))
                                Naziya['secondstep'] = secondstep

                                thirdstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(secondstep*me))
                                Naziya['thirdstep'] = thirdstep

                                if thirdstep < 0:
                                    Naziya['showplus'] = 'nazpar'
                                    Naziya['thirdstep1'] = abs(thirdstep)

                                fourthstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(firststep - thirdstep))
                                Naziya['fourthstep'] = fourthstep

                                fifthstep = NAZIYA.intfloatconverter(NAZIYA.floatstopper(fourthstep/len(firstlist)))
                                Naziya['fifthstep'] = fifthstep
                                
                                #   SOLVING FOR INDIVIDUAL SERIES WITH MEDIAN SHORTCUT METHOD
                                Naziya['method4'] = 'Solve With Median (Shortcut Method)'

                                # FOR SIGMAXAM AND SIGMAXBM
                                dfm = NAZIYA.Indexing(copyformedianx,globalmd).Single_Side_Indexing()
                                zsm_tuple = NAZIYA.Summation_Value(copyformedianx,dfm,globalmd,copyformedianx)
                                sigmaxam = sum(zsm_tuple[0])
                                sigmaxbm = sum(zsm_tuple[1])
                                Naziya['sigmaxam'] = sigmaxam
                                Naziya['sigmaxbm'] = sigmaxbm

                                # FOR SIGMANAM AND SIGMANBM
                                zqm_tuple = NAZIYA.Summation_Value(copyformedianx,dfm,globalmd)
                                sigmanam = sum(zqm_tuple[0])
                                sigmanbm = sum(zqm_tuple[1])
                                Naziya['sigmanam'] = sigmanam
                                Naziya['sigmanbm'] = sigmanbm

                                firststepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmaxam - sigmaxbm))
                                Naziya['firststepm'] = firststepm

                                secondstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sigmanam - sigmanbm))
                                Naziya['secondstepm'] = secondstepm

                                thirdstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(secondstepm*globalmd))
                                Naziya['thirdstepm'] = thirdstepm

                                if thirdstepm < 0:
                                    Naziya['showplusm'] = 'showplusm'
                                    Naziya['thirdstep1m'] = abs(thirdstepm)

                                fourthstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(firststepm - thirdstepm))
                                Naziya['fourthstepm'] = fourthstepm

                                fifthstepm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(fourthstepm/len(firstlist)))
                                Naziya['fifthstepm'] = fifthstepm

                                # CALCULATION OF COEFFICIENT OF MEAN DEVIATION
                                Naziya['coefficientmdmean'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(va))
                                Naziya['coefficientmean'] = me 

                                calcofcomd = NAZIYA.intfloatconverter(NAZIYA.floatstopper(va/me))
                                Naziya['coefficientofmdmean'] = calcofcomd

                                Naziya['coefficientmdmedian'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(mediand))
                                Naziya['coefficientmedian'] = globalmd

                                calcofcomdm = NAZIYA.intfloatconverter(NAZIYA.floatstopper(mediand/globalmd))
                                Naziya['coefficientofmdmedian'] = calcofcomdm
                                #DATABASE
                                NAZIYA.Database_Insertion('Individual_Series', firstinput,secondinput,Collection_Name,IpAddress,'Items')
                            else:
                                if len(list1) != len(list2):
                                    Naziya['x2'] = len(list1)
                                    Naziya['f2'] = len(list2)
                                    Naziya['seriesname1'] = "Please Check that lenght of both( X/C.I. and frequency is equal or may be you entered Two (,,) Commas )"
                                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
                except:
                    Naziya['allerror'] = 'Handle'
                    Naziya['seriesname1'] = 'Please Enter Your Question Correctly'
                    NAZIYA.Database_Insertion('Errors',firstinput,secondinput,Collection_Name,IpAddress,'CI_Items')
    return render(request, "MathsMeanDeviation.html", Naziya)

def combinedmean(request):

    Naziya = {'root':[],
        'parveen':'Click Below To Solve Combined Mean',
        'question':'Combined Mean',
        'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
        'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',}

    if request.method == "POST":
        firstinput = request.POST.get('combinedfirstinput')
        secondinput = request.POST.get('combinedsecondinput')
        thirdinput = request.POST.get('combinedthirdinput')
        fourthinput = request.POST.get('combinedfourthinput')

        if firstinput == '' and secondinput == '' and thirdinput == '' and fourthinput == '':
            Naziya['seriesname1'] = 'Please Enter Your Question First'
            Naziya['emp'] = 0
        else:
            if firstinput == '':
                Naziya['seriesname1'] = 'Please Enter n1'
                Naziya['emp'] = 0
            else:
                if secondinput == '':
                    Naziya['seriesname1'] = 'Please Enter n2'
                    Naziya['emp'] = 0
                else:
                    if thirdinput == '':
                        Naziya['seriesname1'] = 'Please Enter x1'
                        Naziya['emp'] = 0
                    else:
                        if fourthinput == '':
                            Naziya['seriesname1'] = 'Please Enter x2'
                            Naziya['emp'] = 0
                        else:
                            try:
                                Naziya['combinedmatch'] = 'naziya'
                                Naziya['method1'] = 'Combined Mean'

                                n1 = int(firstinput)
                                n2 = int(secondinput)
                                x1 = int(thirdinput)
                                x2 = int(fourthinput)
                                Naziya['n1'] = n1
                                Naziya['n2'] = n2
                                Naziya['x1'] = x1
                                Naziya['x2'] = x2

                                step1 = NAZIYA.intfloatconverter(NAZIYA.floatstopper(n1*x1))
                                Naziya['step1'] = step1
                                step2 = NAZIYA.intfloatconverter(NAZIYA.floatstopper(n2*x2))
                                Naziya['step2'] = step2
                                step3 = NAZIYA.intfloatconverter(NAZIYA.floatstopper(step1+step2))
                                Naziya['step3'] = step3
                                step4 = NAZIYA.intfloatconverter(NAZIYA.floatstopper(n1+n2))
                                Naziya['step4'] = step4
                                step5 = NAZIYA.intfloatconverter(NAZIYA.floatstopper(step3/step4))
                                Naziya['step5'] = step5
                            except:
                                Naziya['allerror'] = 'Handle'
                                Naziya['seriesname1'] = 'Please Enter Your Question Correctly'
    return render(request, "MathsCombinedMean.html", Naziya)