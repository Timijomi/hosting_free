from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def academics(request):
    return render(request, 'main/academics.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def admissions(request):
    return render(request, 'main/admissions.html')

def fees(request):
    return render(request, 'main/fees.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Message from {name}"
        body = f"""
        You have received a new message from the school website:

        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        try:
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ['cachetbearerstech@gmail.com'])
            messages.success(request, f"Thank you {name}, your message has been sent successfully!")
        except Exception as e:
            print("Email sending error:", e)
            messages.error(request, "Sorry, we couldn't send your message. Please try again later.")

        return redirect("contact")

    return render(request, "main/contact.html")