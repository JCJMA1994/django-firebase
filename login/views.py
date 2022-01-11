import pyrebase
from django.shortcuts import render

"""
Inicializacion de la configuracion del SDK de Firebase
que contienen los identificadores y claves para la aplicacion
"""
Config = {
    'apiKey': "AIzaSyDue501VYxKJ4DG8S6gSnre9UqI6dpBdMY",
    'authDomain': "ventas-sidecom.firebaseapp.com",
    'databaseURL': "https://ventas-sidecom-default-rtdb.firebaseio.com/",
    'projectId': "ventas-sidecom",
    'storageBucket': "ventas-sidecom.appspot.com",
    'messagingSenderId': "394339999365",
    'appId': "1:394339999365:web:5b9d22c89c4a0a19f993ec"
}

# Inicializacion de pyrebase para el uso de Firebase con Python
default_app = pyrebase.initialize_app(Config)

# Pase de la configuracion de credenciales para Authentication y Realtime Database
authe = default_app.auth()
databse = default_app.database()


def home(request):
    return render(request, template_name='signIn.html')


def signIn(request):
    return render(request, template_name="signIn.html")


def postSignIn(request):
    """
    Recibimos los datos que vamos a mandar a Firebase Authentication,
    Verificacion de los datos y creacion de usuario
    :param request:
    :return:
    """
    email = request.POST.get('email')
    passw = request.POST.get('password')

    try:
        user = authe.sign_in_with_email_and_password(email, passw)
        return render(request, 'welcome.html')
    except:
        return render(request, 'signIn.html')


def logout(request):
    """
    Eliminamos la sesion creada
    :param request:
    :return:
    """
    try:
        del request.session['uid']
    except KeyError:
        pass
    return render(request, 'signIn.html')


def signUp(request):
    return render(request, 'signup.html')


def postSignUp(request):
    """
    Enviamos los datos name y email al Realtime Database
    :param request:
    :return:
    """
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('password')

    try:
        user = authe.create_user_with_email_and_password(email, passw)
    except:
        message = "unable to create account try again"
        return render(request, 'signup.html', {"messg": message})

    uid = user['localId']
    data = {"name": name, "email": email, "status": "1"}
    databse.child("users").child(uid).child("details").set(data)
    return render(request, "welcome.html")
