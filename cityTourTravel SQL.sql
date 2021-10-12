DROP SCHEMA IF EXISTS cityTourTravel;
CREATE SCHEMA cityTourTravel;

USE cityTourTravel;

CREATE TABLE usuario(
	usu_id bigint NOT NULL PRIMARY KEY,
    usu_tipoId enum ('Cédula de Ciudadanía', 'Cédula de Extranjería', 'NIT') NOT NULL,
    usu_nombreUsuario char(60) NOT NULL,
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

INSERT INTO usuario(usu_tipoId, usu_id, usu_nombreUsuario, usu_password, usu_nombre, usu_apellido1, usu_apellido2, usu_email, usu_telefonoCelular, usu_pais, usu_ciudad, usu_Direccion) VALUES ('Cédula de Ciudadanía', 123456789, 'PepitoP23', 'pepito45&', 'Pepito', 'Perez', 'Perez', 'pepitoperez@correo.com', 3158995636,'Colombia', 'Bogotá', 'Calle falsa 123');

CREATE TABLE ciudad(
	ciu_nombre char(20) NOT NULL PRIMARY KEY,
    ciu_pais char(20) NOT NULL DEFAULT "Colombia"
);

INSERT INTO ciudad(ciu_nombre, ciu_pais) VALUES ('Bogotá', 'Colombia');
INSERT INTO ciudad(ciu_nombre, ciu_pais) VALUES ('Cúcuta', 'Colombia');
INSERT INTO ciudad(ciu_nombre, ciu_pais) VALUES ('Medellín', 'Colombia');
INSERT INTO ciudad(ciu_nombre, ciu_pais) VALUES ('Popayán', 'Colombia');
INSERT INTO ciudad(ciu_nombre, ciu_pais) VALUES ('Santander', 'Colombia');

CREATE TABLE tour(
	tour_nombre char(80) NOT NULL PRIMARY KEY,
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

INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour Avenida el Dorado en bici', 'Bogotá', 'Por la Avenida El Dorado o Avenida Calle 26 podrás montar en tu bicicleta y andar por la 
ciclorruta mientras disfrutas la belleza del panorama con sus espacios verdes y edificios elegantes', 130000, '2021-10-31 08:00:00', '2021-10-31 18:00:00', 10, 'Bicicleta', '2 refrigerios, 1 almuerzo y 2 botellas de agua', 'No', 13, 'Biblioteca Nacional de Colombia', 'Aeropuerto Internacional El Dorado');
INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour Historia & Museos', 'Bogotá', 'Podrás visitar seis de los museos más importantes que ofrece la capital de Colombia mientras aprendes de historia y cultura de 
este país que seguro te encantará', 110000, '2021-10-31 08:00:00', '2021-10-31 17:00:00', 10, 'A pie', '2 refrigerios, 1 almuerzo y 1 botella de agua', 'No', 3, 'Plaza de Bolívar', 'Museo Nacional de Colombia');
INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour Subida a Monserrate', 'Bogotá', 'Este es uno de los sitios más icónicos de Bogotá, no importa si eres o no religioso, todo el mundo sube para admirar la 
maravillosa vista que ofrece este cerro a la capital', 175000, '2021-10-31 08:00:00', '2021-10-31 16:00:00', 8, 'A pie', '2 refrigerios, 1 almuerzo y 2 botellas de agua', 'No', 3, 'Entrada museo Quinta de Bolívar', 'Santuario de Monserrate');
INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour Subida a Guadalupe', 'Bogotá', 'Al lado de Monserrate nos encontramos con la estatua de virgen de Guadalupe vista desde arriba en cualquier lugar de Bogotá. 
También con un increíble mirador, allí podremos observar la imponente cordillera central y sus nevados', 130000, '2021-10-31 08:00:00', '2021-10-31 14:00:00', 6, 'Bus', '1 refrigerio, 1 almuerzo y 2 botellas de agua', 'No', 9, 'Iglesia de Nuestra 
Señora de Egipto', 'Santuario Virgen De Guadalupe');
INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour Conoce los Humedales', 'Bogotá', '¿Sabías que Bogotá cuenta con importantes fuentes de agua llamadas humedales? Hay 11 de ellos categoría RAMSAR en los cuáles 
podemos admirar la paz y la tranquilidad de la naturaleza a su alrededor, así como avistamiento de fauna única en el lugar', 150000, '2021-10-31 06:00:00', '2021-11-01 18:00:00', 24, 'Bus', '2 desayunos, 2 almuerzos, 1 cena y 2 botellas de agua', 'Sí', 70, 'Humedal El Tunjo', 'Humedal Torca – Guaymaral');

INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour al Monumento Cristo Rey', 'Cúcuta', 'Es una importante estatua situada en La Cabrera desde el año 1947 para las fiestas de Cristo Rey. Te encantará visitarlo 
y apreciar la vista del mirador', 100000, '2021-10-31 09:00:00', '2021-10-31 15:00:00', 6, 'A pie', '2 refrigerios, 1 almuerzo y 1 botella de agua', 'No', 2, 'Parque de Cristo Rey', 'Parque San Rafael');
INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour al Santuario Los Siete Chorros', 'Cúcuta', 'Luego de un camino empedrado, rodeado de altísimos árboles que hacen resplandecer las luces y las sombras rumbo a 
la cumbre, está Siete Chorros, un silencioso y pequeño balneario, ubicado en Salazar de las Palmas', 175000, '2021-10-31 08:00:00', '2021-11-01 08:00:00', 24, 'Bus', '2 refrigerios, 1 almuerzo, 1 cena, 1 desayuno y 1 botella de agua', 'Sí', 50, 'Parroquia San Alberto Hurtado', 'Hospedaje Brisas del Río');
INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour por Chinácota', 'Cúcuta', 'Aquí a 40 minutos de la capital de Norte de Santander, encontramos una amplia oferta hotelera y gastronómica debido a sus 
atractivos naturales y sitios de interés histórico y cultural para no perderse', 175000, '2021-10-31 09:00:00', '2021-11-01 08:00:00', 24, 'Bus', '2 refrigerios, 1 almuerzo, 1 cena, 1 desayuno y 1 botella de agua', 'Sí', 33, 'Parque Pisarreal', 'Hotel Chinácota');
INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour por la casa del General Francisco de Paula Santander (Villa del Rosario)', 'Cúcuta', 'Es un bien patrimonial del ámbito nacional, inmueble de grandes valores 
históricos y arquitectónicos, fue la casa donde nació el prócer de nuestra independencia Francisco de Paula Santander y vivió sus primeros años de vida', 100000, '2021-10-31 08:00:00', '2021-10-31 17:00:00', 9, 'A pie', '2 refrigerios, 1 almuerzo y 1 botella de agua', 'No', 2, 'Parque Los Libertadores', 'Museo Casa Natal del General Francisco de Paula Santander');
INSERT INTO tour(tour_nombre, ciu_nombre, tour_descripcion, tour_precio, tour_fechaHoraInicio, tour_fechaHoraFin, tour_duracionHoras, tour_transporte, tour_alimentacion, tour_hospedaje, tour_kilometros, tour_inicio, tour_fin) VALUES ('Tour museo Torre del Reloj', 'Cúcuta', 'Es sede de la Secretaría de Cultura y Turismo de Norte de Santander, hogar de expresiones culturales como obras de teatro 
y alberga un museo de arte moderno en el que se llevan a cabo exposiciones temporales', 100000, '2021-10-31 09:00:00', '2021-10-31 16:00:00', 7, 'A pie', '2 refrigerios, 1 almuerzo y 1 botella de agua', 'No', 2, 'Parque Cúcuta 300 años', 'Centro Cultural Torre del Reloj');


CREATE TABLE carritoCompras(
	usu_id bigint NOT NULL PRIMARY KEY,
    tour_nombre char(60) NOT NULL,
    carritoCompras_numeroPersonas int NOT NULL,
    carritoCompras_precioTotal double NOT NULL,
    FOREIGN KEY(usu_id)REFERENCES usuario(usu_id),
    FOREIGN KEY(tour_nombre)REFERENCES tour(tour_nombre)
);

INSERT INTO carritoCompras(usu_id, tour_nombre, carritoCompras_numeroPersonas, carritoCompras_precioTotal) VALUES (123456789, 'Tour al Monumento Cristo Rey', 1, 100000);

CREATE TABLE compra(
	com_id int AUTO_INCREMENT PRIMARY KEY,
	usu_id bigint NOT NULL,
    com_metodoPago enum('PayU', 'Visa', 'MasterCard', 'American Express', 'Diners Club', 'PSE') NOT NULL,
    com_numeroCuenta bigint NOT NULL,
    com_confirmarPago enum('Sí', 'No', 'Por confirmar') DEFAULT 'Por confirmar',
    com_fechaPago datetime DEFAULT '2021-01-01 00:00:00',
    FOREIGN KEY(usu_id)REFERENCES carritoCompras(usu_id)
);

INSERT INTO compra(usu_id, com_metodoPago, com_numeroCuenta) VALUES (123456789, 'PayU', 1234567890);
