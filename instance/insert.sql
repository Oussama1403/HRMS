PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE matricules (
	matricule INTEGER NOT NULL, 
	is_admin BOOLEAN, 
	PRIMARY KEY (matricule)
);
INSERT INTO matricules VALUES(111777,1);
INSERT INTO matricules VALUES(222333,1);
INSERT INTO matricules VALUES(654321,1);
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
CREATE TABLE demande_conge (
	demande_id INTEGER NOT NULL, 
	type_conge VARCHAR, 
	date_deb DATETIME, 
	date_fin DATETIME, 
	motif VARCHAR, 
	PRIMARY KEY (demande_id)
);
CREATE TABLE avance_salaire (
	demande_id INTEGER NOT NULL, 
	montant INTEGER, 
	motif VARCHAR, 
	PRIMARY KEY (demande_id)
);
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
INSERT INTO user VALUES(111777,'Adel','Bougrine','adelbougrine@gmail.com','adel','Marketing','Cité Nour-Gafsa',95123741,NULL);
INSERT INTO user VALUES(222333,'Oussama','Ben Sassi','obensassi.03@gmail.com','2003','Informatique','Lala-Gafsa',25730171,NULL);
INSERT INTO user VALUES(654321,'John','Doe','john.2003@gmail.com','john','Informatique','Lala-Gafsa',95713962,NULL);
INSERT INTO user VALUES(999666,'Ala','Benabdallah','ala.03@gmail.com','ala','Vente','Gsar-Gafsa',43258974,NULL);
COMMIT;
