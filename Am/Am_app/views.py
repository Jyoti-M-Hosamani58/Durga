import os
from email.message import EmailMessage

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from Am_app.models import Login,contact
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            udata = Login.objects.get(username=username)
            if password == udata.password:  # Use hashed password checks in production
                request.session['username'] = username
                request.session['utype'] = udata.utype

                if udata.utype == 'user':
                    return redirect('index')  # Redirect to a user-specific page
                else:
                    return redirect('admin_dashboard')  # Adjust as necessary
            else:
                messages.error(request, 'Invalid password')
        except Login.DoesNotExist:
            messages.error(request, 'Invalid Username')

    return render(request, 'login.html')


def index(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create a new Contact instance and save it to the database
        contact_instance = contact(
            name=name,
            email=email,
            message=message,
        )
        contact_instance.save()

        # Send a confirmation email
        subject = "New Inquiry from Contact Form"
        email_message = f"""
        You have received a new inquiry!

        Full Name: {name}
        Email: {email}
        Message: {message}
        """

        from_email = 'mahindrag154@gmail.com'  # Change this to the sender's email
        recipient_list = ['mahindrag154@gmail.com']  # Change this to the recipient's email

        email = EmailMessage(
            subject,
            email_message,
            from_email,
            recipient_list,
        )

        try:
            email.send(fail_silently=False)
        except Exception as e:
            return render(request, 'career.html', {
                'error': f"Error sending email: {e}"
            })

        return redirect('index')  # Redirect to the same page (or a success page)

    return render(request, 'index.html')




