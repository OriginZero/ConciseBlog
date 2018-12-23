from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class BlogType(models.Model):
    type_name = models.CharField(u'博客类型', max_length=10)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    # 博客标题
    title = models.CharField(u'标题', max_length=50)
    # 博客类型
    # type_blog = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    type_blog = models.ManyToManyField(BlogType, blank=True)
    # 博客内容
    content = RichTextField(u'内容')
    # 博客作者
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # 博客图片
    ImgFile = models.ImageField(upload_to='photo', null=False, blank=True)
    # 创建时间
    create_time = models.DateTimeField(
        u'发表时间', auto_now_add=True, editable=True)
    # 最后修改时间
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-update_time']
