from django.core.management.base import BaseCommand
from rooms import models as room_models
from users import models as user_models
from django_seed import Seed
import random 


class Command(BaseCommand):
    
    help = 'This command creates many rooms'
    
    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int, help='How many rooms do you want to create?')
        
            
    def handle(self, *args, **options):
        number = int(options.get('number'))
        seeder = Seed.seeder()
        room_types = room_models.RoomType.objects.all()
        all_user = user_models.User.objects.all()
        seeder.add_entity(room_models.Room, number, {
            'name': lambda x: seeder.faker.address(),
            'host': lambda x: random.choice(all_user),
            'room_type': lambda x: random.choice(room_types),
            'guests': lambda x: random.randint(0, 20),
            'price': lambda x: random.randint(0, 300),
            'beds': lambda x: random.randint(0, 5),
            'bedrooms': lambda x: random.randint(0, 5),
            'baths': lambda x: random.randint(0, 5),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created"))