from django.db import models

# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField

#轮播图
class Banner1(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题1')
    twotitle = models.CharField(max_length=100,verbose_name='标题2')
    threetitle = models.CharField(max_length=100,verbose_name='标题3')
    cover = models.ImageField(upload_to='static/img/',verbose_name='轮播图')
    link_url = models.URLField(max_length=1000,verbose_name='图片链接')
    idx = models.IntegerField('索引')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '轮播图1'
        verbose_name_plural = '轮播图1'

class Banner2(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    twotitle = models.CharField(max_length=50,verbose_name='标题2')
    cover = models.ImageField(upload_to='static/img/',verbose_name='轮播图')
    link_url = models.URLField(max_length=100,verbose_name='图片链接')
    idx = models.IntegerField('索引')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '轮播图2'
        verbose_name_plural = '轮播图2'

#标签
class Tags(models.Model):
    b_tags = models.CharField(max_length=100,verbose_name='标签')
    def __str__(self):
        return self.b_tags
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

# 文章分类
# class Pcategory(models.Model):
#     c_name = models.CharField(max_length=200,verbose_name='博客分类')
#     is_delete = models.BooleanField(default=False)
#     def __str__(self):
#         return self.c_name
#     class Meta:
#         verbose_name = '文章分类'
#         verbose_name_plural = '文章分类'

#文章创作
class Blog(models.Model):
    c_title = models.CharField(max_length=100,verbose_name='博客标题')
    c_content = RichTextUploadingField()
    c_views = models.IntegerField(default=0,verbose_name='浏览量')
    c_date = models.DateTimeField(auto_now=True,verbose_name='创建时间')
    c_author = models.CharField(max_length=30,verbose_name='作者')
    c_likes = models.IntegerField(default=100,verbose_name='点赞量')
    c_tags = models.ManyToManyField(Tags,verbose_name='标签')
    c_iamge = models.ImageField(upload_to='static/img')
    is_recommend = models.BooleanField(default=False,verbose_name='是否推荐')
    is_delete = models.BooleanField(default=False,verbose_name='是否删除')
    c_name = models.CharField(max_length=200,verbose_name='博客分类')

    class Meta():
        verbose_name = '文章创作'
        verbose_name_plural = '文章创作'

    def __str__(self):
        return self.c_title



class Cobanner(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    cover = models.ImageField(upload_to='static/img/',verbose_name='轮播图')
    link_url = models.URLField(max_length=100,verbose_name='图片链接')
    idx = models.IntegerField('索引')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '技术交流轮播'
        verbose_name_plural = '技术交流轮播'


#非用户提问
class Comment(models.Model):
    user = models.CharField(max_length=100, verbose_name='非用户匿名')
    iamge = models.ImageField(upload_to='static/img')
    pub_date = models.DateTimeField(auto_now=True,verbose_name='发布时间')
    content = RichTextUploadingField()

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

#非用户发表评论
class Comment2(models.Model):
    post = models.ForeignKey(Comment, verbose_name='提问')
    user = models.CharField(max_length=100, verbose_name='非用户匿名')
    iamge = models.ImageField(upload_to='static/img')
    pub_date = models.DateTimeField(auto_now=True,verbose_name='发布时间')
    content = RichTextUploadingField()

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = '评论2'
        verbose_name_plural = '评论2'

#文章详情评论
class Comment_del(models.Model):
    post = models.ForeignKey(Blog, verbose_name='文章详情评论')
    user = models.CharField(max_length=100, verbose_name='非用户匿名')
    iamge = models.ImageField(upload_to='static/img')
    pub_date = models.DateTimeField(auto_now=True,verbose_name='发布时间')
    content = RichTextUploadingField()

    def __str__(self):
        return self.content
    class Meta:
        verbose_name = '文章详情评论'
        verbose_name_plural = '文章详情评论'

class Music(models.Model):
    title = models.CharField(max_length=100, verbose_name='歌名')
    twotitle = models.CharField(max_length=100, verbose_name='歌手')
    link_url = models.URLField(max_length=1000, verbose_name='mp3链接')
    link_url2 = models.URLField(max_length=1000, verbose_name='ogg链接')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '音乐上传'
        verbose_name_plural = '音乐上传'