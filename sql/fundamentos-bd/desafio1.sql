---1) O resultado traz a quantidade de votos e o nota média para o filme 'Matrix'.
SELECT id_filme, dsc_filme, qtd_votos ,num_nota_media
FROM filmes 
WHERE dsc_filme = 'Matrix'

---2) O resultado traz filmes quantidade de votos inferior a 1000 e nota média enter 80 e 90.
select id_filme, dsc_filme, qtd_votos ,num_nota_media
from filmes 
where qtd_votos < 1000
and num_nota_media > 80 
and num_nota_media < 90
