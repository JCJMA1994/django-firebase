import pyrebase
from django.shortcuts import render

Config = {
  'apiKey': "AIzaSyDue501VYxKJ4DG8S6gSnre9UqI6dpBdMY",
  'authDomain': "ventas-sidecom.firebaseapp.com",
    ''
  'projectId': "ventas-sidecom",
  'storageBucket': "ventas-sidecom.appspot.com",
  'messagingSenderId': "394339999365",
  'appId': "1:394339999365:web:5b9d22c89c4a0a19f993ec"
}

default_app = pyrebase.initialize_app(Config)

authe = default_app.auth()



def signin(request):
    return render(request, template_name="signIn.html")


def postsign(request):
    global authe
    email = request.POST.get('email')
    passw = request.POST.get('password')

    try:
        user = authe.sign_in_with_email_and_password(email, passw)
        return render(request, 'welcome.html')

    except:
        return render(request, 'signIn.html')


def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return render(request, 'signIn.html')


def signUp(request):

    return render(request, 'signup.html')


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('password')

    global authe

    print(authe.create_user_with_email_and_password(email, passw))
    try:
        user = authe.create_user_with_email_and_password(email, passw)
    except:
        message = "unable to create account try again"
        return render(request, 'signup.html', {"messg": message})
    uid = user['localId']

    data = {"name": name, "status": "1"}
    databse.child("users").child(uid).child("details").set(data)
    return render(request, "signIn.html")