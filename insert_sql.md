insert  into `employee`(`id`,`user_id`,`role_id`,`department_id`,`status`,`note`,`code`) values 
(1,1,2,1,6,'employee1','code1'),
(2,1,3,2,3,'employee2','code2'),
(3,1,5,4,2,'employee3','code3'),
(4,2,4,2,4,'employee4','code4'),
(5,2,1,3,5,'employee5','code5'),
(6,3,3,2,2,'employee6','code6'),
(7,4,2,4,3,'employee7','code7');


insert  into `organization`(`id`,`title`,`summary`,`status`,`content`) values 
(1,'Consulting','cons',1,'This is consulting part'),
(2,'Finance','fina',2,'This is finance part'),
(3,'Management','mang',3,'This is management part'),
(4,'Organization 1','org1',4,'This is Organization 1'),
(5,'Organization 2','org2',5,'This is Organization 2'),
(6,'Organization 3','org3',6,'This is organization 3');


insert  into `role`(`id`,`title`,`description`,`type`,`content`) values 
(1,'Manager1','executive level','Executive','This is manger1'),
(2,'Manager2','executive level','Executive','This is manage2'),
(3,'Manager3','executive level','Executive','This is manager3'),
(4,'Manager4','executive level','Marketing manager','this is manager4'),
(5,'Manager5','executive level','Product manager','This is manager5'),
(6,'Manager6','executive level','Project manager','This is manager6');


insert  into `user`(`id`,`role_id`,`first_name`,`last_name`,`username`,`email`,`dob`) values 
(1,1,'John','Smith','js1988','js1988@gmail.com','1988-11-01'),
(2,2,'Paul','Smith','ps1989','ps1989@gmail.com','1989-12-03'),
(3,3,'Robert','Johnson','rj1990','rj1990@gmail.com','1990-04-03'),
(4,4,'Richard','Garcia','rg1982','rg1982@gmail.com','1982-06-12'),
(5,5,'Charles','Miller','cm1991','cm1991@gmail.com','1991-04-24'),
(6,6,'Ronald','Lopez','rl1992','rl1992@gmail.com','1992-12-14');