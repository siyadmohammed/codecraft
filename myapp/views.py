from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.core.mail import EmailMessage


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send email
            email_message = EmailMessage(
                subject=subject,
                body=message,
                from_email='codecraftventures@gmail.com',  # This will still be your email address
                to=['codecraftventures@gmail.com'],  # Replace with your email address
                headers={'Reply-To': email},  # Set Reply-To to the customer's email
            )
            email_message.send(fail_silently=False)
                        # Send a confirmation email to the user
            confirmation_subject = "Thank you for contacting us!"
            confirmation_message = f"Hi {name},\n\nThank you for reaching out. We have received your message and will get back to you shortly.\n\nBest regards,\nYour Company Name"
            email_message = EmailMessage(
                confirmation_subject,
                confirmation_message,
                from_email='codecraftventures@gmail.com',  # This will still be your email address
                to=[email],  # Replace with your email address
                headers={'Reply-To': 'codecraftventures@gmail.com'},  # Set Reply-To to the customer's email
            )
            email_message.send(fail_silently=False)            
            # Redirect to the same page or show a success message
            return render(request, 'index.html', {'form': ContactForm(), 'message_sent': True})
    else:
        form = ContactForm()
    
    return render(request, 'index.html', {'form': form, 'message_sent': False})

def services(request):
    return render(request, 'services-details.html')

