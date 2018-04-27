from .models import *
from django.contrib.auth import *
from django.http import *
from django.shortcuts import *
from django.utils import timezone
from .forms import *
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.urls import reverse_lazy
from django.utils.http import is_safe_url
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from poplib import *
from django.db.models import Q

class LoginView(View):
    template_name = 'main/login.html'
    port = 995
    next = ''

    def get(self, request):
        self.next = request.GET.get('next', '')
        webmail = request.user.username
        if request.user.is_authenticated() and not request.user.is_superuser:
            if(Student.objects.filter(webmail=webmail)):
                return redirect('/stud_profile')
            elif(Faculty.objects.filter(webmail=webmail)):
                return redirect('/faculty_profile')
            elif(DeptAdmin.objects.filter(webmail=webmail)):
                return redirect('/dept_admin')
            else:
                return redirect('/stud_nodues')
        args = dict(form=LoginForm(None), next=self.next)
        return render(request, self.template_name, args)

    def post(self, request):
        redirect_to = request.POST.get('next', self.next)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            login_server = form.cleaned_data.get('login_server')
            role = form.cleaned_data.get('role')
            # em = '%s@iitg.ernet.in' % (username)
            # mail = POP3_SSL(login_server)
            # mail.user(username)
            # try:
            #     mail.pass_(password)
            #     mail.quit()
            # except:
            #     form.add_error(None, 'Wrong Username or Password.')
            #     return render(request, self.template_name, dict(form=form))

            # if not(User.objects.filter(username=username)):
            #     new_user = User.objects.create_user(username=username,
            #                     email=em,
            #                      password=password)
            #     new_user.save()

            user = auth.authenticate(username=username, password=password)
            if user is not None :
                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    auth.login(request=request, user=user)
                    if role == "Student":
                        try:
                            student = Student.objects.get(webmail=username)
                        except Student.DoesNotExist:
                            student = None
                        if student is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_profile')
                    elif role == "Faculty":
                        try:
                            fac = Faculty.objects.get(webmail=username)
                        except Faculty.DoesNotExist:
                            fac = None
                        if fac is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/faculty_profile')
                    elif role == "Warden":
                        try:
                            warden = Warden.objects.get(webmail=username)
                        except Warden.DoesNotExist:
                            warden = None

                        if warden is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')

                    elif role == "Caretaker":
                        try:
                            caretaker = Caretaker.objects.get(webmail=username)
                        except Caretaker.DoesNotExist:
                            caretaker = None

                        if caretaker is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')

                    elif role == "Gymkhana":
                        try:
                            gymkhana = Gymkhana.objects.get(webmail=username)
                        except Gymkhana.DoesNotExist:
                            gymkhana = None
                        if gymkhana is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')
                    elif role == "OnlineCC":
                        try:
                            onlinecc = OnlineCC.objects.get(webmail=username)
                        except OnlineCC.DoesNotExist:
                            onlinecc = None
                        if onlinecc is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')
                    elif role == "CC":
                        try:
                            cc = CC.objects.get(webmail=username)
                        except CC.DoesNotExist:
                            cc = None
                        if cc is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')
                    elif role == "Thesis Manager":
                        try:
                            thesis_manager = SubmitThesis.objects.get(webmail=username)
                        except SubmitThesis.DoesNotExist:
                            thesis_manager = None
                        if thesis_manager is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')
                    elif role == "Library":
                        try:
                            library = Library.objects.get(webmail=username)
                        except Library.DoesNotExist:
                            library = None
                        if library is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')
                    elif role == "Assistant Registrar":
                        try:
                            assistant_registrar = Assistant_registrar.objects.get(webmail=username)
                        except Assistant_registrar.DoesNotExist:
                            assistant_registrar = None
                        if assistant_registrar is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')
                    elif role == "HOD":
                        try:
                            hod = HOD.objects.get(webmail=username)
                        except HOD.DoesNotExist:
                            hod = None
                        if hod is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')
                    elif role == "Account":
                        try:
                            account = Account.objects.get(webmail=username)
                        except Account.DoesNotExist:
                            account = None
                        if account is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')
                    elif role == "Lab":
                        try:
                            lab = Labs.objects.get(webmail=username)
                        except Labs.DoesNotExist:
                            lab = None
                        if lab is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_nodues')
                    elif role == "Admin":
                        try:
                            admin = DeptAdmin.objects.get(webmail=username)
                        except DeptAdmin.DoesNotExist:
                            admin = None
                        if admin is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/dept_admin')

                else:
                    return redirect(redirect_to)
            else:
                form.add_error(None, 'No user exists for given credentials.')
                return render(request, self.template_name, dict(form=form))
        else:
            return render(request, self.template_name, dict(form=form))

class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login_user')
    raise_exception = False
    http_method_names = ['get', 'head', 'options']
    def get(self, request):
        auth.logout(request=request)
        return redirect('/')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #print type(Student.webmail)
                if role == "Student":
                    return redirect('/stud_profile')
                elif role == "Faculty":
                    return redirect('/faculty_profile')
                elif role == "Warden":
                    return redirect('/warden')
                else:
                    return render(request, 'main/login.html', {'error_message': 'Unsuccessful Login'})
            else:
                return render(request, 'main/login.html', {'error_message': 'Session Expired'})
        else:
            return render(request, 'main/login.html', {'error_message': 'Credentials Invalid'})
    return render(request, 'main/login.html',{'error_message': ''})

def stud_profile(request):
    username=request.user.username
    try:
        student = Student.objects.get(webmail=username)
    except Student.DoesNotExist:
        return redirect('/logout');
    return render(request, 'main/stud.html', {'error_message': 'valid login', 'student': student})

def rules(request):
    username=request.user.username
    try:
        student = Student.objects.get(webmail=username)
    except Student.DoesNotExist:
        student = None
    return render(request,'main/rules.html', {'student':student})

def contact(request):
    username = request.user.username
    try:
        student = Student.objects.get(webmail=username)
    except Student.DoesNotExist:
        student = None
    return render(request, 'main/contact.html', {'student': student})

def no_dues_apply(request):
    if request.method == "GET":
        username = request.user.username
        try:
            student = Student.objects.get(webmail=username)
        except Student.DoesNotExist:
            student = None
        if student is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        return render(request, 'main/student_apply.html', {'error_message': 'valid login', 'student': student})
    elif request.method=="POST":
        username = request.user.username
        try:
            student = Student.objects.get(webmail=username)
        except Student.DoesNotExist:
            student = None

        if Stud_Faculty_Status.objects.filter(student=student):
            student.save()

        return redirect("/no_dues_apply")

def update_faculty_status(request):
    print ("updating faculty status")
    stud_webmail = request.GET.get("stud_webmail")
    faculty_webmail = request.GET.get("faculty_webmail")
    dues = request.GET.get("dues")
    remarks = request.GET.get("remarks")
    print(dues)
    print(remarks)
    student = Student.objects.get(webmail=stud_webmail)
    faculty = Faculty.objects.get(webmail=faculty_webmail)
    noDues = Stud_Faculty_Status.objects.get(student = student, faculty=faculty)
    noDues.faculty_approval = dues
    noDues.status_update_time = timezone.now()
    noDues.faculty_remarks = remarks
    noDues.save()
    return JsonResponse({'dues': dues, 'datetime': noDues.status_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})

def faculty_profile(request):
    return redirect("/faculty_pending")

def faculty_pending(request):
    if request.method == "GET":
        username = request.user.username
        fac = Faculty.objects.get(webmail=username)
        dept = fac.department
        studs = Stud_Faculty_Status.objects.filter(faculty=fac)
        students = []
        for stud in studs:
            if(stud.faculty_approval == 1):
                students.append(stud.student)
        status = []
        remarks = []
        update_time = []
        for stud in students:
            status.append(Stud_Faculty_Status.objects.get(faculty = fac, student=stud).faculty_approval)
        for stud in students:
            remarks.append(Stud_Faculty_Status.objects.get(faculty=fac, student=stud).faculty_remarks)
        for stud in students:
            update_time.append(Stud_Faculty_Status.objects.get(faculty=fac, student=stud).status_update_time)
        print(students)
        return render(request, 'main/faculty_pending.html',{'error_message': 'valid login', 'faculty': fac, 'dept': dept,
                                                    'students': zip(students, status, remarks,update_time)})

def faculty_approved(request):
    if request.method == "GET":
        username = request.user.username
        fac = Faculty.objects.get(webmail=username)
        dept = fac.department
        studs = Stud_Faculty_Status.objects.filter(faculty=fac)
        students = []
        for stud in studs:
            if(stud.faculty_approval == 2):
                students.append(stud.student)
        status = []
        remarks = []
        update_time = []
        for stud in students:
            status.append(Stud_Faculty_Status.objects.get(faculty = fac, student=stud).faculty_approval)
        for stud in students:
            remarks.append(Stud_Faculty_Status.objects.get(faculty=fac, student=stud).faculty_remarks)
        for stud in students:
            update_time.append(Stud_Faculty_Status.objects.get(faculty=fac, student=stud).status_update_time)
        print(remarks)
        return render(request, 'main/faculty_approved.html',{'error_message': 'valid login', 'faculty': fac, 'dept': dept,
                                                    'students': zip(students, status, remarks,update_time)})

def faculty_rejected(request):
    if request.method == "GET":
        username = request.user.username
        fac = Faculty.objects.get(webmail=username)
        dept = fac.department
        studs = Stud_Faculty_Status.objects.filter(faculty=fac)
        students = []
        for stud in studs:
            if(stud.faculty_approval == 3):
                students.append(stud.student)
        status = []
        remarks = []
        update_time = []
        for stud in students:
            status.append(Stud_Faculty_Status.objects.get(faculty = fac, student=stud).faculty_approval)
        for stud in students:
            remarks.append(Stud_Faculty_Status.objects.get(faculty=fac, student=stud).faculty_remarks)
        for stud in students:
            update_time.append(Stud_Faculty_Status.objects.get(faculty=fac, student=stud).status_update_time)
        print(remarks)
        return render(request, 'main/faculty_rejected.html',{'error_message': 'valid login', 'faculty': fac, 'dept': dept,
                                                    'students': zip(students, status, remarks,update_time)})



def delete_student(request):
    stud_webmail = request.GET.get("stud_webmail")
    faculty_webmail = request.GET.get("faculty_webmail")
    student = Student.objects.get(webmail=stud_webmail)
    faculty = Faculty.objects.get(webmail=faculty_webmail)
    Stud_Faculty_Status.objects.get(student=student, faculty=faculty).delete()
    if not Stud_Faculty_Status.objects.filter(student=student).exists():
        student.save()
        print ("student updated")
    return JsonResponse({'messege': 'Student is deleted', 'webmail': stud_webmail})


def stud_nodues(request):
    if request.method == "GET":
        username = request.user.username
        students = None
        remarks = []
        update_time = []
        flag = None
        show = username

        if(Assistant_registrar.objects.filter(webmail=username).exists()):
            flag = "Assistant"
            assistant_registrar = Assistant_registrar.objects.get(webmail=username)
            students = assistant_registrar.get_students()
            students = students.filter(hostel_dues=False).filter(gymkhana_dues=False)
            for stud in students:
                remarks.append("Hostel - " + stud.hostel_remarks + ", Gymkhana - " + stud.gymkhana_remarks)
                update_time.append(stud.hostel_update_time)


        elif(Warden.objects.filter(webmail=username).exists()):
            flag = "Hostel"
            warden = Warden.objects.get(webmail=username)
            hostel = warden.hostel
            students = warden.get_students()
            students = students.filter(hostel_dues=False)
            for stud in students:
                remarks.append(stud.hostel_remarks)
                update_time.append(stud.hostel_update_time)
            show = show + " - " + hostel + " Hostel"

        elif(Caretaker.objects.filter(webmail=username).exists()):
            flag = "Hostel"
            caretaker = Caretaker.objects.get(webmail=username)
            hostel = caretaker.hostel
            students = caretaker.get_students()
            students = students.filter(hostel_dues=False)
            for stud in students:
                remarks.append(stud.hostel_remarks)
                update_time.append(stud.hostel_update_time)
            show = show + " - " + hostel + " Hostel"

        elif(Gymkhana.objects.filter(webmail=username).exists()):
            flag = "Gymkhana"
            gymkhana = Gymkhana.objects.get(webmail=username)
            students = gymkhana.get_students()
            students = students.filter(gymkhana_dues=False)
            for stud in students:
                remarks.append(stud.gymkhana_remarks)
                update_time.append(stud.gymkhana_update_time)


        elif(OnlineCC.objects.filter(webmail=username).exists()):
            flag = "CC"
            onlineCC = OnlineCC.objects.get(webmail=username)
            students = onlineCC.get_students()
            students = students.filter(cc_dues=False)
            for stud in students:
                remarks.append(stud.cc_remarks)
                update_time.append(stud.cc_update_time)

        elif(CC.objects.filter(webmail=username).exists()):
            flag = "CC"
            cc = CC.objects.get(webmail=username)
            students = cc.get_students()
            students = students.filter(cc_dues=False)
            for stud in students:
                remarks.append(stud.cc_remarks)
                update_time.append(stud.cc_update_time)

        elif(SubmitThesis.objects.filter(webmail=username).exists()):
            flag = "Library"
            submitThesis = SubmitThesis.objects.get(webmail=username)
            students = submitThesis.get_students()
            students = students.filter(library_dues=False)
            for stud in students:
                remarks.append(stud.library_remarks)
                update_time.append(stud.library_update_time)

        elif(Library.objects.filter(webmail=username).exists()):
            flag = "Library"
            library = Library.objects.get(webmail=username)
            students = library.get_students()
            students = students.filter(library_dues=False)
            for stud in students:
                remarks.append(stud.library_remarks)
                update_time.append(stud.library_update_time)

        elif(Labs.objects.filter(webmail=username).exists()):
            flag = "Lab"
            lab = Labs.objects.get(webmail=username)
            students1 = Stud_Lab_Status.objects.filter(lab=lab)
            students1 = students1.filter(lab_dues=False)
            students = []
            for stud in students1:
                students.append(stud.student)
                remarks.append(stud.lab_remarks)
                update_time.append(stud.lab_update_time)
            show = show + " - " + lab.name

        elif(HOD.objects.filter(webmail=username).exists()):
            flag = "Hod"
            warden = HOD.objects.get(webmail=username)
            students = warden.get_students()
            students = students.filter(hod_dues=False)
            for stud in students:
                remarks.append(stud.hod_remarks)
                update_time.append(stud.hod_update_time)
            show = show + " - " + warden.department + " department"

        elif(Account.objects.filter(webmail=username).exists()):
            flag = "Account"
            warden = Account.objects.get(webmail=username)
            students = warden.get_students()
            students = students.filter(finance_dues=False)
            for stud in students:
                remarks.append(stud.finance_remarks)
                update_time.append(stud.finance_update_time)

        students = list(students)
        context = zip(students, remarks, update_time)
        return render(request, 'main/warden_nodues.html',
                      {'error_message': 'valid login', 'context':context, 'flag':flag, 'webmail':username, 'name':show})

def stud_dues(request):
    if request.method == "GET":
        username = request.user.username
        students = None
        remarks = []
        update_time = []
        flag = None
        show = username
        if(Assistant_registrar.objects.filter(webmail=username).exists()):
            flag = "Assistant"
            assistant_registrar = Assistant_registrar.objects.get(webmail=username)
            students = assistant_registrar.get_students()
            students = students.filter(hostel_dues=False).filter(gymkhana_dues=False)
            students = Student.objects.exclude(pk__in=students.values_list('pk', flat=True))
            for stud in students:
                remarks.append("Hostel - " + stud.hostel_remarks + ", Gymkhana - " + stud.gymkhana_remarks)
                update_time.append(stud.hostel_update_time)

        elif(Warden.objects.filter(webmail=username).exists()):
            flag = "Hostel"
            warden = Warden.objects.get(webmail=username)
            hostel = warden.hostel
            students = warden.get_students()
            students = students.filter(hostel_dues=True)
            for stud in students:
                remarks.append(stud.hostel_remarks)
                update_time.append(stud.hostel_update_time)
            show = show + ' - ' + hostel + ' Hostel'

        elif(Caretaker.objects.filter(webmail=username).exists()):
            flag = "Hostel"
            caretaker = Caretaker.objects.get(webmail=username)
            hostel = caretaker.hostel
            students = caretaker.get_students()
            students = students.filter(hostel_dues=True)
            for stud in students:
                remarks.append(stud.hostel_remarks)
                update_time.append(stud.hostel_update_time)
            show = show + ' - ' + hostel + ' Hostel'


        elif(Gymkhana.objects.filter(webmail=username).exists()):
            flag = "Gymkhana"
            gymkhana = Gymkhana.objects.get(webmail=username)
            students = gymkhana.get_students()
            students = students.filter(gymkhana_dues=True)
            for stud in students:
                remarks.append(stud.gymkhana_remarks)
                update_time.append(stud.gymkhana_update_time)


        elif(OnlineCC.objects.filter(webmail=username).exists()):
            flag = "CC"
            onlineCC = OnlineCC.objects.get(webmail=username)
            students = onlineCC.get_students()
            students = students.filter(cc_dues=True)
            for stud in students:
                remarks.append(stud.cc_remarks)
                update_time.append(stud.cc_update_time)

        elif(CC.objects.filter(webmail=username).exists()):
            flag = "CC"
            cc = CC.objects.get(webmail=username)
            students = cc.get_students()
            students = students.filter(cc_dues=True)
            for stud in students:
                remarks.append(stud.cc_remarks)
                update_time.append(stud.cc_update_time)

        elif(SubmitThesis.objects.filter(webmail=username).exists()):
            flag = "Library"
            submitThesis = SubmitThesis.objects.get(webmail=username)
            students = submitThesis.get_students()
            students = students.filter(library_dues=True)
            for stud in students:
                remarks.append(stud.library_remarks)
                update_time.append(stud.library_update_time)

        elif(Library.objects.filter(webmail=username).exists()):
            flag = "Library"
            library = Library.objects.get(webmail=username)
            students = library.get_students()
            students = students.filter(library_dues=True)
            for stud in students:
                remarks.append(stud.library_remarks)
                update_time.append(stud.library_update_time)

        elif(HOD.objects.filter(webmail=username).exists()):
            flag = "HOD"
            library = HOD.objects.get(webmail=username)
            students = library.get_students()
            students = students.filter(hod_dues=True)
            for stud in students:
                remarks.append(stud.hod_remarks)
                update_time.append(stud.hod_update_time)


        elif(Labs.objects.filter(webmail=username).exists()):
            flag = "Lab"
            lab = Labs.objects.get(webmail=username)
            students1 = Stud_Lab_Status.objects.filter(lab=lab)
            students1 = students1.filter(lab_dues=True)
            students = []
            for stud in students1:
                students.append(stud.student)
                remarks.append(stud.lab_remarks)
                update_time.append(stud.lab_update_time)
            show = show + ' - ' + lab.name

        elif(Account.objects.filter(webmail=username).exists()):
            flag = "Account"
            library = Account.objects.get(webmail=username)
            students = library.get_students()
            students = students.filter(finance_dues=True)
            for stud in students:
                remarks.append(stud.finance_remarks)
                update_time.append(stud.finance_update_time)

        students = list(students)
        context = zip(students, remarks, update_time)
        return render(request, 'main/warden_dues.html',
                      {'error_message': 'valid login', 'context':context, 'flag':flag, 'webmail':username, 'name':show,})

def stud_search(request):
    username = request.user.username
    students = None
    remarks = []
    update_time = []
    check = []
    flag = None
    show = username
    if(Assistant_registrar.objects.filter(webmail=username).exists()):
        flag = "Assistant"
        assistant_registrar = Assistant_registrar.objects.get(webmail=username)
        students = assistant_registrar.get_students()
        for stud in students:
            remarks.append("Hostel - " + stud.hostel_remarks + ", Gymkhana - " + stud.gymkhana_remarks)
            update_time.append(stud.hostel_update_time)
            check.append(not(stud.hostel_dues or stud.gymkhana_dues))


    elif(Warden.objects.filter(webmail=username).exists()):
        flag = "Hostel"
        warden = Warden.objects.get(webmail=username)
        hostel = warden.hostel
        students = warden.get_students()
        for stud in students:
            remarks.append(stud.hostel_remarks)
            update_time.append(stud.hostel_update_time)
            check.append(not(stud.hostel_dues))
        show = show + ' - ' + hostel + ' Hostel'

    elif(Caretaker.objects.filter(webmail=username).exists()):
        flag = "Hostel"
        caretaker = Caretaker.objects.get(webmail=username)
        hostel = caretaker.hostel
        students = caretaker.get_students()
        for stud in students:
            remarks.append(stud.hostel_remarks)
            update_time.append(stud.hostel_update_time)
            check.append(not(stud.hostel_dues))

        show = show + ' - ' + hostel + ' Hostel'


    elif(Gymkhana.objects.filter(webmail=username).exists()):
        flag = "Gymkhana"
        gymkhana = Gymkhana.objects.get(webmail=username)
        students = gymkhana.get_students()
        for stud in students:
            remarks.append(stud.gymkhana_remarks)
            update_time.append(stud.gymkhana_update_time)
            check.append(not(stud.gymkhana_dues))



    elif(OnlineCC.objects.filter(webmail=username).exists()):
        flag = "CC"
        onlineCC = OnlineCC.objects.get(webmail=username)
        students = onlineCC.get_students()
        for stud in students:
            remarks.append(stud.cc_remarks)
            update_time.append(stud.cc_update_time)
            check.append(not(stud.cc_dues))


    elif(CC.objects.filter(webmail=username).exists()):
        flag = "CC"
        cc = CC.objects.get(webmail=username)
        students = cc.get_students()
        for stud in students:
            remarks.append(stud.cc_remarks)
            update_time.append(stud.cc_update_time)
            check.append(not(stud.cc_dues))


    elif(SubmitThesis.objects.filter(webmail=username).exists()):
        flag = "Library"
        submitThesis = SubmitThesis.objects.get(webmail=username)
        students = submitThesis.get_students()
        for stud in students:
            remarks.append(stud.library_remarks)
            update_time.append(stud.library_update_time)
            check.append(not(stud.library_dues))


    elif(Library.objects.filter(webmail=username).exists()):
        flag = "Library"
        library = Library.objects.get(webmail=username)
        students = library.get_students()
        for stud in students:
            remarks.append(stud.library_remarks)
            update_time.append(stud.library_update_time)
            check.append(not(stud.library_dues))


    elif(HOD.objects.filter(webmail=username).exists()):
        flag = "HOD"
        library = HOD.objects.get(webmail=username)
        students = library.get_students()
        for stud in students:
            remarks.append(stud.hod_remarks)
            update_time.append(stud.hod_update_time)
            check.append(not(stud.hod_dues))



    elif(Labs.objects.filter(webmail=username).exists()):
        flag = "Lab"
        lab = Labs.objects.get(webmail=username)
        students1 = Stud_Lab_Status.objects.filter(lab=lab)
        ids = []
        for stud in students1:
            ids.append(stud.student.pk)
            remarks.append(stud.lab_remarks)
            update_time.append(stud.lab_update_time)
            check.append(not(stud.lab_dues))
        students = Student.objects.filter(pk__in=ids)

        show = show + ' - ' + lab.name

    elif(Account.objects.filter(webmail=username).exists()):
        flag = "Account"
        library = Account.objects.get(webmail=username)
        students = library.get_students()
        for stud in students:
            remarks.append(stud.finance_remarks)
            update_time.append(stud.finance_update_time)
            check.append(not(stud.finance_dues))

    if request.method == "POST":
        method1 = request.POST.get('method')
        val = request.POST.get('val')
        print(method1)
        if(method1 == "Roll No."):
            students = students.filter(roll_no__startswith=val)
        elif(method1 == "Name"):
            students = students.filter(name__icontains=val)
        elif(method1 == "Webmail"):
            students = students.filter(webmail__icontains=val)
        elif(method1 == "Department"):
            students = students.filter(department__startswith=val)
        elif(method1 == "Hostel"):
            students = students.filter(hostel__startswith=val)

    students = list(students)
    print(students)
    context = zip(students, remarks, update_time, check)

    return render(request, 'main/warden_search.html',
                  {'error_message': 'valid login', 'context':context, 'flag':flag, 'webmail':username, 'name':show,})




def hostel_update(request):
    stud_webmail = request.GET.get("stud_webmail")
    dues = request.GET.get("dues")
    remarks = request.GET.get("remarks")
    webmail = request.GET.get("webmail")
    flag = request.GET.get("flag")
    student = Student.objects.get(webmail=stud_webmail)
    if(flag == "Hostel"):
        student.hostel_dues = dues
        student.hostel_update_time = timezone.now()
        student.hostel_remarks = remarks
    elif(flag == "Gymkhana"):
        student.gymkhana_dues = dues
        student.gymkhana_update_time = timezone.now()
        student.gymkhana_remarks = remarks
    elif(flag == "CC"):
        student.cc_dues = dues
        student.cc_update_time = timezone.now()
        student.cc_remarks = remarks
    elif(flag == "Library"):
        student.library_dues = dues
        student.library_update_time = timezone.now()
        student.library_remarks = remarks
    elif(flag == "Assistant"):
        student.hostel_dues = dues
        student.hostel_update_time = timezone.now()
        student.hostel_remarks = remarks
        student.gymkhana_dues = dues
        student.gymkhana_update_time = timezone.now()
        student.gymkhana_remarks = remarks

    elif(flag == "HOD"):
        student.hod_dues = dues
        student.hod_update_time = timezone.now()
        student.hod_remarks = remarks

    elif( flag == "Account"):
        student.finance_dues = dues
        student.finance_update_time = timezone.now()
        student.finance_remarks = remarks

    elif(flag == "Lab"):
        print(webmail)
        lab = Labs.objects.get(webmail=webmail)
        lab_stat = Stud_Lab_Status.objects.get(lab=lab, student=student)
        lab_stat.lab_dues = dues
        lab_stat.lab_update_time = timezone.now()
        lab_stat.lab_remarks = remarks
        lab_stat.save()

    student.save()
    return JsonResponse({'dues': dues, 'webmail':student.webmail, 'datetieme':timezone.now()})

def search_faculties(request):
    searchquery = request.POST.get("searchquery")
    print (searchquery)
    faculties = Faculty.objects.filter(Q(name__icontains=searchquery)|Q(webmail__icontains=searchquery))
    faculty_details = {}
    for faculty in faculties:
        print (faculty.webmail)
        print (faculty.name)
        faculty_details[faculty.webmail]=faculty.name
    print  (faculty_details)
    return JsonResponse({'faculties_searched':faculty_details})

def stud_full_dept(request):
    username = request.user.username
    username=str(username)
    student = Student.objects.get(webmail=username)
    related_faculties = student.get_faculties()
    names = []
    status = []
    remarks = []
    time = []
    for fac in related_faculties:
        names.append(fac.faculty.name)
    for fac in related_faculties:
        print(fac.faculty_approval)
        status.append(fac.faculty_approval)
    for fac in related_faculties:
        remarks.append(fac.faculty_remarks)
    for fac in related_faculties:
        time.append(fac.status_update_time)
    return render(request, 'main/stud_full_dept.html', {'error_message': 'valid login', 'student': student, 'details': zip(names,status, remarks,time)})


def add_faculty(request):
    faculty_webmail = request.GET.get("faculty_webmail")
    username = request.user.username
    student = Student.objects.get(webmail=username)
    fac = Faculty.objects.get(webmail=faculty_webmail)
    try:
        x = Stud_Faculty_Status.objects.get(student=student, faculty=fac)
    except Stud_Faculty_Status.DoesNotExist:
        x = None
    if x is None:
        x = Stud_Faculty_Status(student=student, faculty=fac, )
        x.save()
        return JsonResponse({'messege' : "Faculty is added", 'name' : fac.name, 'status' : x.faculty_approval, 'remarks': x.faculty_remarks})
    else:
        return JsonResponse({'messege': 'Faculty is already added', 'name': " "})

def dept_admin(request):
    username = request.user.username
    username=str(username)
    dept = DeptAdmin.objects.get(webmail=username)
    related_labs = Labs.objects.filter(department=dept.department)
    related_labs = list(related_labs)
    return render(request, 'main/dept_admin.html', {'error_message': 'valid login', 'dept': dept.department, 'labs':related_labs})

def add_lab(request):
    username = request.user.username
    username=str(username)
    if(request.method == "POST" and DeptAdmin.objects.filter(webmail=username)):
        print(request.POST)
        lab_name = request.POST.get('lab_name')
        fac = request.POST.get('faculty1')
        department = request.POST.get('dept')
        print(fac)
        faculty = Faculty.objects.get(webmail=fac)
        x = Labs(name = lab_name)
        x.webmail=fac
        x.department = department
        x.save()
        students = Student.objects.filter(department=department)
        for stud in students:
            x1 = Stud_Lab_Status(student=stud)
            x1.lab = x
            x1.save()
        return redirect('/dept_admin')
    else:
        username = request.user.username
        username=str(username)
        try:
            dept = DeptAdmin.objects.get(webmail=username)
        except DeptAdmin.DoesNotExist:
            return redirect('/logout')
        return render(request, 'main/add_lab.html', {'dept':dept.department})

def stud_full_lab(request):
    username = request.user.username
    username=str(username)
    student = Student.objects.get(webmail=username)
    related_labs = Stud_Lab_Status.objects.filter(student=student)
    names = []
    incharge = []
    status = []
    remarks = []
    time = []
    for fac in related_labs:
        names.append(fac.lab.name)
        incharge.append(fac.lab.webmail)
        status.append(fac.lab_dues)
        remarks.append(fac.lab_remarks)
        time.append(fac.lab_update_time)
    dept = student.department
    hod = HOD.objects.get(department=dept)
    return render(request, 'main/stud_full_lab.html', {'hod':hod, 'error_message': 'valid login', 'stud': student, 'details': zip(names, incharge, status, remarks,time)})

def delete_lab(request):
    pk = request.GET.get('lab_pk')
    username = request.user.username
    username=str(username)
    if(DeptAdmin.objects.filter(webmail=username)):
        lab = Labs.objects.get(pk=pk)
        lab.delete()
        return JsonResponse({'message': 'done'})
    return JsonResponse({'message': 'error'})
