---
template: blog_post.html
layout: post
title: "Python Django Restful Framework"
alias: DRF
tags:
  - rest
  - drf
  - django
  - python
url: "[GitHub - encode/django-rest-framework: Web APIs for Django](https://github.com/encode/django-rest-framework)"
date: 2023-12-19
---

- Django Restful Framework Videos
  url:: [drf实战和源码剖析](https://www.bilibili.com/video/BV1xj411C7ws)
  channel:: https://space.bilibili.com/336469068
  tags:: rest, DRF, python, django, web, API
  date:: [[Sep 25th, 2023]]
  tutor:: 武沛齐
- Resources
  heading:: 2
	- [银角大王-武沛齐Django-Drf框架与django3项目搭建案例全套教学 完整版](https://www.bilibili.com/video/BV1Sc41157hr)
	- [银角大王-武沛齐Django-Drf框架与vue项目搭建案例全套教学  完整版](https://www.bilibili.com/video/BV1pA41117U4)
	- [全站最牛逼的DRF（Django-restframework），没有之一！](https://www.bilibili.com/video/BV1XR4y157rk)
	- [【独家专授】我要安利给所有人DRF（Django-rest-framework）与源码解析自学教程全程无广安心食用！！！](https://www.bilibili.com/video/BV1Cv4y1R77V)
	- [黑马 Django REST Framework框架经典教程](https://www.bilibili.com/video/BV1Sz4y1o7E8)
- Jump start
  heading:: 2
	- install
	  heading:: 3
		- [Home - Django REST framework  install](https://www.django-rest-framework.org/#installation)
	- usage
	  heading:: 3
		- [Quickstart - Django REST framework](https://www.django-rest-framework.org/tutorial/quickstart)
		- settings:

		  ``` python
		  INSTALLED_APPS = [
		      ...
		      'rest_framework',
		  ]
		  ```
		- response

		  ``` python
		  # views.py
		  from rest_framework.response import Response
		  from rest_framework.decorators import api_view
		  @api_view(['GET'])
		  def login(reqeust):
		    return Response({'status': 'sucessfull', 'message'})

		  from rest_framework.views import APIView
		  class LoginView(APIView):
		    def get(self, request):
		      return Response({'status': 'sucessfull', 'message'})
		  # urls.py
		  urlpatterns = {
		    path('login/', views.LoginView.as_view())
		    path('login2/', views.login())
		  }
		  ```
	- minium django setup
	  heading:: 3

	  ``` python
	  INSTALLED_APPS = [
	      'django.contrib.staticfiles',
	      'api.apps.ApiConfig', # this include app : api
	      'rest_framework'
	  ]

	  MIDDLEWARE = [
	      'django.middleware.security.SecurityMiddleware',
	      'django.middleware.common.CommonMiddleware',
	      'django.middleware.clickjacking.XFrameOptionsMiddleware',
	  ]

	  TEMPLATES = [
	      {
	          'BACKEND': 'django.template.backends.django.DjangoTemplates',
	          'DIRS': [],
	          'APP_DIRS': True,
	          'OPTIONS': {
	              'context_processors': [
	                  'django.template.context_processors.debug',
	                  'django.template.context_processors.request',
	              ],
	          },
	      },
	  ]

	  REST_FRAMEWORK = {
	      "UNAUTHENTICATED_USER": None   # disable user-content reference
	  }

	  ```
	- ((651210f8-a2fe-4194-9216-f1eefdded8a6))
	  heading:: 2
- APIView
  heading:: 2
  desc:: REST framework provides an ~APIView~ class, which subclasses Django's ~View~ class.
	- APIView <- django.views.View and it implemented `as_view()`
		- APIView has `csrf_exempt`. It implemented `as_view` and `dispatch`
		- Requests passed to the handler methods will be REST framework's `Request` instances, not Django's `HttpRequest` instances.
		- Handler methods may return REST framework's `Response`, instead of Django's `HttpResponse`  The view will manage content negotiation and setting the correct renderer on the response.
		- Any `APIException` exceptions will be caught and mediated into appropriate responses.
		- Incoming requests will be authenticated and appropriate permission and/or throttle checks will be run before dispatching the request to the handler method.
		-
- Requests
  heading:: 2
  desc:: REST framework's ~Request~ class extends the standard ~HttpRequest~,  adding support for REST framework's flexible request parsing and request authentication.
	- [Requests - Django REST framework](https://www.django-rest-framework.org/api-guide/requests/)
	  heading:: 3
	- DRF extend django HttpRequests by adding
	  heading:: 3
		- `data`: use `request.data.get('fieldname')` to get data from a POST request
		- `query_params`  handle URL like `/users/?id=12`
		- Authentication
		- Browser enhancement
		- extends HttpRequest
			- META
			- session
			- version
				- request.version
				- request.versioning_{ schema}
			- parser
			- negotiator
		-
- Authentication
  heading:: 2
  desc:: Auhentication is the mechanism of associating an incoming request with a set of identifying credentials, such as the user the request came from, or the token that it was signed with. The [permission](https://www.django-rest-framework.org/api-guide/permissions/) and [throttling](https://www.django-rest-framework.org/api-guide/throttling/) policies can then use those credentials to determine if the request should be permitted.
  id:: 65136fb1-b3fd-40b2-b22b-d8ea5e0908b9
	- Create a new Authentiation class
	  heading:: 3
	- SimpleAuth
	  heading:: 3
	  ``` python
	  # auth.py
	  class SimpleAuth(BaseAuthentication):
	    def authenticate(self, request):
	      token = request.query_params.get('token')
	      if token:
	        return 'admin', token #return user and token
	    	raise AuthenticationFailed('token missing')
	    def authenticate_header(self, request):
	      return "xxx app" # return when you need something put in header when failed
	  # view.py
	  class UserView(APIView):
	    authentication_class = [SimpleAuth]  # Auth is required
	    def get(self, request):
	      print(request.user, request.auth) # prints 'admin',  token
	      return Response({})

	  ```
	- Apply Authentication Globally
	  heading:: 3
		- in Settings.py

		  ``` python
		  REST_FRAMEWORK= {
		  "DEFAULT_AUTHENTICATION_CLASS": ["api.view.SimpleAuth",] # use string to avoid imporiting packages
		  }
		  ```
		- Override
			- First get Auth from setting.py and in each view read `authentication_class`. The 2nd will override global setting if it is not `None` set 2^{ nd} to `[]` will disable global setting and disable Auth
	- Multi Authenticators
	  heading:: 4
		- If `authenticate()` returns `None` when failed, DRF will go to next Authenticator until the return value is not None.
		- If all returns None. then `self.auth == None `
		- If you want to prevent `None` go through, put an authenticator that will raise fail at end of list
		- Verify token in Authentication middleware

		  ``` python
		  class QueryTokenAuth(BaseAuthentication):
		    def authenticate(self, request):
		      token = request.query_params.get('token')   # api:  GET order/?orderid=12&token=3322-333-111-111-3233
		      if not token
		      	return
		      user = models.UserInfo.objects.filter(token=token).first()
		      if user:
		        return user, token   # request.user = user, request.token=token
		      raise AuthenticationFailed({'code': 401})
		    def authenticate_header(self, request):
		      return "query failure"

		  class HeaderTokenAuth(BaseAuthentication):
		    def authenticate(self, request):
		      token = request.META.get("HTTP_AUTHORIZATION")   # api:  GET order/?orderid=12&token=3322-333-111-111-3233
		      if not token
		      	return
		      user = models.UserInfo.objects.filter(token=token).first()
		      if user:
		        return user, token   # request.user = user, request.token=token
		      raise AuthenticationFailed({'code': 401})
		    def authenticate_header(self, request):
		      return "nead failure"

		  ```
		- Auth success when `any()` of authenticator return `user, auth`
	- Login, Register and token issuing
	  heading:: 3
		- [Login and Register User — Django Rest Framework | by Emre Cevik | Python | Django & Rest | Medium](https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5)
		- Login url

		  ``` python
		  urlpatterns = [
		      path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
		      path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
		  ]
		  ```
		- Simple login with user/password

		  ``` python
		  class LoginView(APIView):
		  	authentication_classes=[]

		      def post(self, request):
		        user = request.data.get('username')
		        pwd = request.data.get('password')
		        user = models.UserInfo.objects.filter(username=user, password=pwd).first()
		        if not user:
		          return Response({'status': 1002, 'message': "user/pass failed"})
		        token=str(uuid.uuid4())
		        user.token = token
		        user.save()
		        return Response({"status": 200, 'data'= token})

		  ```
- Permission
  heading:: 2
  desc:: Together with [authentication](https://www.django-rest-framework.org/api-guide/authentication/) and [throttling](https://www.django-rest-framework.org/api-guide/throttling/), permissions determine whether a request should be granted or denied access.
  url:: [DRF: Permission](https://www.django-rest-framework.org/api-guide/permissions/)
	- Permissions are used to grant or deny access for different classes of users to different parts of the API.
	- The simplest style of permission would be to allow access to any authenticated user, and deny access to any unauthenticated user. This corresponds to the `IsAuthenticated` class in REST framework.
	- Sample permission class

	  ``` python
	  from rest_framework import permissions
	  class IsOwnerOrReadOnly(permissions.BasePermission):
	      """
	      Custom permission to only allow owners of an object to edit it.
	      """
	      # message is used to create a response body when per check failed
	      code = 401 # used to set http code
	      message = {"status":"False", "code": code, "data": "permission error for user", "msg": "IsOwnerCheck"}
	      def has_permission(self, request, view):
	          # Read permissions are allowed to any request,
	          # so we'll always allow GET, HEAD or OPTIONS requests.
	          if request.method in permissions.SAFE_METHODS:
	              return True
	          # Write permissions are only allowed to the owner of the snippet.
	          return False
	      def has_object_permission(self, request, view, obj):
	          # Read permissions are allowed to any request,
	          # so we'll always allow GET, HEAD or OPTIONS requests.
	          if request.method in permissions.SAFE_METHODS:
	              return True
	          # Write permissions are only allowed to the owner of the snippet.
	          return obj.owner == request.user
	  ```
	- Per-View permission check with

	  ``` python
	  permission_classes = [permissions.IsAuthenticatedOrReadOnly,
	                        IsOwnerOrReadOnly]
	  ```
	- `permission_classes` is `all()`, it is not same as `authentication_classes`
	- Global setting with
	  ``` python
	  # settings.py
	  REST_FRAMEWORK = {
	  "DEFAULT_PERMISSION_CLASS": ["ext.per.IsOwnerOrReadOnly"]
	  }
	  ```
	- One difference between ((65136fb1-b3fd-40b2-b22b-d8ea5e0908b9)) is if a list of Per-Class is add. **ALL** Permission check need success/True. It is **AND** operation
	- Add permission check in view

	  ``` python
	  class OrderView(APIView):
	  	permission_classes=[PermUser, PermAPI]
	  ```
	- Check permissions override
		- if you need to override default permission check mechanism, override `check_permissions()` function in view class 💀
- Throttling
  heading:: 2
  desc:: Throttling is similar to [permissions](https://www.django-rest-framework.org/api-guide/permissions/), in that it determines if a request should be authorized. Throttles indicate a temporary state, and are used to control the rate of requests that clients can make to an API.
	- As with permissions, multiple throttles may be used. Your API might have a restrictive throttle for unauthenticated requests, and a less restrictive throttle for authenticated requests.
	- Another scenario where you might want to use multiple throttles would be if you need to impose different constraints on different parts of the API, due to some services being particularly resource-intensive.
	- Settings

	  ``` python
	  REST_FRAMEWORK = {
	      'DEFAULT_THROTTLE_CLASSES': [
	          'rest_framework.throttling.AnonRateThrottle',
	          'rest_framework.throttling.UserRateThrottle'
	      ],
	      'DEFAULT_THROTTLE_RATES': {
	          'anon': '100/day',
	          'user': '1000/day'
	      }
	  }
	  ```
	  And in View

	  ``` python
	  class ExampleView(APIView):
	      throttle_classes = [UserRateThrottle]
	  ```
	  FBV

	  ```
	  @api_view(['GET'])
	  @throttle_classes([UserRateThrottle])
	  def example_view(request, format=None):
	      content = {
	          'status': 'request was permitted'
	      }
	      return Response(content)
	  ```
	- Define a throttle Class
		- In most case throttle class in django is good enough for 99% of the user cases. But in case you need to define a throttle of your own, here is two examples:
		  ``` python
		  class RandomRateThrottle(throttling.BaseThrottle):
		      def allow_request(self, request, view):
		          return random.randint(1, 10) != 1

		  class RandomRateThrottle2(throttling.SimpleRateThrottle):
		      def allow_request(self, request, view):
		        if super().allow_request(request, view):
		          return random.randint(1, 10) != 1

		  class MyRateThrottle(SimpleRateThrottle):
		      cache = default_cache  # 访问记录存放在django的缓存中（需设置缓存）
		      scope = "user"  # 构造缓存中的key different API can have different scope
		      cache_format = 'throttle_%(scope)s_%(ident)s'

		      # 设置访问频率，例如：1分钟允许访问10次
		      # 其他：'s', 'sec', 'm', 'min', 'h', 'hour', 'd', 'day'
		      THROTTLE_RATES = {"user": "10/m"}  #scope : rate

		      def get_cache_key(self, request, view):
		          if request.user:
		              ident = request.user.pk  # 用户ID
		          else:
		              ident = self.get_ident(request)  # 获取请求用户IP（去request中找请求头）

		          # throttle_u # throttle_user_11.11.11.11ser_2

		          return self.cache_format % {'scope': self.scope, 'ident': ident}

		      def throttle_failure(self):
		          wait = self.wait()
		          detail = {
		              "code": 1005,
		              "data": "访问频率限制",
		              'detail': "需等待{}s才能访问".format(int(wait))
		          }
		          raise ThrottledException(detail)
		  ```
- Versioning
  heading:: 2
  desc:: Versioning allows you to alter behavior between different clients. DRF provides for a number of different versioning schemes.
	- Config API version
	  heading:: 3
		- [[../assets/image-20210819154455680_1696666609261_0.png]]
		- settings.py

		  ``` python
		  REST_FRAMEWORK = {
		      'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning'
		  }
		  ```
		- View.py

		  ``` python
		  class ProfileList(APIView):
		      versioning_class = versioning.QueryParameterVersioning
		  ```
		-
	- Version schema
	  heading:: 3
		- [AcceptHeaderVersioning](https://www.django-rest-framework.org/api-guide/versioning/#acceptheaderversioning)
		  heading:: 3

		  > GET *bookings* HTTP/1.1
		  Host: example.com
		  Accept: application/json; version=1.0
		- [URLPathVersioning](https://www.django-rest-framework.org/api-guide/versioning/#urlpathversioning)
		  heading:: 3

		  > GET /v1/bookings/ HTTP/1.1
		  Host: example.com
		  Accept: application/json

		  ``` python
		  urlpatterns = [
		      re_path(
		          r'^(?P<version>(v1|v2))/bookings/$',
		          bookings_list,
		          name='bookings-list'
		      ),
		      re_path(
		          r'^(?P<version>(v1|v2))/bookings/(?P<pk>[0-9]+)/$',
		          bookings_detail,
		          name='bookings-detail'
		      )
		  ]
		  ```
		- [NamespaceVersioning](https://www.django-rest-framework.org/api-guide/versioning/#namespaceversioning)
		  heading:: 3

		  > GET *bookings* HTTP/1.1
		  Host: v1.example.com
		  Accept: application/json

		  ``` python
		  # bookings/urls.py
		  urlpatterns = [
		      re_path(r'^$', bookings_list, name='bookings-list'),
		      re_path(r'^(?P<pk>[0-9]+)/$', bookings_detail, name='bookings-detail')
		  ]

		  # urls.py
		  urlpatterns = [
		      re_path(r'^v1/bookings/', include('bookings.urls', namespace='v1')),
		      re_path(r'^v2/bookings/', include('bookings.urls', namespace='v2'))
		  ]
		  ```
		- [QueryParameterVersioning](https://www.django-rest-framework.org/api-guide/versioning/#queryparameterversioning)
		  heading:: 3

		  > GET *something*?version=0.1 HTTP/1.1
		  Host: example.com
		  Accept: application/json
	- Reverse URL
	  heading:: 3
		- [[../assets/image-20210820105543193-3386187_1696666581416_0.png]]
		- [[../assets/image-20210820112152615_1696666677979_0.png]]
- Request parsing
  heading:: 2
  desc:: REST framework includes a number of built in Parser classes, that allow you to accept requests with various media types. There is also support for defining your own custom parsers
	- Jsonparser
	  [[../assets/image-20210827081058194_1696668405368_0.jpg]]
	- File parser (MultiPartParser)
		- [[../assets/image-20210827083047327_1696668472683_0.jpg]]
	- File uploader
		- [[../assets/image-20210827084403453_1696668497009_0.jpg]]
		-
	-
- Content negotiation
  heading:: 2
  desc:: Content negotiation is the process of selecting one of multiple possible representations to return to a client, based on client or server preferences.
  url:: [Content negotiation - Django REST framework](https://www.django-rest-framework.org/api-guide/content-negotiation/)
	- The client need specify `content-type`and the value should be valid http `media type`
	- the config is through `parser_classes` and `content_negotiation_class`
	  Global setting

	  ``` python
	  REST_FRAMEWORK = {
	      'DEFAULT_CONTENT_NEGOTIATION_CLASS': 'myapp.negotiation.IgnoreClientContentNegotiation',
	  }
	  ```
	- When the code refer to request.data it will trigger the parser
	- Most used `JSONParser` and `FormParserxx`, to upload file `FileUploaderParser`, Large file `MultiPartParser`
	- If not specifed or content does not match parser, a exception will be throw
	-
	-
- Serializers
  heading:: 2
  desc:: Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into ~JSON~, ~XML~ or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
	- Declaring Serializers
	  heading:: 3
		- In a sense, Serializers is similar to ((651cfa1b-ce5c-486b-8f45-5f3cee8f113e))
		- Create a serializer for `Comment`

		  ``` python
		  from datetime import datetime

		  class Comment:
		      def __init__(self, email, content, created=None):
		          self.email = email
		          self.content = content
		          self.created = created or datetime.now()

		  comment = Comment(email='leila@example.com', content='foo bar')

		  from rest_framework import serializers
		  class CommentSerializer(serializers.Serializer):
		      email = serializers.EmailField()
		      content = serializers.CharField(max_length=200)
		      created = serializers.DateTimeField()
		  ```
	- Serializing object
	  heading:: 3
		- use ~CommentSerializer~ to serialize a comment, or list of comments
		  ``` python
		  serializer = CommentSerializer(comment)
		  serializer.data
		  # {'email': 'leila@example.com', 'content': 'foo bar', 'created': '2016-01-27T15:17:10.375877'}
		  comments = [comment, comment] # array of objects
		  serializer = CommentSerializer(comments, many=True)
		  serializer.data # a list of objects
		  from rest_framework.renderers import JSONRenderer

		  json = JSONRenderer().render(serializer.data)
		  ```
	- Deserializing
	  heading:: 3

	  ``` python
	  import io
	  from rest_framework.parsers import JSONParser

	  stream = io.BytesIO(json)
	  data = JSONParser().parse(stream)
	  serializer = CommentSerializer(data=data)
	  serializer.is_valid()
	  # True
	  serializer.validated_data
	  # {'content': 'foo bar', 'email': 'leila@example.com', 'created': datetime.datetime(2012, 08, 22, 16, 20, 09, 822243)}
	  ```
	- ModelSerializer
	  heading:: 3
	  desc:: serializer classes that map closely to Django model definitions.
		- The `ModelSerializer` class provides a shortcut that lets you automatically create a ~Serializer~ class with fields that correspond to the Model fields. It based on `Serializer` class and
		  * It will automatically generate a set of fields for you, based on the model.
		  * It will automatically generate validators for the serializer, such as unique_{ together} validators.
		  * It includes simple default implementations of `.create()` and `.update()`.
		- Declaring
		  heading:: 4

		  ``` python
		  class AccountSerializer(serializers.ModelSerializer):
		      class Meta:
		          model = Account
		          fields = ['id', 'account_name', 'users', 'created']  # similar to ModelForm, you can use fields = '__all__'
		          read_only_fields = ['account_name']
		  ```
		- `read_only` and `write_only`
			- `read_only` can be used for output serializer it can be shown in response
			- `write_only` used for input data serializer, e.g. password/token field
		- choice fields and foreign key
		  heading:: 4
			- e.g. gender: ((1:'male'), (2, 'female'))
			  depart was defined as foreign key to department table (id, name)

			  ``` python
			  # model gender: ((1:'male'), (2, 'female'))
			  class AccountSerializer(serializers.ModelSerializer):
			      gender_info = serializers.CharField(source='get_gender_display', read_only=True)
			      depart = serializers.CharField(source='depart.title') #show department title
			      class Meta:
			          model = Account
			          fields = ['id', 'account_name', 'users', 'created', 'gender_info', 'depart']
			  		extra_kwargs = {'gender': {'write_only': True}}
			  ```
			- It follow conventions of Django ModelForm
			- Use a new name `gender_info` because when write to DB we want a number 1|2, when read and show in API we want string of male|female
		- define own field
		  heading:: 4
		  ``` python
		  class AccountSerializer(serializers.ModelSerializer):
		      class Meta:
		          model = Account
		          fields = ['xxx']
		      def get_xxx(self, obj):
		          return obj.first_name + obj.last_name
		  ```
		- nested and embed
		  heading:: 4
			- Suppose there are multiple tables with 1:1 or m:n relations

			  ``` python
			  from django.db import models
			  class Role(models.Model):
			      title = models.CharField(verbose_name="标题", max_length=32)
			      order = models.IntegerField(verbose_name="顺序")
			  class Tag(models.Model):
			      caption = models.CharField(verbose_name="名称", max_length=32)
			  class UserInfo(models.Model):
			      name = models.CharField(verbose_name="姓名", max_length=32)
			      gender = models.SmallIntegerField(verbose_name="性别", choices=((1, "男"), (2, "女")))
			      role = models.ForeignKey(verbose_name="角色", to="Role", on_delete=models.CASCADE)
			      ctime = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

			      tags = models.ManyToManyField(verbose_name="标签", to="Tag")
			  ```
			- You can create a new ModelSerializer

			  ``` python
			  from rest_framework.views import APIView
			  from rest_framework.response import Response
			  from rest_framework import serializers
			  from api import models

			  class RoleSerializer(serializers.ModelSerializer):
			      class Meta:
			          model = models.Role
			          # fields = "__all__"
			          fields = ["id", 'title']

			  class TagSerializer(serializers.ModelSerializer):
			      class Meta:
			          model = models.Tag
			          fields = "__all__"

			  class InfoSerializer(serializers.ModelSerializer):
			      role = RoleSerializer()
			      tags = TagSerializer(many=True)

			      class Meta:
			          model = models.UserInfo
			          fields = ['id', 'name', "role", "tags"]

			  class InfoView(APIView):
			      def get(self, request):
			          queryset = models.UserInfo.objects.all()
			          ser = InfoSerializer(instance=queryset, many=True)
			          print(type(ser.data), ser.data)
			          return Response(ser.data)
			  ```
		- Inheritances
		  heading:: 4
		  ``` python
		  from rest_framework.views import APIView
		  from rest_framework.response import Response
		  from rest_framework import serializers
		  from api import models


		  class MySerializer(serializers.Serializer):
		      more = serializers.SerializerMethodField()

		      def get_more(self, obj):
		          return "123"

		  # inherit MySerializer
		  class InfoSerializer(serializers.ModelSerializer, MySerializer):
		      class Meta:
		          model = models.UserInfo
		          fields = ["id", "name", 'more']


		  class InfoView(APIView):
		      def get(self, request):
		          instance = models.UserInfo.objects.all().first()
		          ser = InfoSerializer(instance=instance, many=False)

		          print(type(ser.data), ser.data)
		          return Response(ser.data)
		  ```
		- Save/Update data
		  heading:: 4
		- save()/ update() method
		  heading:: 4
		  ``` python
		  serializer = CommentModelSerializer(data=data)
		  serializer.save()
		  # for non model serializer
		  serializer = CommentNonModelSerializer(data=data)
		  serializer.validated_data.pop('confirm_password') # there are filed should not save into database
		  models.Comment.objects.create(**serializer .validate_data)
		  ```
		- In save(), you can add additional fields
		  heading:: 4
		  ``` python
		  serializer.save(updated = datetime.now(), updated_by = request.user )
		  ```
		- Foreign key and many to many
		  heading:: 4
			- When validate/save foriegn key, DRF will check if the key is valid or not
			- It also apply when M2N is passed e.g. {'tags': [1, 1111]}, if `1111` not existed in M2N table, validation will fail
		- Override `to_presentation`
			- If you need to show something in DB in a more friendly way (beyond `display_xxx`) You can override  `to_presentation`
			- [[../assets/image_1696746627345_0.png]]

			  ``` python
			  class SbModelSerializer(NbHookSerializer, serializers.ModelSerializer):
			      class Meta:
			          model = models.NbUserInfo
			          fields = ["id", "name", "age", "gender"]
			          extra_kwargs = {
			              "id": {"read_only": True}
			          }

			      def nb_gender(self, obj): # YOu can define your own getter here
			          return obj.get_gender_display()

			      def nb_name(self, obj):
			          return obj.get_gender_display()
			  class SbView(APIView):
			      def post(self, request, *args, **kwargs):
			          ser = SbModelSerializer(data=request.data)  # the to_presentation was overrided
			          if ser.is_valid():
			              ser.save()
			              return Response(ser.data)
			          else:
			              return Response(ser.errors)
			  ```
	- Under the hood
		- [[../assets/image-20210823235752483_1696691331872_0.jpg]]
		- [[../assets/image-20210824001814091_1696723163568_0.jpg]]
		- [[../assets/image-20210824001844381_1696723308136_0.jpg]]
- Validator
  heading:: 2
  desc:: validation logic into reusable component, DRF validation is performed entirely on the serializer class.
	- Samples

	  ``` python
	  class CustomerReportRecord(models.Model):
	      time_raised = models.DateTimeField(default=timezone.now, editable=False)
	      reference = models.CharField(unique=True, max_length=20)
	      description = models.TextField()
	  # if meta set to CustomerReportRecord, reference max_len will be 20
	  class CustomerReportModelSerializer(serializers.ModelSerializer):
	      class Meta:
	          model = CustomerReportRecord

	  #This works as well
	  class CustomerReportSerializer(serializers.Serializer):
	      reference = serializers.CharField(required=True, max_length=20, min_length=4)
	      description = serializers.CharField(required=True, max_length=20)
	      # email = serializers.EmailField() # implemented email validation
	      email = serializers.CharField( validators=[EmailValidator("email format invalid")])
	      mobile = serializers.CharField( validators=[RegexValidator(r"\d+", message="number only")])
	  ```
	- Model serializer validations
		- You can set it up for more complicated validations schemas

		  ``` python
		  class BillingRecordSerializer(serializers.ModelSerializer):
		      def validate(self, attrs):
		          # Apply custom validation either here, or in the view.

		      class Meta:
		          fields = ['client', 'date', 'amount']
		          validators = [
		              UniqueForYearValidator(
		                  queryset=BlogPostItem.objects.all(),
		                  field='slug',
		                  date_field='published'
		              )
		          ]
		          extra_kwargs = {
		            'client': {'required': False},
		            'title': {'max_length': 10},
		            'phone': {'validators': [RegexValidator(r'\d+', message='phone number')]},
		  		}
		          # validators = []  # Remove a default "unique together" constraint.
		  ```
	- Validator hook
		- Put inside CustomerReportSerializer

		  ``` python
		  class CustomerReportSerializer(serializers.Serializer):
		  	def validate_phone(self, value): # validate {'phone': '02233221123', ...}
		        if len(value) < 10:
		          raise exception.ValidationError("incorrect phone number length")
		        return value
		      def validate(self, attrs): # this validate all fields
		        # api_settings.NON_FIELD_ERRORS_KEY
		  	  if len(attrs['country'] == 'AU' and len(attrs['mobile']) < 11:
		          raise exceptions.ValidationError('incorrect mobile for AU')
		  ```
	- Validation error exception will be captured in DRF and convert to error response
	- Validate a request

	  ``` python
	  class CustomerView(APIView):
	  	def post(self, request, *args, **kwargs):
	        ser = CustomerReportSerializer(data = request.data)
	        ser.is_valid(raise_exception = True)

	        modelser = CustomerReportModelSerializer(data = request.data)
	        modelser.is_valid(raise_exception = True)
	  ```
