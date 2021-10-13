#registrar vistas 
from .usuarioViewSet import CrearUsuarioViewSet, DetalleUsuarioView, EditarUsuarioView, EliminarUsuarioView
from .ciudadViewSet import CiudadView, CiudadGetView
from .tourViewSet import TourViewSet, TourIdGetView, TourCiudadGetView
from .carritoViewSet import CarritoView, CarritoGetView, EditarCarritoView, EliminarCarritoView

