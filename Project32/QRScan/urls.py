"""QRScan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from QRScan import settings
from django.conf.urls.static import static
from qrapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name="inex.html"), name='home'),
    path('', views.QrCodeReader, name='home'),
    url(r'^export/data/$', views.ExportData, name='export_data'),
    url(r'^sendmail_html/$', views.SendMailHTML, name='sendmail_html'),
    url(r'^sendmail_attachment/$', views.SendMailAttachment, name='sendmail_attachment'),
    url(r'^emp_info/$', views.EmployeeInfo, name='emp_info'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
