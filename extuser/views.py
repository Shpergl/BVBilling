from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.template.context_processors import csrf
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from models import MyUser as User
from extuser.forms import ExtUserForm

def login(request):
    pass

@login_required(login_url='login')
def profile(request):
    email = request.user.email
    profile = get_object_or_404(User, email = email)
    context = {
        "profile" : profile,
        "form" : ExtUserForm
    }
    return render(request, 'extuser/profile.html', context)

@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        form = ExtUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile')
        #call_name = form.cleaned_data['call_name']
        #last_name = form.cleaned_data['last_name']
        #first_name = form.cleaned_data['first_name']
        #middle_name = form.cleaned_data['middle_name']

        #bv_id = form.cleaned_data['bv_id']
        #date_of_birth = form.cleaned_data['date_of_birth']
        #cell = form.cleaned_data['cell']
        #add_email = form.cleaned_data['add_email']

        #platoon = form.cleaned_data['platoon']
        #squadron = form.cleaned_data['squadron']
        #squad = form.cleaned_data['squad']
        #specialization = form.cleaned_data['specialization']

        #profile = User(call_name=call_name)
        #profile.save()
        #return redirect ('profile', id=id)
    else:
        return redirect('about')


