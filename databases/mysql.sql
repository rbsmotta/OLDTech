/*-- Cria banco de dados
CREATE DATABASE OLDTech_Ltda;
*/
-- Seleciona banco de dados
USE OLDTech_Ltda;

/*-- Cria tabela vendas
CREATE TABLE IF NOT EXISTS vendas(
	nota_fiscal INTEGER AUTO_INCREMENT,
    nome_vendedor VARCHAR(30) NOT NULL,
    total FLOAT NOT NULL,
    CONSTRAINT dados_pkey PRIMARY KEY (nota_fiscal)
);
*/
SELECT * from vendas;