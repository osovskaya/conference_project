from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class Conference(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class MyUserManager(BaseUserManager):
    def create_user(self, username, name, image='', company=None, password=None):

        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=self.normalize_email(username),
            name=name,
            image=image,
            company=company,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, name):
        user = self.create_user(
            username,
            password=password,
            name=name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(max_length=50, unique=True,)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    conference = models.ManyToManyField(Conference)
    company = models.ForeignKey('self', null=True, blank=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', ]

    class Meta():
        permissions = (
            ('view_sponsors', 'Can view sponsors list'),
            ('add_representative', 'Can add representative'),
        )

    def get_full_name(self):
        return self.get_username()

    def get_short_name(self):
        return self.get_username()

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Speaker(models.Model):  # one to many
    speaker = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)


class Message(models.Model):  # one to many
    sender = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='sender')
    recipient = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name='recipient')
    conference = models.ForeignKey(Conference, on_delete=models.DO_NOTHING)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
