---1 - Liste o número de matrícula e nome do empregados e nome e parentesco de todos os dependentes. Considere também os funcionários que não tem dependentes.
SELECT e.num_matricula, 
e.nom_empregado, 
d.nom_dependente, 
d.dsc_parentesco
FROM empregado e
LEFT JOIN dependente d ON d.num_matricula = e.num_matricula

---2 - Liste o número de matrícula e nome dos empregados que não tem dependentes cadastrados.
SELECT e.num_matricula, 
e.nom_empregado, 
d.nom_dependente, 
d.dsc_parentesco
FROM empregado e
LEFT JOIN dependente d ON d.num_matricula = e.num_matricula
WHERE d.num_matricula is null

---3 - Listar os nomes dos projetos, os locais de execução, o departamento, e os gerentes responsáveis. Considere também os departamentos sem projeto e sem gerente.
SELECT p.nom_projeto, 
p.nom_local, 
d.nom_depto, 
nom_empregado
FROM projeto p
RIGHT JOIN departamento d on d.cod_depto = p.cod_depto
LEFT JOIN empregado e on e.num_matricula = d.num_matricula_gerente