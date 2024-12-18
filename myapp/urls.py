"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from .views import *

urlpatterns = [


    path('topic/', topic_view.as_view()),
    path('topic/<int:id>/', topic_view.as_view()),

    path('author/', author_view.as_view()),
    path('author/<int:id>/', author_view.as_view()),
    path('author/topic_id/<int:topic_id>/', author_view.as_view()),

    path('user/', user_view.as_view()),
    path('user/<int:id>/', user_view.as_view()),
    
    path('admin_login/', admin_login_view.as_view()),
    path('admin_login/<int:id>/', admin_login_view.as_view()),

    path('books/', books_view.as_view()),
    path('books/<int:id>/', books_view.as_view()),
    path('books/topic_id/<int:topic_id>/', books_view.as_view()),

    path('user_data/', login_user_view.as_view()),
    path('user_data/<str:id>/', login_user_view.as_view()),
    path('user_data/email/<str:email>/', login_user_view.as_view()),
    
    path('user_login/', login_user_post_view.as_view()),
    
    #=================ad_get==============================
    path('ad/', ad_view.as_view()),
    path('ad/<int:id>/', ad_view.as_view()),
    
    path('notification/', notification_view.as_view()),
    path('notification/<int:id>/', notification_view.as_view()),
    path('notification/user_id/<str:user_id>/', notification_view.as_view()),
    
    path('buy_book/', add_to_cart_view.as_view()),
    path('buy_book/<int:id>/', add_to_cart_view.as_view()),
    
    
    path('languages/', book_languages_view.as_view()),
    path('languages/<int:id>/', book_languages_view.as_view()),
        
    # =========================== Add Wishlist Book ================     

    path('add_wishlist_book/', add_wishlist_book_view.as_view()),
    path('add_wishlist_book/<int:id>/', add_wishlist_book_view.as_view()),
    
    
    
    path('forgot_password/', views.send_test_email, name='send_test_email'),
    path('home/', views.home, name='home'),
    
    
    path('download_book/', download_view.as_view()),
    path('download_book/<int:id>/', download_view.as_view()),
    
    path('hylighter1/', hylighter_view1.as_view()),
    path('hylighter1/<int:id>/', hylighter_view1.as_view()),

    path('hylighter1/user_id/<str:user_id>/book_id/<int:book_id>/word_id/<int:word_id>/delete/', HylighterDeleteWordView.as_view(), name='delete_highlighter_word'),

    
]


#======get topic by using auto translate=========
#   {     
#             "topic_english": "Rigveda",
#               "number": 0       
#         }

#----------get topic normal-----------
#  {
#             "topic_english": "Rigveda",
#             "topic_hindi": "ऋग्वेद",
#               "number": 0
#         }

#====================get  author======================
# {
#     "topic_data": 2,
#     "author_english": "Valmiki1",
#     "author_hindi": "वाल्मीकि",
#  "number": 0
# }

#=======================user get=======================
#  {    
#             "user_id": "vidhi",
#             "languages": "English",
#             "mobile_no": 9656897412
#         }

#=====================admin_login===============
# http://127.0.0.1:8000/admin_login/3/   <-update only


#  { 
#         "email": "admin@example.com",
#         "password": "12345"
#     }

#===================Books get=========================


# {
        
#         "author_data": [
#            1,2                               
#         ],
#         "topic_data": [
#           3                                  
#         ],
#         "language_data": [
#           1                                   
#         ],

#         "book_keywords": [
#             "Python", "Python", "Python"
           
#         ],
       
                 
#         "book_name_english": "ramayan",
#         "book_name_hindi": "रामायण",
#         "book_subtitle_english": "rama",
#         "book_subtitle_hindi": "रामा",
#         "book_languages": "hindi",
#         "book_details_english": "A comprehensive guide to Python programming.",
#         "book_details_hindi": "पायथन प्रोग्रामिंग पर एक व्यापक गाइड।",
#         "book_price_discount": 50,
#         "book_price": 501.0,
#  "book_free_demo": 0.0,
#   "number": 0
#     }



#----------------
# 04/12/24
#  {
     
#         "author_data": [10
           
#         ],
#         "topic_data": [
#          1
#         ],
#         "language_data": [
#           1
#         ],
#         "book_keywords": [
#             "Python",
#             "Python"        ],
   
      
     
#         "number": 0,
#         "purchase_count": 6,
#         "download_count": 6,
   
#         "sutrakar": [
#             "dfdf"
      
#         ],
#         "vyakhyakar": [
#             "dfdf"
#         ],
#         "anuvadkarta": [
#             "dfdf"
#         ],
#         "book_name_english": "ramayan",
#         "book_name_hindi": "रामायण",
#         "book_subtitle_english": "rama",
#         "book_subtitle_hindi": "रामा",
#         "book_details_english": "A comprehensive guide to Python programming.",
#         "book_details_hindi": "पायथन प्रोग्रामिंग पर एक व्यापक गाइड।",
#         "book_price_discount": 50,
#         "book_price": 501.0,
#         "book_free_demo": 0.0,
#         "purchase": false
#     }
#=========================user_data================
        # {
        #     "user_id": "123b",
        # "device_token": null,
        #     "name": "gohil",
        #     "mobile_no": 9054098332,
        #     "email": "v1@gmail.com",
        #    "image": null,
        #     "password": "12345",
        #     "languages": "english",
        #     "theme": "dark"
        # }
#---------------------------------------------------------
# 04/12/24

#    {
#             "user_id": "123c",
      
#             "name": "gohil",
#             "mobile_no": 9054098332,
#             "email": "v2@gmail.com",
        
#             "password": "12345",
#             "languages": "english",
#             "theme": "dark",
#  "is_expired": false,
#  "download_data": [1],        # when user can add this book in download
#  "wishlist_data": [1],        # when user can add this book in wishlist
#  "purchase_data": [1],        # when user can add this book in add to cart
#    "membership": false,
#             "membership_type": "helloo"
#         }

#=================notifications====================
# {
#   "user_data": ["123b", "123"],
#   "message": "hellloo",
#   "title": "python developer",
#   "read": false}


#===========Languages===========
# {"languages":"english"}

#==========add to cart===============
#  {   
#             "user_data": "123",
#             "book_data":
#                4
            
#         }

#================hylighter1======================
# {
#     "user_data": "123",
#     "book_data": 2,
#     "words": [
#           {"book_page": 3, "color": "green", "word": "new example"},
#           {"book_page": 4, "color": "red", "word": "ok"}
#     ]
# }