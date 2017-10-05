开启一个项目
`django-admin startproject mysite`

数据库 settings.py 
```py
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pynewtest',    ## 数据库名称
        'USER': 'root',
        'PASSWORD': '123654Ab',    ## 安装 mysql 数据库时，输入的 root 用户的密码
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


TIME_ZONE = 'Asia/Shanghai'
```

创建数据表
`python manage.py migrate`

    如果报错
    ```
    import MySQLdb as Database
    ModuleNotFoundError: No module named 'MySQLdb'
    ```
    则 pip install mysqlclient
    ref: https://github.com/PyMySQL/mysqlclient-python



运行服务器
`python manage.py runserver [8000]`

创建模型
`python manage.py startapp qaa`

新建模型类 qaa/models.py
```py
from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

激活模型 mysite/settings.py
```py
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'qaa',
)
```

检查更新
`python manage.py makemigrations qaa`
`python manage.py sqlmigrate qaa 0001`

修改你的模型（在models.py文件中）。
运行python manage.py makemigrations ，为这些修改创建迁移文件
运行python manage.py migrate ，将这些改变更新到数据库中。


启动 shell 玩转 API
`python manage.py shell`
```python
from qaa.models import Question, Choice
Question.objects.all()
Question.objects.filter(id=1)
Question.objects.get(pk=1)
```

后台管理
1. 启动
`python manage.py createsuperuser`
`python manage.py runserver`
http://localhost:8000/admin/
2. 添加模块
qaa/admin.py
```python
from django.contrib import admin
from .models import Question
class QuestionAdmin(admin.ModelAdmin):
  list_display = ('q_id', 'short', 'content') # 列表输出项
admin.site.register(Question, QuestionAdmin) # 注册
```

URL 与视图
qaa/views.py
```py
from django.http import HttpResponse
from .models import Question
def questions(request):
  questions = Question.objects.all()
  output = ', '.join(p.content for p in questions)
  return HttpResponse(output)
```
qaa/urls.py
```py
from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^questions$', views.questions),
]
```
mysite/urls.py
```py
    url(r'^qaa/', include('qaa.urls')),
```


问题：
postman CSRF错误：
设定Headers里的 X-CSRFToken 和 Cookie，值可以参考任意网页 get 请求发送数据



http://python.usyiyi.cn/translate/django_182/intro/tutorial01.html

http://blog.csdn.net/SVALBARDKSY/article/details/50548073

https://eliyar.biz/django_api_design/