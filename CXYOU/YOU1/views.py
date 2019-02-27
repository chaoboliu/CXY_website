from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from django.conf.urls.static import static
from django.views.generic.base import View
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
#首页
def index(request):
    banner = Banner1.objects.all()
    banner2 = Banner2.objects.all()
    blog_list = Blog.objects.order_by('-c_views').all()
    blog_li = Blog.objects.order_by('-c_views').all()[:3]
    blog_list2 = Blog.objects.order_by('-c_date').all()[:3]
    blog_list3 = Blog.objects.order_by('-c_date').all()[:4]
    ctx = {
        'blog_list': blog_list,
        'banner':banner,
        'banner2':banner2,
        'blog_li':blog_li,
        'blog_list2':blog_list2,
        'blog_list3':blog_list3

    }

    return render(request, 'index.html', ctx)

#发布文章页
def write(request):
    return render(request, 'write.html')



def yes4(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    iamge = request.FILES.get('pic', '')
    blog_id = request.POST.get('post_id')

    a = Comment_del()
    a.post = Blog.objects.get(pk=blog_id)
    a.user = title
    a.content = content
    a.iamge = iamge
    a.save()

    return redirect(reverse('/:details', args=(blog_id,)))
#文章详情页
def details(request,page):
    page = int(page)
    blog = Blog.objects.get(id=page)
    # blog.c_views += 1
    # blog.save()
    c_del = Comment_del.objects.filter(post__id=blog.id)
    # de_blog = Blog.objects.get(pk=id)

    ctx = {
        'blog': blog,
        # 'de_blog': de_blog,
        'c_del':c_del
    }
    return render(request, 'details.html', ctx)

#热门文章页
def list(request):
    blog_list = Blog.objects.order_by('-c_views').all()

    ctx = {
        'blog_list': blog_list,


    }
    return render(request, 'list.html',ctx)

#注册页
def c_login(request):
    return render(request, 'c_login.html')
#登录页
def dlu(request):
    return render(request, 'dlu.html')

#博客发布成功页
def yes(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    author = request.POST.get('author', '')
    # tags = request.POST.get('tags', '')
    flei = request.POST.get('flei', '')
    iamge = request.FILES.get('pic', '')


    a = Blog()
    a.c_title = title
    a.c_content = content
    a.c_author = author
    # a.c_tags = tags
    a.c_name = flei
    a.c_iamge = iamge
    a.save()

    return render(request, 'yes.html')


#测试上传代码
# def pic_upload(request):
#     return render(request,'pic_upload.html')
from django.conf import settings
# from django.http import HttpResponse
#
# def pic_handle(request):
#     f1=request.FILES.get('pic')
#     a = Blog()
#     a.c_iamge = f1
#     a.save()
#     return HttpResponse('OK')

#技术交流页
def luntan(request):
    cobanner = Cobanner.objects.all()
    comment = Comment.objects.order_by('-pub_date').all()
    ctx = {
        'cobanner': cobanner,
        'comment':comment

    }
    return render(request, 'luntan.html',ctx)

#提问页
def problem(request):
    return render(request, 'problem.html')

def yes2(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    iamge = request.FILES.get('pic', '')

    a = Comment()
    a.user = title
    a.content = content
    a.iamge = iamge
    a.save()
    return render(request, 'yes3.html')
#评论发布成功页
def yes3(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    iamge = request.FILES.get('pic', '')
    blog_id = request.POST.get('post_id')

    a = Comment2()
    a.post = Comment.objects.get(pk=blog_id)
    a.user = title
    a.content = content
    a.iamge = iamge
    a.save()

    return redirect(reverse('/:fplun', args=(blog_id,)))

#显示技术交流详情
def fplun(request, page):
    page = int(page)
    blog = Comment.objects.get(id=page)
    cplun = Comment2.objects.filter(post__id=blog.id)

    ctx = {
        'blog': blog,
        'cplun':cplun
    }
    return render(request, 'fplun.html',ctx)

#搜索
class SearchView(View):
    # def get(self, request):
    #     return render(request,'index.html')


    def post(self, request,pindex=1):

        qe = request.POST.get('query')
        post_list = Blog.objects.filter(Q(c_title__contains=qe) | Q(c_content__contains=qe))


        ctx = {
            'post_list': post_list,

        }
        return render(request, 'sx.html', ctx)


from json import dumps
from django.core import serializers
def music(request):
    # song = Music.objects.order_by('-c_date').all()
    ctx = {
        # 'song':json.dumps(song),

    }
    return render(request, 'music.html')

# def musicjs(request):
#     song = Music.objects.all()
#
#
#
#     return JsonResponse({"haha":[{"title":"测试","artist":"lbc","mp3":"http://img95.699pic.com/audio/960/604/662136_all.mp3","oga":"http://img95.699pic.com/audio/960/604/662136_all.mp3"},{"title":"刚刚好","artist":"薛之谦","mp3":"http://fs.w.kugou.com/201901080933/0c1a280eba99802cb4f7038facfa9e82/G075/M0A/16/09/K5QEAFdVovWAFZegAD0riCa_Rgo648.mp3","oga":"http://fs.w.kugou.com/201901080933/0c1a280eba99802cb4f7038facfa9e82/G075/M0A/16/09/K5QEAFdVovWAFZegAD0riCa_Rgo648.mp3"},{"title":"你还要我怎样","artist":"薛之谦","mp3":"http://fs.w.kugou.com/201901080932/e06b573b3f3d78c95b3982f71231214c/G014/M0B/06/14/Tg0DAFUJgsSAXfd-AEvvHDNAkmE307.mp3","oga":"http://fs.w.kugou.com/201901080932/e06b573b3f3d78c95b3982f71231214c/G014/M0B/06/14/Tg0DAFUJgsSAXfd-AEvvHDNAkmE307.mp3"},{"title":"春风十里","artist":"鹿先森乐队","mp3":"http://fs.w.kugou.com/201901080959/4e24da1ca0dec37561b78d97f97eab50/G051/M06/07/01/cw0DAFZxi8aANfHOAFvPFmufTRM235.mp3","oga":"http://fs.w.kugou.com/201901080959/4e24da1ca0dec37561b78d97f97eab50/G051/M06/07/01/cw0DAFZxi8aANfHOAFvPFmufTRM235.mp3"},{"title": "靠近一点点", "artist": "封茗囧菌", "mp3": "http://fs.w.kugou.com/201901091507/fcb4db09af4ad0c4db54f3e0bb8930e2/G067/M0A/13/1D/44YBAFe-jAWAVsZMADf8P-x7YLA182.mp3", "oga": "http://fs.w.kugou.com/201901091507/fcb4db09af4ad0c4db54f3e0bb8930e2/G067/M0A/13/1D/44YBAFe-jAWAVsZMADf8P-x7YLA182.mp3"}
# ]})



from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def musicjs(request):
    queryset = Music.objects.all()
    # 转换成python中的列表
    data = []
    for i in queryset:
        # 每一个对象都手动转化成一个字典
        p_tmp = {
            'title': i.title,
            'artist': i.twotitle,
            'mp3':i.link_url,
            'oga':i.link_url2,

        }
        # a={"haha":[data.append(p_tmp)]}
        data.append(p_tmp)

    import json

    return HttpResponse(json.dumps({"haha":data}), content_type='application/json')
