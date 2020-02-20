from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)


class UserManager(BaseUserManager):
    # 이쪽이 기본 user생성을 커스텀한 부분 create user 명령은 마지막에 이쪽에 도달
    # def create_user(self, user_id, email, date_of_birth, phone, password=None):
    def create_user(self, user_id, email, date_of_birth, phone, password=None):
        if not user_id:
            raise ValueError('Users must have an id')

        user = self.model(
            user_id=user_id,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # 이쪽이 createsuperuser 명령으로 수퍼유저 생성부분 이부분도 커스텀 가능
    def create_superuser(self, user_id, email=None, date_of_birth=None, phone=None, password=None):  # 이거임

        user = self.create_user(
            user_id,
            email,
            date_of_birth,
            phone,
            password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

# 이쪽이 회원가입부분 위에 유저매니저로 보내버림 대충 이런 로직? ㅇㅎㅇㅎ


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.CharField(unique=True, max_length=10)
    password = models.CharField(max_length=20)
    email = models.EmailField(
        max_length=255, verbose_name="email"
    )
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=10, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    obejcts = UserManager()

    USERNAME_FIELD = 'user_id'  # 유니크 타입 필드
    REQUIRED_FIELDS = ['date_of_birth', 'email', 'phone']  # 그 외 입력받을 필드들 입력

    def __str__(self):
        return self.user_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
