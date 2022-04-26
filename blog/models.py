from django.db import models
# from simpledjangoblog.user.models import user as BLOGGER
from user.models import userDetail as BLOGGER

# Create your models here.
class cmtDetail(models.Model):
    commentID = models.CharField(max_length=4)
    cmtText = models.TextField()
    commenter = models.ForeignKey(BLOGGER, on_delete=models.CASCADE)

class blogDetail(models.Model):
    blogID = models.CharField(max_length=4)
    ownerUserID = models.ForeignKey(BLOGGER, on_delete=models.CASCADE)
    comments = models.ForeignKey(cmtDetail, on_delete=models.CASCADE)


