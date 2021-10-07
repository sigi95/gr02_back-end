from django.contrib import admin
from .models.usuario import User
from .models.ciudad import Ciudad
from .models.tour import Tour
from .models.carrito import Carrito

# registro los modelos
admin.site.register(User)
admin.site.register(Ciudad)
admin.site.register(Tour)
admin.site.register(Carrito)