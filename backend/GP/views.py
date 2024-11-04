from django.shortcuts import render ,redirect
from django.views import View 
from django.core.validators import validate_email
from django.contrib.auth.models import User 
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from .models import *


class showhome(View) : 
    def get(self , request ) :

        return render(request , 'home.html' , { }) 
    


class showabout(View) :
    def get(self , request) :
        return render(request,'about.html',{} )
    

class showauthentification(View) :
    def get(self,request) :
        message=""
        error=False
        if request.method == "GET" : 
            email=request.GET.get('email' , None)
            password=request.GET.get('password' , None)

        try :
           validate_email(email)
        except :
            error=True
            message="Entrer un email valide svp"
        user = User.objects.filter(Q(email=email))

        for user in user:
            if check_password(password, user.password):
                  error = False
                  message=f"{{email}}"
                    
                  tro={ 'error' : error ,
                          'message' : message ,



                                           }
                    
                 
                  
                  return redirect('home') 
            
            else:
                print(f"Password did not match for user {user.username}.")
        
            


         
         

        return render(request ,'authen.html' , {})
    
class showcreate(View) : 
    def get(self , request) :
        error=False
        message=""
        if request.method == "GET" : 
            name=request.GET.get('name' , None)
            email=request.GET.get('email' , None)
            password=request.GET.get('password' , None)
            repassword=request.GET.get('repassword' , None)
            
        try :
           validate_email(email)
        except :
            error=True
            message="Entrer un email valide svp"
        
        if error == False :
            if password != repassword :
                error= True
                message="Les deux mot de pass ne correspond pas!"
        
        user=User.objects.filter(Q(email=email) | Q(username=name))
        if user :
            print("existe dans la base de donner")
            error=True
            message=f"email est existe deja {email} ou le nom d'utilisateur {name}"
        if error == False:
            user=User(
                username= name ,
                email =email ,
                password=password
             )
            user.save()
            user.password=password
            user.set_password(user.password)
            user.save()
            return redirect('au')
           
        


        

         
        tro={ 'error' : error ,
             'message' : message 



        }
        return render(request,'creat.html',tro)
                            
    

class shows(View):
    def get(self,request):
        return render(request ,'services.html', {})
    
class showpay(View) :
    def get(self,request) :
        frm=product.objects.all()
        return render(request, 'payement.html' ,{'data' : frm})
    


class detail(View) :
    def get(self ,request , name) : 
        ss=product.objects.get(name=name)
        return render(request ,'details.html' ,{'detail' :ss}  )

 
class order(View) :
    def get(self ,request ,name ) : 
        ss=product.objects.get(name=name)
        return render(request ,'details.html' ,{'detail' :ss}  )
    



 

