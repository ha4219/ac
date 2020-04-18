from django.contrib import admin
from . import models
from django.utils.html import mark_safe


@admin.register(models.RoomType, models.Facility,
                models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    ''' Item Admin Definition '''
    
    list_display = (
        'name',
        'used_by'
    )
    
    def used_by(self, obj):
        return obj.rooms.count()
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    
    ''' Room Admin Definition '''
    
    fieldsets = (
        (
            'Basic Info',
            {
                'fields': (
                    'name',
                    'description',
                    'country',
                    'address',
                    'price',
                )
            }
        ),
        (
            'Times',
            {
                'fields': (
                    'check_in',
                    'check_out'
                )
            }
        ),
        (
            'Spaces',
            {
                'fields': (
                    'guests',
                    'beds',
                    'bedrooms',
                    'baths'
                )
            }
        ),
        (
            'More About The Space',
            {
                'classes': ("collapse",),
                'fields': (
                    'amenities',
                    'facilities',
                    'house_rules'
                )
            }
        ),
        (
            'Last Details',
            {
                'fields': (
                    'host',
                )
            }
        )
    )
    
    list_display = (
        'name',
        'country',
        'city',
        'price',
        'guests',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book',
        'count_amenities',
        'count_photos',
        'total_rating',
    )
    
    ordering = ('name', 'price', 'bedrooms')
    
    list_filter = (
        'instant_book',
        'host__superhost',
        'host__gender',
        'city',
        'room_type',
        'amenities',
        'facilities',
        'house_rules',
        'country',
    )
    
    search_fields = (
        '=city',
        '^host__username'
        
    )
    
    filter_horizontal = (
        'amenities',
        'facilities',
        'house_rules',
    )
    
    def count_amenities(self, obj):
        return obj.amenities.count()
    
    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    ''' Photo Admin Definition '''
    
    list_display = ('__str__', 'get_thumbnail')
    
    # django supervise security => dont run script
    def get_thumbnail(self, obj):
        return mark_safe(f'<img width=50px src={obj.file.url}>')

