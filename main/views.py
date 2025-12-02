from django.shortcuts import render
from mailersend import Email
import os

# Static pages
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def academics(request):
    return render(request, 'main/academics.html')

def base(request):
    return render(request, 'main/base.html')

def contact(request):
    return render(request, 'main/contact.html')

def fees(request):
    return render(request, 'main/fees.html')

def gallery(request):
    return render(request, 'main/gallery.html')

def success(request):
    return render(request, 'main/success.html')


# MailerSend API key
MAILERSEND_API_KEY = os.environ.get("MAILERSEND_API_KEY")


# Admissions view
def admissions(request):
    if request.method == 'POST':
        # --- PUPIL'S BIODATA ---
        surname = request.POST.get('surname')
        firstname = request.POST.get('firstname')
        othername = request.POST.get('othername')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')

        # --- ACADEMIC DETAILS ---
        last_school = request.POST.get('last_school')
        last_class = request.POST.get('last_class')
        last_result = request.POST.get('last_result')
        reason = request.POST.get('reason')
        admission_class = request.POST.get('admission_class')
        session = request.POST.get('session')

        # --- GUARDIAN DETAILS ---
        title = request.POST.get('title')
        guardian_surname = request.POST.get('guardian_surname')
        guardian_firstname = request.POST.get('guardian_firstname')
        occupation = request.POST.get('occupation')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # --- MESSAGE ---
        message = request.POST.get('message')

        # --- Construct Email Content ---
        content = f"""
NEW ADMISSION APPLICATION:

--- PUPIL'S BIODATA ---
Surname: {surname}
Firstname: {firstname}
Othername: {othername}
Birthday: {birthday}
Gender: {gender}
Religion: {religion}

--- ACADEMIC DETAILS ---
Last School Attended: {last_school}
Last Class: {last_class}
Last Result: {last_result}
Reason for Leaving: {reason}
Admission Into: {admission_class}
Session: {session}

--- GUARDIAN DETAILS ---
Title: {title}
Guardian: {guardian_surname} {guardian_firstname}
Occupation: {occupation}
Address: {address}
Phone: {phone}
Email: {email}

--- MESSAGE ---
{message}
"""

        # -------- SEND EMAIL WITH MAILERSEND --------
        mailer = Email(api_key=MAILERSEND_API_KEY)

        email_data = {
            "from": {
                "email": "no-reply@cachetbearersschools.com",
                "name": "CB Schools Website"
            },
            "to": [
                {
                    "email": "cachetbearerstech@gmail.com"
                }
            ],
            "subject": f"New Admission Application - {surname} {firstname}",
            "html": f"<pre>{content}</pre>"
        }

        try:
            mailer.send(email_data)
            # Email sent successfully
            return render(request, "main/success.html", {"name": firstname})
        except Exception as e:
            # Email failed, show friendly message
            print("MailerSend Error:", e)
            error_message = "We could not send your application at this time. Please try again later."
            return render(request, "main/admissions.html", {"error": error_message})

    return render(request, "main/admissions.html")
