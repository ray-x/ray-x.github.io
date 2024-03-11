---
layout: post
title: "Session Middleware of DRF"
author: "Ray"
header-style: text
tags:
    - django
    - backend
    - python
    - DRF
date: 2023-12-19
---

# Login, session and cookie

## An \*HTTP cookie\* (web cookie, browser cookie) is a small piece of data that a server sends to a user\'s web browser. The browser may store the cookie and send it back to the same server with later requests. Typically, an HTTP cookie is used to tell if two requests come from the same browser---keeping a user logged in, for example. It remembers stateful information for the [stateless](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#http_is_stateless_but_not_sessionless) HTTP protocol.

## Cookies are mainly used for three purposes:

### Session management, e.g. Logins, shopping carts, game scores, or anything else the server should remember

### Personalization, e.g. User preferences, themes, and other settings

### Tracking. Recording and analyzing user behavior

## sessions are saved on the server side while cookies are saved on the client side.

# Cross Site Request Forgery protection

## The CSRF middleware and template tag provides easy-to-use protection against [Cross Site Request Forgeries](https://www.squarefree.com/securitytips/web-developers.html#CSRF). This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their browser.

## `csrf_exempt(view)`

### This decorator marks a view as being exempt from the protection ensured by the middleware. Example:

``` python
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def my_view(request):
    return HttpResponse("Hello world")
```

## `csrf_protect(view)` {#csrf_protectview collapsed="true"}

### Decorator that provides the protection of CsrfViewMiddleware to a view. Usages:
```python
    from django.shortcuts import render
    from django.views.decorators.csrf import csrf_protect
    @csrf_protect
    def my_view(request):
        return render(request, "a_template.html", {})
```

## `requires_csrf_token(view)`

### Normally the [csrf~token~](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#std-templatetag-csrf_token) template tag will not work if CsrfViewMiddleware.process~view~ or an equivalent like csrf~protect~ has not run. The view decorator \~requires~csrftoken~\~ can be used to ensure the template tag does work.

# Session

## [django session](../assets/Django-Session_1696546798398_0.jpg)

## [session](../assets/django_login_auth.png)

## Default session setup

### setting.py
```python
    SESSION_ENGINE = 'django.contrib.sessions.backends.db' # 引擎（默认）
    # use 'django.contrib.sessions.backends.cached_db' for high traffic
    SESSION_COOKIE_NAME ＝ "sessionid" # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
    SESSION_COOKIE_PATH ＝ "/" # Session的cookie保存的路径（默认）
    SESSION_COOKIE_DOMAIN = None # Session的cookie保存的域名（默认）
    SESSION_COOKIE_SECURE = False # 是否Https传输cookie（默认）
    SESSION_COOKIE_HTTPONLY = True # 是否Session的cookie只支持http传输（默认）
    SESSION_COOKIE_AGE = 1209600 # Session的cookie失效日期（2周）（默认）
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False # 是否关闭浏览器使得Session过期（默认）
    SESSION_SAVE_EVERY_REQUEST = False # 是否每次请求都保存Session，默认修改之后才保存（默认）
```

## Cookie

    request.COOKIES[key]
    request.COOKIES.get(key)
    # 普通cookie是明文传输的，可以直接在客户端直接打开，所以需要加盐，解盐之后才能查看
    request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)

# Login HTML


``` python
{% raw %}
<div class="account">
    <h2>用户登录</h2>
    <div class="panel-body">
        <form method="post" novalidate>
            {% csrf_token %}
            <div class="form-group">
                <label>用户名</label>
                {{ form.username }}
                <span style="color: red;">{{ form.errors.username.0 }}</span>
            </div>
            <div class="form-group">
                <label>密码</label>
                {{ form.password }}
                <span style="color: red;">{{ form.errors.password.0 }}</span>
            </div>

            <button type="submit" class="btn btn-primary center-block" style="width: 80px;">登录</button>
        </form>
    </div>
</div>
{% endraw %}
```


# Login Form

``` python
from django.shortcuts import render, HttpResponse
from django import forms
from employee_management.utils.modelform import BootStrapForm
from employee_management.utils.encrypt import md5
from employee_management.models import Admin

# 使用Form来实现
class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    password = forms.CharField(
        label="用户名",
        # render_value=True 表示当提交后,如果密码输入错误,不会自动清空密码输入框的内容
        widget=forms.PasswordInput(attrs={"class": "form-control"}, ),
        required=True,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功, 获取到的用户名和密码
        # print(form.cleaned_data)
        # {'username': '123', 'password': '123'}
        # {'username': '456', 'password': '0f54af32f41a5ba8ef3a2d40cd6ccf25'}

        # 去数据库校验用户名和密码是否正确
        admin_object = Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})

        # 如果用户名密码正确
        # 网站生成随机字符创,写到用户浏览器的cookie中,再写入到服务器的session中
        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        return redirect("/admin/list/")

    return render(request, 'login.html', {"form": form})

```

# Session storage {#session-storage collapsed="true"}

## The request object has a session attribute, and when the server executes the code, the session middleware and the session's application operate together seamlessly. When you first store data in a session, Django saves the data server-side and associates it with a unique session ID. The server-side session data (object) is created when you store any data in the session and is saved either at the end of the request or when you explicitly call. The `sessionid` cookie is created client-side when you first store any data in the session.

``` sql
mysql> select * from django_session;
+----------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+
| session_key                      | session_data                                                                                    | expire_date                |
+----------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+
| zkgq26t7hqx3yu6xo04bws856002n5aj | eyJpbmZvIjp7ImlkIjoxMiwibmFtZSI6InRva2VyIn19:1pElim:Tus2mHaJUTNTfzhppuah8N0FVdLXQxyvRk_4n-4fP6g | 2023-01-23 06:33:24.373104 |
+----------------------------------+-------------------------------------------------------------------------------------------------+----------------------------+
``` sql

mysql\> select \* from django~session~;

  ---------------------------------- -------------------------------------------------------------------------------------------------- -----------------
  session~key~                       session~data~                                                                                      expire~date~

  zkgq26t7hqx3yu6xo04bws856002n5aj   eyJpbmZvIjp7ImlkIjoxMiwibmFtZSI6InRva2VyIn19:1pElim:Tus2mHaJUTNTfzhppuah8N0FVdLXQxyvRk~4n~-4fP6g   2023-01-23
                                                                                                                                        06:33:24.373104
  ---------------------------------- -------------------------------------------------------------------------------------------------- -----------------


```
# Django Middleware

## Class with `process_request` Input middleware

### if process~request~ return anything, the request will not forward to view.py, it will return the result

### if nothing return, continue with next middleware and then go to view

## `proccess_response(self, request, response)` output middleware

# Auth middleware

## middleware/auth.py

``` python
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 0.排除不需要的页面 否则容易死循环【【【
        if request.path_info == "/login/":
            return

        # 1.读取当前访问的用户的session信息,如果能读到,说明已登录过,就可以继续向后走
        info_dict = request.session.get("info")
        if info_dict:
            return

        # 2.如果没有登录信息
        return redirect("/login/")

```

## setting.py

``` python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'employee_management.middleware.auth.AuthMiddleware',
]
```

## logout

### clean session data

### view.py

``` python
def logout(request):
    """ 注销 """
    # clean session
    request.session.clear()
    return redirect("/login/")
```

