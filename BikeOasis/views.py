# views are functions that handle HTTP requests and return HTTP responses

from django.shortcuts import render

# defines a python function that takes a request paramater
def index(request): # Homepage
    
    user = request.user 
    # retrieves the user associated with the incoming request, request.user attribute represents the currently authenticated user. 
    # if the user is not authenticated, request.user will be an instance of AnonymousUser
    return render (request,'index.html',{'user':user}) # is a context dictionary that contains data you want to pass to the template.






from django.shortcuts import get_object_or_404, redirect, HttpResponse
from .models import *
from .forms import BikeForm, ClientLoginForm, ClientRegistrationForm, contactform
from django.urls import reverse
from django.core.mail import send_mail
from Revival.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as django_login, authenticate, logout




# registration views (Register)
def registration(request):
    if request.method == "POST":
        profile = ClientRegistrationForm(request.POST)
        if profile.is_valid():
            # Extract cleaned data from the form
            nm = profile.cleaned_data["name"]
            eml = profile.cleaned_data["email"]
            br = profile.cleaned_data["birthday"]
            ph = profile.cleaned_data["phone"]
            pa = profile.cleaned_data["password"]
            cpa = profile.cleaned_data["confirm_password"]
            if pa == cpa:
                # Create a new User and UserProfile objects
                b = User.objects.create_user(
                    username=eml, email=eml, password=pa
                )
                user_profile = UserProfile.objects.create(
                    user=b, birthday=br, phone=ph, name=nm
                )
                user_profile.save()
                b.save()
                return redirect(login)  # Redirect to the login page
            else:
                return HttpResponse("Incorrect password...")
        else:
            return HttpResponse("Enter valid data")
    return render(request, "register.html")  # Display the registration form

# Define the login view
def login(request):
    if request.method == "POST":
        form = ClientLoginForm(request.POST)
        if form.is_valid():
            eml = form.cleaned_data["email"]
            pas = form.cleaned_data["password"]
            user = authenticate(request, username=eml, password=pas)
            if user is not None:
                django_login(request, user)
                # Return user profile data to the ClientHomepage template
                return render(
                    request,
                    "ClientHomepage.html",
                    {
                        "name": user.userprofile.name,
                        "email": user.email,
                        "birthday": user.userprofile.birthday,
                        "phone": user.userprofile.phone,
                        "id": user.id,
                    },
                )
            else:
                return HttpResponse("Password incorrect...")
        else:
            return HttpResponse("Error...")
    return render(request, "login.html")  # Display the login form

# Define the view to edit user profile details
@login_required
def EditDetails(request, id):
    try:
        client = UserProfile.objects.get(id=id)
    except User.DoesNotExist:
        return redirect(reverse('login'))  # Redirect to the 'login' URL pattern

    if request.method == "POST":
        # Update client's profile information
        client.name = request.POST.get("name")
        client.email = request.POST.get("email")
        client.birthday = request.POST.get("birthday")
        client.phone = request.POST.get("phone")
        client.save()
        return redirect(reverse('login'))  # Redirect to the 'login' URL pattern

    return render(request, "ClientEdit.html", {"client": client})

# Define the view to display a list of bikes
def bike_list(request):
    bikes = Bike.objects.all()
    profile = UserProfile.objects.all()
    return render(request, "bike_list.html", {"bikes": bikes, "profile": profile})


# Define the view to display bike details
@login_required
def bike_detail(request, pk):
    bike = get_object_or_404(Bike, pk=pk)
    return render(request, "bike_detail.html", {"bike": bike})
    

# Define the view to create a new bike
@login_required
def bike_new(request):
    if request.method == "POST":
        form = BikeForm(request.POST, request.FILES)
        if form.is_valid():
            bike = form.save(commit=False)
            bike.user = request.user  # Assign the current user as the owner of the bike
            bike.save()
            return redirect("bike_list")
    else:
        form = BikeForm()
    return render(request, "bike_edit.html", {"form": form})

# Define the view to delete a bike
@login_required
def delete_bike(request, bike_id):
    bike = get_object_or_404(Bike, pk=bike_id)

    if request.user == bike.user:
        if request.method == "POST":
            bike.delete()
            return redirect("bike_list")
        else:
            return render(request, "bike_detail.html", {"bike": bike})
    else:
        return HttpResponse("You don't have permission to delete this bike.")

# Define the view to edit a bike's details
@login_required
def bike_edit(request, bike_id=None):
    if bike_id is not None:
        bike = get_object_or_404(Bike, pk=bike_id)
    else:
        bike = None
    if request.user == bike.user:
        if request.method == "POST":
            form = BikeForm(request.POST, instance=bike)
            if form.is_valid():
                bike = form.save()
                return redirect("bike_list")
        else:
            form = BikeForm(instance=bike)

        return render(request, "bike_edit.html", {"form": form})
    else:
        return HttpResponse("You don't have permission to edit this bike.")

# Define the view to log out the user
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to the index page or any other desired page

# email 
def send_mail_regis(email,token):
    subject="your account has been verified"
    message=f'pass the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def success(request):
    return render(request,"success.html")
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile  # Import your UserProfile model

def send_message(request):
    sub = contactform()
    

    if request.method == 'POST':
        sub = contactform(request.POST)
        if sub.is_valid():
            name = sub.cleaned_data['name']
            message = sub.cleaned_data['message']
            email = sub.cleaned_data['email']

            # Get the user's email from UserProfile
            user_profile = UserProfile.objects.get(user=request.user)
            user_email = user_profile.user.email

            subject = f"{name} || {message} || {user_email}"  # Include user's email in the subject
            message = f"Name: {name}\nMessage: {message}\nUser Email: {user_email}\nEntered Email: {email}"

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            return render(request, 'success.html')

    return render(request, 'message.html', {'form': sub})


