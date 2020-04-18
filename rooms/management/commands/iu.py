from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    help = 'This command tells me hello'
    
    def add_arguments(self, parser):
        parser.add_argument('--times', help='How many times do you wnat me to tell you that I hello you?')
        
    def handle(self, *args, **options):
        times = int(options.get("times"))
        for i in range(times):
            self.stdout.write(self.style.WARNING('hello'))