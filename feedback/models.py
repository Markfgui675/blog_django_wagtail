from django.db import models



class StatusFeedback(models.Model):
    status = models.CharField('Status', max_length=200)

    def __str__(self) -> str:
        return self.status
    
    def __repr__(self) -> str:
        return self.__str__()

class Feedback(models.Model):
    data = models.DateField('Data')
    titulo = models.CharField('Título', max_length=150)
    descricao = models.TextField('Descrição')
    slug = models.CharField('Slug', max_length=250)
    status = models.ForeignKey(StatusFeedback, on_delete=models.SET_NULL, null=True, blank=True, default='Não registrado')

    def __str__(self) -> str:
        return self.titulo
    
    def __repr__(self) -> str:
        return self.__str__()
