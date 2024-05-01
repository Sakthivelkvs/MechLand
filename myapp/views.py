from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.db.models import F, Max

import datetime

from django.core.files.storage import FileSystemStorage

from myapp.models import *

from django.db.models import Sum

from django.core.mail import send_mail

from django.contrib import messages

from django.db.models import Q


# Create your views here.

def unitcard(request):
    return render(request, 'card_index.html')

def dashboard(request):
    return render(request, 'manager_index copy.html')


##Login
def login1(request):
    return render(request, 'login.html')

def unit_login(request):
    aj = request.session.get('unit')
    val2 = uint_registration.objects.get(Email=aj)             
    return render(request, 'unit_index.html', {'data': val2})
    #return render(request, 'unit_index.html')

def staff_login(request):
    aj = request.session.get('staff')
    var2 = staff.objects.get(Email=aj)  
    return render(request,'staff_index.html', {'data': var2})

def manager_login(request):
    aj = request.session.get('mngr')
    var2 = manager.objects.get(Email=aj)
    aj=unit_order.objects.filter(status="Pending").count()
    print(aj)
    aj2=staff.objects.filter(job_id__job_role="Supervisor").count()
    print(aj2)
    aj3=unit_order.objects.filter(status="Approved").count()
    print(aj)
    aj4=cancel.objects.filter(status="Requested").count()
    return render(request,'manager_index3.html',{'data': var2,'data2':aj, 'data1':aj2, 'data3':aj3, 'data4':aj4})

def supervisor_login(request):
    aj = request.session.get('sprvr')
    var2 = staff.objects.get(Email=aj)  
    return render(request,'supervisor_index.html',{'data': var2})

def login1_post(request):
   if request.method=='POST':
        uname=request.POST.get('email')
        paword=request.POST.get('password')

        data=login.objects.all()
        flag=0

        for i in data:
            if uname==i.username and paword==i.password:
                type=i.category
                flag=1
                if type=="Admin":
                    request.session['adm']=uname
                    messages.success(request, 'Your Are Logged In!')
                    return redirect('/admin3/')
                    # return HttpResponse('''<script>alert('Login Succesfull');window.location="/admin3/"</script>''')

                # elif type=="User":
                #     request.session['use']=uname
                #     return redirect("/user_home")
                elif type=="Unit":
                    request.session['unit']=uname
                    messages.success(request, 'Your Are Logged In!')
                    return redirect('/unit_login/')
                    # return HttpResponse('''<script>alert('Login Succesfull');window.location="/unit_login/"</script>''')
                
                elif type=="staff":
                    request.session['staff']=uname
                    messages.success(request, 'Your Are Logged In!')
                    return redirect('/staff_login/')
                    # return HttpResponse('''<script>alert('Login Succesfull');window.location="/staff_login/"</script>''')
                
                elif type=="manager":
                    request.session['mngr']=uname
                    messages.success(request, 'Your Are Logged In!')
                    return redirect('/manager_login/')
                    # return HttpResponse('''<script>alert('Login Succesfull');window.location="/manager_login/"</script>''')

                elif type=="Supervisor":
                    request.session['sprvr']=uname
                    messages.success(request, 'Your Are Logged In!')
                    return redirect('/supervisor_login/')
                    # return HttpResponse('''<script>alert('Login Succesfull');window.location="/supervisor_login/"</script>''')

                else:
                    return HttpResponse("Invalid Category")
        if flag==0:
            messages.error(request, 'Invalid User!')
            return redirect('/login/')
            # return HttpResponse('''<script>alert('InvalidUser');window.location="/login/"</script>''')
        
def logout(request):
    request.session.clear()
    messages.error(request, 'You Are Logged Out!')
    return redirect('/public_home2/')

def admin_logout(request):
    del request.session['adm']
    messages.error(request, 'You Are Logged Out!')
    return redirect('/public_home2/')

def staff_logout(request):
    del request.session['staff']
    messages.error(request, 'You Are Logged Out!')
    return redirect('/public_home2/')

def supervisor_logout(request):
    del request.session['sprvr']
    messages.error(request, 'You Are Logged Out!')
    return redirect('/public_home2/')

def manager_logout(request):
    del request.session['mngr']
    messages.error(request, 'You Are Logged Out!')
    return redirect('/public_home2/')

def unit_logout(request):
    del request.session['unit']
    messages.error(request, 'You Are Logged Out!')
    return redirect('/public_home2/')



### Admin Home   ########

def admin(request):
    return render(request, 'index.html')

def admin2(request):
    return render(request, 'admin_index.html')

def admin3(request):
    obj=Leave3.objects.filter(status="Pending").count()
    print(obj)
    obj1=job_apply.objects.filter(status="Pending").count()
    print(obj1)
    obj2=uint_registration.objects.filter(status="Pending").count()
    print(obj2)
    obj3=loan.objects.filter(status="Pending").count()
    print(obj3)
    return render(request, 'Admin/admin_master2.html', {'data': obj, 'data2': obj1, 'data3': obj2,'data4':obj3})

#### Mould Management     ########

def admin_add_mould(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        return render(request, 'Admin/admin_add_mould.html')
def admin_add_mould_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        mn=request.POST['textfield']
        mt=request.POST['select']
        Description=request.POST['textarea']
        sizet=request.POST['select2']
        size1=request.POST['textfield4']
        size2=request.POST['textfield5']
        size3=request.POST['textfield6']
        size=request.POST['textfield7']
        price=request.POST['textfield2']
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        filename=fs.save(photo.name,photo)
        uploaded_file_url = fs.url(filename)
        
        aj=add_mould()
        aj.mname=mn
        aj.mtype=mt
        aj.Description=Description
        aj.price=price
        aj.stock="0"
        aj.size_type=sizet
        aj.size1=size1
        aj.size2=size2
        aj.size3=size3
        aj.size=size
        aj.photo = uploaded_file_url
        aj.save()
        messages.success(request, 'Added successfully!')
        return redirect('/admin_view_mould/')
        # return HttpResponse('''<script>alert('Success');window.location="/admin_view_mould/"</script>''')

def admin_view_mould(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        values=add_mould.objects.all().order_by('-id')
        return render(request,"Admin/admin_view_moulds.html",{'data':values})

def admin_edit_mould(request,s1):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data=add_mould.objects.get(id=s1)
        return render(request,"Admin/admin_edit_mould.html",{'data':data})

def admin_edit_mould_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id = request.POST.get('id')
        v1=request.POST['textfield']
        v2=request.POST['select']
        v3=request.POST['textarea']
        v4=request.POST['textfield2']
        sizet=request.POST['select2']
        size1=request.POST['textfield4']
        size2=request.POST['textfield5']
        size3=request.POST['textfield6']
        size=request.POST['textfield7']
        if 'photo' in request.FILES:
            photo = request.FILES['photo']

            photo=request.FILES['photo']
            fs=FileSystemStorage()
            filename=fs.save(photo.name,photo)
            uploaded_file_url = fs.url(filename)

            aj=add_mould.objects.get(id=id)
            aj.mname=v1
            aj.mtype=v2
            aj.Description=v3
            aj.size_type=sizet
            aj.size1=size1
            aj.size2=size2
            aj.size3=size3
            aj.size=size
            aj.price=v4
            aj.stock="0"
            aj.photo = uploaded_file_url
            aj.save()
            messages.success(request, 'Edited successfully!')
            return redirect('/admin_view_mould/')

        else:
            aj = add_mould.objects.get(id=id)
            aj.mname=v1
            aj.mtype=v2
            aj.Description=v3
            aj.size_type=sizet
            aj.size1=size1
            aj.size2=size2
            aj.size3=size3
            aj.size=size
            aj.price=v4
            aj.stock="0"
            aj.save()
            messages.success(request, 'Edited successfully!')
            return redirect('/admin_view_mould/')

def admin_delete_mould(request,s2):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        values=add_mould.objects.get(id=s2)
        values.delete()
        messages.error(request, 'Deleted successfully!')
        return redirect('/admin_view_mould/')


##### Predict Mould management    ########

def admin_add_predict_mould(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        return render(request, 'Admin/admin_add_predict_mould.html')

def admin_add_predict_mould_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        mn=request.POST['textfield']
        photo1=request.FILES['photo1']
        fs=FileSystemStorage()
        filename=fs.save(photo1.name,photo1)
        uploaded_file_url = fs.url(filename)

        photo2=request.FILES['photo2']
        fs2=FileSystemStorage()
        filename1=fs2.save(photo2.name,photo2)
        uploaded_file_url2 = fs2.url(filename1)

        photo3=request.FILES['photo3']
        fs3=FileSystemStorage()
        filename2=fs3.save(photo3.name,photo3)
        uploaded_file_url3 = fs3.url(filename2)

        aobj=predict_mould()
        aobj.mldname=mn
        aobj.photo1=uploaded_file_url
        aobj.photo2=uploaded_file_url2
        aobj.photo3=uploaded_file_url3
        aobj.save()
        messages.success(request, 'Added successfully!')
        return render('/admin_view_predict_mould/')
        # return HttpResponse('''<script>alert('Success');window.location="/admin_view_predict_mould/"</script>''')
        # return HttpResponse("Success")
    
def admin_view_predict_mould(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        values=predict_mould.objects.all()
        return render(request,"Admin/admin_view_predict_mould.html",{'data': values})

def admin_edit_predict_mould(request,s3):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data=predict_mould.objects.get(id=s3)
        return render(request,"Admin/admin_edit_predict_mould.html",{'data':data})

def admin_edit_predict_mould_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id = request.POST.get('id')
        v1=request.POST['textfield']
        if 'photo1' in request.FILES:
            photo = request.FILES['photo1']  
            fs = FileSystemStorage()
            filename = fs.save(photo.name, photo)
            uploaded_file_url = fs.url(filename)

            aj = predict_mould.objects.get(id=id)
            aj.mldname = v1
            aj.photo1 = uploaded_file_url
            aj.save()
            messages.success(request, 'Edited successfully!')
            return redirect('/admin_view_predict_mould/')

        elif 'photo2' in request.FILES:
            photo1 = request.FILES['photo2']  
            fs2 = FileSystemStorage()
            filename2 = fs2.save(photo1.name, photo1)
            uploaded_file_url2 = fs2.url(filename2)

            aj = predict_mould.objects.get(id=id)
            aj.mldname = v1
            aj.photo2 = uploaded_file_url2
            aj.save()
            messages.success(request, 'Edited successfully!')
            return redirect('/admin_view_predict_mould/')

        elif 'photo3' in request.FILES:
            photo2 = request.FILES['photo3'] 
            fs3 = FileSystemStorage()
            filename3 = fs3.save(photo2.name, photo2)
            uploaded_file_url3 = fs3.url(filename3)

            aj = predict_mould.objects.get(id=id)
            aj.mldname = v1
            aj.photo3 = uploaded_file_url3
            aj.save()
            messages.success(request, 'Edited successfully!')
            return redirect('/admin_view_predict_mould/')

        else:
            aj = predict_mould.objects.get(id=id)
            aj.mldname = v1
            aj.save()
            messages.success(request, 'Edited successfully!')
            return redirect('/admin_view_predict_mould/')
    
def delete_predict_mouold(request,s4):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        values=predict_mould.objects.get(id=s4)
        values.delete()
        messages.error(request, 'Deleted successfully!')
        return redirect('/admin_view_predict_mould/')

def admin_view_public_ratting(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        values=predict_mould.objects.all()
        return render(request,"Admin/admin_view_public_ratting.html",{'data':values})

    
def admin_view_public_ratting2(request,s1):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        instance=ratting.objects.get(predict_mould_id_id=s1)
        result = instance.get_column_with_highest_value()
        
        if result=="p1_ratting":
            data=predict_mould.objects.get(id=s1)
            res=data.photo1
            return render(request,"Admin/rattingresult.html",{'res':res})
        elif result=="p2_ratting":
            data=predict_mould.objects.get(id=s1)
            res=data.photo2
            return render(request,"Admin/rattingresult.html",{'res':res})   
        elif result=="p3_ratting":
            data=predict_mould.objects.get(id=s1)
            res=data.photo3
            return render(request,"Admin/rattingresult.html",{'res':res})     


    

    

   

##### Job Master    ########

def admin_add_job(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        return render(request, 'Admin/admin_add_job.html')

def admin_add_job_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        job_role=request.POST['textfield']
        basic_salary=request.POST['textfield2']
        # allowance=request.POST['textfield3']
        loan_allowance=request.POST['textfield3']
        salary=request.POST['textfield4']
        r=request.POST['textfield5']
        v=request.POST['textfield6']
        q=request.POST['textfield7']
        e=request.POST['textfield8']
        d=request.POST['textfield9']

        aj=job_master()
        aj.job_role=job_role
        aj.basic_salary=basic_salary
        # aj.allowance=allowance
        aj.cut_salary=salary 
        aj.loan_allowance=loan_allowance
        aj.requirements=r
        aj.vacancies=v
        aj.qualifications=q
        aj.experiences=e
        aj.date=d
        aj.status="ok"
        aj.save()
        messages.success(request, 'Added successfully!')
        return redirect('/admin_view_job/')
        # return HttpResponse('''<script>alert('Success');window.location="/admin_view_job/"</script>''')


def admin_view_job(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        values=job_master.objects.all()
        return render(request,"Admin/admin_view_job.html",{'data':   values})

def admin_edit_job(request,s5):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data=job_master.objects.get(id=s5)
        return render(request,"Admin/admin_edit_job.html",{'data':data})
def admin_edit_job_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id = request.POST.get('id')
        v1=request.POST['textfield']
        v2=request.POST['textfield2']
        v3=request.POST['textfield3']
        v4=request.POST['textfield4']
        r=request.POST['textfield5']
        v=request.POST['textfield6']
        q=request.POST['textfield7']
        e=request.POST['textfield8']
        d=request.POST['textfield9']

        aj=job_master.objects.get(id=id)
        aj.job_role=v1
        aj.basic_salary=v2
        aj.cut_salary=v3
        # aj.allowance=v3
        aj.loan_allowance=v4
        aj.requirements=r
        aj.vacancies=v
        aj.qualifications=q
        aj.experiences=e
        aj.date=d
        aj.save()
        messages.success(request, 'Edited successfully!')
        return redirect('/admin_view_job/')

def admin_delete_job(request,s6):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        values=job_master.objects.get(id=s6)
        values.delete()
        messages.error(request, 'Deleted successfully!')
        return redirect('/admin_view_job/')



####### Staff Management    ########

# def admin_allot_interview(request,s30):
#     data=job_apply.objects.get(id=s30)
#     return render(request,"Admin/admin_allot_interview.html",{'data':data})

# def admin_allot_interview_post(request):
#     id=request.POST.get('id')
#     d=request.POST.get('textfield')
#     t=request.POST.get('textfield4')
#     v=request.POST.get('textarea')
#     bobj=job_apply.objects.get(id=id)
#     bobj.int_date=d
#     bobj.int_time=t
#     bobj.int_status='Scheduled'
#     bobj.save()
#     send_mail('Thanks for Responding...','Mr'+bobj.Name+'Please Visit Our Company on''Date:'+d+'and''Time:'+t+' ''Venue:'+v, 'from@example.co',[bobj.Email,])
#     messages.success(request, 'Interview Alloted!')
#     return redirect('/admin_view_carrier_application/')


    
def  admin_allotstaff(request,s16):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        return render(request, 'Admin/admin_add_staff.html',{'s16':s16})


def  admin_add_staff_post(request,id):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        joindate=request.POST['textfield']
        remark=request.POST['textfield2']
        sec=request.POST['select']
        data=job_apply.objects.get(id=id)
        data.status="accepted"
        data.save()
        aj=staff()
        aj.Name=data.Name
        aj.Gender=data.Gender
        aj.Date_of_birth=data.Date_of_birth
        aj.Email=data.Email
        aj.Phone_Number=data.Phone_Number
        aj.Address=data.Address
        aj.Photo=data.Photo
        aj.join_date=joindate
        aj.remark=remark
        aj.section=sec
        aj.job_id_id=data.job_id_id
        aj.status="active"
        aj.save()
        # send_mail('Congratulations you are Appointed...','Username:'+data.Name,'Password:'+data.Phone_Number,'from@example.co',[aj.Email,]) 
        data3=login.objects.filter(username=data.Email).count()
        if data3>0:
            return HttpResponse('''<script>alert('Already Exist');window.location="/admin_view_carrier_application/"</script>''')
        else:
            if data.job_id.job_role == "Supervisor":
                data2=login()
                data2.username=data.Email
                data2.password=data.Phone_Number
                data2.category='Supervisor'
                data2.save()     
            else:      


                data2=login()
                data2.username=data.Email
                data2.password=data.Phone_Number
                data2.category='staff'
                data2.save()  
        messages.success(request, 'Staff is Alloted!')
        return redirect('/admin_view_carrier_application/')      
        # return HttpResponse('''<script>alert('Success');window.location="/admin_view_carrier_application/"</script>''')



def admin_allot_manager(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        return render(request, 'Admin/admin_allot_manager.html')

def admin_allot_manager_post2(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        search=request.POST['textfield']
        if search:
            aj=staff.objects.filter(Name__icontains=search)
            if aj:
                return render(request,"Admin/admin_allot_manager.html",{'data':aj})
            else:
                return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/admin_allot_manager/"</script>''')

def admin_allot_manager_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        name=request.POST['textfield']
        gndr=request.POST['RadioGroup1']
        dob=request.POST['textfield4']
        email=request.POST['textfield2']
        phn=request.POST['textfield6']
        hn=request.POST['textfield7']
        place=request.POST['textfield8']
        city=request.POST['textfield10']
        state=request.POST['textfield9']
        pin=request.POST['textfield11']
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        filename=fs.save(photo.name,photo)
        uploaded_file_url = fs.url(filename)

        data=manager()
        data.Name=name
        data.Gender=gndr
        data.Date_of_birth=dob
        data.Email=email
        data.Phone_Number=phn
        data.house_name=hn
        data.Place=place
        data.City=city
        data.State=state
        data.Pincode=pin
        data.photo=uploaded_file_url
        data.save()

        data2=login()
        data2.username=data.Email
        data2.password=data.Phone_Number
        data2.category='manager'
        data2.save()
        messages.success(request, 'Manager Added!')
        return redirect('/admin_allot_manager/')
        # return HttpResponse('''<script>alert('Success');window.location="/admin_allot_manager/"</script>''')
        
        
        # data=staff.objects.get(id=s20)
        # data10=job_master.objects.get(job_role="manager")
        # data.job_id_id=data10.id
        # data.save()
        # data2=login.objects.get(username=data.Email)
        # data2.category="manager"
        # data2.save()
        # return HttpResponse('''<script>alert('Success');window.location="/admin_allot_manager/"</script>''')

# def admin_add_Labour(request):
#     aj=job_master.objects.all()
#     return render(request, 'Admin/admin_allot_manager.html',{'data':aj})

# def admin_add_Labour_post(request):


def admin_view_manager(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data10=manager.objects.all()
        return render(request, 'Admin/admin_view_manager.html',{'data':data10})

def admin_view_manager_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        search=request.POST['textfield']
        if search:
            aj=staff.objects.filter(Name__icontains=search)
            if aj:
                return render(request,"Admin/admin_view_manager.html",{'data':aj})
            else:
                return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/admin_view_manager/"</script>''')

def admin_delete_manager(request,s21):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        values=manager.objects.get(id=s21)
        values.delete()
        messages.error(request, 'Manager Deleted!')
        return redirect('/admin_view_manager/')

def admin_view_staff(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data10=job_master.objects.filter(job_role="manager")
        data=staff.objects.exclude(job_id_id__in=[ct.id for ct in data10])
        return render(request,"Admin/admin_view_staff.html",{'data': data})

def admin_view_staff_details(request,s12):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data=staff.objects.get(id=s12)
        return render(request,"Admin/admin_view_staff_details.html",{'data':data})


def admin_view_staff_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        search=request.POST['textfield']
        if search:
            data=staff.objects.filter(Name__icontains=search)
            return render(request,"Admin/admin_view_staff.html",{'data': data})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/admin_view_staff/"</script>''')


def admin_edit_staff(request,s7):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data=staff.objects.get(id=s7)
        return render(request,"Admin/admin_edit_staff.html",{'data':data})
def admin_edit_staff_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id=request.POST.get('id')
        n=request.POST['textfield']
        g=request.POST['RadioGroup1']
        dob=request.POST['textfield2']
        email=request.POST['textfield4']
        phone=request.POST['textfield5']
        address=request.POST['textfield7']
        jd=request.POST['textfield9']
        sec=request.POST['select']
        rem=request.POST['textfield8']
        if 'Photo' in request.FILES:
            Photo = request.FILES['Photo']  
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo)
            uploaded_file_url = fs.url(filename)

            aj=staff.objects.get(id=id)
            aj.Name=n
            aj.Gender=g
            aj.Date_of_birth=dob
            aj.Email=email
            aj.Phone_Number=phone
            aj.Address=address
            aj.join_date=jd
            aj.remark=rem
            aj.section=sec
            aj.Photo=uploaded_file_url
            aj.save()
            return redirect('/admin_view_staff/')
        else:
            aj=staff.objects.get(id=id)
            aj.Name=n
            aj.Gender=g
            aj.Date_of_birth=dob
            aj.Email=email
            aj.Phone_Number=phone
            aj.Address=address
            aj.join_date=jd
            aj.remark=rem
            aj.section=sec
            aj.save()
            messages.success(request, 'Successfully Edited!')
            return redirect('/admin_view_staff/')



def admin_delete_staff(request, s8):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data = staff.objects.get(id=s8)
        data.delete()
        messages.error(request, 'Successfully Deleted!')
        return redirect('/admin_view_staff/')

######### Vacancy Management #########

def admin_add_vacancy(request,s3):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        values=job_master.objects.get(id=s3)
        return render(request, 'Admin/admin_add_vacancies.html',{'data':values})

def admin_add_vacancy_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id=request.POST.get('id')
        r=request.POST['textfield']
        v=request.POST['textfield2']
        q=request.POST['textfield3']
        e=request.POST['textfield4']
        

        aj=job_master.objects.get(id=id)
        aj=vaccancy()
        aj.job_id_id=id
        aj.requirements=r
        aj.vacancies=v
        aj.qualifications=q
        aj.experiences=e
        aj.status="ok"
        aj.save()
        return HttpResponse('''<script>alert('Success');window.location="/admin_view_job/"</script>''')

def admin_view_vacancy(request,job_id):
    job = job_master.objects.get(id=job_id)
    vacancies = vaccancy.objects.filter(job_id=job)
    return render(request, "Admin/admin_view_vacancies.html", {'job': job, 'data': vacancies})

def admin_edit_vacancy(request,s9):
    data=vaccancy.objects.get(id=s9)
    values=job_master.objects.all()
    return render(request,"Admin/admin_edit_vacancy.html",{'data':data,'values':values})

def admin_edit_vacancy_post(request,s1):
    job_id = request.POST['job_id']
    r=request.POST['textfield']
    v=request.POST['textfield2']
    q=request.POST['textfield3']
    e=request.POST['textfield4']

    aj=vaccancy.objects.get(id=s1)
    aj.job_id_id=job_id
    aj.requirements=r
    aj.vacancies=v
    aj.qualifications=q
    aj.experiences=e
    aj.save()
    return HttpResponse('''<script>alert('Updated');window.location="/admin_view_job/"</script>''')

def admin_delete_vacancy(request,s10):
    values=vaccancy.objects.get(id=s10)
    values.delete()
    return HttpResponse('''<script>alert('Deleted');window.location="/admin_view_job/"</script>''')



######## Shift Management #########

def admin_add_shift(reqest):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        return render(reqest,'Admin/admin_add_shif.html')

def admin_add_shift_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        shift_nbr=request.POST['textfield']
        shift_time=request.POST['appt']
        aj=shift()
        aj.shift_nbr=shift_nbr
        aj.shift_time=shift_time
        aj.save()
        messages.success(request, 'Shift is Successfully Added!')
        return redirect('/admin_view_shift/')
        # return HttpResponse('''<script>alert('Success');window.location="/admin_view_shift/"</script>''')

def admin_view_shift(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=shift.objects.all()
        return render(request,"Admin/admin_view_shift.html",{'data':aj})

def admin_edit_shift(request,s11):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=shift.objects.get(id=s11)
        return render(request,'Admin/admin_edit_shift.html',{'data':aj})

def admin_edit_shift_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id=request.POST.get('id')
        shift_nbr=request.POST['textfield']
        shift_time=request.POST['appt']
        aj=shift.objects.get(id=id)
        aj.shift_nbr=shift_nbr
        aj.shift_time=shift_time
        aj.save()
        messages.success(request, 'Shift is Successfully Edited!')
        return redirect('/admin_view_shift/')


######## Unit Request Management #########

def admin_view_unit_request(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=uint_registration.objects.filter(status='Pending')
        return render(request,"Admin/admin_view_unit_request.html",{'data':aj})

def admin_view_unit_request_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        search=request.POST['textfield']
        if search:
            aj=uint_registration.objects.filter(Name__icontains=search)
            if aj:
                return render(request,"Admin/admin_view_unit_request.html",{'data':aj})
            else:
                return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/admin_view_unit_request/"</script>''')


def admin_approve_unit_request(request,s12):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=uint_registration.objects.get(id=s12)
        aj.status='Approved'
        aj.save()
        log=login()
        log.username=aj.Email
        log.password=aj.password
        log.category='Unit'
        log.save()
        messages.success(request, 'Approved!')
        return redirect('/admin_view_unit_request/')
        # return HttpResponse('''<script>alert('Approved');window.location="/admin_view_unit_request/"</script>''')

def admin_view_approve_unit_request(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=uint_registration.objects.filter(status='Approved')
        return render(request,"Admin/admin_view_approve_unit_request.html",{'data':aj})


def admin_reject_unit_request(request,s13):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=uint_registration.objects.get(id=s13)
        aj.status='Rejected'
        aj.save()
        messages.error(request, 'Rejected!')
        return redirect('/admin_view_unit_request/')
        # return HttpResponse('''<script>alert('Rejected');window.location="/admin_view_unit_request/"</script>''')


###### Carrier Management  ########


def admin_view_carrier_application(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=job_apply.objects.filter(status="Pending")
        return render(request,"Admin/admin_view_carrier_application.html",{'data':aj})

def admin_view_personal_details(request,s9):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=job_apply.objects.get(id=s9)
        return render(request,"Admin/admin_View_personal_details.html",{'data':aj})

def admin_allot_interview(request,s30):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data=job_apply.objects.get(id=s30)
        return render(request,"Admin/admin_allot_interview.html",{'data':data})

def admin_allot_interview_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id=request.POST.get('id')
        d=request.POST.get('textfield')
        t=request.POST.get('textfield4')
        v=request.POST.get('textarea')
        bobj=job_apply.objects.get(id=id)
        bobj.int_date=d
        bobj.int_time=t
        bobj.venue=v
        bobj.int_status='Scheduled'
        bobj.save()
        send_mail('Thanks for Your Response...','Mr'+bobj.Name+'   ''Your Are SortListed By Mechland Tools''    ''Your Interview Will be on''   ''Date:'+d+'   ''and''   ''Time:'+t+'  ''Venue:'+v, 'from@example.co',[bobj.Email,])
        messages.success(request, 'Interview Alloted!')
        return redirect('/admin_view_carrier_application/')
        # return HttpResponse('''<script>alert('Interview Alloted');window.location="/admin_view_carrier_application/"</script>''')



def admin_view_carrier_application_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        search=request.POST['textfield']
        if search:
            aj=job_apply.objects.filter(Name__icontains=search)
            if aj:
                return render(request,"Admin/admin_view_carrier_application.html",{'data':aj})
            else:
                return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/admin_view_carrier_application/"</script>''')

def admin_view_carrier_application_labour(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        # aj=job_master.objects.filter(job_role="Labour")
        var2=job_apply.objects.filter(job_id_id__job_role="Labour",status="Pending")
        return render(request,"Admin/admin_view_carrier_application_labour.html",{'data':var2})

def admin_view_carrier_application_supervisor(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        var2=job_apply.objects.filter(job_id_id__job_role="Supervisor",status="Pending")
        return render(request,"Admin/admin_view_carrier_application_labour.html",{'data':var2})


def admin_delete_carrier_application(request,s15):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=job_apply.objects.get(id=s15)
        aj.delete()
        messages.error(request, 'Deleted!')
        return redirect('/admin_view_carrier_application/')



###### Business Request Management  ########

def admin_view_business_request(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=business.objects.filter(status='Pending')
        return render(request,"Admin/admin_view_business_request.html",{'data':aj})

def admin_approve_business_request(request,s16):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=business.objects.get(id=s16) 
        return render(request,"Admin/admin_reply_business_request.html",{'data':aj})

def admin_approve_business_request_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id=request.POST.get('id')
        d=request.POST.get('textfield')
        t=request.POST.get('textfield4')
        bobj=business.objects.get(id=id)
        bobj.date=d
        bobj.time=t
        bobj.status='Approved'
        bobj.save()
        send_mail('Thanks for Responding...','Mr'+bobj.Name+'Please Visit Our Company on''Date:'+d+'and''Time:'+t, 'from@example.co',[bobj.Email,])
        messages.success(request, 'Apporved!')
        return redirect('/admin_view_business_request/')
        # return HttpResponse('''<script>alert('Accepted');window.location="/admin_view_business_request/"</script>''')




def admin_reject_business_request(request,s17):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=business.objects.get(id=s17)
        aj.status='Rejected'
        aj.save()
        messages.error(request, 'Apporved!')
        return redirect('/admin_view_business_request/')
        # return HttpResponse('''<script>alert('Rejected');window.location="/admin_view_business_request/"</script>''')


def admin_view_approved_business_request(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=business.objects.filter(status='Approved')
        return render(request,"Admin/admin_view_approved_business_request.html",{'data':aj})



######## LOAN REQUEST ########

# def admin_add_loan_master(request):
#     return render(request,'Admin/admin_add_loan_master.html')

# def admin_add_loan_master_post(request):
#     lt=request.POST['textfield']
#     ll=request.POST['textfield2']
#     aj=loan_master()
#     aj.loan_type=lt
#     aj.loan_limit=ll
#     aj.save()
#     return HttpResponse('''<script>alert('Success');window.location="/admin_add_loan_master/"</script>''')

# def admin_view_loan_master(request):
#     aj=loan_master.objects.all()
#     return render(request,"Admin/admin_view_loan_master.html",{'data':aj})

# def admin_edit_loan_master(request,s12):
#     aj=loan_master.objects.get(id=s12)
#     return render(request,'Admin/admin_edit_loan_master.html',{'data':aj})

# def admin_edit_loan_master_post(request):
#     id=request.POST.get('id')
#     lt=request.POST['textfield']
#     ll=request.POST['textfield2']
#     aj=loan_master.objects.get(id=id)
#     aj.loan_type=lt
#     aj.loan_limit=ll
#     aj.save()
#     return redirect('/admin_view_loan_master/')

# def admin_delete_loan_master(request,s19):
#     aj=loan_master.objects.get(id=s19)
#     aj.delete()
#     return redirect('/admin_view_loan_master/')


    
def admin_view_loan_request(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=loan.objects.filter(status='Pending')
        return render(request,"Admin/admin_view_loan_request.html",{'data':aj})


def admin_approve_loan_request(request,s18):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=loan.objects.get(id=s18)
        aj.status='Approved'
        aj.save()
        aj=loan_master()
        from datetime import datetime
        aj.approval_date=datetime.now().strftime('%Y-%m-%d')
        aj.installment=aj.installment
        aj.staff_id_id=aj.staff_id_id
        aj.loan_id_id=aj.id
        aj.status='pending'
        aj.save()
        messages.success(request, 'Loan Apporved!')
        return redirect('/admin_view_loan_request/')
        # return HttpResponse('''<script>alert('Approved');window.location="/admin_view_loan_request/"</script>''')

def admin_reject_loan_request(request,s19):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=loan.objects.get(id=s19)
        aj.status='Rejected'
        aj.save()
        messages.success(request, 'Loan Rejected!')
        return redirect('/admin_view_loan_request/')
        # return HttpResponse('''<script>alert('Rejected');window.location="/admin_view_loan_request/"</script>''')

def admin_view_approved_loan_request(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=loan.objects.filter(status='Approved')
        return render(request,"Admin/admin_view_approved_loan_request.html",{'data':aj})


##### LEAVE REQUEST ######

def admin_set_leave_master(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        return render(request,'Admin/admin_add_leave_master.html')

def admin_set_leave_master_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        lt=request.POST['textfield']
        nod=request.POST['textfield2']
        # sal=request.POST['textfield3']
        aj=leave_master()
        aj.leave_type=lt
        aj.leave_limit=nod
        # aj.salary=sal
        aj.save()
        messages.success(request, 'Added Succesfully!')
        return redirect('/admin_view_leave_master/')
        # return HttpResponse('''<script>alert('Success');window.location="/admin_view_leave_master/"</script>''')

def admin_view_leave_master(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=leave_master.objects.all()
        return render(request,"Admin/admin_view_leave_master.html",{'data':aj})

def admin_view_leave_request(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=Leave3.objects.filter(status='Pending')
        return render(request,"Admin/admin_view_leave_request.html",{'data':aj})

def admin_view_leave_request_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        search=request.POST['date']
        if search:
            aj=Leave3.objects.filter(req_date__icontains=search)
            if aj:
                return render(request,"Admin/admin_view_leave_request.html",{'data':aj})
            else:
                return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/admin_view_leave_request/"</script>''')

def admin_edit_leave_master(request,s14):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=leave_master.objects.get(id=s14)
        return render(request,'Admin/admin_edit_leave_master.html',{'data':aj})

def admin_delete_leave_master(request,s18):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=leave_master.objects.get(id=s18)
        aj.delete()
        messages.error(request, 'Deleted Succesfully!')
        return redirect('/admin_view_leave_master/')



def admin_edit_leave_master_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id=request.POST.get('id')
        lt=request.POST['textfield']
        nod=request.POST['textfield2']
        # sal=request.POST['textfield3']
        aj=leave_master.objects.get(id=id)
        aj.leave_type=lt
        aj.leave_limit=nod
        # aj.salary=sal
        aj.save()
        messages.success(request, 'Edited Succesfully!')
        return redirect('/admin_view_leave_master/')
        # return HttpResponse('''<script>alert('Success');window.location="/admin_view_leave_master/"</script>''')


def admin_approve_leave_request(request,s22):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=Leave3.objects.get(id=s22)
        aj.status='Approved'
        aj.save()
        messages.success(request, 'Leave Approved!')
        return redirect('/admin_view_leave_request/')
        # return HttpResponse('''<script>alert('Approved');window.location="/admin_view_leave_request/"</script>''')

def admin_reject_leave_request(request,s23):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=Leave3.objects.get(id=s23)
        aj.status='Rejected'
        aj.save()
        messages.error(request, 'Leave Rejected!')
        return redirect('/admin_view_leave_request/')
        # return HttpResponse('''<script>alert('Rejected');window.location="/admin_view_leave_request/"</script>''')

def admin_view_approved_leave_request(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=Leave3.objects.filter(status='Approved')
        return render(request,"Admin/admin_view_approved_leave_request.html",{'data':aj})


################ REVIEWS AND COMPLAINTS ######################

def admin_view_unit_reviews(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=unit_review1.objects.all()
        return render(request,"Admin/admin_view_unit_reviews.html",{'data':aj})

def admin_view_unit_complaints(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=unit_complaint.objects.filter(status='Pending')
        return render(request,"Admin/admin_view_unit_complaints.html",{'data':aj})

def admin_respond_unit_complaint(request,s25):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=unit_complaint.objects.get(id=s25)
        aj.status='We will sort it out soon, Thanks!'
        aj.save()
        messages.success(request, 'Success!')
        return redirect('/admin_view_unit_complaints/')
        # return HttpResponse('''<script>alert('Success');window.location="/admin_view_unit_complaints/"</script>''')


################ Attendance ######################

def admin_view_section(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data10 = job_master.objects.filter(job_role="manager")
        selected_section = request.POST.get('select')
        if selected_section:
            data = staff.objects.exclude(job_id_id__in=[ct.id for ct in data10]).filter(section=selected_section)
        else:
            data = staff.objects.exclude(job_id_id__in=[ct.id for ct in data10])

        return render(request, 'Admin/admin_view_section.html', {'data': data})


def admin_view_staff_for_attendance(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data10=job_master.objects.filter(job_role="manager")
        data=staff.objects.exclude(job_id_id__in=[ct.id for ct in data10]).filter(section=request.POST.get('select'))
        return render(request,"Admin/admin_view_staff_for_attendance.html",{'data': data})


def admin_add_excel(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        return render(request, 'Admin/admin_add_excel.html')



def Import_Excel_pandas(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        import pandas as pd
        if request.method == 'POST' and request.FILES['myfile']:      
            myfile = request. FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(myfile)              
            at_data = pd.read_excel(myfile)        
            dbd = at_data
            for dbd in dbd.itertuples():
                obj = attendance.objects.create(month=dbd.month,year=dbd.year, no_of_working_days=dbd.no_of_working_days,staff_id_id=dbd.staff_id_id )           
                obj.save()
            return redirect('/admin_view_attendance/')   
        return redirect('/admin_view_attendance/')  



# def admin_add_excel(request):
#     import pandas as pd
#     if request.method == 'POST' and request.FILES['excel_file']:
#         excel_file = request.FILES['excel_file']
        
#         # Load the Excel file into a pandas DataFrame
#         df = pd.read_excel(excel_file)
        
#         # Iterate over each row in the DataFrame and create attendance objects
#         for index, row in df.iterrows():
#             attendance.objects.create(
#                 month=row['month'],
#                 year=row['year'],
#                 no_of_working_days=row['no_of_working_days'],
#                 staff_id_id=row['staff_id_id']
#             )
        
#         # Optionally, you can redirect the user to another page after successful import
#         return redirect('/admin_view_attendance/')
    
#     return render(request, 'Admin/admin_add_excel.html')


def admin_add_attendance(request,s2):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=staff.objects.get(id=s2)
        return render(request,'Admin/admin_add_attendance.html',{'data':aj})

def admin_add_attendance_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        id=request.POST.get('id')
        wd=request.POST['textfield4']
        aj=attendance()
        aj.staff_id_id=id
        from datetime import datetime
        aj.month=datetime.now().strftime('%m')
        aj.year=datetime.now().strftime('%Y')
        aj.no_of_working_days=wd
        aj.save()
        messages.success(request, 'Attendance Added Succesfully!')
        return redirect('/admin_view_attendance/')
        # return HttpResponse('''<script>alert('Success');window.location="/admin_view_attendance/"</script>''')

def admin_view_attendance(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=attendance.objects.all()
        return render(request,"Admin/admin_view_attendance.html",{'data':aj})

def admin_delete_attendance(request,s11):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=attendance.objects.get(id=s11)
        aj.delete()
        messages.error(request, 'Deleted Succesfully!')
        return redirect('/admin_view_attendance/')
   


def admin_change_password(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=request.session.get('adm')
        aj=login.objects.get(username=aj)
        return render(request,"Admin/admin_change_password.html",{'data':aj})


def admin_change_password_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        oldpass=request.POST['password']
        newpass=request.POST['password2']
        confpass=request.POST['password3']
        res=login.objects.filter(username=request.session['adm'],password=oldpass)
        if res.exists():
            if newpass == confpass:
                ress = res.update(password=newpass)
                messages.success(request, 'Password Updated Succesfully!')
                return redirect('/admin2/')
                # return HttpResponse('''<script>alert('Password Updated');window.location="/admin2/"</script>''')
            else:
                messages.error(request, 'Password Does Not Match!')
                return redirect('/admin_change_password/')
                # return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/admin_change_password/";</Script>''')
        else:
            messages.error(request, 'Old Password DoesNot Match New Password!')
            return redirect('/admin_change_password/')
            # return HttpResponse('''<Script>alert("Old Password DoesNot Match New Password");window.location="/admin_change_password/";</Script>''')
        

def admin_view_section_for_salary(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data10 = job_master.objects.filter(job_role="manager")
        selected_section = request.POST.get('select')
        if selected_section:
            data = staff.objects.exclude(job_id_id__in=[ct.id for ct in data10]).filter(section=selected_section)
        else:
            data = staff.objects.exclude(job_id_id__in=[ct.id for ct in data10])

        return render(request, 'Admin/admin_view_section_for_salary.html', {'data': data})

def admin_view_staff_leave_for_salary(request,l1):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:

        data10=leave_master.objects.filter(leave_type="CasualLeave")
        obj=Leave3.objects.filter(staff_id_id=l1).filter(status="Approved").filter(leave_id_id__in=[ct.id for ct in data10]).aggregate(sum=Sum('no_of_days'))['sum'] 
        print(obj)
        data11=leave_master.objects.filter(leave_type="MedicalLeave")
        obj1=Leave3.objects.filter(staff_id_id=l1).filter(status="Approved").filter(leave_id_id__in=[ct.id for ct in data11]).aggregate(sum=Sum('no_of_days'))['sum'] 
    
        print(obj1)
        data12=leave_master.objects.filter(leave_type="SickLeave")
        obj2=Leave3.objects.filter(staff_id_id=l1).filter(status="Approved").filter(leave_id_id__in=[ct.id for ct in data12]).aggregate(sum=Sum('no_of_days'))['sum'] 
        print(obj2)
        if obj==None:
            obj=0
        if obj1==None:
            obj1=0
        if obj2==None:
            obj2=0        
        total=obj+obj2+obj1
        print(total)
        finaltotal=total*500
        d1=staff.objects.get(id=l1) 
        d2=job_master.objects.get(id=d1.job_id_id)
        
        data10=leave_master.objects.filter(leave_type="CasualLeave")
    
        obj=Leave3.objects.filter(staff_id_id=l1).filter(status="Approved").filter(leave_id_id__in=[ct.id for ct in data10]).aggregate(sum=Sum('no_of_days'))['sum'] 
        
        return render(request,"Admin/admin_view_staff_leave_for_salary.html",{'c1':obj,'m1':obj1,'s1':obj2,'data':d1,'total':total,'ns':finaltotal,'bs':d2.basic_salary})

def admin_view_staff_loan_for_salary(request,l2):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        d1 = loan.objects.filter(staff_id_id=l2, status="Approved")
        return render(request,"Admin/admin_view_staff_loan_for_salary.html",{'data':d1})

def admin_view_staff_loanmaster_for_salary(request,l3):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        d2 = loan_master.objects.get(loan_id=l3)
        return render(request,"Admin/admin_view_staff_loanmaster_for_salary.html",{'i':d2})

def admin_view_staff_adttendance_for_salary(request,s2):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        d6=attendance.objects.filter(staff_id_id=s2)
        return render(request,"Admin/admin_view_staff_adttendance_for_salary.html",{'data':d6})

def admin_view_staff_advance(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        d1 = advance.objects.filter(status="Pending")
        return render(request, "Admin/admin_view_staff_advance_for_salary copy.html", {'data2': d1})

def admin_approve_advance_request(request,a2):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=advance.objects.get(id=a2)
        aj.status="Approved"
        aj.save()
        return HttpResponse('''<script>alert('Success');window.location="/admin_view_staff_advance/"</script>''')

def admin_reject_advance_request(request,a3):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        aj=advance.objects.get(id=a3)
        aj.status="Rejected"
        aj.save()
        return HttpResponse('''<script>alert('Success');window.location="/admin_view_staff_advance/"</script>''')


def admin_view_staff_advance_for_salary(request, a1):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        from datetime import datetime
        current_month = datetime.now().strftime('%m')
        d1 = advance.objects.filter(staff_id_id=a1, month=current_month)
        return render(request, "Admin/admin_view_staff_advance_for_salary.html", {'data2': d1})


def admin_prepare_salary_slip(request,p1):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data10=leave_master.objects.filter(leave_type="CasualLeave")
        obj=Leave3.objects.filter(staff_id_id=p1).filter(status="Approved").filter(leave_id_id__in=[ct.id for ct in data10]).aggregate(sum=Sum('no_of_days'))['sum'] 
        print(obj)
    
        data12=leave_master.objects.filter(leave_type="SickLeave")
        obj2=Leave3.objects.filter(staff_id_id=p1).filter(status="Approved").filter(leave_id_id__in=[ct.id for ct in data12]).aggregate(sum=Sum('no_of_days'))['sum'] 
        print(obj2)
        if obj==None:
            obj=0

        if obj2==None:
            obj2=0        
        leave_total=obj+obj2
        print(leave_total)
        d3=staff.objects.get(id=p1)
        d1=job_master.objects.get(id=d3.job_id_id)

        bs=d1.basic_salary

        print(bs)

        # from datetime import datetime
        
        # current_month1 = datetime.now().strftime('%m')
        # current_year = datetime.now().strftime('%Y')



        # conditions1 = {'staff_id_id': d3.id}
        # conditions2 = {'month': current_month1}
        # conditions3 = {'year': current_year}
            
        
        # d6 = get_object_or_404(attendance, **conditions1, **conditions2, **conditions3)

        

        # # d6=attendance.objects.get(staff_id_id=d3.id)
        # print(d6.no_of_working_days)
        # atdnce=int(d6.no_of_working_days) * int(d1.cut_salary)
        # print(atdnce)

        final1=int(leave_total)*float(d1.cut_salary)

        from datetime import datetime
        
        current_month = datetime.now().strftime('%m')
        advance1=0
        count1 = advance.objects.filter(staff_id_id=p1, month=current_month).count()
        if count1==0:
            advance1=0
        else:    
            condition1 = {'staff_id_id': d3.id}
            condition2 = {'month': current_month}
            
        
            d2 = get_object_or_404(advance, **condition1, **condition2)

            advance1=int(d2.amount)


        c=loan_master.objects.filter(staff_id_id=p1).count()
        loan=0
        if c==0:
            loan=0
        else:   
            
            print("hhhhhhhhhhhhhhhhhh") 
            d4 = loan_master.objects.get(staff_id_id=p1)
            current_month = datetime.now().strftime('%m')

            if d4.ins_status == current_month:
                print("Increment")
            else:
                print("Decrement")
                loan = float(d4.loan_id.initial_amount)
                loan_instalment = int(d4.installment)
                print(loan_instalment)
                total_install = loan_instalment - 1
                print(total_install)

                if total_install == 0:
                    d4.installment = total_install
                    d4.status = "Loan Completed"
                    d4.save()
                else:
                    d4.installment = total_install
                    d4.ins_status = current_month
                    d4.save()


            
        net=int(bs)-(advance1+int(loan)+final1)

        return render(request, "Admin/admin_prepare_salary_slip.html",{'month':current_month,'staff':d3.id,'job':d1,'value1':leave_total,'value2':final1,'value3':advance1,'value4':loan,'value5':net,'bsal':bs})

def admin_salary_post(request,id):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        count1 = salary.objects.filter(staff_id_id=id, month=request.POST.get('month')).count()
        from datetime import datetime
        yr=datetime.now().strftime('%Y')
    

        if count1==0:
            data=salary()
            data.staff_id_id=id
            data.leave=request.POST.get('leave')
            # data.days=request.POST.get('days')
            data.leaveamount=request.POST.get('lamount')
            data.advance=request.POST.get('advance')
            data.loan=request.POST.get('loan')
            data.net_salary=request.POST.get('net')
            data.month=request.POST.get('month')
            data.year=yr
            data.save()
            messages.success(request, 'Salary Slip Created!')
            return redirect('/admin_view_section_for_salary/')
            # return HttpResponse('''<script>alert('Salary Slip Created');window.location="/admin_view_section_for_salary/"</script>''')
        else:
            messages.error(request, 'Salary Slip Already Created!')
            return redirect('/admin_view_section_for_salary/')
            # return HttpResponse('''<script>alert('Already Created');window.location="/admin_view_section_for_salary/"</script>''')

        # return render(request,'admin_master.html')


def admin_salary_report(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data=salary.objects.all()
        return render(request, "Admin/admin_salary_report.html", {'data': data})

def admin_salary_report_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        month=request.POST.get('select')
        year=request.POST.get('select2')
        data=salary.objects.filter(month=month,year=year)   
        if data:
            return render(request, "Admin/admin_salary_report_post.html", {'data': data})
        else:
            return HttpResponse('''<script>alert('No results Found');window.location="/admin_salary_report/"</script>''')

def admin_salary_report_post2(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        name=request.POST.get('textfield')
        data=salary.objects.filter(staff_id_id__Name=name)
        if data:
            return render(request, "Admin/admin_salary_report_post.html", {'data': data})
        else:
            return HttpResponse('''<script>alert('No results Found');window.location="/admin_salary_report/"</script>''')

def admin_leave_report(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data=salary.objects.all()
        return render(request, "Admin/admin_leave_report.html", {'data': data})

def admin_leave_report_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        month=request.POST.get('select')
        year=request.POST.get('select2')
        data=salary.objects.filter(month=month,year=year)   
        if data:
            return render(request, "Admin/admin_leave_report_post.html", {'data': data})
        else:
            return HttpResponse('''<script>alert('No results Found');window.location="/admin_leave_report/"</script>''')

def admin_leave_report_post2(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        name=request.POST.get('textfield')
        data=salary.objects.filter(staff_id_id__Name=name)
        if data:
            return render(request, "Admin/admin_leave_report_post.html", {'data': data})
        else:
            return HttpResponse('''<script>alert('No results Found');window.location="/admin_leave_report/"</script>''')

def admin_loan_report(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        data=salary.objects.all()
        return render(request, "Admin/admin_loan_report.html", {'data': data})

def admin_loan_report_post(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        month=request.POST.get('select')
        year=request.POST.get('select2')
        data=salary.objects.filter(month=month,year=year)   
        if data:
            return render(request, "Admin/admin_loan_report_post.html", {'data': data})
        else:
            return HttpResponse('''<script>alert('No results Found');window.location="/admin_loan_report/"</script>''')

def admin_loan_report_post2(request):
    if 'adm' not in request.session:
        return redirect('/public_home2/')
    else:
        name=request.POST.get('textfield')
        data=salary.objects.filter(staff_id_id__Name=name)
        if data:
            return render(request, "Admin/admin_loan_report_post.html", {'data': data})
        else:
            return HttpResponse('''<script>alert('No results Found');window.location="/admin_loan_report/"</script>''')




###########################     UNIT INFO      ###############################################################################################

def unitinner(request):
    return render(request,'Unit/inner-page.html')
def unit_about(request):
    return render(request,'Unit/public_about.html')
def unit_service(request):
    return render(request,'Unit/public_service.html')
def unit_contact(request):
    return render(request,'Unit/public_contact.html')

def unit_reg(request):
    return render(request,'Unit/unit_registration.html')

def unit_reg_post(request):
    name=request.POST['textfield']
    c_name=request.POST['textfield2']
    email=request.POST['textfield4']
    pn=request.POST['textfield5']
    place=request.POST['textfield8']
    city=request.POST['textfield9']
    state=request.POST['textfield10']
    pin=request.POST['textfield11']
    password=request.POST['textfield13']
    Photo=request.FILES['Photo']
    fs=FileSystemStorage()
    filename=fs.save(Photo.name,Photo)
    uploaded_file_url = fs.url(filename)

    aj=uint_registration()
    aj.Name=name
    aj.Company_Name=c_name
    aj.Email=email
    aj.Phone_Number=pn
    aj.Place=place
    aj.City=city
    aj.State=state
    aj.Pincode=pin
    aj.password=password
    aj.Photo=uploaded_file_url
    aj.status='Pending'
    aj.save()
    messages.success(request, 'Successfully Registered!')
    return redirect('/public_home2/')
    # return HttpResponse('''<script>alert('Success');window.location="/public_home2/"</script>''')

def unit_view_profile(request):
    aj=request.session.get('unit')
    aj=uint_registration.objects.get(Email=aj)
    return render(request,'Unit/unit_view_profile.html',{'data':aj})

def unit_edit_profile(request,s6):
    aj=uint_registration.objects.get(id=s6)
    return render(request,'Unit/unit_edit_profile.html',{'data':aj})

def unit_edit_profile_post(request):
    id=request.POST.get('id')
    name=request.POST['name']
    c_name=request.POST['company_name']
    email=request.POST['email']
    pn=request.POST['phone']
    place=request.POST['place']
    city=request.POST['city']
    state=request.POST['state']
    pin=request.POST['pincode']
    if 'Photo' in request.FILES:
        Photo = request.FILES['Photo']

        Photo=request.FILES['Photo']
        fs=FileSystemStorage()
        filename=fs.save(Photo.name,Photo)
        uploaded_file_url = fs.url(filename)

        aj=uint_registration.objects.get(id=id)
        aj.Name=name
        aj.Company_Name=c_name
        aj.Email=email
        aj.Phone_Number=pn
        aj.Place=place
        aj.City=city
        aj.State=state
        aj.Pincode=pin
        aj.Photo=uploaded_file_url
        aj.save()
        return HttpResponse('''<script>alert('Updated');window.location="/unit_view_profile/"</script>''') 
    else:
        aj=uint_registration.objects.get(id=id)
        aj.Name=name
        aj.Company_Name=c_name
        aj.Email=email
        aj.Phone_Number=pn
        aj.Place=place
        aj.City=city
        aj.State=state
        aj.Pincode=pin
        aj.save()
        messages.success(request, 'Successfully Updated!')
        return redirect('/unit_view_profile/')
        # return HttpResponse('''<script>alert('Updated');window.location="/unit_view_profile/"</script>''')

def unit_view_moulds(request):
    aj=add_mould.objects.all()
    return render(request, 'Unit/unit_view_moulds.html',{'data':aj})

def unit_view_moulds_post(request, s7):
    # aj=add_mould.objects.all()
    data2 = add_mould.objects.get(id=s7)
    data3 = product_review.objects.filter(order_id__mould_id=data2)
    return render(request, 'Unit/unit_view_mould_detail.html', {'data2': data2,'data3':data3})





def unit_mould_review(request, s28):
    aj = unit_order.objects.get(id=s28)
    return render(request, 'Unit/unit_mould_review.html', {'data': aj})

def unit_mould_review_post(request):
    review = request.POST['textarea']
    mid = request.POST.get('id')

    from datetime import datetime
    data = uint_registration.objects.get(Email=request.session['unit'])
    
    # Check if the unit has already reviewed the product
    if not product_review.objects.filter(order_id_id=mid, order_id__unit_id_id=data.id).exists():
        aj = product_review()
        aj.review = review
        aj.date = datetime.now().strftime('%Y-%m-%d')
        data = uint_registration.objects.get(Email=request.session['unit'])
        aj.order_id_id__unit_id_id = data.id
        aj.order_id_id = mid
        aj.save()
        messages.success(request, 'Successfully Posted!')
    else:
        messages.error(request, 'already reviewed!')
    
    return redirect('/unit_view_moulds/')



def unit_send_complaint(request):
    return render(request, 'Unit/unit_send_complaint.html')

def unit_send_complaint_post(request):
    complaint=request.POST['textarea5']
    date=request.POST['textfield2']
    aj=unit_complaint()
    aj.complaint=complaint
    aj.date=date
    aj.status='Pending'
    aj.unit_id=uint_registration.objects.get(Email=request.session['unit'])
    aj.save()
    messages.success(request, 'Successfully Posted!')
    return redirect('/unit_send_complaint/')
    # return HttpResponse('''<script>alert('Success');window.location="/unit_send_complaint/"</script>''')

def unit_view_complaint(request):
    aj = request.session.get('unit')
    val2 = uint_registration.objects.get(Email=aj)
    val3 = unit_complaint.objects.filter(unit_id_id=val2)
    return render(request, 'Unit/unit_view_complaint.html',{'data':val3})

def unit_order_moulds(request,s1):
    aj=add_mould.objects.get(id=s1)
    return render(request, 'Unit/unit_order_moulds.html',{'data':aj})

def unit_order_moulds_post(request):
    mn=request.POST.get('id')
    q=request.POST['textfield2']
    net=request.POST['textfield1']
    st=request.POST['textfield3']
    sze=request.POST.get('size1')
    sze2=request.POST.get('size')
    print(sze)
    pm=request.POST['payment_method']
    request.session['stp']=st
    request.session['ss']=sze
    request.session['ss2']=sze2
    request.session['q']=q
    request.session['mn']=mn
    request.session['net']=net
    request.session['pm']=pm




    if pm == "Online":  
        return HttpResponse('''<script>window.location="/unit_make_payment/'''+net+'''"</script>''')
    else:  
        aj=unit_order()
        aj.mould_id_id=request.session['mn']
        data=uint_registration.objects.get(Email=request.session['unit'])
        aj.unit_id_id=data.id
        aj.quantity=request.session['q']
        if st == "Fixed":
            aj.size=sze2
        else:
            aj.size=sze
        aj.payment_method=request.session['pm']
        from datetime import datetime
        aj.date=datetime.now().strftime('%Y-%m-%d')
        aj.status="Pending"
        aj.save()
        data=unit_order.objects.last()


        aj1=payment()
        aj1.unit_order_id_id=data.id
        aj1.bank=""
        aj1.Account_num=""
        aj1.ifsc=""
        aj1.amount=net
        from datetime import datetime
        aj1.date=datetime.now().strftime('%Y-%m-%d')
        aj1.status="Paid"
        aj1.save()
        messages.success(request, 'SucessfullY Order!')
        return redirect('/unit_view_moulds/')
        # return HttpResponse('''<script>alert('Ordered Sucessfull');window.location="/unit_view_moulds/"</script>''')

def unit_make_payment(request,s4):
    return render(request, 'Unit/unit_make_payment.html',{'s4':s4})

def unit_make_payment_post(request):
    aj=unit_order()
    aj.mould_id_id=request.session['mn']
    data=uint_registration.objects.get(Email=request.session['unit'])
    aj.unit_id_id=data.id
    aj.quantity=request.session['q']
    if request.session['stp'] == "Fixed":
        aj.size=request.session['ss2']
    else:
        aj.size=request.session['ss']
    aj.payment_method=request.session['pm']
    from datetime import datetime
    aj.date=datetime.now().strftime('%Y-%m-%d')
    aj.status="Pending"
    aj.save()

    bank=request.POST['textfield1']
    an=request.POST['textfield']
    ifsc=request.POST['textfield4']
    amnt=request.session['net']
    d1=unit_order.objects.last()
    aj=payment()
    aj.unit_order_id_id=d1.id
    aj.bank=bank
    aj.Account_num=an
    aj.ifsc=ifsc
    aj.amount=amnt
    from datetime import datetime
    aj.date=datetime.now().strftime('%Y-%m-%d')
    aj.status=""
    aj.save()
    messages.success(request, 'Transaction Sucessfull!')
    return redirect('/unit_view_moulds/')
    # return HttpResponse('''<script>alert('Transaction Sucessfull');window.location="/unit_view_moulds/"</script>''')

def unit_view_order_status(request):
    aj = request.session.get('unit')
    val2 = uint_registration.objects.get(Email=aj)
    val3 = unit_order.objects.filter(unit_id_id=val2).order_by('-id')
    aj=cancel.objects.all()
    return render(request, 'Unit/unit_view_order_status.html',{'data':val3, 'aj':aj})

def unit_view_delivery_status(request,s8):
    aj=unit_order.objects.get(id=s8)
    return render(request, 'Unit/unit_view_delivery_status.html',{'data':aj})

# def unit_recieve_product(request,s9):
#     aj=unit_order.objects.get(id=s9)
#     aj.status="Recieved"
#     aj.save()
#     return redirect('/unit_view_order_status/')

def unit_cancel_order(request,s3):
    aj=unit_order.objects.get(id=s3)
    from datetime import datetime
    aj.c_date=datetime.now().strftime('%Y-%m-%d')
    aj.order_id_id=aj.id
    aj.status="Cancelled"
    if aj.payment_method == "COD":
        aj.cancel_status="Your Order is Cancelled"
    else:
        aj.cancel_status="Your Money will be refunded within 4 days"
    aj.save()
    messages.success(request, 'Cancelled!')
    return redirect('/unit_view_cancel_status/')
    # return HttpResponse('''<script>alert('Cancel Request Sent!');window.location="/unit_view_order_status/"</script>''')

def unit_view_cancel_status(request):
    aj = request.session.get('unit')
    val2 = uint_registration.objects.get(Email=aj)
    val3 = unit_order.objects.filter(unit_id=val2,status="Cancelled").order_by('-id')

    return render(request, 'Unit/unit_view_cancel_status.html',{'data':val3})

def unit_change_password(request):
    aj=request.session.get('unit')
    aj=login.objects.get(username =aj)
    return render(request,"Unit/unit_change_password.html",{'data':aj})


def unit_change_password_post(request):
    oldpass=request.POST['password']
    newpass=request.POST['password2']
    confpass=request.POST['password3']
    res=login.objects.filter(username=request.session['unit'],password=oldpass)
    if res.exists():
        if newpass == confpass:
            ress = res.update(password=newpass)
            messages.success(request, 'Password Updated!')
            return redirect('/unit_view_profile/')
            # return HttpResponse('''<script>alert('Password Updated');window.location="/unit_view_profile/"</script>''')
        else:
            messages.error(request, 'Password Does Not Match!')
            return redirect('/unit_change_password/')
            # return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/unit_change_password/";</Script>''')
    else:
        messages.error(request, 'Old Password DoesNot Match New Password!')
        return redirect('/unit_change_password/')
        # return HttpResponse('''<Script>alert("Old Password DoesNot Match New Password");window.location="/unit_change_password/";</Script>''')





def public_view_predict_mould(request):
    aj=predict_mould.objects.all()
    return render(request,"Public/public_view_predict_mould.html",{'data':aj})

def public_rate_mould(request,s2):
    aj=predict_mould.objects.get(id=s2)
    return render(request,"Public/public_rate_mould.html",{'data':aj})

def public_rate_mould_post(request):
    id=request.POST.get('id')
    mn=request.POST['textfield5']
    img=request.POST['rating1']
    sug=request.POST['suggestions']
    c=ratting.objects.filter(predict_mould_id_id=id).count()
    print("jjjjjjjjjjjjj")
    print(c)
    if c==0:

        aj=ratting()
        aj.predict_mould_id_id=id
        
        aj.mname=mn
        if img=="1":

            aj.p1_ratting=1
            aj.p2_ratting=0
            aj.p3_ratting=0
        elif img=="2":
            aj.p1_ratting=0
            aj.p2_ratting=1
            aj.p3_ratting=0
        else:    
            aj.p1_ratting=0
            aj.p2_ratting=0
            aj.p3_ratting=1
        aj.suggestion=sug
        aj.save()
    else:
        aj=ratting.objects.get(predict_mould_id_id=id)
        if img=="1":

            aj.p1_ratting=int(aj.p1_ratting)+1
        elif img=="2":
            aj.p2_ratting=int(aj.p2_ratting)+1
        else:    
            aj.p3_ratting=int(aj.p3_ratting)+1
        aj.save()    
    messages.success(request, 'Rating Sucessfully Rated!')
    return redirect('/public_view_predict_mould/')
    # return HttpResponse('''<script>alert('Success');window.location="/public_view_predict_mould/"</script>''')



###########################             PUBLIC INFO             ###############################################################################################

def public_home(request):
    return render(request,'public_index.html')
def public_about(request):
    return render(request,'Public/public_about.html')
def public_service(request):
    return render(request,'Public/public_service.html')
def contact_service(request):
    return render(request,'Public/public_contact.html')
def public_home2(request):
    return render(request,'index copy.html')
def publicinner(request):
    return render(request,'Public/inner-page.html')

def public_view_carrier(request):
    from datetime import datetime
    cur_date = datetime.now().strftime('%Y-%m-%d')

    aj=job_master.objects.exclude(date__lt=cur_date).values()

           
    return render(request,"Public/public_view_carrier.html",{'data':aj})

def public_view_vacancy(request,s13):
    aj=job_master.objects.filter(id=s13)
    return render(request,"Public/public_view_vacancy.html",{'data':aj})

def public_apply_job(request,s14):
    values=job_master.objects.get(id=s14)
    return render(request,'Public/public_apply_job.html',{'data':values})

def public_apply_job_post(request):
    jid=request.POST.get('textfield1')
    

    name=request.POST['textfield']
    gender=request.POST['RadioGroup1']
    dob=request.POST['textfield2']
    email=request.POST['textfield4']
    phone=request.POST['textfield5']
    hn=request.POST['HouseName']
    place=request.POST['Place']
    city=request.POST['City']
    state=request.POST['State']
    pin=request.POST['pin']
    quali=request.POST['textfield7']
    exp=request.POST['textfield8']
    rem=request.POST['textarea']

    Photo=request.FILES['Photo']
    fs=FileSystemStorage()
    filename=fs.save(Photo.name,Photo)
    uploaded_file_url1 = fs.url(filename)
    
    aj=job_apply()
    aj.job_id_id=jid
    aj.Name=name
    aj.Gender=gender
    aj.Date_of_birth=dob
    aj.Email=email
    aj.Phone_Number=phone
    aj.Hname=hn
    aj.Place=place
    aj.City=city
    aj.State=state
    aj.Pin=pin
    aj.qualifications=quali
    aj.experiences=exp
    aj.remark=rem
    aj.Photo=uploaded_file_url1
    data=job_master.objects.get(id=jid)
    if data.job_role!='Labour':
        Resume=request.FILES['Resume']
        fs=FileSystemStorage()
        filename=fs.save(Resume.name,Resume)
        uploaded_file_url = fs.url(filename)
        aj.resume=uploaded_file_url

    
    aj.status='Pending'
    aj.save()
    messages.success(request, 'Applied Sucessfully!')
    return redirect('/public_view_carrier/')
    # return HttpResponse('''<script>alert('Success');window.location="/public_view_carrier/"</script>''')

def public_business_request(request):
    return render(request,'Public/public_business_request.html')

def public_business_request_post(request):
    cname=request.POST['textfield1']
    name=request.POST['textfield']
    email=request.POST['textfield4']
    phone=request.POST['textfield5']
    address=request.POST['textarea2']
    comments=request.POST['textarea']

    aj=business()
    aj.Company_name=cname
    aj.Name=name
    aj.Email=email
    aj.Phone_Number=phone
    aj.Address=address
    aj.Comments=comments
    aj.status='Pending'
    aj.save()
    messages.success(request, 'Request Sent!')
    return redirect('/public_business_request/')
    # return HttpResponse('''<script>alert('Success');window.location="/public_business_request/"</script>''')

def public_view_business_request(request):
    aj=business.objects.all()
    

def public_view_predict_mould(request):
    aj=predict_mould.objects.all()
    return render(request,"Public/public_view_predict_mould.html",{'data':aj})

def public_rate_mould(request,s2):
    aj=predict_mould.objects.get(id=s2)
    return render(request,"Public/public_rate_mould.html",{'data':aj})

def public_rate_mould_post(request):
    id=request.POST.get('id')
    mn=request.POST['textfield5']
    img=request.POST['rating1']
    sug=request.POST['suggestions']
    c=ratting.objects.filter(predict_mould_id_id=id).count()
    print("jjjjjjjjjjjjj")
    print(c)
    if c==0:

        aj=ratting()
        aj.predict_mould_id_id=id
        
        aj.mname=mn
        if img=="1":

            aj.p1_ratting=1
            aj.p2_ratting=0
            aj.p3_ratting=0
        elif img=="2":
            aj.p1_ratting=0
            aj.p2_ratting=1
            aj.p3_ratting=0
        else:    
            aj.p1_ratting=0
            aj.p2_ratting=0
            aj.p3_ratting=1
        aj.suggestion=sug
        aj.save()
    else:
        aj=ratting.objects.get(predict_mould_id_id=id)
        if img=="1":

            aj.p1_ratting=int(aj.p1_ratting)+1
        elif img=="2":
            aj.p2_ratting=int(aj.p2_ratting)+1
        else:    
            aj.p3_ratting=int(aj.p3_ratting)+1
        aj.save()    
    messages.success(request, 'Rated Sucessfully !')
    return redirect('/public_view_predict_mould/')
    # return HttpResponse('''<script>alert('Success');window.location="/public_view_predict_mould/"</script>''')





#########  Employee LOAN REQUEST #########

def empinner(request):
    return render(request,'Employee/emp_inner-page.html')

def employee_view_profile(request):
    aj=request.session.get('staff')
    aj=staff.objects.get(Email=aj)
    return render(request, 'Employee/employee_view_profile.html',{'i':aj})

def employee_edit_profile(request,s7):
    data=staff.objects.get(id=s7)
    return render(request,"Employee/employee_edit_profile.html",{'data':data})
def employee_edit_profile_post(request):
    id=request.POST.get('id')
    n=request.POST['textfield']
    g=request.POST['RadioGroup1']
    dob=request.POST['textfield2']
    email=request.POST['textfield4']
    phone=request.POST['textfield5']
    address=request.POST['textfield7']
    if 'Photo' in request.FILES:
        Photo = request.FILES['Photo']  
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo)
        uploaded_file_url = fs.url(filename)

        aj=staff.objects.get(id=id)
        aj.Name=n
        aj.Gender=g
        aj.Date_of_birth=dob
        aj.Email=email
        aj.Phone_Number=phone
        aj.Address=address
        aj.Photo=uploaded_file_url
        aj.save()
        messages.success(request, 'Sucessfully Updated !')
        return redirect('/employee_view_profile/')
    else:
        aj=staff.objects.get(id=id)
        aj.Name=n
        aj.Gender=g
        aj.Date_of_birth=dob
        aj.Email=email
        aj.Phone_Number=phone
        aj.Address=address
        aj.save()
        messages.success(request, 'Sucessfully Updated !')
        return redirect('/employee_view_profile/')

def employee_loan_request(request):
    aj=request.session['staff']
    data=staff.objects.get(Email=aj)
    aj=job_master.objects.get(id=data.job_id_id)
    return render(request,'Employee/employee_loan_request.html',{'data':data,'data2':aj})

def employee_loan_request_post(request):
    id = request.POST.get('id')
    la = int(request.POST['t2'])  
    intsa = int(request.POST['select'])
    p = request.POST['t4']
    # aj=staff.objects.get(id=id)
    aj = loan()
    val2=request.session['staff']
    data5=staff.objects.get(Email=val2)
    aj.staff_id_id = data5.id
    aj.loan_amount = la
    aj.installment = intsa
    from datetime import datetime
    aj.date = datetime.now().strftime('%Y-%m-%d')
    aj.purpose = p
    aj.status = 'Pending'

    if la:      
        floan = la / intsa
        print(floan)
        aj.initial_amount = floan

    aj.save()
    messages.success(request, 'Loan Request Sent!')
    return redirect('/employee_loan_request/')
    # return HttpResponse('''<script>alert('Success');window.location="/employee_loan_request/"</script>''')


def employee_view_loan_status(request):
    staff_un = request.session.get('staff')
    staff_data = staff.objects.get(Email=staff_un)
    aj = loan.objects.filter(staff_id_id=staff_data)
    return render(request, "Employee/employee_view_loan_status.html", {'data': aj})

def employee_apply_advance(request):
    aj=request.session['staff']
    data=staff.objects.get(Email=aj)
    return render(request,'Employee/employee_apply_advance.html',{'data': data})

def employee_apply_advance_post(request):
    from datetime import datetime
    id=request.POST.get('id')
    amount=request.POST['t2']
    purpose=request.POST['t4']
    mnth=datetime.now().strftime('%m')

    existing_advance = advance.objects.filter(month=mnth, staff_id_id=id).exists()
    if existing_advance:
        return HttpResponse('''<script>alert('You have already applied for advance this month');window.location="/employee_apply_advance/"</script>''')
    else:
        aj=advance() 
        aj.month = mnth
        aj.date=datetime.now().strftime('%Y-%m-%d')
        aj.amount=amount
        aj.purpose=purpose
        aj.staff_id_id=id
        aj.status='Pending'
        aj.save()
        return HttpResponse('''<script>alert('Success');window.location="/employee_apply_advance/"</script>''')
    
def employee_view_advance_status(request):
    staff_un = request.session.get('staff')
    staff_data = staff.objects.get(Email=staff_un)
    aj = advance.objects.filter(staff_id_id=staff_data)
    return render(request, "Employee/employee_view_advance_status.html", {'data': aj})
    


    

######### LEAVE REQUEST ###########

def employee_leave_request(request):
    aj=request.session['staff']
    data=staff.objects.get(Email=aj)
    aj=leave_master.objects.all()
    return render(request,'Employee/employee_leave_request.html',{'data': data,'data2': aj})

def employee_leave_request_post(request):
    name=request.POST.get('textfield1')
    lt=request.POST['select']
    ll=request.POST['leavelimit']
    fd=request.POST['textfield4']
    td=request.POST['textfield9']
    nod=request.POST['textfield5']
    reason=request.POST['textarea2']
    print(lt)
    print(ll)
    data=leave_master.objects.get(leave_type=lt)
    print(data)
    aj = staff.objects.get(Name=name)
    

    obj=Leave3.objects.filter(staff_id_id=aj).filter(status="Approved").filter(leave_id_id=data.id).aggregate(sum=Sum('no_of_days'))['sum'] 
    print("gggggggggggggggggggg")
    print(obj)
    if obj==None:
        print("hhhhhhhhhhhhhhhhhhhhh")
        aj=Leave3()
        aj.leave_id=data
        aj.staff_id = aj
        from datetime import datetime
        aj.req_date=datetime.now().strftime('%Y-%m-%d')

        aj.fromdate=fd
        aj.todate=td
        aj.no_of_days=nod
        aj.reason=reason
        aj.status='Pending'
        aj.save()
        messages.success(request, 'Leave Request Sent!')
        return redirect('/employee_leave_request/')
        # return HttpResponse('''<script>alert('Success');window.location="/employee_leave_request/"</script>''')
    else:

        if int(obj)>=int(ll):
            messages.error(request, 'Your leave limit is over!')
            return redirect('/employee_leave_request/')
            # return HttpResponse('''<script>alert('Your leave limit is over');window.location="/employee_leave_request/"</script>''')  
        else:
            aj=Leave3()
            aj.leave_id=data
            aj.staff_id = aj
            from datetime import datetime
            aj.req_date=datetime.now().strftime('%Y-%m-%d')

            aj.fromdate=fd
            aj.todate=td
            aj.no_of_days=nod
            aj.reason=reason
            aj.status='Pending'
            aj.save()
            messages.success(request, 'Leave Request Sent!')
            return redirect('/employee_leave_request/')
            # return HttpResponse('''<script>alert('Success');window.location="/employee_leave_request/"</script>''')


def employee_view_leave_status(request):
    aj=request.session.get('staff')
    var2=staff.objects.get(Email=aj)
    var3=Leave3.objects.filter(staff_id_id=var2)
    return render(request, 'Employee/employee_leave_status.html',{'data':var3})


############ Shift Allots #########################

def employee_view_shift_allotment(request):
    aj=staff.objects.get(Email=request.session.get('staff'))
    var2=shift_allotment.objects.filter(staff_id_id=aj.id)
    return render(request, 'Employee/employee_view_shift_allotment.html',{'data':var2})


def employee_view_salary_slip(request):
    aj=staff.objects.get(Email=request.session.get('staff'))
    var2=salary.objects.filter(staff_id_id=aj.id)
    return render(request, 'Employee/employee_view_salary_slip.html',{'data':var2})


def employee_change_password(request):
    aj=request.session.get('staff')
    aj=login.objects.get(username=aj)
    return render(request,"Employee/employee_change_password.html",{'data':aj})


def employee_change_password_post(request):
    oldpass=request.POST['password']
    newpass=request.POST['password2']
    confpass=request.POST['password3']
    res=login.objects.filter(username=request.session['staff'],password=oldpass)
    if res.exists():
        if newpass == confpass:
            ress = res.update(password=newpass)
            messages.error(request, 'Password Updated!')
            return redirect('/staff_login/')
            # return HttpResponse('''<script>alert('Password Updated');window.location="/staff_login/"</script>''')
        else:
            messages.error(request, 'Password Does Not Match!')
            return redirect('/employee_change_password/')
            return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/employee_change_password/";</Script>''')
    else:
        messages.error(request, 'Old Password DoesNot Match!')
        return redirect('/employee_change_password/')
        # return HttpResponse('''<Script>alert("Old Password DoesNot Match");window.location="/employee_change_password/";</Script>''')

def employee_view_attendance(request):
    aj=staff.objects.get(Email=request.session.get('staff'))
    aj2 = attendance.objects.filter(staff_id_id=aj)
    return render(request, 'Employee/employee_view_attendance.html',{'data':aj2})


    



################################## MANAGER #################################################################

def manager_view_profile(request):
    aj=manager.objects.get(Email=request.session.get('mngr'))
    return render(request,'Manager/manager_view_profile.html',{'i':aj})

def manager_edit_profile(request,s7):
    data=manager.objects.get(id=s7)
    return render(request,"Manager/manager_edit_profile.html",{'data':data})
def manager_edit_profile_post(request):
    id=request.POST.get('id')
    n=request.POST['textfield']
    g=request.POST['RadioGroup1']
    dob=request.POST['textfield2']
    email=request.POST['textfield4']
    phone=request.POST['textfield5']
    hn=request.POST['textfield7']
    place=request.POST['textfield8']
    city=request.POST['textfield9']
    state=request.POST['textfield10']
    pin=request.POST['textfield11']
    if 'Photo' in request.FILES:
        Photo = request.FILES['Photo']  
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo)
        uploaded_file_url = fs.url(filename)

        aj=manager.objects.get(id=id)
        aj.Name=n
        aj.Gender=g
        aj.Date_of_birth=dob
        aj.Email=email
        aj.Phone_Number=phone
        aj.house_name=hn
        aj.Place=place
        aj.City=city
        aj.State=state
        aj.Pincode=pin
        aj.photo=uploaded_file_url
        aj.save()
        messages.success(request, "Successfully Updated!")
        return redirect('/manager_view_profile/')
        # return HttpResponse('''<script>alert('Updated');window.location="/manager_view_profile/"</script>''')
    else:
        aj=manager.objects.get(id=id)
        aj.Name=n
        aj.Gender=g
        aj.Date_of_birth=dob
        aj.Email=email
        aj.Phone_Number=phone
        aj.house_name=hn
        aj.Place=place
        aj.City=city
        aj.State=state
        aj.Pincode=pin
        aj.save()
        messages.success(request, "Successfully Updated!")
        return redirect('/manager_view_profile/')
        # return HttpResponse('''<script>alert('Updated');window.location="/manager_view_profile/"</script>''')


def manager_view_staff(request):
    data11 = job_master.objects.filter(job_role="Supervisor")
    selected_section = request.POST.get('select')

    if selected_section and selected_section != 'All':
        data = staff.objects.filter(job_id_id__in=[ct.id for ct in data11]).filter(section=selected_section)
    else:
        data = staff.objects.filter(job_id_id__in=[ct.id for ct in data11])

    return render(request, 'Manager/manager_view_section.html', {'data': data})



# def manager_view_staff2(request):
#     data11 = job_master.objects.filter(job_role="Labour")
#     selected_section = request.POST.get('select')
#     if selected_section:
#         data = staff.objects.filter(job_id_id__in=[ct.id for ct in data11],status="active").filter(section=selected_section)
#     else:
#         data = staff.objects.filter(job_id_id__in=[ct.id for ct in data11])
#     return render(request,'Manager/manager_view_section2.html',{'data':data})

def manager_allot_staff(request,s11):
    staff_data = staff.objects.get(id=s11)
    request.session['srid']=s11
    data11 = job_master.objects.filter(job_role="Supervisor")
    data13 = job_master.objects.filter(job_role="Labour")
    data = staff.objects.exclude(job_id_id__in=[ct.id for ct in data11]).filter(job_id_id__in=[ct.id for ct in data13],status="active").exclude(status="Allotted")
    return render(request,'Manager/manager_allot_staff.html',{'data': data})

def manager_allot_staff_post(request):
    data11 = job_master.objects.filter(job_role="Supervisor")
    selected_section = request.POST.get('select')
    request.session['selected']=selected_section
    data = staff.objects.exclude(job_id_id__in=[ct.id for ct in data11]).filter(section=selected_section,status="active")
    return render(request,'Manager/manager_allot_staff.html',{'data': data})



def manager_view_section(request):
    return render(request,'Manager/manager_view_section.html')

def manager_allot_shift(request,s27):
    data=shift_allot()
    data.staff_id_id=s27
    data.supervisor_id=request.session['srid']
    from datetime import datetime
    data.date=datetime.now().strftime('%Y-%m-%d')
    data.status="Alloted"
    data.save()
    data1=staff.objects.get(id=s27)
    data1.status="Allotted"
    data1.save()

    data11 = job_master.objects.filter(job_role="Supervisor")
    
    selected_section=request.session['selected']
    data = staff.objects.exclude(job_id_id__in=[ct.id for ct in data11]).filter(section=selected_section,status="active")
    return render(request,'Manager/manager_allot_staff.html',{'data': data})
    # return HttpResponse('''<script>alert('Alloted');window.location="/manager_view_staff2/"</script>''')


def manager_allot_shift_post(request):
    sid=request.POST.get('select')
    tid=request.POST.get('select2')
    name=request.POST.get('textfield2')
    aj=shift_allotment()
    aj.shift_id_id=sid
    data=staff.objects.get(Name=name)
    aj.staff_id_id=data.id
    from datetime import datetime
    aj.date=datetime.now().strftime('%Y-%m-%d')
    aj.save()
    messages.success(request, "Successfully Alloted!")
    return redirect('/manager_view_staff/')
    # return HttpResponse('''<script>alert('Alloted');window.location="/manager_view_staff/"</script>''')

def manager_view_alloted_staff(request):
    data11 = job_master.objects.filter(job_role="Supervisor")
    data12=staff.objects.filter(job_id_id__in=[ct.id for ct in data11])
    return render(request, 'Manager/manager_view_alloted_staff.html',{'data':data12})

def manager_view_alloted_staff_post(request):
    selected_section = request.POST.get('select')

    if selected_section == 'All':
        data12 = job_master.objects.filter(job_role="Labour")
        data = staff.objects.exclude(job_id_id__in=[ct.id for ct in data12]) 
    else:
        data13 = job_master.objects.filter(job_role="Labour")
        data = staff.objects.exclude(job_id_id__in=[ct.id for ct in data13]).filter(section=selected_section)

    return render(request, 'Manager/manager_view_alloted_staff.html', {'data': data})


def manager_view_alloted_staff_details(request, s11):
    aj = shift_allot.objects.filter(supervisor_id=s11)
    return render(request, 'Manager/manager_view_alloted_staff_details.html', {'data': aj})







def manager_view_alloted_shift(request):
    from datetime import datetime
    aj = request.session.get('sprvr')
    supervisor = staff.objects.get(Email=aj)
    shift_allotments = shift_allot.objects.filter(supervisor_id=supervisor.id)
    aj=shift_allot.objects.all()
    return render(request,'Manager/manager_view_alloted_shift.html',{'data':aj})

def manager_view_alloted_shift_post(request):
    fd=request.POST['textfield4']
    if fd:
      result=shift_allotment.objects.filter(date__icontains=fd)  
      if result:
         return render(request,'manager_view_alloted_shift.html',{'data':result})
      else:      
         return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_alloted_shift/"</script>''')
      
def manager_view_moulds(request):
    aj=add_mould.objects.all()
    return render(request,'Manager/manager_view_moulds.html',{'data':aj})

def manager_add_stock(request, s2):
    aj = add_mould.objects.get(id=s2)
    return render(request,'Manager/manager_add_stock.html',{'data':aj})

def manager_add_stock1(request, s2):
    gt=request.POST.get('textfield2')
    aj = add_mould.objects.get(id=s2)
    stk = int(aj.stock) + int(gt)
    aj.stock = str(stk)
    aj.save()
    messages.success(request, "Successfully Added!")
    return redirect('/manager_view_moulds/')
    # return HttpResponse('''<script>alert('Successfully Added');window.location="/manager_view_moulds/"</script>''')
      
def manager_view_order(request):
    aj=unit_order.objects.filter(status="Pending")
    return render(request,'Manager/manager_view_order.html',{'data':aj})

def manager_delete_order(request,id):
    values=unit_order.objects.get(id=id)
    values.delete()
    messages.error(request, "Successfully Added!")
    return redirect('/manager_view_moulds/')



def manager_check_payament(request,s4):
    aj=payment.objects.filter(unit_order_id_id=s4)
    return render(request,'Manager/manager_check_payament.html',{'data':aj})

def manger_approve_order(request,s6):
    aj=unit_order.objects.get(id=s6)
    return render(request,'Manager/manger_approve_order.html',{'i':aj})

def manager_approve_order_post(request):
    oid=request.POST.get('id')
    dd=request.POST['textfield']
    dt=request.POST['appt']
    rem=request.POST['textfield2']
    cn=request.POST['appt3']
    vn=request.POST['appt2']
    aj=unit_order.objects.get(id=oid)
    aj.vehicle_number=vn
    aj.contact_number=cn
    aj.delivary_date=dd
    aj.delivary_time=dt
    aj.remarks=rem
    aj.status="Approved"
    estk=int(aj.mould_id.stock)
    qnt=aj.quantity
    print(qnt)
    print(estk)
    if int(estk) < int(qnt):
        return HttpResponse('''<script>alert('Out of Stock');window.location="/manager_view_order/"</script>''')
    else:
        aj.mould_id.stock =int(estk) - int(qnt)
        aj.mould_id.save()
        
    aj.save()
    messages.success(request, "Approved Successfully!")
    return redirect('/manager_view_order/')
    # return HttpResponse('''<script>alert('Approved');window.location="/manager_view_order/"</script>''')
    
def manager_reject_order(request,s7):
    aj=unit_order.objects.get(id=s7)
    aj.status="Rejected"
    aj.save()
    messages.error(request, "Rejected Successfully!")
    return redirect('/manager_view_order/')
    # return HttpResponse('''<script>alert('Rejected');window.location="/manager_view_order/"</script>''')

def manager_view_approved_order(request):
    aj=unit_order.objects.filter(status="Approved")
    return render(request,'Manager/manager_view_approved_order.html',{'data':aj})

def manager_update_delivery_status(request,a1):
    aj=unit_order.objects.get(id=a1)
    aj.status="Delivered"
    aj.save()
    messages.success(request, "Delivered Successfully!")
    return redirect('/manager_view_approved_order/')



def manager_view_cancel_request(request):
    aj=unit_order.objects.filter(status="Cancelled")
    return render(request,'Manager/manager_view_cancel_request.html',{'data':aj})

def manager_check_cancel_payament(request,s8):
    aj=payment.objects.filter(unit_order_id_id=s8)
    return render(request,'Manager/manager_check_cancel_payament.html',{'data':aj})

def manager_approve_cancel_request(request,s9):
    aj=unit_order.objects.get(id=s9)
    aj.cancel_status="Refunded"
    aj.save()
    messages.success(request, "Refunded Successfully!")
    return redirect('/manager_view_cancel_request/')
    # return HttpResponse('''<script>alert('Approved');window.location="/manager_view_cancel_request/"</script>''')

def manager_change_password(request):
    aj=request.session.get('mngr')
    aj=login.objects.get(username=aj)
    return render(request,"Manager/manager_change_password.html",{'data':aj})


def manager_change_password_post(request):
    oldpass=request.POST['password']
    newpass=request.POST['password2']
    confpass=request.POST['password3']
    res=login.objects.filter(username=request.session['mngr'],password=oldpass)
    if res.exists():
        if newpass == confpass:
            ress = res.update(password=newpass)
            messages.success(request, "Password Updated!")
            return redirect('/manager_login/')
            # return HttpResponse('''<script>alert('Password Updated');window.location="/manager_login/"</script>''')
        else:
            messages.error(request, "Password Does Not Match!")
            return redirect('/manager_change_password/')
            # return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/manager_change_password/";</Script>''')
    else:
        messages.error(request, "Old Password DoesNot Match New Password!")
        return redirect('/manager_change_password/')
        # return HttpResponse('''<Script>alert("Old Password DoesNot Match New Password");window.location="/manager_change_password/";</Script>''')


def manager_import_excel(request):
    return render(request,"Manager/manager_import_excel.html")


def manager_import_excel_post(request):
    import pandas as pd
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request. FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(myfile)              
        exceldata = pd.read_excel(myfile)        
        db = exceldata
        for db in db.itertuples():
            obj = Production.objects.create(date=db.date,shift=db.shift, unit=db.unit,product_id_id=db.product_id_id )           
            obj.save()
        return redirect('/manager_view_production_report/')  
    return redirect('/manager_view_production_report/')


def manager_view_production_report(request):
    aj=Production.objects.all()
    return render(request,'Manager/manager_view_production_report.html',{'data':aj})

def manager_view_production_report_post(request):
    name = request.POST.get('textfield')
    shift = request.POST.get('select')
    date = request.POST.get('date')
    if name and shift:
        aj=Production.objects.filter(product_id__mname__icontains=name,shift__icontains=shift)
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    elif name and date:
        aj=Production.objects.filter(product_id__mname__icontains=name,date=date)
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    elif shift and date:
        aj=Production.objects.filter(shift__icontains=shift,date=date)
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    elif shift and name:
        aj=Production.objects.filter(shift__icontains=shift,product_id__mname__icontains=name)
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    elif date and shift:
        aj=Production.objects.filter(shift__icontains=shift,date=date)
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    elif date and name:
        aj=Production.objects.filter(product_id__mname__icontains=name,date=date)
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    elif date:
        aj=Production.objects.filter(date=date)
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    elif name:
        aj=Production.objects.filter(product_id__mname__icontains=name)
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    elif shift:
        aj=Production.objects.filter(shift__icontains=shift)
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    else:
        aj=Production.objects.all()
        if aj:
            return render(request,"Manager/manager_view_production_report.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
        

def manager_view_production_report_post2(request):
    shift = request.POST.get('select')
    date = request.POST.get('date')
    if shift and date: 
        aj=Production.objects.filter(shift__icontains=shift,date=date)
        if aj:
            return render(request,"Manager/manager_view_production_report_post2.html",{'data':aj})
        else:
            return HttpResponse('''<script>alert('Search Not Found!!!!!');window.location="/manager_view_production_report/"</script>''')
    






################### SUPERVISOR #################


def supervisor_view_profile(request):
    aj=request.session.get('sprvr')
    aj=staff.objects.get(Email=aj)
    return render(request, 'Supervisor/supervisor_view_profile.html',{'i':aj})

def supervisor_edit_profile(request,s7):
    data=staff.objects.get(id=s7)
    return render(request,"Supervisor/supervisor_edit_profile.html",{'data':data})
def supervisor_edit_profile_post(request):
    id=request.POST.get('id')
    n=request.POST['textfield']
    g=request.POST['RadioGroup1']
    dob=request.POST['textfield2']
    email=request.POST['textfield4']
    phone=request.POST['textfield5']
    address=request.POST['textfield7']
    if 'Photo' in request.FILES:
        Photo = request.FILES['Photo']  
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo)
        uploaded_file_url = fs.url(filename)

        aj=staff.objects.get(id=id)
        aj.Name=n
        aj.Gender=g
        aj.Date_of_birth=dob
        aj.Email=email
        aj.Phone_Number=phone
        aj.Address=address
        aj.Photo=uploaded_file_url
        aj.save()
        messages.success(request, "Updated!")
        return redirect('/supervisor_view_profile/')
    else:
        aj=staff.objects.get(id=id)
        aj.Name=n
        aj.Gender=g
        aj.Date_of_birth=dob
        aj.Email=email
        aj.Phone_Number=phone
        aj.Address=address
        aj.save()
        messages.success(request, "Updated!")
        return redirect('/supervisor_view_profile/')


def supervisor_change_password(request):
    aj=request.session.get('sprvr')
    aj=login.objects.get(username=aj)
    return render(request,"Supervisor/supervisor_change_password.html",{'data':aj})


def supervisor_change_password_post(request):
    oldpass=request.POST['password']
    newpass=request.POST['password2']
    confpass=request.POST['password3']
    res=login.objects.filter(username=request.session['sprvr'],password=oldpass)
    if res.exists():
        if newpass == confpass:
            ress = res.update(password=newpass)
            messages.success(request, "Password Updated!")
            return redirect('/supervisor_login/')
            # return HttpResponse('''<script>alert('Password Updated');window.location="/supervisor_login/"</script>''')
        else:
            messages.error(request, "Password Does Not Match!")
            return redirect('/supervisor_change_password/')
            # return HttpResponse('''<Script>alert("Password Does Not Match");window.location="/supervisor_change_password/";</Script>''')
    else:
        messages.error(request, "Old Password DoesNot Match!")
        return redirect('/supervisor_change_password/')
        # return HttpResponse('''<Script>alert("Old Password DoesNot Match");window.location="/supervisor_change_password/";</Script>''')
    
def supervisor_view_staffs(request):
    from datetime import datetime
    aj = request.session.get('sprvr')
    supervisor = staff.objects.get(Email=aj)
    

    cur_date = datetime.now().strftime('%Y-%m-%d')
    

    leaves_today = Leave3.objects.filter(fromdate=cur_date, status="approved")

    shift_allotments = shift_allot.objects.filter(supervisor_id=supervisor.id)
    

    staff_with_leaves_today = [leave.staff_id_id for leave in leaves_today]
    

    return render(request, "Supervisor/supervisor_view_staffs.html", {'data': shift_allotments, 'staff_with_leaves_today': staff_with_leaves_today})



    # aj=request.session.get('sprvr')
    # val1=staff.objects.get(Email=aj)
    # print("kkkkkkkkkkkkkkkkkkkkkkk")
    # print(val1.id)
    # aj = shift_allot.objects.filter(supervisor_id=val1.id)
    # from datetime import datetime
    # cur_date=datetime.now().strftime('%Y-%m-%d')
    # data10=Leave3.objects.filter(date__range=(fromdate,todate)).filter(status="approved")
    # data=shift_allot.objects.exclude(staff_id_id__in=[ct.staff_id_id for ct in data10])
    # print(data)
    # return render(request, "Supervisor/supervisor_view_staffs.html",{'data':aj})

def supervisor_allot_shift(request,s2):
    aj=shift_allot.objects.get(id=s2)
    aj=shift.objects.all()
    return render(request,"Supervisor/supervisor_allot_shift.html",{'data':aj,'aj':aj})



def supervisor_allot_shift_post(request):
    from datetime import datetime
    if request.method == 'POST':
        sid = request.POST.get('select')
        tid = request.POST.get('select2')
        name = request.POST.get('textfield2')

        # Check if an allotment for the current date already exists for the selected staff member
        staff_instance = staff.objects.get(Name=name)
        existing_allotment = shift_allotment.objects.filter(staff_id=staff_instance, date=datetime.now().strftime('%Y-%m-%d')).exists()
        
        if not existing_allotment:
            # Create a new allotment if none exists for the current date
            new_allotment = shift_allotment()
            new_allotment.shift_id_id = sid
            new_allotment.staff_id_id = staff_instance.id
            new_allotment.date = datetime.now().strftime('%Y-%m-%d')
            new_allotment.save()
            messages.success(request, "Shift Alloted!")
            return redirect('/supervisor_view_staffs/')
            # return HttpResponse('''<script>alert('Alloted');window.location="/supervisor_view_staffs/"</script>''')
        else:
            messages.error(request, "Cannot allot shift. Staff already has a shift for today!")
            return redirect('/supervisor_view_staffs/')
            # If an allotment already exists for the current date, show a message
            # return HttpResponse('''<script>alert('Cannot allot shift. Staff already has a shift for today.');window.location="/supervisor_view_staffs/"</script>''')
    else:
        # Handle the case where the request method is not POST
        return HttpResponse("Method Not Allowed")



    # sid=request.POST.get('select')
    # tid=request.POST.get('select2')
    # name=request.POST.get('textfield2')
    # aj=shift_allotment()
    # aj.shift_id_id=sid
    # data=staff.objects.get(Name=name)
    # aj.staff_id_id=data.id
    # from datetime import datetime
    # aj.date=datetime.now().strftime('%Y-%m-%d')
    # aj.save()
    # return HttpResponse('''<script>alert('Alloted');window.location="/supervisor_view_staffs/"</script>''')


def supervisor_loan_request(request):
    aj=request.session['sprvr']
    data=staff.objects.get(Email=aj)
    aj=job_master.objects.get(id=data.job_id_id)
    return render(request,'Supervisor/supervisor_loan_request.html',{'data':data,'data2':aj})

def supervisor_loan_request_post(request):
    aj = loan.objects.filter(staff_id__Email=request.session['sprvr'], status='Pending').exists()
    if aj:
        messages.error(request, "You already have a pending loan request. Please wait until the current loan is completed.")
        return redirect('/supervisor_loan_request/')
        # return HttpResponse('''<script>alert('Loan Request Already Sent!');window.location="/supervisor_loan_request/"</script>''')
    else:
        id = request.POST.get('id')
        la = int(request.POST['t2'])  
        intsa = int(request.POST['select'])
        p = request.POST['t4']
        # aj=staff.objects.get(id=id)
        aj = loan()
        val2=request.session['sprvr']
        data5=staff.objects.get(Email=val2)
        aj.staff_id_id = data5.id
        aj.loan_amount = la
        aj.installment = intsa
        from datetime import datetime
        aj.date = datetime.now().strftime('%Y-%m-%d')
        aj.purpose = p
        aj.status = 'Pending'

        if la:      
            floan = la / intsa
            print(floan)
            aj.initial_amount = floan

        aj.save()
        messages.success(request, "Loan Request Sent!")
        return redirect('/supervisor_loan_request/')
        # return HttpResponse('''<script>alert('Success');window.location="/supervisor_loan_request/"</script>''')


def supervisor_view_loan_status(request):
    staff_un = request.session.get('sprvr')
    staff_data = staff.objects.get(Email=staff_un)
    aj = loan.objects.filter(staff_id_id=staff_data)
    return render(request, "Supervisor/supervisor_view_loan_status.html", {'data': aj})

def supervisor_view_existing_loan(request,s5):
    d2 = loan_master.objects.get(loan_id=s5)
    return render(request,'Supervisor/supervisor_view_existing_loan.html',{'i':d2})  



def supervisor_apply_advance(request):
    aj=request.session['sprvr']
    data=staff.objects.get(Email=aj)
    return render(request,'Supervisor/supervisor_apply_advance.html',{'data': data})

def supervisor_apply_advance_post(request):
    from datetime import datetime
    id=request.POST.get('id')
    amount=request.POST['t2']
    purpose=request.POST['t4']
    mnth=datetime.now().strftime('%m')

    existing_advance = advance.objects.filter(month=mnth, staff_id_id=id).exists()
    if existing_advance:
        return HttpResponse('''<script>alert('You have already applied for advance this month');window.location="/supervisor_apply_advance/"</script>''')
    else:
        aj=advance() 
        aj.month = mnth
        aj.date=datetime.now().strftime('%Y-%m-%d')
        aj.amount=amount
        aj.purpose=purpose
        aj.staff_id_id=id
        aj.status='Pending'
        aj.save()
        return HttpResponse('''<script>alert('Success');window.location="/supervisor_apply_advance/"</script>''')

def supervisor_view_advance_status(request):
    staff_un = request.session.get('sprvr')
    staff_data = staff.objects.get(Email=staff_un)
    aj = advance.objects.filter(staff_id_id=staff_data)
    return render(request, "Supervisor/supervisor_view_advance_status.html", {'data': aj})

def supervisor_leave_request(request):
    aj=request.session['sprvr']
    data=staff.objects.get(Email=aj)
    aj=leave_master.objects.all()
    return render(request,'Supervisor/supervisor_leave_request.html',{'data': data,'data2': aj})

def supervisor_leave_request_post(request):
    name=request.POST.get('textfield1')
    name=request.POST.get('textfield1')
    lt=request.POST['select']
    ll=request.POST['leavelimit']
    fd=request.POST['textfield4']
    td=request.POST['textfield9']
    nod=request.POST['textfield5']
    reason=request.POST['textarea2']
    print(lt)
    print(ll)
    data=leave_master.objects.get(leave_type=lt)
    print(data)
    aj = staff.objects.get(Name=name)
    

    obj=Leave3.objects.filter(staff_id_id=aj).filter(status="Approved").filter(leave_id_id=data.id).aggregate(sum=Sum('no_of_days'))['sum'] 
    print("gggggggggggggggggggg")
    print(obj)
    if obj==None:
        print("hhhhhhhhhhhhhhhhhhhhh")
        aj=Leave3()
        aj.leave_id=data
        aj.staff_id = aj
        from datetime import datetime
        aj.req_date=datetime.now().strftime('%Y-%m-%d')

        aj.fromdate=fd
        aj.todate=td
        aj.no_of_days=nod
        aj.reason=reason
        aj.status='Pending'
        aj.save()
        messages.success(request, 'Leave Request Sent!')
        return redirect('/supervisor_leave_request/')
        # return HttpResponse('''<script>alert('Success');window.location="/employee_leave_request/"</script>''')
    else:

        if int(obj)>=int(ll):
            messages.error(request, 'Your leave limit is over!')
            return redirect('/supervisor_leave_request/')
            # return HttpResponse('''<script>alert('Your leave limit is over');window.location="/supervisor_leave_request/"</script>''')  
        else:
            aj=Leave3()
            aj.leave_id=data
            aj.staff_id = aj
            from datetime import datetime
            aj.req_date=datetime.now().strftime('%Y-%m-%d')

            aj.fromdate=fd
            aj.todate=td
            aj.no_of_days=nod
            aj.reason=reason
            aj.status='Pending'
            aj.save()
            messages.success(request, 'Leave Request Sent!')
            return redirect('/supervisor_leave_request/')
            # return HttpResponse('''<script>alert('Success');window.location="/employee_leave_request/"</script>''')


def supervisor_view_leave_status(request):
    aj=request.session.get('sprvr')
    var2=staff.objects.get(Email=aj)
    var3=Leave3.objects.filter(staff_id_id=var2)
    return render(request, 'Supervisor/supervisor_leave_status.html',{'data':var3})


def supervisor_view_salary_slip(request):
    aj=request.session.get('sprvr')
    var2=staff.objects.get(Email=aj)
    var3=salary.objects.filter(staff_id_id=var2.id)
    return render(request, 'Supervisor/supervisor_view_salary_slip.html',{'data':var3})

def supervisor_view_attendance(request):
    aj=request.session.get('sprvr')
    var2=staff.objects.get(Email=aj)
    var3=attendance.objects.filter(staff_id_id=var2.id)
    return render(request, 'Supervisor/supervisor_view_attendance.html',{'data':var3})

def mnr_idx(request):
    return render(request, 'manager_index3.html')










