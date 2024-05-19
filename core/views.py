from django.shortcuts import render, redirect
from django.core.mail import send_mail
from core.models import GeneralSetting


# Create your views here.
def index(request):
    name = GeneralSetting.objects.get(name='name').parameter
    title = GeneralSetting.objects.get(name='title').parameter
    aboutMeText = GeneralSetting.objects.get(name='aboutMe.text').parameter
    birthDate = GeneralSetting.objects.get(name='birthDate').parameter
    email = GeneralSetting.objects.get(name='email').parameter
    currentCity = GeneralSetting.objects.get(name='currentCity').parameter
    


    context = {
        'title': title,
        'name': name,
        'aboutMeText': aboutMeText,
        'birthDate': birthDate,
        'email': email,
        'currentCity': currentCity,
    }
    return render(request, 'index.html', context=context)




def contact(request):
    return render(request, 'index.html')



def contact_form(request):
    print("hello from contact_from function")
    if request.method == 'POST':
        nameText = request.POST['name']
        emailText = request.POST['email']
        subjectText = request.POST['subject']
        messageText = request.POST['message']
        print("hello from contact_from if state")

        send_mail(
            "Message From :" + subjectText,
            f"Name: {nameText}\nEmail: {emailText}\n\n{messageText}",  # E-posta gövdesi
            'your-email@example.com',  # Gönderen e-posta adresi
            ['ardabzlk@gmail.com'],  # Alıcı e-posta adresi
        )

        print("if worked")
        return render(request, 'index.html', {"message_name": nameText})
    else:

        print("else worked")
        return render(request, 'index.html', {"message_name": "sa"})
