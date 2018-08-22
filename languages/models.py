from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class SkillLevel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    #paradigm = models.CharField(max_length=50)
    paradigm = models.ForeignKey( Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Programmer(models.Model):
    name = models.CharField(max_length=50)
    #languages = models.ManyToManyField(Language)
    language = models.ManyToManyField(Language, through='LanguageSkill')

    def __str__(self):
        return self.name


class LanguageSkill(models.Model):
    level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('programmer','language'),)

    def __str__(self):
        return str(self.programmer) + "-" + str(self.language)


class Role(models.Model):
    name = models.CharField(max_length=20)
    member = models.ManyToManyField( User, through='RoleMember')

    def __str__(self):
        return self.name


class RoleMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey( Role, on_delete=models.CASCADE)
    # define other fields

    class Meta:
        unique_together = (('user','role'),)

    def __str__(self):
        return str(self.user) + "-" + str(self.role)
