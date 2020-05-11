#from clonevirtualenv import logger
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from .forms import QrCodeForm
from .models import QrCode, EmployeeData
from datetime import datetime, timedelta, time
import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as se
from io import StringIO
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect


def QrCodeReader(request):
    form = QrCodeForm()
    if request.method == 'POST':
        form = QrCodeForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            emp_code = form.cleaned_data.get("emp_code")
            # scan_date = form.cleaned_data.get("scan_date")
            fs.scan_date = datetime.now()
            fs.scan_time = datetime.now()
            punch_type = QrCode.objects.filter(emp_code=emp_code, scan_date=datetime.now()).count()
            if punch_type % 2 == 0:
                fs.punch = 'In'
            else:
                fs.punch = 'Out'
            fs.save()
        return redirect(request.path_info)
    ctx = {
        'form': QrCodeForm,
        'qr_data': QrCode.objects.filter(scan_date=datetime.now().date()),
        'emp_data': EmployeeData.objects.all()
    }
    return render(request, 'inex.html', ctx)


def EmployeeInfo(request):
    if request.method == 'GET' and request.is_ajax():
        selection_id = request.GET['searchkey']
        emp_data = EmployeeData.objects.get(emp_code=selection_id)
        # emp_data = EmployeeData.objects.filter(emp_code=selection_id).values('emp_code', 'emp_name','emp_photo')
        data = {
            'emp_code': emp_data.emp_code,
            'emp_name': emp_data.emp_name,
            'emp_photo': emp_data.emp_photo.url
        }
        return JsonResponse(data)


def ExportData(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['emp_code', 'scan_date', 'scan_time', 'temperature', 'punch'])

    users = QrCode.objects.filter(scan_date=datetime.now().date()).values_list('emp_code', 'scan_date', 'scan_time',
                                                                               'temperature', 'punch')
    for user in users:
        writer.writerow(user)

    # writer.writerow([user.username, user.first_name, user.last_name, user.email, ])

    return response


def SendMailHTML(request):
    html_message = render_to_string('mail_template.html',
                                    {'context': QrCode.objects.filter(scan_date=datetime.now().date())})
    plain_message = strip_tags(html_message)
    send_mail('Orbicular Attendance Date Of: ' + str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S")),
              # str(datetime.now().date().strftime("%d/%m/%Y")),
              plain_message, se.EMAIL_HOST_USER, ['it.rameshy@gmail.com'], html_message=html_message)

    # return HttpResponseRedirect(request.path_info)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def SendMailAttachment(request):
    email_subject = 'Orbicular Attendance Date Of: ' + str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
    to_list = 'it.rameshy@gmail.com'
    # csvwriter.writerow(['emp_code', 'scan_date', 'scan_time', 'temperature', 'punch'])

    # rows = [{'col1': 'value1', 'col2': 'value2'}]
    rows = [QrCode.objects.filter(scan_date=datetime.now().date())]
    csvfile = StringIO()
    fieldnames = list(rows[0].keys())

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

    email = EmailMessage(email_subject, "Your Leads", se.EMAIL_HOST_USER, [to_list], )
    email.attach('file.csv', csvfile.getvalue(), 'text/csv')
    email.send()
    # return HttpResponseRedirect(request.path_info)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
