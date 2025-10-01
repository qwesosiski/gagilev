from django.db import models


class Subscription(models.Model):
    title = models.CharField("Описание", max_length=50)
    price = models.DecimalField ("Цена")
    validity_period = models.DateField("Срок истечения")
    
    class Meta:
        verbose_name = "Подписка" 
        verbose_name_plural = "Подписки"
        subscription = ["price"]
        indexes = [
            models.Index(fields=["validity_period"]), 
            models.Index(fields=["price"]),
            models.Index(fields=["title"])
        ]
        
    def str(self):
        return f"{self.surname} {self.name}"

    
class User(models.Model):
    username = models.CharField("Имя пользователя", max_length=50)
    password = models.DecimalField("Пароль", max_length=50)
    email = models.CharField("Почта", max_length=50)
    phone_number = models.CharField("Номер телефона", max_length=11)
    subscription_id = models.ForeignKey(Subscription, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]
        indexes = [
            models.Index(fields=["Имя пользователя"]), # для быстрого поиска
            models.Index(fields=["Номер телефона"]),
            models.Index(fields=["Почта"])
        ]

    def str(self):
        return f"{self.surname} {self.name}"
    

class Chat (models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField("Описание")
    data = models.CharField("Данные")
    name = models.CharField("Имя")

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]), 
        ]

    def str(self):
        return f"{self.surname} {self.name}"
    
class Message(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    sending_time = models.CharField("Время отправки")
    Chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["sednding_time"]
        indexes = [
            models.Index(fields=["sending_time"]),
            models.Index(fields=["Chat_id"]),
            models.Index(fields=["User_id"]), 
        ]

    def str(self):
        return f"{self.surname} {self.name}"
    


class Channel(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField("Описание")
    data = models.CharField("Данные")
    name = models.CharField("Имя")

    class Meta:
        verbose_name = "Канал"
        verbose_name_plural = "Каналы"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]), 
        ]

    def str(self):
        return f"{self.surname} {self.name}"