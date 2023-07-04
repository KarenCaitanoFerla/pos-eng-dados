---1) Listar todos os dados das tabelas empregado, departamento e projeto
SELECT * FROM empregado

SELECT * FROM departamento

SELECT * FROM projeto

---2) Listar os projetos que acontecem em BH
SELECT * 
FROM projeto
WHERE nom_local = 'BH'

---3) Listar todos os empregados do sexo masculino que moram em MG
SELECT * 
FROM empregado
WHERE sex_empregado = 'M'
AND sig_uf = 'MG'