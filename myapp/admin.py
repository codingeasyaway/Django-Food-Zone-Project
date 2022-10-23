from django.contrib import admin
from  .models import Contact, Dish, Profile, Category, Team, Order
# Register your models here.
admin.site.site_header = "Food Zone  | Gull Brohi"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'image', 'icon', 'added_on', 'updated_on']
admin.site.register(Category, CategoryAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'image', 'added_on', 'updated_on']
admin.site.register(Team, TeamAdmin)


class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'details', 'ingredients', 'price', 'category', 'discounted_price', 'is_avaible']
admin.site.register(Dish, DishAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'profile_pic', 'contact_number', 'address', 'updated_on']
admin.site.register(Profile, ProfileAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'added_on', 'is_approved']
admin.site.register(Contact, ContactAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'item', 'status', 'invoice_id', 'payer_id', 'ordered_on']
admin.site.register(Order, OrderAdmin)

