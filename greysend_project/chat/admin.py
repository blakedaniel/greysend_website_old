from django.contrib import admin
from .models import ChatUser, Conversation, ConversationHasUser, Message, Tag, ConversationHasTag, Emoji, MessageHasReacji

# Register your models here.
admin.site.register(ChatUser)
admin.site.register(Conversation)
admin.site.register(ConversationHasUser)
admin.site.register(Message)
admin.site.register(Tag)
admin.site.register(ConversationHasTag)
admin.site.register(Emoji)
admin.site.register(MessageHasReacji)
