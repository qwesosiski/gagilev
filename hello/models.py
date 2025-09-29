from django.db import models


class Subscription(models.Model):
    title = models.CharField("Описание", max_length=50)
    price = models.DecimalField ("Цена")
    expiry_date = models.DateField("Срок истечения")
    
    class Meta:
        verbose_name = "Подписка" 
        verbose_name_plural = "Подписки"
        subscription = ["price"]
        indexes = [
            models.Index(fields=["expiry_date"]), 
            models.Index(fields=["price"]),
            models.Index(fields=["title"])
        ]

        constraints = [
            models.UniqueConstraint(
                fields = ["price", "title"],
                condition = models.Q(desc = "expiry_date"),
                name = "unique_surname_bio"
            ),
            ]
        
    def str(self):
        return f"{self.surname} {self.name}"

class User(models.Model):
    title = models.CharField("Должность", unique=True)
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        indexes = [
            models.Index(fields=["Должность"])
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
            models.Index(fields=["Имя"]), # для быстрого поиска
            models.Index(fields=["Номер телефона"]),
            models.Index(fields=["Почта"])
        ]

        constraints = [
            models.UniqueConstraint(
                fields = ["surname", "bio"],
                condition = models.Q(desc = "Жив"),
                name = "unique_surname_bio"
            ),
            ]
    def str(self):
        return f"{self.surname} {self.name}"
    

class Chats(models.Model):
    UserId = models.CharField ("Имя пользователя")
    MessageID = models.CharField ("Сообщения")

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"
        ordering = ["start_time"]
        indexes = [
            models.Index(fields=["start_time"]), 
            models.Index(fields=["end_time"])
        ]

        constraints = [
            models.UniqueConstraint(
                fields = ["surname", "bio"],
                condition = models.Q(desc = "Жив"),
                name = "unique_surname_bio"
            ),
            ]
    def str(self):
        return f"{self.surname} {self.name}"