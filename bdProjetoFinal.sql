--Tabela de lançamento de aeroportos

CREATE TABLE aeroportos(
    id INTEGER CONSTRAINT nn_id_aero NOT NULL,
    codigo VARCHAR(3) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    CONSTRAINT pk_id_aeroporto PRIMARY KEY (id)
);

DROP TABLE aeroportos;

-- Tabela de lançamento de Voos

CREATE TABLE voos(
	id INTEGER CONSTRAINT nn_id_voo NOT NULL,
	aeroporto_origem_id INTEGER NOT NULL,
	aeroporto_destino_id INTEGER NOT NULL,
	data_partida DATE NOT NULL,
	hora_partida TIME NOT NULL,
	data_chegada DATE NOT NULL,
	hora_chegada TIME NOT NULL,
	companhia_aerea VARCHAR(50) NOT NULL,
	preco NUMERIC(10,2) NOT NULL,
	assentos_disponíveis INTEGER NOT NULL,
	created_at TIMESTAMP NOT NULL,
	CONSTRAINT pk_id_voo PRIMARY KEY(id),
	FOREIGN KEY (aeroporto_origem_id) REFERENCES aeroportos(id),
	FOREIGN KEY (aeroporto_destino_id) REFERENCES aeroportos(id)
);

DROP TABLE voos;

-- Inserts para a tabela aeroportos

INSERT INTO aeroportos (id, codigo, nome, cidade, pais) VALUES
(1, 'GRU', 'Aeroporto Internacional de São Paulo–Guarulhos', 'Guarulhos', 'Brasil'),
(2, 'GIG', 'Aeroporto Internacional do Rio de Janeiro–Galeão', 'Rio de Janeiro', 'Brasil'),
(3, 'BSB', 'Aeroporto Internacional de Brasília–Presidente Juscelino Kubitschek', 'Brasília', 'Brasil'),
(4, 'CNF', 'Aeroporto Internacional de Belo Horizonte–Confins', 'Confins', 'Brasil'),
(5, 'VCP', 'Aeroporto Internacional de Viracopos', 'Campinas', 'Brasil'),
(6, 'JFK', 'John F. Kennedy International Airport', 'New York', 'Estados Unidos'),
(7, 'LAX', 'Los Angeles International Airport', 'Los Angeles', 'Estados Unidos'),
(8, 'CDG', 'Charles de Gaulle Airport', 'Paris', 'França'),
(9, 'LHR', 'Heathrow Airport', 'London', 'Reino Unido'),
(10, 'DXB', 'Dubai International Airport', 'Dubai', 'Emirados Árabes Unidos');

-- Inserts para a tabela voos

INSERT INTO voos (id, aeroporto_origem_id, aeroporto_destino_id, data_partida, hora_partida, data_chegada, hora_chegada, companhia_aerea, preco, assentos_disponíveis) VALUES
(1, 1, 2, '2025-05-10', '10:00:00', '2025-05-10', '11:00:00', 'LATAM', 150.00, 100),
(2, 3, 1, '2025-05-12', '14:30:00', '2025-05-12', '16:00:00', 'GOL', 120.50, 80),
(3, 2, 4, '2025-05-15', '08:00:00', '2025-05-15', '09:30:00', 'Azul', 95.75, 120),
(4, 5, 3, '2025-05-18', '19:00:00', '2025-05-18', '20:45:00', 'LATAM', 180.20, 90),
(5, 1, 6, '2025-05-20', '22:00:00', '2025-05-21', '09:00:00', 'American Airlines', 800.00, 50),
(6, 7, 8, '2025-05-25', '15:00:00', '2025-05-26', '07:00:00', 'Air France', 950.50, 60),
(7, 9, 10, '2025-05-28', '09:30:00', '2025-05-28', '19:00:00', 'Emirates', 1200.00, 40),
(8, 4, 5, '2025-05-30', '11:30:00', '2025-05-30', '12:30:00', 'GOL', 75.90, 110),
(9, 2, 1, '2025-06-02', '16:45:00', '2025-06-02', '17:45:00', 'Azul', 135.40, 75),
(10, 3, 2, '2025-06-05', '07:00:00', '2025-06-05', '08:30:00', 'LATAM', 110.60, 95);

--Selects

SELECT * FROM voos;

SELECT * FROM usuarios;
 
SELECT * FROM aeroportos;

SELECT * FROM reservas;


DROP TABLE usuarios CASCADE;

INSERT INTO voos (id, aeroporto_origem_id, aeroporto_destino_id, data_partida, hora_partida, data_chegada, hora_chegada, companhia_aerea, preco, assentos_disponíveis) VALUES
(11, 1, 3, '2025-11-10', '06:00:00', '2025-11-10', '07:40:00', 'GOL', 210.00, 150),
(12, 3, 1, '2025-11-10', '09:00:00', '2025-11-10', '10:40:00', 'Azul', 225.50, 130),
(13, 2, 5, '2025-11-11', '12:15:00', '2025-11-11', '13:20:00', 'LATAM', 180.80, 115),
(14, 5, 2, '2025-11-11', '15:00:00', '2025-11-11', '16:05:00', 'GOL', 175.00, 140),
(15, 4, 1, '2025-11-15', '20:30:00', '2025-11-15', '21:50:00', 'Azul', 190.25, 100),
(16, 6, 9, '2025-11-18', '19:00:00', '2025-11-19', '07:00:00', 'British Airways', 1150.00, 45),
(17, 9, 6, '2025-11-20', '11:00:00', '2025-11-20', '14:00:00', 'American Airlines', 1250.00, 55),
(18, 8, 2, '2025-11-22', '23:00:00', '2025-11-23', '08:00:00', 'Air France', 1300.70, 38),
(19, 10, 1, '2025-11-25', '03:00:00', '2025-11-25', '18:00:00', 'Emirates', 1850.00, 60),
(20, 1, 7, '2025-11-28', '13:00:00', '2025-11-28', '22:00:00', 'Delta', 980.00, 70),
(21, 1, 4, '2025-12-01', '17:00:00', '2025-12-01', '18:10:00', 'LATAM', 145.00, 95),
(22, 2, 3, '2025-12-03', '09:45:00', '2025-12-03', '11:25:00', 'GOL', 165.50, 88),
(23, 5, 1, '2025-12-05', '21:00:00', '2025-12-05', '22:00:00', 'Azul', 99.90, 130),
(24, 6, 8, '2025-12-10', '10:00:00', '2025-12-10', '21:30:00', 'Delta', 1050.00, 42),
(25, 8, 6, '2025-12-12', '14:00:00', '2025-12-12', '16:30:00', 'Air France', 1100.00, 48),
(26, 9, 1, '2025-12-15', '08:00:00', '2025-12-15', '20:00:00', 'LATAM', 1400.00, 65),
(27, 1, 10, '2025-12-18', '01:00:00', '2025-12-18', '18:00:00', 'Emirates', 1990.80, 35),
(28, 7, 1, '2025-12-20', '18:00:00', '2025-12-21', '11:00:00', 'Delta', 1350.00, 50),
(29, 3, 4, '2025-12-22', '13:20:00', '2025-12-22', '14:20:00', 'Azul', 85.00, 110),
(30, 4, 2, '2025-12-28', '22:10:00', '2025-12-28', '23:40:00', 'GOL', 195.00, 77);








