from django.contrib import admin

from .models import ( SkillLevel, Paradigm, Language, Programmer,
                        LanguageSkill, Role, RoleMember)

# Register your models here.
admin.site.register(SkillLevel)
admin.site.register(Paradigm)
admin.site.register(Language)
admin.site.register(Programmer)
admin.site.register(LanguageSkill)
admin.site.register(Role)
admin.site.register(RoleMember)
