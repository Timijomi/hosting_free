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
    return render(request, 'admissions.html')

def fees(request):
    return render(request, 'fees.html')




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




from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def admissions(request):
    if request.method == 'POST':
        surname = request.POST.get('surname')
        firstname = request.POST.get('firstname')
        othername = request.POST.get('othername')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')

        last_school = request.POST.get('last_school')
        last_class = request.POST.get('last_class')
        last_result = request.POST.get('last_result')
        reason = request.POST.get('reason')

        admission_class = request.POST.get('admission_class')
        session = request.POST.get('session')

        title = request.POST.get('title')
        guardian_surname = request.POST.get('guardian_surname')
        guardian_firstname = request.POST.get('guardian_firstname')
        occupation = request.POST.get('occupation')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        message = request.POST.get('message')

        # Prepare email
        subject = f"New Admission Application - {surname} {firstname}"
        body = f"""
New Admission Application Submitted:

--- PUPIL'S BIODATA ---
Surname: {surname}
Firstname: {firstname}
Othername: {othername}
Birthday: {birthday}
Gender: {gender}
Religion: {religion}

--- ACADEMIC DETAILS ---
Last School Attended: {last_school}
Last Classroom: {last_class}
Last Result: {last_result}
Reason for Leaving: {reason}
Admission Into: {admission_class}
Session: {session}

--- GUARDIAN DETAILS ---
Title: {title}
Guardian Name: {guardian_surname} {guardian_firstname}
Occupation: {occupation}
Address: {address}
Phone: {phone}
Email: {email}

--- MESSAGE ---
{message}
        """

        # SEND EMAIL
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            ['cachetbearerstech@gmail.com'],  # where you want to receive admission alerts
            fail_silently=False,
        )

        return render(request, 'success.html', {
            'name': firstname
        })

    return render(request, 'admissions.html')
