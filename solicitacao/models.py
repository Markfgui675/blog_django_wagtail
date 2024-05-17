from django.contrib.auth.models import User, Group
from django.db import models



class StatusSolicitacao(models.Model):
    status = models.CharField('Status', max_length=250)

    def __str__(self) -> str:
        return self.status
    
    def __repr__(self) -> str:
        return self.__str__()


class Solicitacao(models.Model):
    data = models.DateField('Data', null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(StatusSolicitacao, on_delete=models.SET_NULL, null=True)
    motivo = models.TextField('Motivo', null=True, blank=False)

    def __str__(self) -> str:
        return f'({self.user}, {self.group}, {self.status})'

    def __repr__(self) -> str:
        return self.__str__()

