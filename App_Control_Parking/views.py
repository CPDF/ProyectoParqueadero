from django.shortcuts import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import datetime
import pytz

# Models
from App_Control_Parking.models import Usuario, Vehiculo, LugarParqueo


def index(request):
    return render(request, 'index.html')
   

class GestionarEntradaVehiculo(TemplateView):
    template_name = "register_vehicle.html"

    def post(self, request):
        if(request.POST):
            name = request.POST.get('nombres')
            email = request.POST.get('correo')
            phone = request.POST.get('telefono')
            placa_vehiculo = request.POST.get('placa_vehiculo')
            documento_usuario = request.POST.get('documento_usuario')
            modelo = request.POST.get('modelo')
            fecha_entrada = request.POST.get('fecha_entrada')
            lugar = request.POST.get('lugar')

            #print(f"name: {name}, email: {email}, phone: {phone}, placa_vehiculo: {placa_vehiculo}, documento_usuario: {documento_usuario}, modelo: {modelo}, fecha_entrada: {fecha_entrada}, lugar: {lugar}")
            #Register the user in the database if it doesn't exist
            user = Usuario(nombres=name, correo=email, telefono=phone, documento_usuario=documento_usuario)
            #if user already exists, dont save
            if(Usuario.objects.filter(documento_usuario=documento_usuario).exists()):
                return redirect('/') #TODO: Show an alert message to the user
            
            user.save()

            #Register the vehicle in the database if it doesn't exist
            #If the plate already exists, give alert
            if(Vehiculo.objects.filter(placa_vehiculo=placa_vehiculo).exists()):
                return redirect('/') #TODO: Show an alert message to the user

            
            lugar_parqueo = LugarParqueo(codigo_lugar=lugar, placa_vehiculo_asignado=placa_vehiculo, documento_usuario=documento_usuario, fecha_entrada=fecha_entrada)
            #If the partking lot is full, give alert
            if(LugarParqueo.objects.filter(codigo_lugar=lugar).exists()):
                return redirect('/') #TODO: Show an alert message to the user 
            lugar_parqueo.ocupado = True
            lugar_parqueo.save()
            
            #Direct assignment to the forward side of a many-to-many
            documentos = Usuario.objects.filter(documento_usuario=documento_usuario)
            lugares = LugarParqueo.objects.filter(codigo_lugar=lugar)

            #Create a Vehicicle instance that stores the relationship between the user and the parking lot
            instance = Vehiculo.objects.create(documento_usuario=documento_usuario) 

            instance.typology.set(documentos)
            instance.typology_lugar.set(lugares)
            #Fill the rest
            instance.documento_usuario = documento_usuario
            instance.placa_vehiculo = placa_vehiculo
            instance.modelo = modelo
            instance.fecha_entrada = fecha_entrada

            instance.save()
            return redirect('/')
        return render(request, 'register_vehicle.html')
    

class GestionarSalidaVehiculo(TemplateView):
    template_name = "checkout.html"

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        vehiculos = Vehiculo.objects.filter(documento_usuario=id)
        current_date = datetime.datetime.now()
        fecha_entrada = vehiculos.first().typology_lugar.first().fecha_entrada
        fecha_salida = current_date
        fecha_salida = pytz.utc.localize(fecha_salida)
        tiempo_transcurrido = fecha_salida - fecha_entrada

        context = {}
        
        context["dias"] = tiempo_transcurrido.days
        context["precio"] = tiempo_transcurrido.days * 10000

        return render(request, 'checkout.html', {'context': context})

    def post(elf, request, *args, **kwargs):
        if(request.POST):
            id = kwargs['id']
            vehiculos = Vehiculo.objects.filter(documento_usuario=id)
            usuario = Usuario.objects.filter(documento_usuario=id)
            lugar_parqueo = LugarParqueo.objects.filter(documento_usuario=id)
            usuario.delete()
            lugar_parqueo.delete()
            vehiculos.delete()
            return redirect('/')
        return render(request, 'checkout.html')




class Consultar(TemplateView):
    template_name = "consult.html"

    def get(self, request):
        context = {}
        try:
            if ((request.method == 'GET') and ((request.GET.get('user_document') != None) or (request.GET.get('vehicle_plate') != None))):
                
                user_document = request.GET.get('user_document')
                placa = request.GET.get('placa_vehiculo')

                if((user_document == '') and (placa == '')):
                    context['error'] = 'Debe ingresar un documento o placa'
                    return render(request, 'consult.html', context) #TODO: Show an alert message to the user

                if(user_document):
                    user_document = request.GET.get('user_document')
                    placa = request.GET.get('placa_vehiculo')

                    users = Usuario.objects.get(documento_usuario=user_document)
                    context["nombres"] = users.nombres
                    context["telefono"] = users.telefono
                    context["correo"] = users.correo
                    context["documento_usuario"] = users.documento_usuario
                    context["nombre_gestion"] = "Gestionar entrada"
                    context["enlace_gestion"] = "manage_user/"+str(users.documento_usuario)
                    context["nombre_salida"] = "Dar salida"
                    context["enlace_salida"] = "checkout/"+str(users.documento_usuario)
                    return render(request, 'consult.html', {'context': context})


            return render(request, 'consult.html', {'context': context})
        except:
            context['error'] = 'No se encontró el usuario o vehículo'
            return render(request, 'consult.html', {'context': context}) #TODO: Show an alert message to the user



class GestionarUsuario(TemplateView):
    template_name = "register_user.html"

    #TODO: Determinar si se puede borrar esta función "post"
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


    #TODO: Implement edit user
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


    #TODO: Change function name to "delete_user" or "borrar_usuario".
    def gestionar_usuario(request, *args, **kwargs):
        id = kwargs['id']
        context = {}
        users = Usuario.objects.get(documento_usuario=id)
        context["nombres"] = users.nombres
        context["telefono"] = users.telefono
        context["correo"] = users.correo
        context["documento_usuario"] = users.documento_usuario
        
        #Borrar usuario si se hace click en el botón borrar
        if("Borrar" in request.POST):
            user = Usuario.objects.get(documento_usuario=id)
            user.delete()
            return redirect('/')

        return render(request, 'manage_user.html', {'context': context})
