from django.shortcuts import render,HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


# --------------- topic View ----------------------  
      
class topic_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = topic.objects.get(id=id)
                serializer = topic_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except topic.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = topic.objects.all().order_by("-id")
            serializer = topic_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = topic_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = topic.objects.get(id=id)
        except topic.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = topic_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = topic.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except topic.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})


# --------------- Author View ----------------------  
      
class author_view(APIView):
    def get(self, request, id=None , topic_id=None ):
        if id:
            try:
                uid = author.objects.get(id=id)
                serializer = author_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except author.DoesNotExist:
                return Response({'status': "Invalid"})
        elif topic_id:
            try:
                uid=author.objects.filter(topic_data__id=topic_id).order_by("-id")
                
                serializer=author_serializers(uid,many=True)
                print(len(serializer.data))
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})       
        else:
            uid = author.objects.all().order_by("-id")
            serializer = author_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = author_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = author.objects.get(id=id)
        except author.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = author_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = author.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except author.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})

# --------------- User View ----------------------  
      
class user_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = user.objects.get(id=id)
                serializer = user_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except user.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = user.objects.all().order_by("-id")
            serializer = user_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = user_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = user.objects.get(id=id)
        except user.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = user_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = user.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except user.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})


#======================admin_login_view=======================
class admin_login_view(APIView):
    def get(self,request,id=None , email=None):

        if id:

            try:
                uid=admin_login.objects.get(id=id)
                serializer=admin_login_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid email"})
        elif email:

            try:
                uid=admin_login.objects.get(email=email)
                serializer=admin_login_serializers(uid)
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid email"})
        else:
            uid=admin_login.objects.all().order_by("-id")
            serializer=admin_login_serializers(uid,many=True)
            return Response({'status':'success','data':serializer.data})

    def post(self,request):
            serializer=admin_login_serializers(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')

                uid=admin_login.objects.filter(email=email).exists()
                if uid:
                    uid=admin_login.objects.get(email=email)
                    if uid.password == password:
                        serializer=admin_login_serializers(uid)

                        return Response({'status':'success','data':serializer.data})
                    else:
                        return Response({'status':'invalid password'})
                else:
                    return Response({'status':'invalid email'})

            else:
                return Response({'status':"invalid data"})


    def patch(self,request,id=None):
        try:
            uid=admin_login.objects.get(id=id)
        except:
            return Response({'status':"invalid email"})
        serializer=admin_login_serializers(uid,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success','data':serializer.data})
        else:
            return Response({'status':"invalid email"})
    def delete(self,request,id=None,email=None):
        if id:
            try:
                uid=admin_login.objects.get(id=id)
                uid.delete()
                return Response({'status':'Deleted data'})
            except:
                return Response({'status':"invalid id"})
        elif email:
            del request.session['email']
            return Response({'status': 'Logged out successfully'})

        else:
            return Response({'status':"invalid data"})
    def logout(self, request):
        try:
            del request.session['email']
        except KeyError:
            pass
        return Response({'status': 'Logged out successfully'})
    
    
#=========================Books view============================
      
class books_view(APIView):
    def get(self, request, id=None , topic_id=None):
        if id:
            try:
                uid = Books.objects.get(id=id)
                serializer = BooksSerializer(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Books.DoesNotExist:
                return Response({'status': "Invalid"})
        
        elif topic_id:
            try:
                uid=Books.objects.filter(topic_data__id=topic_id).order_by("-id")
                
                serializer=BooksSerializer(uid,many=True)
                print(len(serializer.data))
                return Response({'status':'success','data':serializer.data})
            except:
                return Response({'status':"Invalid"})          
        
        else:
            uid = Books.objects.all().order_by("-id")
            serializer = BooksSerializer(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Books.objects.get(id=id)
        except Books.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = BooksSerializer(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Books.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Books.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})




# --------------- Login User View ----------------------  
      
class login_user_view(APIView):
    def get(self, request, id=None,email=None):
        if id:
            try:
                uid = login_user.objects.get(user_id=id)
                serializer = login_user_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except login_user.DoesNotExist:
                return Response({'status': "Invalid"})
            
        elif email:
                try:
                    uid=login_user.objects.get(email=email)
                    
                    serializer=login_user_serializers(uid)
                    print(len(serializer.data))
                    return Response({'status':'success','data':serializer.data})
                except:
                    return Response({'status':"Invalidd"})     
        

        else:
            uid = login_user.objects.all().order_by("-id")
            serializer = login_user_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

      

    # def post(self, request):
    #     serializer = login_user_serializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status': 'success', 'data': serializer.data})
    #     else:
    #         return Response({'status': "invalid data", 'errors': serializer.errors})



    def post(self,request):
        
        serializer = login_user_serializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...1",'errors': serializer.errors})



    def patch(self, request, id=None,email=None):
        if id:
            try:
                uid = login_user.objects.get(user_id=id)
            except login_user.DoesNotExist:
                return Response({'status': "invalid data"})
            
            serializer = login_user_serializers(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})
        elif email:    
            try:
                uid = login_user.objects.get(email=email)
            except login_user.DoesNotExist:
                return Response({'status': "invalid data"})
            
            serializer = login_user_serializers(uid, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data})
            else:
                return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = login_user.objects.get(user_id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except user.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})

#==========



class login_user_post_view(APIView):
    
    def post(self,request):
            serializer=login_user_serializers(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')

                uid=login_user.objects.filter(email=email).exists()
                if uid:
                    uid=login_user.objects.get(email=email)
                    if uid.password == password:
                        serializer=login_user_serializers(uid)

                        return Response({'status':'success','data':serializer.data})
                    else:
                        return Response({'status':'invalid password'})
                else:
                    return Response({'status':'invalid email'})

            else:
                return Response({'status':"invalid data"})



# ================================ ad =========================
        

class ad_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = ad.objects.get(id=id)
                serializer = ad_serializers(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = ad.objects.order_by("-id")
            serializer = ad_serializers(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
  
        serializer = ad_serializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data..."})



    def patch(self,request,id=None):

        if id:
            uid = ad.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = ad_serializers(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data..."})


    def delete(self,request,id=None):
        if id:
            try:
                uid = ad.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})

                
# ================== notification ====================



class notification_view(APIView):

    def get(self,request,id=None,user_id=None):

        if id:
            try:
                uid = show_notification.objects.get(id=id)
                serializer = NotificationSerializer(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})
        elif user_id:
            try:
                print(user_id)
                uid = show_notification.objects.filter(user_data__user_id=user_id)
                if uid.exists():
                    serializer = NotificationSerializer(uid, many=True)
                    return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({'status': 'No data found for user_id'}, status=status.HTTP_404_NOT_FOUND)
            except show_notification.DoesNotExist:
                return Response({'status': 'Invalid user_id'}, status=status.HTTP_404_NOT_FOUND)

        else:
            uid = show_notification.objects.order_by("-id")
            serializer = NotificationSerializer(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
     
        serializer = NotificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})



    def patch(self,request,id=None):

        if id:
            uid = show_notification.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = NotificationSerializer(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid = show_notification.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})
               


#==============add_to_cart_view=============
class add_to_cart_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = add_to_cart.objects.get(id=id)
                serializer = add_to_cart_serializer(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = add_to_cart.objects.order_by("-id")
            serializer = add_to_cart_serializer(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
 
        serializer = add_to_cart_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data..."})



    def patch(self,request,id=None):

        if id:
            uid = add_to_cart.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = add_to_cart_serializer(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data..."})


    def delete(self,request,id=None):
        if id:
            try:
                uid = add_to_cart.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})
                
#====================book_languages===========================           
     
class book_languages_view(APIView):
    def get(self, request, id=None):
        if id:
            try:
                uid = Languages.objects.get(id=id)
                serializer = book_languages_serializers(uid)
                return Response({'status': 'success', 'data': serializer.data})
            except Languages.DoesNotExist:
                return Response({'status': "Invalid"})
        else:
            uid = Languages.objects.all().order_by("-id")
            serializer = book_languages_serializers(uid, many=True)
            return Response({'status': 'success', 'data': serializer.data})

    def post(self, request):
        serializer = book_languages_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def patch(self, request, id=None):
        try:
            uid = Languages.objects.get(id=id)
        except Languages.DoesNotExist:
            return Response({'status': "invalid data"})
        
        serializer = book_languages_serializers(uid, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data})
        else:
            return Response({'status': "invalid data", 'errors': serializer.errors})

    def delete(self, request, id=None):
        if id:
            try:
                uid = Languages.objects.get(id=id)
                uid.delete()
                return Response({'status': 'Deleted data'})
            except Languages.DoesNotExist:
                return Response({'status': "invalid id"})
        else:
            return Response({'status': "invalid data"})
        
        
        
# =========================== Add Book Wishlist ================    


class add_wishlist_book_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = wishlist.objects.get(id=id)
                serializer = Add_Wishlist_Book_Serializer(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = wishlist.objects.order_by("-id")
            serializer = Add_Wishlist_Book_Serializer(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
        
        serializer = Add_Wishlist_Book_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})



    def patch(self,request,id=None):

        if id:
            uid = wishlist.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = Add_Wishlist_Book_Serializer(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid = wishlist.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})
               

               
               
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import timedelta
@api_view(['POST'])
def send_test_email(request):
    
    email = request.data.get('email', None)

    if email is None:
        return Response({"error": "email email is required."})

    from_email = settings.EMAIL_HOST_USER


    html_content = render_to_string('email_template.html', {
        
        'email': email,
    })

    try:
        send_mail("Pustakam Email", "Test", from_email, [email],html_message=html_content) 
        uid=login_user.objects.get(email=email)
        uid.password_time=timezone.now() + timedelta(seconds=60)
        uid.save()
        return Response({"success": "HTML email sent successfully!"})
    except Exception as e:
        return Response({"error": str(e)})
    
def home(request):
    return render(request,"email_template.html")    



# =========================== download ================    


class download_view(APIView):

    def get(self,request,id=None):

        if id:
            try:
                uid = download.objects.get(id=id)
                serializer = download_Serializer(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})

        else:
            uid = download.objects.order_by("-id")
            serializer = download_Serializer(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
        
        serializer = download_Serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})



    def patch(self,request,id=None):

        if id:
            uid = download.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = download_Serializer(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid = download.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                   return Response({'status' : "invalid data..."})
               
               
# ================== Hylighter ====================



class hylighter_view1(APIView):

    def get(self,request,id=None,user_id=None):

        if id:
            try:
                uid = hylighter1.objects.get(id=id)
                serializer = HylighterSerializer1(uid)

                return Response({'status' : 'success','data':serializer.data})
            except:
                return Response({'status' : "invalid data..."})
        elif user_id:
            try:
                print(user_id)
                uid = hylighter1.objects.filter(user_data__user_id=user_id)
                if uid.exists():
                    serializer = HylighterSerializer1(uid, many=True)
                    return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({'status': 'No data found for user_id'}, status=status.HTTP_404_NOT_FOUND)
            except hylighter1.DoesNotExist:
                return Response({'status': 'Invalid user_id'}, status=status.HTTP_404_NOT_FOUND)
        else:
            uid = hylighter1.objects.order_by("-id")
            serializer = HylighterSerializer1(uid,many=True)

            return Response({'status' : "success",'data' : serializer.data})

    def post(self,request):
  
        serializer = HylighterSerializer1(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})



    def patch(self,request,id=None):

        if id:
            uid = hylighter1.objects.get(id=id)

        else:
            return Response({'status' : 'success','data':serializer.data})

        serializer = HylighterSerializer1(uid,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status':'success','data' : serializer.data})
        else:
            return Response({'status' : "invalid data...","errors":serializer.errors})


    def delete(self,request,id=None):
        if id:
            try:
                uid = hylighter1.objects.get(id=id).delete()

                return Response({'status' : 'success'})
            except:
                return Response({'status' : "invalid data..."})
        else:
                return Response({'status' : "invalid data..."})


class HylighterDeleteWordView(APIView):
    def delete(self, request, user_id=None,book_id=None, word_id=None):
        try:
            highlighter_data = hylighter1.objects.get(user_data__user_id=user_id,book_data__id=book_id)
            print(highlighter_data)
            
            words_list = json.loads(highlighter_data.words)

            
            word_to_delete = next((word for word in words_list if word.get('id') == word_id), None)
            
            if word_to_delete:
                words_list.remove(word_to_delete) 

                highlighter_data.words = json.dumps(words_list)
                highlighter_data.save()

                return Response({'status': 'success', 'message': 'Word deleted successfully'})
            else:
                return Response({'status': 'error', 'message': 'Word not found'}, status=status.HTTP_404_NOT_FOUND)

        except hylighter1.DoesNotExist:
            return Response({'status': 'error', 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)