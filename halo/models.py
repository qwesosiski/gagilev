from django.db import models
from django.contrib.auth.hashers import make_password


class Subscription(models.Model):
    BASIC = 'basic'
    PREMIUM = 'premium'
    PRO = 'pro'

    SUBSCRIPTION_CHOICES = [
        (BASIC, 'Basic'),
        (PREMIUM, 'Premium'),
        (PRO, 'Pro'),
    ]
    
    title = models.CharField(
        'Тип подписки', 
        max_length=50,
        choices=SUBSCRIPTION_CHOICES,
        default=BASIC
    )
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    validity_period = models.DateField('Срок истечения')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ['price']
        indexes = [
            models.Index(fields=['price']),
            models.Index(fields=['title'])
        ]

    def __str__(self):
        return self.get_title_display()


class User(models.Model):
    username = models.CharField('Имя пользователя', max_length=50, unique=True)
    password = models.CharField('Пароль', max_length=128)
    email = models.EmailField('Email', unique=True)                    
    phone_number = models.CharField('Телефон', max_length=15, blank=True)
    subscription = models.ForeignKey(
        Subscription,
        related_name='users',
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        verbose_name='Подписка'                     
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']
        indexes = [
            models.Index(fields=['username']),
        ]

    def save(self, *args, **kwargs):
        # Хэшируем пароль при сохранении
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Message(models.Model):
    user = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    text = models.TextField('Текст сообщения', max_length=500)
    sending_time = models.DateTimeField('Время отправки', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-sending_time']
        indexes = [
            models.Index(fields=['text']),
            models.Index(fields=['sending_time']),
        ]

    def __str__(self):
        return f'Сообщение от {self.user.username}'


class Chat(models.Model):
    users = models.ManyToManyField(User, related_name='user_chats')
    messages = models.ManyToManyField(Message, related_name='chat_messages', blank=True)
    description = models.TextField('Описание', max_length=255, blank=True)
    data = models.JSONField('Дополнительные данные', default=dict, blank=True)
    name = models.CharField('Название чата', max_length=50)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Channel(models.Model):
    user = models.ForeignKey(User, related_name='user_channels', on_delete=models.CASCADE)
    messages = models.ManyToManyField(Message, related_name='channel_messages', blank=True)
    description = models.TextField('Описание', max_length=255, blank=True)
    name = models.CharField('Название канала', max_length=50)

    class Meta:
        verbose_name = 'Канал'
        verbose_name_plural = 'Каналы'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name