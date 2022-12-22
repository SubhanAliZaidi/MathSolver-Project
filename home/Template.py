import Naziya as NAZIYA
from django.shortcuts import render
import requests

def Template(request):

    Naziya = {
        'root':[],
        'parveen':'Click Below To Solve Mean Deviation',
        'cando':'Please enter your question with comma seperated in textbox',
        'question':'Mean Deviation',
        'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
        'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',
    }

    if request.method == "POST":
        firstinput = request.POST.get('firstinput')
        secondinput = request.POST.get('secondinput')

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
                    list2 = (secondinput).strip().split(',')
                    list1 = list12
                    li = list12

                    try:
                        cixitem = NAZIYA.Try(li)
                    except ValueError:
                        q = NAZIYA.ErrorHandling(list12)
                        colo = NAZIYA.Exception(q)
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

                    else:
                        # FOR DISCRETE SERIES
                        if len(list1) == len(list2):
                            Naziya['seriesname'] = "DISCRETE SERIES"

                            firstlist = NAZIYA.intfloatconverter_list(list1)
                            Naziya['x'] = firstlist

                            secondlist = NAZIYA.intfloatconverter_list(list2)
                            Naziya['f'] = secondlist

                        else:
                            if secondinput == '0':
                                Naziya['seriesname'] = "INDIVIDUAL SERIES"

                                firstlist = NAZIYA.intfloatconverter_list(list1)
                                Naziya['x'] = firstlist

                                for i in list2:
                                    y2 = int(i)
                                    Naziya['f1'] = y2
                                Naziya['len1'] = len(list1)

                            else:
                                if len(list1) != len(list2):
                                    Naziya['x2'] = len(list1)
                                    Naziya['f2'] = len(list2)
                                    Naziya['seriesname1'] = "Please Check that lenght of both( X/C.I. and frequency is equal or may be you entered Two (,,) Commas )"
                    
                except:
                    Naziya['allerror'] = 'Handle'
                    Naziya['seriesname1'] = 'Please Enter Your Question Correctly'

    return render(request, "MathsMeanDeviation.html", Naziya)

def Api_Test(request):

    naz = 'https://drive.google.com/file/d/1YzRXMISnRRw4s3tdSeuKFHi2EoypEpPD/view?usp=sharing'

    url = "https://api.apilayer.com/image_to_text/url?url="+naz

    payload = {}
    headers= {
    "apikey": "YL3dJPo5CvzLxJjLehG8AOXk6tuvPTgu"
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    result = response.text

    print(result)

    return render(request, "Template.html")