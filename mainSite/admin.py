from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(Users)
admin.site.register(Candidates)
admin.site.register(Votes)
admin.site.register(ChallengeStrings)
admin.site.register(PublicKeys)
admin.site.register(UploadedDocuments)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Agenda)
admin.site.register(CommentLikes)
admin.site.register(GlobalVariables)