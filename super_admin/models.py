from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin

class User(AbstractUser,PermissionsMixin):
    class Role(models.TextChoices):
        DIRECTOR = "DIRECTOR",'director'
        MANAGER = "MANAGER","manager"
    role = models.CharField(max_length=15,choices=Role.choices,null=True,blank=True)
    class Meta:
        db_table = "User"

class DirectorManager(BaseUserManager):
    def create_user(self , username , password = None):
        if not username or len(username) <= 0 : 
            raise  ValueError("Username field is required !")
        if not password :
            raise ValueError("Password is must !")
        
        user = self.model(
            username= username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def get_queryset(self,*args,**kwargs):
        result =super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.DIRECTOR)

    
    

# ManagerManager
class ManagerManager(BaseUserManager):
    def create_user(self , username , password = None):
        if not username or len(username) <= 0 : 
            raise  ValueError("Username field is required !")
        if not password :
            raise ValueError("Password is must !")
        
        user = self.model(
            username= username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    def get_queryset(self,*args,**kwargs):
        result =super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.MANAGER)

   

# Director
class Director(User):
    base_role = User.Role.DIRECTOR
    class Meta:
        proxy = True
    def save(self,*args,**kwargs):
        if not self.pk:
           self.role = self.base_role
           return super().save(*args,**kwargs)
    objects = DirectorManager()

    class Meta:
            verbose_name = "Direktor"
            verbose_name_plural = "Direktorlar"

# Manager
class Manager(User):
    base_role = User.Role.MANAGER
    class Meta:
        proxy = True
    def save(self,*args,**kwargs):
        if not self.pk:
           self.role = self.base_role
           return super().save(*args,**kwargs)
    objects = ManagerManager()
    
    
    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managerlar"
