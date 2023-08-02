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
INSERT INTO departements VALUES('Management',NULL);
INSERT INTO departements VALUES('Marketing',NULL);
INSERT INTO departements VALUES('Sales',NULL);
INSERT INTO departements VALUES('IT',NULL);
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
	is_admin BOOLEAN, 
	PRIMARY KEY (matricule), 
	FOREIGN KEY(matricule) REFERENCES matricules (matricule), 
	UNIQUE (email), 
	FOREIGN KEY(dep_name) REFERENCES departements (name), 
	FOREIGN KEY(is_admin) REFERENCES matricules (is_admin)
);
INSERT INTO user VALUES(222333,'Oussama','Ben Sassi','obensassi.03@gmail.com','oussama','Informatique','Lala-Gafsa',25730171,2500,1);
INSERT INTO user VALUES(999666,'Adel','Bougrine','adelbougrine@gmail.com','adel','Vente','Cité Nour-Gafsa',95123741,1200,0);
CREATE TABLE demande_conge (
	matricule INTEGER NOT NULL, 
	type_conge VARCHAR, 
	date_deb DATETIME, 
	date_fin DATETIME, 
	motif VARCHAR, 
	status BOOLEAN, 
	PRIMARY KEY (matricule), 
	FOREIGN KEY(matricule) REFERENCES matricules (matricule)
);
CREATE TABLE avance_salaire (
	matricule INTEGER NOT NULL, 
	montant INTEGER, 
	motif VARCHAR, 
	status BOOLEAN, 
	PRIMARY KEY (matricule), 
	FOREIGN KEY(matricule) REFERENCES matricules (matricule)
);
COMMIT;
