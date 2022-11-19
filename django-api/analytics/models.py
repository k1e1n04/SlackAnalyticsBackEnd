from django.db import models
from django.db.models import Q
import analytics.process.gettime as gettime
one_week_ago = gettime.get_diff_days_ago(7)
two_week_ago = gettime.get_diff_days_ago(14)
# Create your models here.

class Organization(models.Model):
    name = models.CharField(verbose_name="団体名",max_length=100,unique=True)
    slack_app_token = models.CharField(verbose_name="SlackAppToken",max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 


class Base(models.Model):
    name = models.CharField(verbose_name="拠点",max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name='団体',
        default=1,
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "organization"],
                name="name_organization_unique"
            ),
        ]
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(verbose_name="部署",max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    base = models.ForeignKey(
        Base,
        on_delete=models.PROTECT,
        verbose_name='拠点',
    )
    
    def __str__(self):
        return self.name   

class Channel(models.Model):
    name = models.CharField(verbose_name="チャンネル",max_length=50)
    channel_id = models.CharField(verbose_name="チャンネルID",max_length=50,default="",unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        verbose_name='部署',
        default="",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(verbose_name="名前",max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slack_id = models.CharField(verbose_name="SlackID",max_length=30,unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        verbose_name='部署',
    )
    

    def __str__(self):
        return self.name


class Post(models.Model):
    channel = models.ForeignKey(
        Channel,
        on_delete=models.PROTECT,
        verbose_name='チャンネル',
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name='メンバー',
    )
    base = models.ForeignKey(
        Base,
        on_delete=models.PROTECT,
        verbose_name='拠点',
        default="",
    )
    created_at = models.DateTimeField(verbose_name="投稿日時")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["channel", "created_at","employee"],
                name="channel_date_employee_unique"
            ),
        ]
    def __str__(self):
        return self.channel.name
# Create your models here.
