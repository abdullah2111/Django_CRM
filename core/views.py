from django.shortcuts import render, redirect
from .models import User, Contact
from .forms import CustomUserCreationForm, ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages





def home(request):
    return render(request, 'core/index.html')


@login_required
def dashboard(request):
    total_contacts = Contact.objects.filter(user=request.user).count()
    new_leads = Contact.objects.filter(user=request.user, status='New Lead').count()
    contacted = Contact.objects.filter(user=request.user, status='Contacted').count()
    qualified = Contact.objects.filter(user=request.user, status='Qualified').count()
    converted = Contact.objects.filter(user=request.user, status='Converted').count()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user  
            contact.save()
            messages.success(request, "Contact successfully created!")
            return redirect('dashboard')  
    else:
        form = ContactForm()

    return render(request, 'core/dashboard.html', 
    {   'form': form, 
        'total_contacts': total_contacts,
        'new_leads': new_leads,
        'contacted': contacted,
        'qualified': qualified,
        'converted': converted,})



@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)

    return render(request, 'core/contactList.html',{'contacts': contacts})


@login_required
def view_contact(request, pk):
    contact = Contact.objects.get(pk=pk)

    return render(request, 'core/view_contact.html', {'contact':contact})



@login_required
def edit_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated successfully!")
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    
    return render(request, 'core/edit_contact.html', {'form': form})


@login_required
def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    messages.success(request, "Contact deleted successfully!")
    return redirect('contact_list')



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully')
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'core/signup.html', {'form': form})




def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get("password")

        user = authenticate (request, username = email, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.full_name}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

