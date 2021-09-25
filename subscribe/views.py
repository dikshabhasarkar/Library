from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import Subscribe

# s= Subscribe()
# print(s)

from django.conf import settings
from django.core.mail import send_mail,send_mass_mail, EmailMessage

# Create your views here.
#DataFlair #Send Email
def subscribe_email(request): #Function Based view
    print("in subscribe_email")
    sub = Subscribe()
    # print(sub)
    if request.method == 'POST':
        sub = Subscribe(request.POST)
        subject1 = 'Welcome to DataFlair'
        message1 = 'Hope you are enjoying your Django Tutorials'
        recepient = request.POST["email"].strip()  #str(sub['Email'].value())
        # print(recepient)
        final_rec_list=None
        if ";" in recepient:
            final_rec_list=recepient.split(";")
        else:
            final_rec_list=[recepient]
        print(final_rec_list,"final_rec_list")
        if final_rec_list:
            Msg = EmailMessage(subject=subject1, body=message1, from_email=settings.EMAIL_HOST_USER, to=final_rec_list)
            # Msg.send(fail_silently=False)
            # Msg.attach_file("C:\\Users\\Rupendra\\Desktop\\New Text Document.txt") #"C:\\Users\\Admin\\Desktop\\ht1.txt"
            # Msg.send(fail_silently=False)
            # Msg.recipients()
            send_mail(subject=subject1, message=message1,from_email= settings.EMAIL_HOST_USER, recipient_list=final_rec_list) #["dikshabhasarkar@gmail.com","rupen2610@gmail.com"])
        return render(request, 'sucess.html', {'recepient': recepient})
        # return HttpResponse('Hi.......')
    return render(request, 'index.html', context={'form1':sub})



