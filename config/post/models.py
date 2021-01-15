from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    writer= models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content=models.TextField()
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)

# Create your models here.

# #이 뒤부터는 오늘 시간상 구현 못할것 같지만 모델만 짜보도록 하겠습니다.
# # class Profile(models.Model):
# #     user=models.OneToOneField(User, related_name='userProfile')
# #     bookmarkPost=models.ManyToManyField(Post, related_name='bookmarkProfiles')
# #
# #
# #
# #
# # #위 아래 서로 같음 유저 id가 1인 유저의 프로필을 만듬
# # Profile.objects.create(user_id=1)
# # /
# # user1=User.objects.get(id=1)
# # Profile.objects.create(user=user1)
# #
# #
# #
# # profile=Profile.objects.get(pk=3)#프로파일 pk 가 3인 오브젝트를 가져옴
# # profile.user.username# 해당 프로파일을 갖는 유저의 유저네임
# # profile.user.email# 해당 프로파일을 갖는 유저의 이메일
# #
# #
# # post1=Profile.objects.get(pk=1)
# # post2=Profile.objects.get(pk=2)
# # user1=User.objects.get(pk=1)
# # user1.userProfile.bookmarkPost.add(post1, post2) -> id가 1인 유저의 프로필에 ManytoMany 필드 추가 방법
# #
# #
# # profile1=Profile.objects.get(pk=1)#
# # profile1.bookmarkPost.all() -> 해당 프로필이 가지고있는 북마크를 전부 가져옴
# # profile1.bookmarkPost.count() -> 해당 프로필이 가지고 있는 북마크 갯수
# # profile1.bookmarkPost.filter(writer=request.user) -> 해당프로필의 북마크 글 중에서 자기자신이 쓴 글 찾기  view함수 내에서만 사용
# # profile1.bookmarkPost.filter(writer__username='admin1', title__contains='킁')-> 북마크글중 유저네임이'admin1'이고 제목에'킁'을 포함하는 글
# #
# # post1=Post.objects.get(pk=1)
# # post1.bookmarkProfiles.all() -> 글1번을 북마크하고있는 프로필을 전부가져옴
# # post1.bookmarkProfiles.count() -> 글1 번을 북마크하고있는 프로필의 수