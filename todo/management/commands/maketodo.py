from django.core.management import BaseCommand
from todo.models import todo
from random import choice

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("make todo start :)")
        for i in range(1,101):
            todos, create = todo.objects.get_or_create(name = f"todo test 생성 {i}")
            if create:
                print(f"{i}번째 생성완료")
                
            else:
                print("이미 존재함")
            # todo.objects.create(name = f"todo test 생성 {i}", complete = choice([True,False]))
            # print(f"{i}번째 생성")
            
        print("make todo end:)")