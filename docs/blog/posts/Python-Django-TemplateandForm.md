---
layout: post
title: "Template and Form of DRF"
author: "Ray"
header-style: text
tags:
    - django
    - backend
    - python
    - DRF
date: 2023-12-19
---

# reference

## Django REST API

### \| Udemy\]\]

# KickStart

## manage.py command line

### runserver

### makemigrations

1.  create a new migration plan

### migrate

### createsuperuser

### startapp

1.  create a new app/rest API

### shell

### help

## /admin URL for admin user

## A django APP

### An app in a Django project is a Python package that does a particular job. A Django project contains one or more apps and each of them handles a particular task. For example, a Django blog website will have a list of posts, user authentication, user profiles, etc. The best practice is to create different apps for each one of them.

### Apps are meant to be portable and can be shared between different projects. For example, a Django e-commerce website and a Django blog website both will have user authentication. You can make a single app for user authentication and share it between different Django projects.

### create a new APP

``` bash
python manage.py startapp [app name]
```

## Project structure

### [project structure](https://miro.medium.com/max/700/1*aICZBUzrgLgc5GoWuiFHcw.jpeg)

### `manage.py~ file provides a command-line utility for a Django project.
*** ~asgi~ stands for *Asynchronous Server Gateway Interface* and ~wsgi` stands for \*Web Server Gateway Interface.\*

1.  After your development process is completed, you will move to
    production and hosting. For hosting you will
    use \~asgi\~ or \~wsgi\~ compatible servers. According to the type
    of server you use, you have to import middleware accordingly.

2.  \~asgi.py\~ enables ASGI compatible servers and \~wsgi.py\~ enables
    WSGI compatible servers to serve your Django web app.

### settings.py

1.  This is the main configuration file for a Django project. This is
    the main settings file and here you will configure all the apps and
    middleware for your project.

2.  This file also handles the database settings. By default Django uses
    sqlite3. But if you use a different database, which you will most
    probably do, you will configure it in \~settings.py\~.

3.  \~settings.py\~ also handles templates, static files, and media
    files related settings.

### urls.py

1.  URLs are different endpoints of your website. \~urls.py\~ contains
    the URL configurations for your website. By
    default, \~urls.py\~ comes with the URL pattern for the admin panel.
    You will create other endpoints for your web app in this file.

### Inside your APP

1.  admin.py

    1.  This file is used to register the models in your app in the
        Django administration. You will use this file to display the
        models of your app in the admin panel.

    2.  e.g. register article

        ``` python
        from django.contrib import admin
        from .models import Article

        # Register article models here.
        admin.site.register(Article)
        ```

2.  app.py

    1.  It is a common configuration file for all Django apps. You can
        configure the attributes for your app using this file. However,
        the default configuration is sufficient for most cases. So,
        adding app configuration is a rare case.

3.  \~migrations\~ folder

    1.  Once you start making changes in your database,
        the \~migrations\~ folder will be populated with the records for
        all those migrations.

4.  models.py

5.  You create your models in this
    file. [Models](https://docs.djangoproject.com/en/3.2/topics/db/models/) define
    the database structure of your app. In \~models.py\~ you basically
    create database tables for your app with proper relationships using
    Python classes.

6.  \~models.py\~ is one of the most important files in your app. Django
    follows the MVT (Model-View-Template) design architecture. The \'M\'
    represents models. So, models are one of the basic components of a
    Django app.

7.  views.py

    1.  is another important
        file. [Views](https://docs.djangoproject.com/en/3.2/topics/http/views/) are
        the \'V\' of MVT. Views provide an interface through which users
        interact with a Django website. It connects models and templates
        together.

    2.  In this file, you write the business logic for your app. A view
        can be either function-based or class-based. You decide if you
        want to write your views using functions or classes.

    3.  You can learn more about the MVT architecture from this article:

    4.  [The MVT Design Pattern of
        Django](https://python.plainenglish.io/the-mvt-design-pattern-of-django-8fd47c61f582)

8.  tests.py

    1.  is where you write test codes for your app. It is used to test
        the overall working of a Django app.

### Other folder/files

1.  Templates

    1.  django **MVT** \*T\*emplate

    2.  each app can have own template and the search sequence is
        defined same as how different app is loaded

2.  static

    1.  css, js, images, json..

    2.  `{% raw %}{% load static %}{% endraw %}` to load static files 👍

    3.  `{% raw %}{% static  'css/bootstrap.css' %}{% endraw %}` to refer to those files

3.  urls.py in app

    1.  if your application is complex, use a dedicatd url.py

4.  forms.py

    1.  If your website expects to receive user inputs you need to
        use [forms](https://docs.djangoproject.com/en/3.2/topics/forms/).
        To work with forms in an app you need to create the `forms.py`
        file in that app. Here you will write the codes to handle forms.

## Request and response [Request & Response 4.2](https://docs.djangoproject.com/en/4.2/ref/request-response/)

### Requests

1.  method, GET, POST (used for form submit)， META

2.  Query parameters `/query/?id=123` #card

    1.  request.Get.get(\'id\')

        ``` html
        <form>
        <input type="text" name="id" value = "{{search_data}}">
        <button type="submit">search</button>
        </form>
        ```

### Reponse

1.  HttpResponse; render; redirect

# Models

## Default and AutoField

### BigAutoField(64bit) and AutoField

### app.py set default auto field

``` python
default_auto_field = "django.db.models.BigAutoField"
```

1.  if default~autofield~ present, each table will have `id` and you do
    not need to define aut-inc auto field

## ForeignKey and auto join

### define a foreigh key relationship #card

``` python
depart = models.ForeignKey(
  "Department",
  on_delete=models.CASCADE
xx)
# table "Department", to_field='id'
# if 'id' is default (auto_field) to_field can be ignore
```

#card

1.  `django` will append `id` and create `depart_id` automatically from
    `depart` for foreign key #magic

2.  `on_delete` should be specified. Normally `CASCADE`, can also be
    `SET_NULL` if it is nullable

### AutoJoin

1.  Instead of join two table to get info from 2nd table like this

    ``` python
    user = model.User.objects.filter(id=1).first()
    user_depart = models.Department.objects.filter(id=user.depart_id).first()
    ```

    Django know how two table are associated and We can dereference
    department info with `depart` field directly without
    `filter(id=user.depart_id)`

    ``` python
    print(user.depart.id)
    print(user.depart.name)
    ```

## enum with `choices`

### define with `{field_name}_choices`

``` python
gender_choices = ( (1,"Male"),(2,"Female") )
gender = models.SmallIntegerField(choices=gender_choices,default=1)
```

### when retrieve gender value, it will be 1/2. But it can be display nicely with #magic method `models.get_{field_name}_display()` e.g. `get_gender_display()` will show `Male|Female`

## `order_by()`

### `order_by("field_name")`

### reverse order with `order_by("-field_name")`

**\*** **\***

## `filter()` with magic naming

### filter with field and value (field name : myid in all examples )

### Number filter

1.  `filter(myid__gt=12)` -\> value \>12, You can also filter on
    `myid__lte` `myid_lt` etc

### String filter

1.  `mytext__startwith`, `mytext__endwith`, `mytext__contains`

### Multi field filter : `filter(myid_gte=12, mytext_contains="123")`

## pagination

**\***

# Django Template

## Abstract

### A template is a text file. It can generate any text-based format (HTML, XML, CSV, etc.).

### A template contains \*variables\*, which get replaced with values when the template is evaluated, and \*tags\*, which control the logic of the template.

## -----

### :main-idea-checkbox:

-   What is this aims?
-   What is the their research question?
-   What is the author arguing?
-   What is their answer to the question?
-   What points support their argument?
-   What are their main reasons?
-   What evidence have they used to support their argument?
-   What's the significance of these facts?
-   What principle are they based on?
-   How can I apply them?  How do they fit in with what I already know?
-   What's beyond them?
-   What\'re supporting details and explanations?

::: {.END .drawer}
:::

### Cheatsheet

``` python
render(request, 'template_file.html', {"var1": value, "var2", value})
```

``` django
{{ var1 }}
{{ listVar.1 }} <!-- listVar[0] -->
{% raw %}{% for item in lst %}{% endraw %}  <!-- loop list -->
<span> {{ item }} </span>
{% raw %}{% endfor %}{% endraw %}

<span> {{ dict }} </span> <!-- object  -->
<span> {{ dict.name }} </span> <!-- object attribute -->

{{ list.1.name }}  <!-- list[1].name
```

Loop and condition

``` django
{% raw %}{% for item in dict.keys %}{% endraw %}  <!-- loop object  -->
<span> {{ item }} </span>
{% raw %}{% endfor %}{% endraw %}

{% raw %}{% for k, v in dict.items %}{% endraw %}  <!-- loop object  -->
<span> {{ k }} = {{ v }} </span>
{% raw %}{% endfor %}{% endraw %}

{% raw %}{% if n == 'xxx' %}{% endraw %}
<h1> xxxx </h1>
{% raw %}{% elif n == "XXX" %}{% endraw %}
<h1> XXX </h1>
{% raw %}{% else %}{% endraw %}
<h1> ssss </h1>
{% raw %}{% endif %}{% endraw %}
```

### Template tags `{% raw %}{% ... %}{% endraw %}` generally do not require double curly braces or quotes for variable names, as they inherently expect Python-like syntax.

### `value="{{ title|default:'depart name' }}"` or `value={{ title|default:'depart name' }}`

1.  double quotes is strongly recommended

### Call a function inside `{{}}` or `{% raw %}{% %}{% endraw %}`

1.  `{{ obj.get_gender_display() }}` is invalid. You can not call a
    function with `()` inside `{{}}`, use `{{ obj.get_gender_display }}`
    instead

2.  How about arguments? see ((651c1c60-a6bd-47c4-9b9a-889f3d41cf5f))

## Template extends

### `extends` tag is used for inheritance of templates in django. One needs to repeat the same code again and again. Using extends we can inherit templates as well as variables.

### syntax

``` html
{% raw %}{% extends 'template_name.html' %}{% endraw %}

# examples
{% raw %}{% extends "./base2.html" %}{% endraw %}
{% raw %}{% extends "../base1.html" %}{% endraw %}
{% raw %}{% extends "./my/base3.html" %}{% endraw %}
```

### extends examples

1.  template.html

    ``` django
    <h1>Main Template</h1>
    {% raw %}{% block content %}{% endraw %}
    {% raw %}{% endblock %}{% endraw %}
    ```

2.  extends.html overwrite block: content

    ``` django
    {% raw %}{% extends "template.html" %}{% endraw %}

    {% raw %}{% block content %}{% endraw %}
    <h2> GeeksForGeeks is the Best
    {% raw %}{% endblock %}{% endraw %}

    ```

3.  block can extends anything, e.g css reference, js code blocks etc

## pipe operator `|` and filter

### In Django template language, the pipe character `|` is used to apply filters to variables. Filters are used to format variables or perform some operation on them before they are rendered in the template.

### Syntax

``` django
{{ variable|filter_name:"argument" }}
Sample:
{{ my_list|join:", "|escape }}
```

1.  `|join:", "`: The `join` filter concatenates items in the list into
    a single string, using \~, \~(comma and space) as a separator.

### As function call with parameter is not allowed inside template, do this instead

``` django
<td class="py-2 px-4">{{ obj.create_time.strftime('%Y-%m-%d') }}</td>
Should be write as
<td class="py-2 px-4">{{ obj.create_time | date:'Y-m-d' }}</td>
```

## include another template file

### top.html

``` html
<div class = '{{ mycss }}'> this is header </div>
```

### index.html

``` django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

{% raw %}{% include 'top.html' with mycss="acss" %}{% endraw %}

<h2> 网页body部分 </h2>

</body>
</html>
```

### include passing multiple values

``` django
{% raw %}{% include "name_snippet.html" with person="Jane" greeting="Hello" %}{% endraw %}
```

And with django variables from python codes

``` django
{% raw %}{% extends 'base.html' %}{% endraw %}

{% raw %}{% block panel %}{% endraw %}
{% raw %}{% include 'form.html' with title=title id=id %}{% endraw %}
{% raw %}{% endblock %}{% endraw %}
```

# Form

## Django's form functionality can simplify and automate vast portions of this work, and can also do it more securely than most programmers would be able to do in code they wrote themselves.

### Django handles three distinct parts of the work involved in forms:

### preparing and restructuring data to make it ready for rendering

### creating HTML forms for the data

### receiving and processing submitted forms and data from the client

### [flowChart-1](https://media.geeksforgeeks.org/wp-content/uploads/20200107124202/flowChart-1-1024x682.png)

## Create a form

### How to create a FormClass #card

1.  Sample

    ``` python
    from django import forms

    class FormName(forms.Form):
             # each field would be mapped as an input field in HTML
            field_name = forms.Field(**options)
    ```

    #card #card

### Form class sample

``` python
from django import forms

class InputForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                    help_text = "Enter 6 digit roll number"
                    )
    password = forms.CharField(widget = forms.PasswordInput())

```

1.  Note if field defined as `auto` (`auto_now`, `auto_now_add`), it may
    not shown in Form

### Form view.py

``` python
from django.shortcuts import render
from .forms import InputForm
def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)
```

### Render in template

1.  A form comes with 3 in-built methods that can be used to render
    Django form fields.

2.  [`{{ form.as_table }}`](https://www.geeksforgeeks.org/form-as_table-render-django-forms-as-table/) will
    render them as table cells wrapped in \<tr\> tags

3.  [`{{ form.as_p }}`](https://www.geeksforgeeks.org/form-as_p-render-django-forms-as-paragraph/) will
    render them wrapped in \<p\> tags

4.  [`{{ form.as_ul }}`](https://www.geeksforgeeks.org/form-as_ul-render-django-forms-as-list/) will
    render them wrapped in \<li\> tags

### Template:

There are a few ways to present form objects

-   Field by field

``` python
<form action = "" method = "post">
    {{ form.first_name }}
    {{ form.last_name }}
    {{ form.phone_number }}
    <input type="submit" value=Submit">
</form>
```

-   Loop

``` django
<form action = "" method = "post">
    {% raw %}{% csrf_token %}{% endraw %}
    {% raw %}{% for field in form %}{% endraw %}
    {{ field }}
    {% raw %}{% endfor %}{% endraw %}
    <input type="submit" value=Submit">
</form>
```

-   `{{ form }}`

``` django
<form action = "" method = "post">
    {% raw %}{% csrf_token %}{% endraw %}
    {{ form }}
    <input type="submit" value=Submit">
</form>
```

## Validate a form object

### The easiest way to validate a single field is to override the method `clean_<fieldname>()` for the field you want to check. e.g. Validate `renewal_date` field

``` python
import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

```

## Django Form from Models

### If the form is coupled with database table, it is easy to use ModelForm

### Models

1.  Sample:

    ``` python
    from django.db import models
    class Movie(models.Model):
        movie_title = models.CharField(max_length=150)
        release_year = models.IntegerField()
        director = models.CharField(max_length=100)
        movie_poster = models.ImageField(upload_to='images/', None=True)
        movie_plot = models.TextField()
        def __str__(self):
            return self.movie_title  # when print movie object it shows title. Also useful
            #when movie object is showed in dropdown etc
    ```

2.  FieldValidator

    1.  `django.core.validators`

        ``` python
        mobile = forms.CharField(label = "mobile number"
            validators=[RegexValidator(r'^159[0-9]+$', 'mobile start with 159') ],
        )
        ```

3.  A **disabled** field

    1.  For read only field set `disabled=True`, e.g.
        `mobile = forms.CharField(disabled=True, label='mobile number')`

### Create ModelForm class

1.  How to create a ModelForm Class #card

    1.  Code

        ``` python
        from django import forms
        from .models import Movie

        class MovieForm(forms.ModelForm):
            class Meta:
                model = Movie
                fields = ('movie_title', 'release_year', 'director', 'movie_poster', 'movie_plot')
        ```

2.  Sample

    ``` python
    from django import forms
    from .models import Movie


    # Create your forms here.
    class MovieForm(forms.ModelForm):

        class Meta:
            model = Movie
            fields = ('movie_title', 'release_year', 'director', 'movie_poster', 'movie_plot')
    ```

3.  The `Meta` class is used to change the behavior of the `ModelForm` .
    Within it, specify the model your fields come from and the fields
    you want to use from that model.

4.  Key components of `Meta` class in ModelForm #card

    1.  model the data model class

    2.  fields: the fields will be shown in the form

    3.  widgets: used to generate HTML code that override default
        behavior. e.g. inputbox with CSS styling

5.  Explains of Meta class

    -   `model` The Model class
    -   `fields` It is strongly recommended that you explicitly set all
        fields that should be edited in the form using the fields
        attribute. Failure to do so can easily lead to security problems
        when a form unexpectedly allows a user to set certain fields,
        especially when new fields are added to a model. If those are
        not your concerns \~fields = \"[[all]{.underline}]{.underline}\"
        \~ can easy your job
    -   `exclude` Set the exclude attribute of the ModelForm's inner
        Meta class to a list of fields to be excluded from the form.

    ``` python
    class PartialAuthorForm(ModelForm):
        class Meta:
            model = Author
            exclude = ['title']
    ```

    -   `field_classes` or formfield~callback~ can be used to customize
        the type of fields instantiated by the form.
    -   `widgets`: override default `forms.TextInput`, It is helpful if
        you need setup `css` e.g.

    ``` python
    class PartialAuthorForm(ModelForm):
        class Meta:
            model = Author
            exclude = ['title']
            widgets = {
                "name": forms.widgets.TextInput(attrs={"class": "form-control"}),
                "password": forms.widgets.PasswordInput(attrs={"class": "form-control"}),
                "age": forms.widgets.NumberInput(attrs={"class": "form-control"}),
                "account": forms.widgets.NumberInput(attrs={"class": "form-control"}),
                "department": forms.widgets.Select(attrs={"class": "form-control"}),
            }
    ```

    -   If you want to apply same attributes for all field, do this
        instead by override `__init__`

    ``` python
    class UserModelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for name, field in self.fields.items():
                field.widget.attrs["class"] = style
                if name == "password":
                    field.required = False  # Make the password field optional
                    field.widget = forms.widgets.PasswordInput(attrs={"class": style})
        class Meta:
            model = UserInfo
            fields = "__all__" # It can be a list of all fields you want to display
         # password field can also be setup here
         # password = forms.CharField(required=False, widget=forms.PasswordInput()) # some field need special attention
         # can also  be put here
    ```

    -   Error messages

    You can reuse the default error messages. In case the message need
    to be customered for specific field

    ``` python
    error_messages = {
          "name": {
              "required": "用户名不能为空, 并且不能重复",
          },
          "age": {
              "required": "年龄不能为空， 并且应该处于0~140",
          },
      }

    ```

6.  Add New field to ModelForm

    1.  e.g. Add password confirm input field

        ``` python
        class UserModelForm(forms.ModelForm):
          confirm_password = forms.CharField(
                label = "please input password again",
                widget = forms.PasswordInput(render_value=True)
            )
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for name, field in self.fields.items():
                    field.widget.attrs["class"] = style
                    if name == "password":
                        field.required = False  # Make the password field optional
                        field.widget = forms.widgets.PasswordInput(attrs={"class": style})
            class Meta:
                model = UserInfo
                fields = "__all__"
        ```

    2.  `render_values` allow pre-fill values

### The html template

``` django
<form method="post" enctype="multipart/form-data">
  {% raw %}{% csrf_token %}{% endraw %}
      {{movie_form}}
      <button class="btn btn-primary my-4" type="submit">Submit</button>
</form>
```

### For ((651b71c9-7e23-4638-a89c-240b474388a8)) Add `__str__`

``` python
class Department(models.Model):
    title = models.CharField(verbose_name="Department", max_length=32)
    def __str__(self):
        return self.title
```

So that when adding user\'s department in the dropdown, it will show the
`title` instead of \"Python Object\"

### Create a ModelForm object #card

1.  an empyt object (create a new entry) `form = UserModelForm()`

2.  From a POST request (for parse form submit and save data)
    `form = userModelForm(request.POST)`

3.  From database instance (foir re-edit data)
    `form = UserModelForm(instance=models.User.objects.filter(id=id).first())`

4.  From both POST and database (normally when reedit data when form
    submission failed)
    `form = UserModelForm(request.POST, instance=models.User.objects.filter(id=id).first())`

### Save ModelForm(),

1.  You can either parse the POST request and get all fields, You can
    Also do:

    ``` python
    form = UserModelForm(request.POST)  # POST to form class
    if form.is_valid():
        form.save()  # save to DB
        return redirect("/user/list/")
    # invalid data auto refill the form and you can re-send again
    return render(request, "user_add.html", {"form": form})
    ```

### Handle form errors

**\*\***

# Pagination

## with python slicing `[start:end]`

``` python
qs = models.Users.objects.all()
qs = models.Users.objects.filter(id=123)[0:10]
qs = models.Users.objects.filter(id=123)[10:20]

qs = models.Users.objects.filter(id=123).order_by('name')[0:20]
qs = models.Users.objects.filter(id=123).order_by('name')[20:40]

page = int(request.GET.get('page', 1))
qs = models.Users.objects.filter(id=123).order_by('name')[(page-1)*page_size:page*page_size]
```

## django template

``` django
<ul class='pagination'>
  <li><a href="?page=1">1</a></li>
  <li><a href="?page=2">2</a></li>
</ul>
```

## Pagination generate by python

``` python
from django.utils.safestring import mark_safe
...
total = models.Users.objects.filter(id=123).order_by('name').count()
total_pages = totla//page_size + 1
start = cur_page - 5
end = cur_page + 5
for i in range(start, end + 1):
  sel = '""'
  if i == page:
    sel = f'"active"'
  ele = f'<li class={sel} ><a href="?page={i}">{i}</a></li>'
  page_list.append(ele)
page_string=mark_safe(''.join(page_list))
return render(request, 'list.html', {"queryset": qs, "page_list": page_string})
```

## Template

``` django
<ul class="pagination">
    <li><a href="{{ head_page }}" aria-label="Previous"><span aria-hidden="true">首页</span></a></li>
    {{ page_string }}
    <li><a href="{{ end_page }}" aria-label="Next"><span aria-hidden="true">尾页</span></a></li>

</ul>
<br>

<form method="get">
    <div style="display:inline-block; width: 150px;">
        <div class="input-group">
            <span> <input type="text" class="form-control" placeholder="请输入页码" name="page"></span>
            <span class="input-group-btn">
                <button class="btn btn-primary" type="submit">跳转</button>
            </span>
        </div>
    </div>
</form>
```

# FBV and CBV

## FBV: Function based View

### sample

``` python
def my_create_view(request, pk):
  template_name = 'form.html'
  form_class = MyForm

  form = form_class

  if request.method == 'POST':
    form = form_class(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('list-view'))
  elif request.method == 'PUT':
    return ...
  return render(request, template_name, {'form': form})
# url

```

## CBV: Class based view

### use `as_view()` and internally use `dispatch()`

### Pros

1.  reuseablity by inherited another view

2.  DRY

3.  extendability

### Cons

1.  Implicit code flow

2.  decorators require extra override

### sample

``` python
class MyCreateView(View):
  template_name = 'form.html'
  form_class = MyForm

  def get(self, request, *args, **kwargs):
    form = self.form_class
    return render(request, template_name, {'form': form})

  def post(self, request, *args, **kwargs):
    form = self.form_class(request.POST)
    if form.is_valid():
      form.save()
      return HttpResonseRedirect(reverse('list-view'))
    else:
      return render(request, self.template_name, {'form': form})
# URL
urlpatterns = [
    url(r'^new/$', MyCreateView.as_view(), name='original-create-view')
    url(r'^new_two/$', MyCreateView.as_view(template_name='other_form.html', form_class='MyOtherForm'), name='modified-create-view')
  ]
```

## Django's views requirements:

### callable. CBV has `as_view()`

### accept `HttpRequest` as first positional argument

### return `HttpResponse` or raise exception

## reference: [Django : Class Based Views vs Function Based Views \| by Sarthak Kumar \| Medium](https://medium.com/@ksarthak4ever/django-class-based-views-vs-function-based-view-e74b47b2e41b)

## which should you use

[what type of view should
use](https://miro.medium.com/v2/resize:fit:1400/1*1NgVsYmmLCiwXUy-uE0VLA.jpeg)

### If it is single method (e.g. Get only) use FBV otherwise CBV
