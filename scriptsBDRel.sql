CREATE DATABASE `integracion_datos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `calificaciones` (
  `valorNum` int NOT NULL,
  `valor` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`valorNum`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `emergencia` (
  `emergenciaId` int NOT NULL AUTO_INCREMENT,
  `emergenciaURI` text,
  `emergenciaNombre` text,
  PRIMARY KEY (`emergenciaId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `instituto` (
  `institutoId` int NOT NULL AUTO_INCREMENT,
  `instututoURI` text,
  `institutoNombre` text,
  PRIMARY KEY (`institutoId`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `localidad` (
  `localidadId` int NOT NULL AUTO_INCREMENT,
  `localidadURI` text NOT NULL,
  `localidadNombre` text,
  PRIMARY KEY (`localidadId`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `serviciosalud` (
  `serviciosaludId` int NOT NULL AUTO_INCREMENT,
  `servicioSaludURI` text,
  `servicioSaludNombre` text,
  PRIMARY KEY (`serviciosaludId`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
