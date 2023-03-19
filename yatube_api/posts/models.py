from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, verbose_name='Автор', on_delete=models.CASCADE,
        related_name='posts')
    image = models.ImageField(
        verbose_name='Картинка', upload_to='posts/', blank=True)
    group = models.ForeignKey(Group,
                              verbose_name='Группа',
                              on_delete=models.SET_NULL,
                              related_name='posts',
                              blank=True,
                              null=True,)

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, verbose_name='Автор комментария',
        on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, verbose_name='Пост', on_delete=models.CASCADE,
        related_name='comments')
    text = models.TextField(verbose_name='Текст комментария',)
    created = models.DateTimeField(
        'Дата создания', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(
        User, verbose_name='Подписчик', on_delete=models.CASCADE,
        related_name='follower')
    following = models.ForeignKey(
        User, verbose_name='Подписка', on_delete=models.CASCADE,
        related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique following'
            )
        ]

    def __str__(self):
        return self.user.username
