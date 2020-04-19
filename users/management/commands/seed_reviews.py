from django.core.management.base import BaseCommand
from rooms import models as room_models
from users import models as user_models
from reviews.models import Reviews
from django_seed import Seed
import random


class Command(BaseCommand):
    
    help = 'This command creates many reviews'
    
    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='How many reviews do you want to create?')
        
            
    def handle(self, *args, **options):
        number = options.get('number')
        seeder = Seed.seeder()
        rooms = room_models.Room.objects.all()
        users = user_models.User.objects.all()
        seeder.add_entity(Reviews, number, {
            'accuracy': lambda x: random.randint(0, 6),
            'communication': lambda x: random.randint(0, 6),
            'cleanliness': lambda x: random.randint(0, 6),
            'location': lambda x: random.randint(0, 6),
            'check_in': lambda x: random.randint(0, 6),
            'value': lambda x: random.randint(0, 6),
            'room': lambda x: random.choice(rooms),
            'user': lambda x: random.choice(users),
        })
        self.stdout.write(self.style.SUCCESS(f"{number} Reviews created"))