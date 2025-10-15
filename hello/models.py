from django.db import models

class Subscription(models.Model):
    title = models.CharField("Описание", max_length=50)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2) 
    validity_period = models.DateField("Срок истечения")
    
    class Meta:
        verbose_name = "Подписка" 
        verbose_name_plural = "Подписки"
        ordering = ["price"] 
        indexes = [ 
            models.Index(fields=["price"]),
            models.Index(fields=["title"])
        ]
    def __str__(self):
      return f"{self.title}"
        
 

class User(models.Model):
    username = models.CharField("Имя пользователя", max_length=50)
    password = models.CharField("Пароль", max_length=50) 
    email = models.CharField("Почта", max_length=50)
    phone_number = models.CharField("Номер телефона", max_length=11)
    subscription_id = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]
        indexes = [
            models.Index(fields=["username"]),
        ]

    def __str__(self):
        return f"{self.username}"  

class Chat(models.Model):
    users = models.ManyToManyField(User)
    description = models.CharField("Описание", max_length=255)  
    data = models.CharField("Данные", max_length=255)  
    name = models.CharField("Имя", max_length=50)  

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]), 
        ]

    def __str__(self):
        return f"{self.name}"  

class Message(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sending_time = models.DateTimeField("Время отправки") 
    Chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.CharField("Сообщение", max_length=500)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["sending_time"] 
        indexes = [
            models.Index(fields=["Chat_id"]), 
            models.Index(fields=["sending_time"]), 
        ]

    def __str__(self):
        return f"Сообщение от {self.User_id} в {self.sending_time}"
      
class Channel(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField("Описание", max_length=255) 
    Message = models.ForeignKey(Message, ) 
    name = models.CharField("Имя", max_length=50) 
    class Meta:
        verbose_name = "Канал"
        verbose_name_plural = "Каналы"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]), 
        ]

    def __str__(self):
        return f"{self.name}"