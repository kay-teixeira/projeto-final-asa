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









