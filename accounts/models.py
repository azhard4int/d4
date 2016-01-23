from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """
    Email Activation Token and Email Forgot Token
    """
    user = models.ForeignKey(User)
    email_token = models.CharField(default=None, blank=True, max_length=255)
    forgot_token = models.CharField(default=None, blank=True, max_length=255)
    company = models.CharField(default=None, blank=True, max_length=255)
    level = models.CharField(default='Client', blank=True, max_length=50, null=True)


class Packages(models.Model):
    """
    Packages like D2408 etc.
    """
    name = models.CharField(default=None, max_length=255)
    ram = models.CharField(default=None, blank=True, null=True, max_length=255)
    disk = models.CharField(default=None, blank=True, null=True, max_length=255)
    kvmswap = models.CharField(default=1024, blank=True, null=True, max_length=30)
    bandwidth = models.CharField(default=None, blank=True, null=True, max_length=200)
    cpus = models.CharField(default=4, blank=True, null=True, max_length=100)


class Nodes(models.Model):

    name = models.CharField(default=None, max_length=100, null=False)
    ip = models.CharField(default=None, max_length=30, null=False)
    hostname = models.CharField(default=None, max_length=100, null=False)
    max_vms = models.IntegerField(default=30, null=False)
    max_mem = models.IntegerField(default=0, null=False)
    max_disk = models.IntegerField(default=0, null=False)
    internalip = models.CharField(default=None, max_length=30, null=False)


class VMSManager(models.Manager):

    def list_all_vms(self, client_id):
        return self.filter(client_id=client_id)

    def vm_node(self, vm_id, client_id):
        return self.filter(client_id=client_id, id=vm_id)[0]

class VMS(models.Model):
    """
    Virtual Machine
    """
    name = models.CharField(default=None, max_length=255, unique=True)
    client = models.ForeignKey(User, default=None)
    node = models.ForeignKey(Nodes, default=None)
    mainipaddress = models.CharField(default=None, max_length=30)
    hostname = models.CharField(default=None, max_length=100)
    disk = models.CharField(default=None, max_length=30)
    ram = models.CharField(default=None, max_length=30)
    kvmswap = models.CharField(default=1024, max_length=10)
    template = models.CharField(default=None, max_length=200)
    templatename = models.CharField(default=None, max_length=200)
    rootpassword = models.CharField(default=None, max_length=200)
    templateid = models.IntegerField(default=0)
    vncport = models.CharField(default=None, max_length=30)
    vm_state = models.SmallIntegerField(default=1) # 0 for off, 1 is for on and 2 is for suspended.
    objects = VMSManager()


class Commands(models.Model):

    node = models.ForeignKey(Nodes, max_length=64, null=False, default=None)
    vm = models.ForeignKey(VMS, max_length=64, null=False, default=None)
    action = models.TextField(null=False, default=None)
    executed = models.BooleanField(default=False)