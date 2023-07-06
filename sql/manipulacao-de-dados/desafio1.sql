---1 - Considere os registros sem dados ao liste os filmes que estão sem link de foto 
SELECT * 
FROM filmes
WHERE dsc_link_foto is null

---2 - Liste nome e data de lançamento dos filmes que contenham a palavra 'Bela'
SELECT dsc_filme, dat_lancamento
FROM filmes
WHERE dsc_filme like '%bela%'

---3 - Liste apenas os nomes dos filmes que contenham a palavra 'Bela'  retirando os itens duplicados
SELECT DISTINCT dsc_filme
FROM filmes
WHERE dsc_filme like '%bela%'

---4 - Liste a descrição e a quantidade de votos dos filmes que tiveram mais de 1000 votos, ordenar pela quantidade de votos em ordem decrescente
SELECT dsc_filme, qtd_votos
FROM filmes
WHERE qtd_votos > 1000
ORDER BY qtd_votos DESC

---5 - Liste os filmes da série '007' com quantidade de votos acima de 3000 ou nota média acima de 65
SELECT * 
FROM filmes
WHERE dsc_filme like '%007%'
AND (qtd_votos > 3000
OR num_nota_media > 65)

---6 - Liste nome e o índice de popularidade dos 5 filmes da série '007' com maior popularidade
SELECT top 5 dsc_filme, num_popularidade
FROM filmes
WHERE dsc_filme like '%007%'
ORDER BY num_popularidade DESC