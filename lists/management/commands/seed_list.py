from django.core.management.base import BaseCommand
from rooms import models as room_models
from users import models as user_models
from lists.models import List
from django_seed import Seed
from django.contrib.admin.utils import flatten
import random

NAME = 'lists'

class Command(BaseCommand):
    
    help = f'This command creates many {NAME}'
    
    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help=f'How many {NAME} do you want to create?')
        
            
    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        rooms = room_models.Room.objects.all()
        users = user_models.User.objects.all()
        seeder.add_entity(List, number, {
            'user': lambda x: random.choice(users),
        })
        created = seeder.execute()
        created_clean = flatten(list(created.values()))
        for pk in created_clean:
            list_model = List.objects.get(pk=pk)
            to_add = rooms[random.randint(0,5):random.randint(6, 30)]
            list_model.rooms.add(*to_add)
            
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created"))