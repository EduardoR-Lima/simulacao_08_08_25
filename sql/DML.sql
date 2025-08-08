-- -----------------------------------------------------
-- Data for table `vida_mais_saude`.`cliente`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_saude`;
INSERT INTO `vida_mais_saude`.`cliente` (`id_cliente`, `nome`, `telefone`, `cpf`, `rua`, `numero`, `email`, `hash_senha`) VALUES (1, 'Guilherme Bento Tomás Assis', '85987871402', '18240503802', 'Rua Alto da Bela Vista', 124, 'guilherme-assis71@picolotoengenharia.com.br', 'scrypt:32768:8:1$XJ9NUOaI64tkbWig$283386b6d56aa3fc12359316b6e8e8ba90ac93af2a4e7a7580b4545bdd83280c976e3a5e22eec0959aa84f9c82655146e3cdd4037dd01337d72996355d02565c');
INSERT INTO `vida_mais_saude`.`cliente` (`id_cliente`, `nome`, `telefone`, `cpf`, `rua`, `numero`, `email`, `hash_senha`) VALUES (2, 'Mariane Santos', '85985759809', '59662051325', 'Rodovia BR-020 Km 4', 410, 'mariane.santos@gmail.com', 'scrypt:32768:8:1$lS48sp6eDDLIrHFw$a6bedb7bbd94e7c9a45929a4860da01600edb6c9f3a9ef7986cf3701d7f3c4f3e86612dccf3ca3c7201febc0728225a20e779f9ed02c901d2a1c617b9aa3476f');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_saude`.`indicador`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_saude`;
INSERT INTO `vida_mais_saude`.`indicador` (`id_indicador`, `tipo`, `valor`, `observacoes`, `id_cliente`, `data_registro`) VALUES (DEFAULT, 'Pressão', '140/80', 'Senti um pouco de dor de cabeça antes do café da manhã', 1, DEFAULT);
INSERT INTO `vida_mais_saude`.`indicador` (`id_indicador`, `tipo`, `valor`, `observacoes`, `id_cliente`, `data_registro`) VALUES (DEFAULT, 'Oxigenação', '96', NULL, 1, DEFAULT);
INSERT INTO `vida_mais_saude`.`indicador` (`id_indicador`, `tipo`, `valor`, `observacoes`, `id_cliente`, `data_registro`) VALUES (DEFAULT, 'Pressão', '13/9', NULL, 2, DEFAULT);

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_saude`.`especialidade`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_saude`;
INSERT INTO `vida_mais_saude`.`especialidade` (`id_especialidade`, `nome`) VALUES (1, 'Otorrinolaringologia');
INSERT INTO `vida_mais_saude`.`especialidade` (`id_especialidade`, `nome`) VALUES (2, 'Ortopedia');
INSERT INTO `vida_mais_saude`.`especialidade` (`id_especialidade`, `nome`) VALUES (3, 'Geriatria');
INSERT INTO `vida_mais_saude`.`especialidade` (`id_especialidade`, `nome`) VALUES (4, 'Cuidador');
INSERT INTO `vida_mais_saude`.`especialidade` (`id_especialidade`, `nome`) VALUES (5, 'Endocrinologia');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_saude`.`profissional`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_saude`;
INSERT INTO `vida_mais_saude`.`profissional` (`id_profissional`, `nome`, `telefone`, `id_especialidade`, `registro_profissional`, `descricao`) VALUES (1, 'Cristina da Silva Almeida', '85984100230', 1, '340578CRM/CE', 'Formada pela Universidade Federal do Ceará em 2010. Tenho 40 anos e atuo com o público idoso há mais de 10 anos');
INSERT INTO `vida_mais_saude`.`profissional` (`id_profissional`, `nome`, `telefone`, `id_especialidade`, `registro_profissional`, `descricao`) VALUES (2, 'Vinicius Benício Emanuel Ribeiro', '85997511633', 5, '521123CRM/CE', 'Especializado em endocrinologia desde 2015. Durante toda a minha carreira, me dediquei ao público idoso');
INSERT INTO `vida_mais_saude`.`profissional` (`id_profissional`, `nome`, `telefone`, `id_especialidade`, `registro_profissional`, `descricao`) VALUES (3, 'Hugo Bruno Melo', '85981106750', 4, NULL, 'Trabalho como cuidador há 10 anos. Sou muito disciplinado quanto as rotinas dos meus clientes e sempre tive muito zelo pelos meus clientes');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_saude`.`hora`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_saude`;
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (1, '07:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (2, '08:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (3, '09:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (4, '10:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (5, '11:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (6, '12:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (7, '13:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (8, '14:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (9, '15:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (10, '16:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (11, '17:00');
INSERT INTO `vida_mais_saude`.`hora` (`id_hora`, `valor`) VALUES (12, '18:00');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_saude`.`dia`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_saude`;
INSERT INTO `vida_mais_saude`.`dia` (`id_dia`, `nome`) VALUES (1, 'Segunda');
INSERT INTO `vida_mais_saude`.`dia` (`id_dia`, `nome`) VALUES (2, 'Terça');
INSERT INTO `vida_mais_saude`.`dia` (`id_dia`, `nome`) VALUES (3, 'Quarta');
INSERT INTO `vida_mais_saude`.`dia` (`id_dia`, `nome`) VALUES (4, 'Quinta');
INSERT INTO `vida_mais_saude`.`dia` (`id_dia`, `nome`) VALUES (5, 'Sexta');
INSERT INTO `vida_mais_saude`.`dia` (`id_dia`, `nome`) VALUES (6, 'Sábado');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_saude`.`agendamento`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_saude`;
INSERT INTO `vida_mais_saude`.`agendamento` (`id_agendamento`, `id_profissional`, `id_cliente`, `id_hora`, `id_dia`, `data`) VALUES (DEFAULT, 1, 1, 5, 3, '2025-08-13');
INSERT INTO `vida_mais_saude`.`agendamento` (`id_agendamento`, `id_profissional`, `id_cliente`, `id_hora`, `id_dia`, `data`) VALUES (DEFAULT, 2, 2, 7, 5, '2025-08-15');

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_saude`.`horario_disponivel`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_saude`;
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (1, 1);
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (5, 1);
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (9, 1);
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (2, 2);
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (7, 2);
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (10, 2);
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (1, 3);
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (3, 3);
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (7, 3);
INSERT INTO `vida_mais_saude`.`horario_disponivel` (`id_hora`, `id_profissional`) VALUES (9, 3);

COMMIT;


-- -----------------------------------------------------
-- Data for table `vida_mais_saude`.`dia_disponivel`
-- -----------------------------------------------------
START TRANSACTION;
USE `vida_mais_saude`;
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (1, 1);
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (3, 1);
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (5, 1);
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (1, 2);
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (4, 2);
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (5, 2);
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (1, 3);
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (2, 3);
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (4, 3);
INSERT INTO `vida_mais_saude`.`dia_disponivel` (`id_dia`, `id_profissional`) VALUES (5, 3);

COMMIT;

