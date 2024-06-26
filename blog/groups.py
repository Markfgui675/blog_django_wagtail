from django.contrib.auth.models import Group, User

def addGroup(user: User, group: Group):
    user.groups.add(group)

def addModeratorGroup(user: User):
    user.groups.add(Group.objects.filter(name='Moderador').first())

def addEditorGroup(user: User):
    user.groups.add(Group.objects.filter(name='Editor').first())
