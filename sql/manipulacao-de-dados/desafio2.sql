---1 - Liste o número de matrícula e nome do empregados e nome e parentesco de todos os dependentes
SELECT e.num_matricula, 
       e.nom_empregado, 
       d.nom_dependente, 
       d.dsc_parentesco
FROM empregado e
JOIN dependente d ON d.num_matricula = e.num_matricula

---2 - Liste nome dos departamentos com número de matrícula e nome de todos os funcionário. Ordene o resultado por departamento e nome do empregado.
SELECT nom_depto, 
       num_matricula, 
       nom_empregado
FROM departamento d
JOIN empregado e ON e.cod_depto = d.cod_depto
ORDER BY nom_depto, nom_empregado

---3 - Para cada departamento um dos funcionários tem a função de gerência. Liste nome dos departamentos com número de matrícula e nome do gerente responsável.
SELECT nom_depto, 
       num_matricula, 
       nom_empregado
FROM departamento d
JOIN empregado e ON e.num_matricula = d.num_matricula_gerente

---4 - Liste o número de matrícula e nome dos supervisores e número de matrícula e nome dos funcionários sob sua supervisão. Ordene os supervisores e empregados em ordem alfabética
SELECT sup.num_matricula as matricula_supervisor, 
       sup.nom_empregado as nome_supervisor, 
       e.num_matricula as matricula_empregado, 
       e.nom_empregado as nome_empregado
FROM empregado e
JOIN empregado sup ON e.num_matricula_supervisor = sup.num_matricula

---5 - Liste os funcionários dos projetos de BH com o total de horas alocado.  Exibir nome e local do projeto, número de matrícula e nome do empregado e o total de horas alocado.
SELECT p.nom_projeto, 
       p.nom_local, 
       e.num_matricula, 
       e.nom_empregado, 
       a.num_horas
FROM projeto p
JOIN alocacao a ON a.cod_projeto = p.cod_projeto
JOIN empregado e ON e.num_matricula = a.num_matricula
WHERE nom_local = 'BH'