from django.db import models

STATUS_CHOICES = [
    ('New', 'New'),
    ('In progress', 'In progress'),
    ('Pending', 'Pending'),
    ('Blocked', 'Blocked'),
    ('Done', 'Done')
]


class Task(models.Model):
    title = models.CharField(max_length=255, unique_for_date='created_at', verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    categories = models.ManyToManyField('Category', related_name='tasks', verbose_name='Categories')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New', verbose_name='Status')
    deadline = models.DateTimeField(verbose_name='Deadline')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE, verbose_name='Task')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New', verbose_name='Status')
    deadline = models.DateTimeField(verbose_name='Deadline')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return self.title
