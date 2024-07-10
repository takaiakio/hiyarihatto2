from django.db import models

class HiyariHatto(models.Model):
    title = models.CharField('題名', max_length=100)
    process = models.CharField('工程', max_length=100)
    action = models.CharField('やるべきこと', max_length=100)
    situation = models.TextField('ヒヤリとした場面')
    consequence = models.TextField('気づけなければ、どうなるのか')
    avoidance = models.TextField('回避事由')
    danger_level = models.IntegerField('危険度', choices=[(i, str(i)) for i in range(1, 6)])
    phase = models.CharField('様態評価', max_length=20, choices=[
        ('input', 'インプット情報'),
        ('reception', '受容'),
        ('judgment', '判断'),
        ('action', '行動')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
