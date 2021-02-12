# 外部文件使用django的models,需要配置django环境
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project02.settings")
    import django

    django.setup()

    from app01 import models

    obj_list = []
    for i in range(1, 10):
        obj = models.Test(
            name='葵花宝典第%s式' % i,
            age=20 + i,
            date='198%s-11-11' % i,
            date_time='198%s-11-11 11:11:11'%i

        )
        obj_list.append(obj)

    models.Test.objects.bulk_create(obj_list)
