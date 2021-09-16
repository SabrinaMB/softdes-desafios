# Documentação de usuário - Professor

## Adicionando usuários
1. Crie um arquivo "users.csv"
    1. Insira seu {nome} e o {tipo} de usuario que você é nesse arquivo, no formato "{nome}, {tipo}"
2. Rode o comando "python3 adduser.py"
## Adicionando desafios
1. Você terá que incluir um novo desafio na tabela QUIZ 
   1. Exemplo: inserir o quiz 3, que expira dia 21 de setembro de 2021, o nome do problema é "Problema 3", os testes que serão rodados são o 1, o 2 e o 3, o resultado de todos os testes deve ser 0 e as notas dadas serão a, b e c passando em cada um dos testes respectivamente 
   2. Comandos:
      1. sqlite3
      2. INSERT INTO QUIZ (numb, expire, problem, tests, results, diagnosis)
      VALUES(3, "2021-12-31 23:59:59", "Problema 3", [[1],[2],[3]],[0, 0, 0],["a","b","c"]);
      3. .exit