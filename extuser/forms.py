# -*- coding: utf-8 -*-
from django import forms

from models import MyUser as User


class ExtUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('call_name', 'last_name', 'first_name', 'middle_name',
                  'bv_id', 'date_of_birth', 'cell', 'add_email',
                  'platoon', 'squadron', 'squad', 'specialization')
    #call_name = forms.CharField(label='Позивний', initial=User.call_name ,max_length=50)
    #last_name = forms.CharField(label='Прізвище', max_length=100)
    #first_name = forms.CharField(label='Ім\'я',max_length=50)
    #middle_name = forms.CharField(label='По батьков', max_length=50)

#    bv_id = forms.IntegerField(label='Номер жетона')
 #   date_of_birth = forms.DateField(label='DДата народження')
  #  cell = forms.CharField(label='Контактний телефон', max_length=20)
   # add_email = forms.EmailField(label='Додатковий email', max_length=50)

    #platoon = forms.ChoiceField(widget=forms.Select, choices=User.PLATOON, label='Рота')
    #squadron = forms.ChoiceField(widget=forms.Select, choices=User.SQUADRON, label='Взвод')
    #squad = forms.ChoiceField(widget=forms.Select, choices=User.SQUAD, label='Відділення')
    #specialization = forms.ChoiceField(widget=forms.Select, choices=User.SQUAD, label='Спеціалізація')

    #permissions = forms.DateField(label='permissions')