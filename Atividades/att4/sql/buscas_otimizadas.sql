-- Disclaimer: Ainda não paguei a cadeira de banco de dados.
-- Por isso tá bem feinho

SELECT Autor.Nome, Livro.Titulo
FROM Autor 
INNER JOIN livro ON Autor.ID_Autor = Livro.ID_Autor;

SELECT Emprestimo.ID_Emprestimo, Usuario.nome 
FROM Emprestimo
INNER JOIN Usuario ON Emprestimo.ID_Usuario = Usuario.ID_Usuario;

SELECT Livro.Titulo, Categoria.Nome 
FROM Livro, Livro_Categoria
JOIN Categoria ON Livro_Categoria.ID_Categoria = Categoria.ID_Categoria
WHERE Livro.ID_Livro = Livro_Categoria.ID_Livro;

SELECT Livro.Titulo, Usuario.Nome 
FROM Livro
join Usuario on Usuario.ID_Usuario = Emprestimo.ID_Usuario
join Emprestimo on Emprestimo.livro = Livro.ID_Livro;

SELECT Autor.Nome, Livro.Titulo 
FROM Autor
join Livro on Autor.ID_Autor = Livro.ID_Autor;