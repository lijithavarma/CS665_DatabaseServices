/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.6.7-MariaDB : Database - employeemanagementsystemdb
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`employeemanagementsystemdb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;

USE `employeemanagementsystemdb`;

/*Table structure for table `employee` */

DROP TABLE IF EXISTS `employee`;

CREATE TABLE `employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `department_id` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `note` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `role_id` (`role_id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`),
  CONSTRAINT `employee_ibfk_3` FOREIGN KEY (`department_id`) REFERENCES `organization` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;

/*Data for the table `employee` */

insert  into `employee`(`id`,`user_id`,`role_id`,`department_id`,`status`,`note`,`code`) values 
(1,1,2,1,6,'employee1','code1'),
(2,1,3,2,3,'employee2','code2'),
(3,1,5,4,2,'employee3','code3'),
(4,2,4,2,4,'employee4','code4'),
(5,2,1,3,5,'employee5','code5'),
(6,3,3,2,2,'employee6','code6'),
(7,4,2,4,3,'employee7','code7');

/*Table structure for table `organization` */

DROP TABLE IF EXISTS `organization`;

CREATE TABLE `organization` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `summary` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `content` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3;

/*Data for the table `organization` */

insert  into `organization`(`id`,`title`,`summary`,`status`,`content`) values 
(1,'Consulting','cons',1,'This is consulting part'),
(2,'Finance','fina',2,'This is finance part'),
(3,'Management','mang',3,'This is management part'),
(4,'Organization 1','org1',4,'This is Organization 1'),
(5,'Organization 2','org2',5,'This is Organization 2'),
(6,'Organization 3','org3',6,'This is organization 3');

/*Table structure for table `role` */

DROP TABLE IF EXISTS `role`;

CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `type` varchar(255) NOT NULL,
  `content` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;

/*Data for the table `role` */

insert  into `role`(`id`,`title`,`description`,`type`,`content`) values 
(1,'Manager1','executive level','Executive','This is manger1'),
(2,'Manager2','executive level','Executive','This is manage2'),
(3,'Manager3','executive level','Executive','This is manager3'),
(4,'Manager4','executive level','Marketing manager','this is manager4'),
(5,'Manager5','executive level','Product manager','This is manager5'),
(6,'Manager6','executive level','Project manager','This is manager6');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3;

/*Data for the table `user` */

insert  into `user`(`id`,`role_id`,`first_name`,`last_name`,`username`,`email`,`dob`) values 
(1,1,'John','Smith','js1988','js1988@gmail.com','1988-11-01'),
(2,2,'Paul','Smith','ps1989','ps1989@gmail.com','1989-12-03'),
(3,3,'Robert','Johnson','rj1990','rj1990@gmail.com','1990-04-03'),
(4,4,'Richard','Garcia','rg1982','rg1982@gmail.com','1982-06-12'),
(5,5,'Charles','Miller','cm1991','cm1991@gmail.com','1991-04-24'),
(6,6,'Ronald','Lopez','rl1992','rl1992@gmail.com','1992-12-14');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
