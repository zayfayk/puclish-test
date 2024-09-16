from django.contrib import admin
from django.contrib.auth.models import User
from .models import Customer,Category

admin.site.register(Category)



# Registering the Customer model
admin.site.register(Customer)

# Unregistering the default User admin and registering the custom UserAdmin

