from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

# Models
from App_Control_Parking.models import Usuario, Vehiculo


def index(request):
    return render(request, 'index.html')
   

class GestionarVehiculo(TemplateView):
    template_name = "register_vehicle.html"

    def post(self, request):
        if(request.POST):
            placa_vehiculo = request.POST.get('placa_vehiculo')
            documento_usuario = request.POST.get('documento_usuario')
            modelo = request.POST.get('modelo')
            fecha_entrada = request.POST.get('fecha_entrada')

            #If the plate already exists, dont save
            if(Vehiculo.objects.filter(placa_vehiculo=placa_vehiculo).exists()):
                return redirect('/')

            #Direct assignment to the forward side of a many-to-many
            documentos = Usuario.objects.filter(documento_usuario=documento_usuario)
            instance = Vehiculo.objects.create(documento_usuario=documento_usuario)
            instance.typology.set(documentos)
            #Fill the rest
            instance.placa_vehiculo = placa_vehiculo
            instance.modelo = modelo
            instance.fecha_entrada = fecha_entrada

            instance.save()
            return redirect('/')
        return render(request, 'register_vehicle.html')
    



class Consultar(TemplateView):
    template_name = "consult.html"

    def get(self, request):
        context = {}
        if ((request.method == 'GET') and ((request.GET.get('user_document') != None) or (request.GET.get('vehicle_plate') != None))):
            user_document = request.GET.get('user_document')
            placa = request.GET.get('placa_vehiculo')

            if((user_document == '') and (placa == '')):
                context['error'] = 'Debe ingresar un documento o placa'
                return render(request, 'consult.html', context)

            if(user_document):
                user_document = request.GET.get('user_document')
                placa = request.GET.get('placa_vehiculo')

                users = Usuario.objects.get(documento_usuario=user_document)
                context["nombres"] = users.nombres
                context["telefono"] = users.telefono
                context["correo"] = users.correo
                context["documento_usuario"] = users.documento_usuario
                return render(request, 'consult.html', {'context': context})

            elif(placa):
                vehicles = Vehiculo.objects.get(placa_vehiculo=placa)
                context["modelo"] = vehicles.modelo
                context["fecha_entrada"] = vehicles.fecha_entrada
                context["placa_vehiculo"] = vehicles.placa_vehiculo
                context["documento_usuario"] = vehicles.documento_usuario
                return render(request, 'consult.html', {'context': context})

        return render(request, 'consult.html', {'context': context})




class GestionarUsuario(TemplateView):
    template_name = "register_user.html"

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            user_document = request.POST.get('user_document')
            user = Usuario(nombres=name, correo=email, telefono=phone, documento_usuario=user_document)
            #if user already exists, dont save
            if(Usuario.objects.filter(documento_usuario=user_document).exists()):
                return redirect('/')
            user.save()
            return redirect('/')
        return render(request, 'register_user.html')


    def edit(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            user_document = request.POST.get('user_document')
            user = Usuario.objects.get(documento_usuario=user_document)
            user.nombres = name
            user.correo = email
            user.telefono = phone
            user.save()
            return redirect('/')
        return render(request, 'register_user.html')

    def delete_user(self, request):
        if request.method == 'POST':
            user_document = request.POST.get('user_document')
            user = Usuario.objects.get(documento_usuario=user_document)
            user.delete()
            return redirect('/')
        return render(request, 'register_user.html')
        


