from django.db import models
from googletrans import Translator
from django_mysql.models import ListTextField,ListCharField


import os
def delete_file_in_folder(file_name):
    folder_path="u_image\\"

    file_nae=file_name.name
    xyz=folder_path + file_nae
    print(xyz)
    if os.path.isfile(xyz):  # Check if the file exists
        os.remove(xyz)
        print("File deleted successfully.")
    else:
        print("File not found.")
        

class topic(models.Model):
    topic_english = models.CharField(max_length=255)
    topic_hindi = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    number=models.IntegerField(default=0,blank=True,null=True)
    def __str__(self) -> str:
        return self.topic_english
    
    # def save(self, *args, **kwargs):
    #     if not self.topic_hindi:
    #         translator = Translator()
    #         translation = translator.translate(self.topic_english, src='en', dest='hi')
    #         self.topic_hindi = translation.text
    #     super().save(*args, **kwargs)
    
class author(models.Model):
    topic_data=models.ForeignKey(topic,on_delete=models.CASCADE,blank=True,null=True)  
    author_english=models.CharField(max_length=50,blank=True,null=True)      
    author_hindi=models.CharField(max_length=50,blank=True,null=True) 
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    number=models.IntegerField(default=0,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.author_english     
    
class user(models.Model):
    user_id=models.CharField(max_length=100,blank=True,null=True)  
    languages=models.CharField(max_length=100,blank=True,null=True) 
    mobile_no=models.IntegerField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    image=models.ImageField(upload_to="u_image",blank=True,null=True)
    
    
    
    def __str__(self) -> str:
        return self.user_id 
    


#==============admin_login=======
class admin_login(models.Model):
    email=models.EmailField(max_length=255,blank=True,null=True)
    password=models.CharField(max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.email     
    
#==========Languages============
class Languages(models.Model):
    languages=models.CharField(max_length=255,blank=True,null=True)
    number=models.IntegerField(default=0,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.languages 
    
#=================Books models=======================
class Books(models.Model):
    book_name_english=models.CharField(max_length=255,blank=True,null=True)
    book_name_hindi=models.CharField(max_length=255,blank=True,null=True)
    book_subtitle_english=models.CharField(max_length=255,blank=True,null=True)
    book_subtitle_hindi=models.CharField(max_length=255,blank=True,null=True)
    
    book_front_image=models.ImageField(upload_to='image', null=True, blank=True)
    
    author_data=models.ManyToManyField(author)
    topic_data=models.ManyToManyField(topic,blank=True,null=True)
    language_data=models.ManyToManyField(Languages)
    book_details_english=models.TextField(blank=True,null=True)
    book_details_hindi=models.TextField(blank=True,null=True)
    book_price_discount=models.IntegerField()
    book_price=models.FloatField()
    book_keywords=ListTextField(base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    
    book_file=models.FileField(upload_to="book",blank=True,null=True)
    book_free_demo=models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    number=models.IntegerField(default=0,blank=True,null=True)
    purchase = models.BooleanField(default=False)
    
    
    purchase_count=models.IntegerField(default=0)
    download_count=models.IntegerField(default=0)
    draft = models.BooleanField(default=False)  
      
    sutrakar=ListTextField(base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    vyakhyakar=ListTextField(base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    anuvadkarta=ListTextField(base_field=models.CharField(max_length=255,blank=True,null=True),size=100,blank=True,null=True)
    
    def __str__(self):
        return self.book_name_hindi   
     
#======================login_user=======================

class login_user(models.Model): 
    user_id=models.CharField(max_length=100,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    mobile_no=models.IntegerField(blank=True,null=True)
    image=models.ImageField(upload_to="image",blank=True,null=True) 
    password=models.CharField(max_length=100,blank=True,null=True)
    languages=models.CharField(max_length=100,blank=True,null=True)
    theme=models.CharField(max_length=100,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    password_time = models.DateTimeField(blank=True,null=True)
    membership = models.BooleanField(default=False)
    membership_type = models.CharField(max_length=255,blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name 
    
    
#===================add=====================
class ad(models.Model):
    file=models.FileField(upload_to="video")
    type=models.CharField(max_length=255,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    url=models.CharField(max_length=255,blank=True,null=True)
    

#==============notification============
class show_notification(models.Model):
    user_data = models.ManyToManyField(login_user, blank=True, null=True)
    message=models.TextField()
    title = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    
#======================add_to_cart================
class add_to_cart(models.Model):
    user_data=models.ForeignKey(login_user,on_delete=models.CASCADE,blank=True,null=True)  
    book_data=models.ForeignKey(Books,on_delete=models.CASCADE,blank=True,null=True)  
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    
# ===========================Add Wishlist Book ================    



class wishlist(models.Model):
    user_data = models.ForeignKey(login_user,on_delete=models.CASCADE)  
    book_data = models.ForeignKey(Books,on_delete=models.CASCADE,blank=True,null=True)  
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
#=====================download=========================================
class download(models.Model):
    user_data = models.ForeignKey(login_user,on_delete=models.CASCADE)  
    book_data = models.ForeignKey(Books,on_delete=models.CASCADE,blank=True,null=True)  
    timestamp = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    
    
# =========================== Hylighter ================

class hylighter1(models.Model):    
    user_data = models.ForeignKey(login_user,on_delete=models.CASCADE)  
    book_data = models.ForeignKey(Books,on_delete=models.CASCADE)  
    words = models.TextField(default='[]',blank=True,null=True)