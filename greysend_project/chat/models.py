from django.db import models
from django.contrib.auth.models import User
from accounts.models import AccountUser

#users
    # Require Richie to replace User model here with custom user model
class ChatUser (models.Model):
    User = models.OneToOneField(
        AccountUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    profile_url = models.CharField(max_length=100)
    date_of_birth = models.DateField()

#convos and msgs
class Conversation(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='created_conversations')
    is_archived = models.BooleanField()
    admin_id = models.ForeignKey(ChatUser, on_delete=models.CASCADE, related_name='admin_conversations')

    ##new columns
    updated_at = models.DateTimeField()
    is_group = models.BooleanField()
    is_public = models.BooleanField()
    is_muted = models.BooleanField()
    is_read = models.BooleanField()
    is_typing = models.BooleanField()


class ConversationHasUser(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(ChatUser, on_delete=models.CASCADE)

class Message(models.Model):
    text = models.CharField(max_length=100)
    sent_time = models.DateTimeField()
    read_time= models.DateTimeField()   
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender_id= models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    is_deleted= models.BooleanField()
    deleted_time= models.DateTimeField()

    #new columns
    is_edited= models.BooleanField()

#tags
class Tag(models.Model):
    text = models.CharField(max_length=100)
    creator_id = models.ForeignKey(ChatUser, on_delete=models.CASCADE, null=True)
    #"global" renamed as "is_system"
    is_system = models.BooleanField()

class ConversationHasTag(models.Model):
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Emoji (models.Model):
    image_url = models.CharField(max_length=100)


#emojis
class MessageHasReacji(models.Model):
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE)
    emoji_id = models.ForeignKey(Emoji, on_delete=models.CASCADE)
    user_id = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    placed_at = models.DateTimeField()

    