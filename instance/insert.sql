PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE matricules (
	matricule INTEGER NOT NULL, 
	is_admin BOOLEAN, 
	PRIMARY KEY (matricule)
);
INSERT INTO matricules VALUES(111777,1);
INSERT INTO matricules VALUES(222333,1);
INSERT INTO matricules VALUES(654321,0);
INSERT INTO matricules VALUES(999666,0);
CREATE TABLE departements (
	name VARCHAR(20) NOT NULL, 
	employee_count INTEGER, 
	PRIMARY KEY (name)
);
INSERT INTO departements VALUES('Production',NULL);
INSERT INTO departements VALUES('Gestion',NULL);
INSERT INTO departements VALUES('Marketing',NULL);
INSERT INTO departements VALUES('Vente',NULL);
INSERT INTO departements VALUES('Informatique',NULL);
CREATE TABLE user (
	matricule INTEGER NOT NULL, 
	first_name VARCHAR(20), 
	last_name VARCHAR(20), 
	email VARCHAR(100), 
	password VARCHAR(100), 
	dep_name INTEGER, 
	address VARCHAR(100), 
	phone INTEGER, 
	salaire INTEGER, 
	PRIMARY KEY (matricule), 
	FOREIGN KEY(matricule) REFERENCES matricules (matricule), 
	UNIQUE (email), 
	FOREIGN KEY(dep_name) REFERENCES departements (name)
);
INSERT INTO user VALUES(111777,'Adel','Bougrine','adelbougrine@gmail.com','adel','Marketing','Cité Nour-Gafsa',95001300,1200);
INSERT INTO user VALUES(222333,'Oussama','Ben Sassi','obensassi.03@gmail.com','2003','Informatique','Lala-Gafsa',25730171,2500);
INSERT INTO user VALUES(654321,'Ahmed','Ben Ali','ahmed.2003@gmail.com','ahmed','Informatique','Lala-Gafsa',95713962,800);
INSERT INTO user VALUES(999666,'Ala','Hamed','ala.03@gmail.com','ala','Vente','Gsar-Gafsa',43258974,1200);
CREATE TABLE demande_conge (
	matricule INTEGER NOT NULL, 
	type_conge VARCHAR, 
	date_deb DATETIME, 
	date_fin DATETIME, 
	motif VARCHAR, status BOOLEAN, 
	PRIMARY KEY (matricule), 
	FOREIGN KEY(matricule) REFERENCES matricules (matricule)
);
INSERT INTO demande_conge VALUES(111777,'Congé occasionnel','2023-07-16 00:00:00.000000','2023-08-16 00:00:00.000000','Voyage',NULL);
INSERT INTO demande_conge VALUES(222333,'Congé de maladie','2023-07-12 00:00:00.000000','2023-07-31 00:00:00.000000','maladie',1);
CREATE TABLE avance_salaire (
	matricule INTEGER NOT NULL, 
	montant INTEGER, 
	motif VARCHAR, status BOOLEAN, 
	PRIMARY KEY (matricule), 
	FOREIGN KEY(matricule) REFERENCES matricules (matricule)
);
INSERT INTO avance_salaire VALUES(222333,700,'maladie',0);
COMMIT;
