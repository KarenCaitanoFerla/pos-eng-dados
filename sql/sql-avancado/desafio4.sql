---1 - Listar os filmes que são do gênero Guerra ou do Gênero Ação
SELECT DISTINCT dsc_filme
FROM filmes f
JOIN filmes_genero fg on fg.id_filme = f.id_filme
JOIN generos g on g.id_genero = fg.id_genero
WHERE g.dsc_genero IN ('Guerra', 'Ação')

---2 - Listar os filmes que são do gênero Guerra e também do Gênero Ação
SELECT dsc_filme
FROM filmes f
JOIN filmes_genero fg on fg.id_filme = f.id_filme
JOIN generos g on g.id_genero = fg.id_genero
WHERE g.dsc_genero = 'Guerra'
INTERSECT
SELECT dsc_filme
FROM filmes f
JOIN filmes_genero fg on fg.id_filme = f.id_filme
JOIN generos g on g.id_genero = fg.id_genero
WHERE g.dsc_genero = 'Ação'


---3 - Listar os filmes que são do gênero Guerra e não são do Gênero Ação
SELECT dsc_filme
FROM filmes f
JOIN filmes_genero fg on fg.id_filme = f.id_filme
JOIN generos g on g.id_genero = fg.id_genero
WHERE g.dsc_genero = 'Guerra'
EXCEPT
SELECT dsc_filme
FROM filmes f
JOIN filmes_genero fg on fg.id_filme = f.id_filme
JOIN generos g on g.id_genero = fg.id_genero
WHERE g.dsc_genero = 'Ação'
