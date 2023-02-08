from django.shortcuts import render
from .models import *
import pandas as pd

# Create your views here.
def ImportExportExcel(request):
    if request.method == 'POST':
        # gettting data from html form
        date_of_birth = request.POST['date_of_birth']
        last_name = request.POST['last_name']
        first_name = request.POST["first_name"]

        # create the user
        new_user = UserInformation(date_of_birth=date_of_birth,last_name=last_name,first_name=first_name)
        
        file = request.FILES['file']
        # reading excel document
        df = pd.read_excel(file)
        mylist = df.values.tolist()

        # saving user into database
        new_user.save()

        # printing out data to check if they are correct
        print(len(mylist))
        print(mylist)
        print('name',first_name,'last',last_name,'date',date_of_birth)

        # redirecting to result.html page and passing data to be visualized
        return render(request,'resuts.html',{'mylist1':mylist,'row1':'Month','row2':'Income','row3':'Expense',"iterator":0})
    
    # if the method is not POST, this page will be displayed
    return render(request, 'upload.html')