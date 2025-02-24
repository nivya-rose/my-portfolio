from django.shortcuts import render
from .models import Project
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactForm
from django.http import FileResponse
from django.conf import settings
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    projects = Project.objects.all()  
    return render(request, 'base.html')


@csrf_exempt  # Use only if CSRF is causing issues
def contact_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON request
            name = data.get("name")
            email = data.get("email")
            message = data.get("message")

            # Simple validation
            if not name or not email or not message:
                return JsonResponse({"success": False, "message": "All fields are required."})

            # Example: Sending email (update settings.py for real email sending)
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
                from_email="your-email@example.com",  # Change this to your email
                recipient_list=["your-recipient@example.com"],  # Change this to the admin email
                fail_silently=False,
            )

            return JsonResponse({"success": True, "message": "Your message has been sent successfully!"})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON data."})

    return JsonResponse({"success": False, "message": "Invalid request method."})



def download_resume(request):
    file_path = os.path.join(settings.BASE_DIR, 'protected', 'Nivya Rose Resume.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Nivya Rose Resume.pdf')

