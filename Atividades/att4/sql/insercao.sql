
-- Insercao dos dados
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (1, 'J.K. Rowling', '1965-07-31');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (2, 'George R.R. Martin', '1948-09-20');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (3, 'J.R.R. Tolkien', '1892-01-03');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (1, 'Fantasia');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (2, 'Ficção Científica');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (3, 'Aventura');
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (1, 'Harry Potter e a Pedra Filosofal', 1, 1997);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (2, 'A Guerra dos Tronos', 2, 1996);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (3, 'O Senhor dos Anéis', 3, 1954);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (1, 1);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (1, 3);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (2, 1);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (2, 2);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (3, 1);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (3, 3);
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (1, 'Alice', 'alice@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (2, 'Bob', 'bob@example.com');
INSERT INTO Usuario (ID_Usuario, Nome, Email) VALUES (3, 'Charlie', 'charlie@example.com');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (1, 1, 1, '2024-07-01', '2024-07-10');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (2, 2, 2, '2024-07-05', '2024-07-15');
INSERT INTO Emprestimo (ID_Emprestimo, ID_Livro, ID_Usuario, Data_Emprestimo, Data_Devolucao) VALUES (3, 3, 3, '2024-07-10', NULL);

-- Minha parte
-- Disclaimer: Ainda não paguei a cadeira de banco de dados.
-- Por isso tá bem feinho

INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (4, 'Robert T. Kyosaki', '47-04-08');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (5, 'Olavo de Carvalho', '1947-04-29');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (6, 'Max Gunther', '1927-06-28');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (7, 'Gilberto Freire', '1900-3-15');
INSERT INTO Autor (ID_Autor, Nome, Data_Nascimento) VALUES (8, 'Dante Alighieri', '1265-6-13');

INSERT INTO Categoria (ID_Categoria, Nome) VALUES (4, 'Filosofia');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (5, 'Direito');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (6, 'Economia');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (7, 'História');
INSERT INTO Categoria (ID_Categoria, Nome) VALUES (8, 'Medicina');

INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (4, 'Pai rico pai pobre', 4, 1997);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (5, 'O mínimo pra você não ser um webnamorado', 5, 2013);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (6, 'Axiomas de Zurique', 6, 1985);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (7, 'Casa Grande e senzala', 7, 1933);
INSERT INTO Livro (ID_Livro, Titulo, ID_Autor, Ano_Publicacao) VALUES (8, 'Divina comédia', 8, 1321);

INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (4, 6);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (5, 4);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (6, 6);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (7, 7);
INSERT INTO Livro_Categoria (ID_Livro, ID_Categoria) VALUES (8, 1);