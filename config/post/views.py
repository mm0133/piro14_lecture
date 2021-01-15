from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, Comment


def post_list(request):
    posts=Post.objects.all()
    ctx={"Tposts":posts}
    return render(request, template_name='post/post_list.html', context=ctx)


def post_detail(request, pk):
    post=Post.objects.get(pk=pk)
    comments=Comment.objects.filter(post=post)
    #comments=Comment.objects.filter(Post_id=pk)
    ctx={"Tpost":post, "Tcomments":comments}
    return render(request, template_name='post/post_detail.html', context=ctx)


def post_create(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            new_Post=Post.objects.create(
                title=request.POST.get("Vtitle"),
                content=request.POST.get("Vcontent"),
                writer=request.user
            )
            new_pk=new_Post.pk
            return redirect('post:Udetail', pk=new_pk)
        else:
            return HttpResponse('로그인 필요!')
    else:
        return render(request, "post/post_create.html")


def post_delete(request, dpk):
    if request.method == "POST":
        post = Post.objects.get(id=dpk)
        if request.user ==post.writer:
            post.delete()
            return redirect('post:Ulist')
        else:
            return HttpResponse('자기글만 삭제 가능')
    else:
        return HttpResponse(' 해당 url은 post요청만 받음')



def comment_create(request, pk):
    if request.method == "POST":
        if request.user.is_authenticated:
            post=Post.objects.get(pk=pk)
            new_comment=Comment()
            new_comment.writer=request.user
            new_comment.content=request.POST.get("Vcocontent")
            new_comment.post=post
            new_comment.save()
            return redirect('post:Udetail', pk=pk)
        else:
            return HttpResponse('로그인 필요!')
    else:
        return HttpResponse(' 해당 url은 post요청만 받음')


