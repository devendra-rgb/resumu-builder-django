from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from sepi.update_excel import update_data,calculate_month_difference
# Create your views here.

class Update_data(APIView):
    def post(self,request):
        data = request.data
        print(data)
        #print(data.keys())
        saving_data={}
        saving_data['Certifications']=data['skills'][0]['skills']
        saving_data['Awards and Achievements']=data['awards']
        #saving_data['SIP Project Description']=data['SIP']
        saving_data['roll_no']= 'P221D025'
        for i in range(len(data['workExperience'])):
            j=data['workExperience'][i]
            #import pdb;pdb.set_trace()
            saving_data[f'Company Name-{i+1}'] = j['company']
            saving_data[f'Designation-{i+1}'] = j['position']
            #saving_data[f'Industry-{i+1}'] = j['industry']
            saving_data[f'Duration-{i+1}\n (mons)'] = calculate_month_difference(j['startYear'],j['endYear'])
            saving_data[f'Role Description-{i+1}'] = j['description']
        update_data(saving_data)
        return Response("Successfully Updated!",status=200)
    
