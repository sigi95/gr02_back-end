DROP SCHEMA IF EXISTS cityTourTravel;
CREATE SCHEMA cityTourTravel;
USE cityTourTravel;

CREATE TABLE usuario(
	usu_nombreUsuario char(60) NOT NULL PRIMARY KEY,
    usu_password char(20) NOT NULL,
    usu_nombre  char(20) NOT NULL,
    usu_apellido1 char(40) NOT NULL,
    usu_apellido2 char(40),
    usu_email  char(60) NOT NULL,
    usu_telefonoCelular bigint,
    usu_pais char(20),
    usu_ciudad char(20),
    usu_Direccion char(60)
);

CREATE TABLE ciudad(
	ciu_nombre char(20) NOT NULL PRIMARY KEY,
    ciu_pais char(20) NOT NULL DEFAULT "Colombia"
);

CREATE TABLE tour(
	tour_nombre char(60) NOT NULL PRIMARY KEY,
    ciu_nombre char(20) NOT NULL,
    tour_descripcion char(255) NOT NULL,
    tour_precio double NOT NULL,
    tour_fechaHoraInicio datetime DEFAULT '2021-01-01 00:00:00',
    tour_fechaHoraFin datetime DEFAULT '2021-01-02 00:00:00',
    tour_duracionHoras int NOT NULL,
    tour_transporte enum('A pie', 'Bicicleta', 'Moto', 'Bus', 'Carro', 'Lancha', 'Barco', 'Avión') DEFAULT 'A pie',
    tour_alimentacion char(100) NOT NULL,
    tour_hospedaje enum('Sí', 'No') DEFAULT 'No',
    tour_kilometros int NOT NULL,
    tour_inicio char(60) NOT NULL,
    tour_fin char(60) NOT NULL,
    FOREIGN  KEY(ciu_nombre)REFERENCES ciudad(ciu_nombre)
);
    
CREATE TABLE carritoCompras(
	usu_nombreUsuario char(60) NOT NULL PRIMARY KEY,
    tour_nombre char(60) NOT NULL,
    carritoCompras_numeroPersonas int NOT NULL,
    carritoCompras_precioTotal double NOT NULL,
    FOREIGN KEY(usu_nombreUsuario)REFERENCES cuenta(usu_nombreUsuario),
    FOREIGN KEY(tour_nombre)REFERENCES tour(tour_nombre)
);
