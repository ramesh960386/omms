import copy

from crispy_forms.layout import Layout, Field, Submit, Reset
from django import forms
from .models import QrCode
from crispy_forms.helper import FormHelper


class QrCodeForm(forms.ModelForm):
    class Meta:
        model = QrCode
        fields = '__all__'  # ['emp_code', 'scan_date', 'scan_time', 'temperature']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # form_fields = copy.deepcopy(self.fields) #.pop("emp_code", None)
        # form_fields.pop("scan_date", None)

        # [(self.fields[field_name].widget.attrs.update(readonly=True)) for field_name in ['emp_code', 'scan_date', 'scan_time']]
        # [(self.fields[field_name].widget.attrs.update(readonly=True)) for field_name in self.fields if field_name not in ['emp_code', 'temperature']]
        for field_name in self.fields:
            if field_name not in ['temperature','emp_code']:
                self.fields[field_name].widget.attrs['readonly'] = True

        # self.fields['emp_code'].widget.attrs['readonly'] = True
        # self.fields['scan_date'].widget.attrs['readonly'] = True
        # self.fields['scan_time'].widget.attrs['readonly'] = True
        # self.fields['emp_code'].widget.attrs = {'readonly': 'readonly', 'onblur': "this.style.backgroundColor='red'"}
        # self.fields['emp_code'].widget.attrs.update(style='max-width: 28em', readonly=True)
        # self.fields['scan_date'].widget.attrs.update(style='max-width: 28em', readonly=True)
        # self.fields['scan_time'].widget.attrs.update(style='max-width: 28em', readonly=True)

        """
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Save person'))
    
    
        def __init__(self, *args, **kwargs):
           super(QrCodeForm, self).__init__(*args, **kwargs)
    
           #self.fields['emp_code'].widget.attrs.update(style='max-width: 28em', readonly=True)
           #self.fields['time'].widget.attrs.update(style='max-width: 28em', readonly=True)
    
           
           self.helper = FormHelper()
           self.helper.add_input(Submit('submit', 'Save', css_class='btn btn-info'))
           self.helper.add_input(Reset('reset', 'reset', css_class='btn btn-danger'))
    
          
           helper = self.helper = FormHelper()
           layout = helper.layout = Layout()
           for field_name, field in self.fields.items():
               layout.append(Field(field_name, placeholder=field.label))
           helper.form_show_labels = False
           """
