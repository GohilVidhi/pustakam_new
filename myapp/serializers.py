
from rest_framework import serializers
from .models import*
from googletrans import Translator
import pytz   

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
        



#------------- topic ----------------

class topic_serializers(serializers.Serializer):
    
    topic_id = serializers.IntegerField(source='id',required=False)
    topic_english=serializers.CharField(max_length=50,required=False)
    topic_hindi=serializers.CharField(max_length=50,required=False)
    timestamp = serializers.SerializerMethodField()
    number = serializers.IntegerField(required=False)
    

    class Meta:
        models=topic
        fields ='__all__'
        exclude = ('id',) 
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  

    # def create(self, validated_data):
    #     if 'topic_hindi' not in validated_data or not validated_data['topic_hindi']:
    #         translator = Translator()
    #         translation = translator.translate(validated_data['topic_english'], src='en', dest='hi')
    #         validated_data['topic_hindi'] = translation.text
        
    #     return topic.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.topic_english = validated_data.get('topic_english', instance.topic_english)
        
    #     if 'topic_hindi' in validated_data:
    #         instance.topic_hindi = validated_data['topic_hindi']
            
    #     else:
    #         translator = Translator()
    #         translation = translator.translate(instance.topic_english, src='en', dest='hi')
    #         instance.topic_hindi = translation.text
        
    #     instance.save()
    #     return instance
    
    def create(self, validated_data):
        return topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.topic_english=validated_data.get('topic_english',instance.topic_english)
        
        instance.topic_hindi=validated_data.get('topic_hindi',instance.topic_hindi)
        instance.number=validated_data.get('number',instance.number)


        instance.save()
        return instance        
    
#-------------Author_serializers ----------------
class author_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    topic_data = serializers.SlugRelatedField(slug_field='id', queryset=topic.objects.all(), required=False)    
    author_english = serializers.CharField(max_length=100, required=True)
    author_hindi=serializers.CharField(max_length=50,required=True)
    timestamp = serializers.SerializerMethodField()
    number = serializers.IntegerField(required=False)

    class Meta:
        model = author
        fields = '__all__'
        exclude = ('id',)
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        return author.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.topic_data=validated_data.get('topic_data',instance.topic_data)
        instance.author_english=validated_data.get('author_english',instance.author_english)
        instance.author_hindi=validated_data.get('author_hindi',instance.author_hindi)
        instance.number=validated_data.get('number',instance.number)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.topic_data is not None:
            representation["topic_data"] = topic_serializers(instance.topic_data).data
        else:
            representation["topic_data"] = None
        return representation

#-------------User_serializers----------------

class user_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user_id=serializers.CharField(max_length=100,required=False)
    languages=serializers.CharField(max_length=20,required=False,allow_null=True)   
    mobile_no = serializers.IntegerField(required=True)
    timestamp = serializers.SerializerMethodField()
    image=serializers.ImageField(required=True,validators=[delete_file_in_folder])
    
    class Meta:
        model = user
        fields = '__all__'
        exclude = ('id',) 
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    
    def create(self, validated_data):
        return user.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.user_id=validated_data.get('user_id',instance.user_id)
        instance.languages=validated_data.get('languages',instance.languages)
        instance.mobile_no=validated_data.get('mobile_no',instance.mobile_no)
       

        

        instance.save()
        return instance   
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('languages') is None:
            representation['languages'] = ""
        return representation  
    
    
#-------------admin_login_serializers ----------------
class admin_login_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    email=serializers.CharField(max_length=50,required=True)
    password=serializers.CharField(max_length=50,required=True)
    timestamp = serializers.SerializerMethodField()
    class Meta:
        models=admin_login
        fields ='__all__'
        exclude = ('id',)
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  

    def create(self, validated_data):
        return admin_login.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email=validated_data.get('email',instance.email)
        instance.password=validated_data.get('password',instance.password)

        instance.save()
        return instance
    
#=============in book show topic===================
class topic___Serializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = topic
        fields ='__all__'

#=========in book show author=========================
class author___Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = author
        fields ='__all__'
        
#==============in book show language===================
class language___Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Languages
        fields ='__all__'
    

#====================BooksSerializer================
class BooksSerializer(serializers.ModelSerializer):
    author_data = serializers.PrimaryKeyRelatedField(many=True, queryset=author.objects.all(), required=True)
    topic_data = serializers.PrimaryKeyRelatedField(many=True, queryset=topic.objects.all(), required=False)
    language_data = serializers.PrimaryKeyRelatedField(many=True, queryset=Languages.objects.all(), required=True)
    book_keywords = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False)
    
    book_front_image=serializers.ImageField(required=False)

    book_file=serializers.FileField(required=True)
    timestamp = serializers.SerializerMethodField()
    number = serializers.IntegerField(required=False)
    purchase_count=serializers.IntegerField(required=False)
    download_count=serializers.IntegerField(required=False)
    draft=serializers.BooleanField(required=False)
    book_name_english=serializers.CharField(max_length=255,required=True)
    
    book_price=serializers.IntegerField(required=True)
    
    sutrakar = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False  )
    
    vyakhyakar = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False  )
    
    anuvadkarta = serializers.ListField(
        child=serializers.CharField(max_length=255, allow_blank=True),
        required=False  )

    class Meta:
        model = Books
        fields = '__all__'
        
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata') 
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    def create(self, validated_data):
        author_data = validated_data.pop('author_data', [])
        topic_data = validated_data.pop('topic_data', [])
        language_data = validated_data.pop('language_data', [])
        
        book = Books.objects.create(**validated_data)
        book.author_data.set(author_data)
        book.topic_data.set(topic_data)
        book.language_data.set(language_data)
        
        return book

    
        
    def update(self, instance, validated_data):
        instance.book_name_english = validated_data.get('book_name_english', instance.book_name_english)
        instance.book_name_hindi = validated_data.get('book_name_hindi', instance.book_name_hindi)
        instance.book_subtitle_english = validated_data.get('book_subtitle_english', instance.book_subtitle_english)
        instance.book_subtitle_hindi = validated_data.get('book_subtitle_hindi', instance.book_subtitle_hindi)
        instance.book_front_image = validated_data.get('book_front_image', instance.book_front_image)

        instance.book_details_english = validated_data.get('book_details_english', instance.book_details_english)
        instance.book_details_hindi = validated_data.get('book_details_hindi', instance.book_details_hindi)
        instance.book_price_discount = validated_data.get('book_price_discount', instance.book_price_discount)
        instance.book_price = validated_data.get('book_price', instance.book_price)
        instance.book_keywords = validated_data.get('book_keywords', instance.book_keywords)
        instance.number=validated_data.get('number',instance.number)
        instance.book_file = validated_data.get('book_file', instance.book_file)
        instance.book_free_demo = validated_data.get('book_free_demo', instance.book_free_demo)
        
        instance.sutrakar = validated_data.get('sutrakar', instance.sutrakar)
        
        instance.vyakhyakar = validated_data.get('vyakhyakar', instance.vyakhyakar)
        
        instance.anuvadkarta = validated_data.get('anuvadkarta', instance.anuvadkarta)
        instance.purchase_count=validated_data.get('purchase_count',instance.purchase_count)
        instance.download_count=validated_data.get('download_count',instance.download_count)
        instance.book_name_english=validated_data.get('book_name_english',instance.book_name_english)
        instance.draft=validated_data.get('draft',instance.draft)

        if 'author_data' in validated_data:
            instance.author_data.set(validated_data.get('author_data'))
        if 'topic_data' in validated_data:
            instance.topic_data.set(validated_data.get('topic_data'))
        if 'language_data' in validated_data:
            instance.language_data.set(validated_data.get('language_data'))

        instance.save()
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        
        if not instance.book_front_image:
            representation['book_front_image'] = instance.book_name_english

        
        representation['topic_data'] = topic___Serializer(instance.topic_data.all(), many=True).data if instance.topic_data.exists() else None
        
        representation['author_data'] = author___Serializer(instance.author_data.all(), many=True).data if instance.author_data.exists() else None
        
                            
        representation['language_data'] = language___Serializer(instance.language_data.all(), many=True).data if instance.language_data.exists() else None
        return representation
            
            
#-------------Login_User_serializers ----------------
class BookSerializer11(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','book_name_english','book_name_hindi']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        purchase_data = self.context.get('purchase_data', [])
        for book in representation.get("wishlist_data", []):
            if any(purchase['book_data']['id'] == book['id'] for purchase in purchase_data):
                book["purchase"] = True
            else:
                book["purchase"] = False
        return representation        


from datetime import datetime
class login_user_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user_id=serializers.CharField(max_length=100,required=False)   
    name=serializers.CharField(max_length=100,required=True)
    mobile_no = serializers.IntegerField(required=True)
    email=serializers.CharField(max_length=100,required=True)
    image=serializers.ImageField(required=True)
    password=serializers.CharField(max_length=100,required=True)
    languages=serializers.CharField(max_length=20,required=False)
    theme=serializers.CharField(max_length=20,required=False)
    timestamp = serializers.SerializerMethodField()
    password_time=serializers.DateTimeField(required=False,format="%Y-%m-%d %H:%M:%S.%f", read_only=True)
    is_expired=serializers.SerializerMethodField()
    purchase_data = serializers.SerializerMethodField()
    wishlist_data = serializers.SerializerMethodField()
    download_data = serializers.SerializerMethodField()
    membership=serializers.BooleanField(required=False)
    membership_type=serializers.CharField(max_length=255,required=False)
    
    class Meta:
        model = login_user 
        fields = '__all__'
        exclude = ('id',) 
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    
    
    def get_is_expired(self, obj):
        if obj.password_time:
            current_time = datetime.now(pytz.timezone('Asia/Kolkata'))
        
            return obj.password_time >= current_time
        return False
    
    def get_purchase_data(self, obj):
        
        purchase_instances = add_to_cart.objects.filter(user_data=obj)
        print(purchase_instances, "data")

    
        if purchase_instances.exists():
            
            books = [purchase.book_data for purchase in purchase_instances]
            return BookSerializer11(books, many=True).data  
        return []
    
    
    def get_wishlist_data(self, obj):
        
        purchase_instances = wishlist.objects.filter(user_data=obj)
        print(purchase_instances, "data")


        if purchase_instances.exists():
            
            books = [purchase.book_data for purchase in purchase_instances]
            return BookSerializer11(books, many=True).data
        return []
    
    def get_download_data(self, obj):

        purchase_instances = download.objects.filter(user_data=obj)
        print(purchase_instances, "data")


        if purchase_instances.exists():
            
            books = [purchase.book_data for purchase in purchase_instances]
            return BookSerializer11(books, many=True).data 
        return []
    
    
    
    def create(self, validated_data):
        return login_user.objects.create(**validated_data)
        

    def update(self, instance, validated_data):
        instance.user_id=validated_data.get('user_id',instance.user_id)
        instance.name=validated_data.get('name',instance.name)
        instance.mobile_no=validated_data.get('mobile_no',instance.mobile_no)
        instance.email=validated_data.get('email',instance.email)
        instance.image=validated_data.get('image',instance.image)
        instance.password=validated_data.get('password',instance.password)
        instance.languages=validated_data.get('languages',instance.languages)
        instance.theme=validated_data.get('theme',instance.theme)
        instance.membership=validated_data.get('membership',instance.membership)
        instance.membership_type=validated_data.get('membership_type',instance.membership_type)

        instance.save()
        return instance   
    def to_representation(self, instance):
        
        representation = super().to_representation(instance)


        purchase_data = representation.get('purchase_data', [])

    
        for book in representation.get("wishlist_data", []):

            book["purchase"] = any(purchase['id'] == book['id'] for purchase in purchase_data)


        return representation

    

#==========================ad_serializers==================================
class ad_serializers(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()
    class Meta:
        model = ad
        fields = "__all__"
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    
    def create(self, validated_data):
        
        ad_instance = ad.objects.create(**validated_data)
        return ad_instance

    def update(self, instance, validated_data):

        instance.file = validated_data.get('file', instance.file)
        instance.type = validated_data.get('type', instance.type)
        instance.url = validated_data.get('url', instance.url)
        
        instance.save()
        return instance
    
    
# ========================== notification =========================

class user_data_notification(serializers.ModelSerializer):
    class Meta:
        model = login_user
        fields ="__all__"


class NotificationSerializer(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True,many=True)
    timestamp = serializers.SerializerMethodField()
    class Meta:
        model = show_notification
        fields = ['id', 'user_data', 'message', 'title', 'read', 'timestamp']
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    def create(self, validated_data):
        user_data_1 = validated_data.pop('user_data', [])
        noti=show_notification.objects.create(**validated_data)
        noti.user_data.set(user_data_1)
        noti.save()
        return noti
    def update(self, instance, validated_data):
        user_data_1 = validated_data.pop('user_data', [])
        if user_data_1:
                        
            instance.user_data.set(user_data_1)
            instance.message=validated_data.get('message',instance.message)
            instance.title=validated_data.get('title',instance.title)
            instance.read=validated_data.get('read',instance.read)
            instance.save()
            return instance    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user_data"] = user_data_notification(instance.user_data,many=True).data 
        return representation  
    
    
    
    
#==================add_to_cart==================

class login_user___Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = login_user
        fields ='__all__'

class show_buy_book(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields =['id','book_name_english','book_name_hindi','book_price']



class add_to_cart_serializer(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True)
    book_data= serializers.SlugRelatedField(slug_field='id', queryset=Books.objects.all(), required=True)
    timestamp = serializers.SerializerMethodField()
    
    class Meta:
        model = add_to_cart
        fields = ['id', 'user_data', 'book_data','timestamp']
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
        
    def create(self, validated_data):
        return add_to_cart.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        
        instance.user_data=validated_data.get('user_data',instance.user_data)
        instance.book_data=validated_data.get('book_data',instance.book_data)
         
        instance.save()
        return instance    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["book_data"] = show_buy_book(instance.book_data).data 
        
        representation["user_data"] = login_user___Serializer(instance.user_data).data 
        return representation  
    
    
#===============book_languages==========
class book_languages_serializers(serializers.Serializer):
    
    id = serializers.IntegerField(required=False)
    languages=serializers.CharField(max_length=255,required=False)
    number = serializers.IntegerField(required=False)
    timestamp = serializers.SerializerMethodField()
    

    class Meta:
        models=Languages
        fields ='__all__'
        exclude = ('id',) 
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  # Set to your desired time zone
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
        
    def create(self, validated_data):
        return Languages.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        
        instance.languages=validated_data.get('languages',instance.languages)
        instance.number=validated_data.get('number',instance.number)
        instance.save()
        return instance  
    
# =========================== Add Wishlist Book ================    
class Wishlist_user___Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = login_user
        fields =['user_id','name','email','languages']

class Wishlist_show_book(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields =['id','book_name_english','book_name_hindi','book_price']



class Add_Wishlist_Book_Serializer(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True)
    book_data= serializers.SlugRelatedField(slug_field='id', queryset=Books.objects.all(), required=True)
    timestamp = serializers.SerializerMethodField()
    
    
    class Meta:
        model = wishlist
        fields = "__all__"
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')  
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    
    def create(self, validated_data):
        return wishlist.objects.create(**validated_data)
               
    def update(self, instance, validated_data):
        instance.user_data=validated_data.get('user_data',instance.user_data)
        instance.book_data=validated_data.get('book_data',instance.book_data)
        

        instance.save()   
        return instance    
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["book_data"] = Wishlist_show_book(instance.book_data).data 
        
        representation["user_data"] = Wishlist_user___Serializer(instance.user_data).data 
        return representation  
    
     
    
 #=====================================================   
    
class download_user___Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = login_user
        fields =['user_id','name','email','languages']

class download_show_book(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields =['id','book_name_english','book_name_hindi']



class download_Serializer(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True)
    book_data= serializers.SlugRelatedField(slug_field='id', queryset=Books.objects.all(), required=True)
    timestamp = serializers.SerializerMethodField()
    
    
    class Meta:
        model = download
        fields = "__all__"
        read_only_fields = ['timestamp']
    def get_timestamp(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata') 
        local_dt = obj.timestamp.astimezone(local_tz)
        return local_dt.strftime('%Y-%m-%d %H:%M:%S')  
    
    def create(self, validated_data):
        return download.objects.create(**validated_data)
   
          
               
    def update(self, instance, validated_data):

        instance.user_data=validated_data.get('user_data',instance.user_data)
        instance.book_data=validated_data.get('book_data',instance.book_data)

        

        instance.save()   
        return instance      
    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["book_data"] = download_show_book(instance.book_data).data 
        
        representation["user_data"] = download_user___Serializer(instance.user_data).data 
        return representation  
#==============================================

# =========================== Hylighter ================
import json
from datetime import datetime
import pytz

class WordsField(serializers.Field):
    def to_representation(self, value):
        
        try:
            words_list = json.loads(value)
        except (TypeError, ValueError):
            words_list = []

        for word in words_list:
            ordered_word = {}
            if 'id' in word:
                ordered_word['id'] = word.pop('id')  
            if 'book_page' in word:
                ordered_word['book_page'] = word.pop('book_page') 
            ordered_word.update(word) 
            word.clear()
            word.update(ordered_word)
        return words_list
    
    def to_internal_value(self, data):
        allowed_keys = {'book_page', 'color', 'word', 'timestamp'}
        if isinstance(data, list):
            existing_data = self.parent.instance.words if self.parent.instance and self.parent.instance.words else "[]"
            try:
                existing_data_list = json.loads(existing_data)
            except (TypeError, ValueError):
                existing_data_list = []

            max_id = max((entry.get('id', 0) for entry in existing_data_list), default=0)
            updated_data = existing_data_list
            for word in data:
                if not isinstance(word, dict):
                    raise serializers.ValidationError("Each item in the list must be a dictionary.")
                if not allowed_keys.issuperset(word.keys()):
                    raise serializers.ValidationError(f"Only these fields are allowed: {allowed_keys}")
                max_id += 1
                word['id'] = max_id

                if 'timestamp' not in word:
                    local_tz = pytz.timezone('Asia/Kolkata')
                    word['timestamp'] = datetime.now(local_tz).strftime('%Y-%m-%d %H:%M:%S')
                updated_data.append(word)
            try:
                value = json.dumps(updated_data)
            except (TypeError, ValueError):
                raise serializers.ValidationError("Invalid format for words.")
        else:
            raise serializers.ValidationError("Expected a list of dictionaries.")
        return value



class HylighterSerializer1(serializers.ModelSerializer):
    user_data= serializers.SlugRelatedField(slug_field='user_id', queryset=login_user.objects.all(), required=True)
    book_data= serializers.SlugRelatedField(slug_field='id', queryset=Books.objects.all(), required=True)
    words = WordsField()

    
    class Meta:
        model = hylighter1
        fields = "__all__"
 
    def create(self, validated_data):
        return hylighter1.objects.create(**validated_data)
       
    def update(self, instance, validated_data):
        
        instance.user_data=validated_data.get('user_data',instance.user_data)
        instance.book_data=validated_data.get('book_data',instance.book_data)
        instance.words=validated_data.get('words',instance.words)
        instance.save()
        return instance    
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["user_data"] = user_data_notification(instance.user_data).data 
        representation["book_data"] = BooksSerializer(instance.book_data).data

        return representation 
    
#==============================================