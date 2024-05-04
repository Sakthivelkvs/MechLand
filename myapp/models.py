from django.db import models

class add_mould(models.Model):
    id=models.AutoField(primary_key=True)
    mname=models.CharField(max_length=50)
    mtype=models.CharField(max_length=50)
    Description=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    stock=models.CharField(max_length=100,default="")
    size_type=models.CharField(max_length=100,default="")
    size1=models.CharField(max_length=100,default="")
    size2=models.CharField(max_length=100,default="")
    size3=models.CharField(max_length=100,default="")
    size=models.CharField(max_length=100,default="")
    photo=models.CharField(max_length=200)
    class Meta:
        db_table="add_mould"
       

class predict_mould(models.Model):
    id=models.AutoField(primary_key=True)
    mldname=models.CharField(max_length=50)
    photo1 = models.ImageField(upload_to='photos/')  
    photo2 = models.ImageField(upload_to='photos/')  
    photo3 = models.ImageField(upload_to='photos/') 
    class Meta:
        db_table="predict_mould"

class job_master(models.Model):
    id=models.AutoField(primary_key=True)
    job_role=models.CharField(max_length=50)
    basic_salary=models.CharField(max_length=50)
    allowance=models.CharField(max_length=50)
    loan_allowance=models.CharField(max_length=50)
    cut_salary=models.CharField(max_length=50)
    requirements=models.CharField(max_length=50,default="")
    vacancies=models.CharField(max_length=50,default="")
    qualifications=models.CharField(max_length=50,default="")
    experiences=models.CharField(max_length=50,default="")
    date=models.DateField()
    status=models.CharField(max_length=50,default="")
    class Meta:
        db_table="job_master"

class staff(models.Model):
    id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Date_of_birth = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    house_name=models.CharField(max_length=150,default="")
    place=models.CharField(max_length=150,default="")
    city=models.CharField(max_length=150,default="")
    state=models.CharField(max_length=150,default="")
    pin=models.CharField(max_length=150,default="")
    join_date=models.CharField(max_length=50,default="")
    remark=models.CharField(max_length=100,default="")
    section=models.CharField(max_length=50,default="")
    Photo=models.CharField(max_length=200)
    job_id=models.ForeignKey(job_master,on_delete=models.CASCADE)
    status=models.CharField(max_length=200)
    father_name=models.CharField(max_length=50,default="")
    aadhar=models.CharField(max_length=50,default="")
    nation=models.CharField(max_length=50,default="")
    bank_name=models.CharField(max_length=50,default="")
    bank_account_no=models.CharField(max_length=50,default="")
    bank_ifsc=models.CharField(max_length=50,default="")
    branch=models.CharField(max_length=50,default="")
    class Meta:
        db_table="staff"

class manager(models.Model):
    id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Date_of_birth = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    house_name=models.CharField(max_length=150,default="")
    Place=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100,default="")
    Pincode=models.CharField(max_length=100)
    photo=models.CharField(max_length=200)
    class Meta:
        db_table="manager"

# class vaccancy(models.Model):
#     id=models.AutoField(primary_key=True)
#     job_id=models.ForeignKey(job_master,on_delete=models.CASCADE, related_name='vacancies')
#     requirements=models.CharField(max_length=50)
#     vacancies=models.CharField(max_length=50)
#     qualifications=models.CharField(max_length=50)
#     experiences=models.CharField(max_length=50)
#     status=models.CharField(max_length=50,default="")
#     class Meta:
#         db_table="vaccancy"

class shift(models.Model):
    id=models.AutoField(primary_key=True)
    shift_nbr=models.CharField(max_length=30)
    shift_time=models.TimeField()
    class Meta:
        db_table="shift"

class uint_registration(models.Model):
    id=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Company_Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100,default="")
    Pincode=models.CharField(max_length=100)
    Photo=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    class Meta:
        db_table="unit_registration"

class login(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    class Meta:
        db_table="login"

class job_apply(models.Model):
    id=models.AutoField(primary_key=True)
    job_id=models.ForeignKey(job_master,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Date_of_birth = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    Hname=models.CharField(max_length=50,default="")
    Place=models.CharField(max_length=50,default="")
    City=models.CharField(max_length=50,default="")
    State=models.CharField(max_length=50,default="")
    Pin=models.CharField(max_length=50,default="")
    Photo=models.CharField(max_length=200,default="")
    qualifications=models.CharField(max_length=50)
    experiences=models.CharField(max_length=50)
    remark=models.CharField(max_length=100)
    int_date=models.CharField(max_length=200,default="")
    int_time=models.CharField(max_length=200,default="")
    venue=models.CharField(max_length=200,default="")
    int_status=models.CharField(max_length=200,default="")
    resume=models.CharField(max_length=200,default="")
    status=models.CharField(max_length=200,default="")

    class Meta:
        db_table="job_apply"

class business(models.Model):
    id=models.AutoField(primary_key=True)
    Company_name=models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    Address=models.CharField(max_length=150)
    Comments=models.CharField(max_length=150)
    date=models.CharField(max_length=50,default="")
    time=models.CharField(max_length=50,default="")
    status=models.CharField(max_length=50,default="")
    class Meta:
        db_table = "business"




class loan(models.Model):
    id=models.AutoField(primary_key=True)
    # loan_id=models.ForeignKey(loan_master,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    loan_amount=models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    purpose=models.CharField(max_length=200)
    initial_amount=models.CharField(max_length=50,default="")
    installment=models.CharField(max_length=50,default="")
    status=models.CharField(max_length=50)
    class Meta:
        db_table="loan"

class loan_master(models.Model):
    id=models.AutoField(primary_key=True)
    loan_id=models.ForeignKey(loan, on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff, on_delete=models.CASCADE)
    approval_date=models.CharField(max_length=50)
    installment=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    ins_status=models.CharField(max_length=50)
    class Meta:
        db_table="loan_master"


class leave_master(models.Model):
    id=models.AutoField(primary_key=True)
    leave_type=models.CharField(max_length=50)
    leave_limit=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    class Meta:
        db_table="leave_master"

class Leave(models.Model):
    id=models.AutoField(primary_key=True)
    leave_id=models.ForeignKey(leave_master,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    req_date=models.CharField(max_length=50)
    laeve_date=models.CharField(max_length=50)
   
    no_of_days=models.IntegerField()
    reason=models.CharField(max_length=200)
    status=models.CharField(max_length=50)  
    class Meta:
        db_table="Leave"



class Leave3(models.Model):
    id=models.AutoField(primary_key=True)
    leave_id=models.ForeignKey(leave_master,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    req_date=models.CharField(max_length=50)
    fromdate=models.CharField(max_length=50)
    todate=models.CharField(max_length=50)
    no_of_days=models.IntegerField()
    reason=models.CharField(max_length=200)
    status=models.CharField(max_length=50)  
    certificate=models.CharField(max_length=250,default="")
    class Meta:
        db_table="Leave3"

class unit_review(models.Model):
    id=models.AutoField(primary_key=True)
    unit_id=models.ForeignKey(uint_registration,on_delete=models.CASCADE)
    mould_id1=models.ForeignKey(add_mould, on_delete=models.CASCADE)
    review=models.CharField(max_length=200)
    date=models.CharField(max_length=50)
    class Meta:
        db_table="unit_review"
class unit_review1(models.Model):
    id=models.AutoField(primary_key=True)
    unit_id=models.ForeignKey(uint_registration,on_delete=models.CASCADE)
    mould_id1=models.ForeignKey(add_mould, on_delete=models.CASCADE)
    review=models.CharField(max_length=200)
    date=models.CharField(max_length=50)
    class Meta:
        db_table="unit_review1"        
    
class unit_complaint(models.Model):
    id=models.AutoField(primary_key=True)
    unit_id=models.ForeignKey(uint_registration,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=200)
    date=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    class Meta:
        db_table="unit_complaint"

class attendance(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    month=models.CharField(max_length=50,default='')
    year=models.CharField(max_length=50,default='')
    no_of_working_days=models.CharField(max_length=50,default='')
    class Meta:
        db_table="attendance"

class shift_allotment(models.Model):
    id=models.AutoField(primary_key=True)
    shift_id=models.ForeignKey(shift,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    class Meta:
        db_table="shift_allotment"

class unit_order(models.Model):
    id=models.AutoField(primary_key=True)
    unit_id=models.ForeignKey(uint_registration,on_delete=models.CASCADE)
    mould_id=models.ForeignKey(add_mould,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=50)
    size=models.CharField(max_length=50,default="")
    date=models.CharField(max_length=50)
    c_date=models.CharField(max_length=50,default="")
    status=models.CharField(max_length=50)
    cancel_status=models.CharField(max_length=50,default="")
    vehicle_number=models.CharField(max_length=50,default="")
    contact_number=models.CharField(max_length=50,default="")
    delivary_date=models.CharField(max_length=50,default="")
    delivary_time=models.CharField(max_length=50,default="")
    remarks=models.CharField(max_length=50,default="")
    payment_method=models.CharField(max_length=50,default="")
    class Meta:
        db_table="unit_order"

class payment(models.Model):
    id=models.AutoField(primary_key=True)
    Account_num=models.CharField(max_length=50)
    bank=models.CharField(max_length=50)
    ifsc=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    unit_order_id=models.ForeignKey(unit_order, on_delete=models.CASCADE)
    class Meta:
        db_table="payment"

class ratting(models.Model):
    id=models.AutoField(primary_key=True)
    predict_mould_id=models.ForeignKey(predict_mould, on_delete=models.CASCADE)
    mname=models.CharField(max_length=50)
    p1_ratting=models.IntegerField()
    p2_ratting=models.IntegerField()
    p3_ratting=models.IntegerField()
    suggestion=models.CharField(max_length=200)
    def get_column_with_highest_value(self):
        max_column_value = max(self.p1_ratting, self.p2_ratting, self.p3_ratting)
        if max_column_value == self.p1_ratting:
            return 'p1_ratting'
        elif max_column_value == self.p2_ratting:
            return 'p2_ratting'
        else:
            return 'p3_ratting' 
    class Meta:
        db_table="ratting"

class advance(models.Model):
    id=models.AutoField(primary_key=True)
    month=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    purpose=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default="")
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    class Meta:
        db_table="advance"

class salary(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    days=models.CharField(max_length=50,default="")
    leave=models.CharField(max_length=50)
    leaveamount=models.CharField(max_length=50)
    loan=models.CharField(max_length=50)
    advance=models.CharField(max_length=50)
    net_salary=models.CharField(max_length=50)
    month=models.CharField(max_length=50)
    year=models.CharField(max_length=50,default="")
    class Meta:
        db_table="salary"

class cancel(models.Model):
    id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(unit_order,on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    class Meta:
        db_table="cancel"  

class shift_allot(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    supervisor_id=models.CharField(max_length=50,default="")
    date=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    class Meta:
        db_table="shift_allot"

class Attendance_File(models.Model):
    id=models.AutoField(primary_key=True)
    file = models.FileField(upload_to="excel") 
    class Meta:
        db_table="Attendance_File"


class Production(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField(default="")
    shift=models.CharField(max_length=50,default="")
    unit=models.CharField(max_length=50,default="")
    product_id=models.ForeignKey(add_mould,on_delete=models.CASCADE)
    class Meta:
        db_table="Production"

class product_review(models.Model):
    id=models.AutoField(primary_key=True)
    order_id=models.ForeignKey(unit_order,on_delete=models.CASCADE)
    review=models.CharField(max_length=200)
    date=models.CharField(max_length=50)
    class Meta:
        db_table="product_review"










    






# Create your models here.
