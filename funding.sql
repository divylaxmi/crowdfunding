-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: funding
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`admin_id`),
  UNIQUE KEY `user_UNIQUE` (`user`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin@1','4321');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank`
--

DROP TABLE IF EXISTS `bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank` (
  `bid` int NOT NULL AUTO_INCREMENT,
  `aname` varchar(255) NOT NULL,
  `pan` varchar(255) NOT NULL,
  `bname` varchar(255) NOT NULL,
  `account` varchar(255) NOT NULL,
  `bmobile` varchar(255) NOT NULL,
  `user_email` varchar(255) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank`
--

LOCK TABLES `bank` WRITE;
/*!40000 ALTER TABLE `bank` DISABLE KEYS */;
INSERT INTO `bank` VALUES (3,'Sandhya','EGP144','BOI','45111011000258','8475978989','araj40132@gmail.com'),(4,'Priyanshu','EGP14458','SBI','338759977858','8475978989','sandhyak23901@gmail.com');
/*!40000 ALTER TABLE `bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact` (
  `cid` int NOT NULL AUTO_INCREMENT,
  `cname` varchar(255) DEFAULT NULL,
  `cemail` varchar(255) DEFAULT NULL,
  `csub` varchar(255) DEFAULT NULL,
  `cmobile` varchar(255) DEFAULT NULL,
  `cdesc` longtext,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (1,'Abhi','c@gmail.com','Awin','124587','something'),(2,'Abhi','c@gmail.com','Awin','124587','something');
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donor`
--

DROP TABLE IF EXISTS `donor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donor` (
  `did` int NOT NULL AUTO_INCREMENT,
  `dname` varchar(255) NOT NULL,
  `demail` varchar(255) NOT NULL,
  `dpan` varchar(255) DEFAULT NULL,
  `damt` int DEFAULT NULL,
  `caseid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donor`
--

LOCK TABLES `donor` WRITE;
/*!40000 ALTER TABLE `donor` DISABLE KEYS */;
INSERT INTO `donor` VALUES (5,'Abhi','ara@jh.com','Edww',500,'10'),(6,'priti','p@gmail.com','54789',500,'18'),(7,'priti','p@gmail.com','54789',500,'18'),(8,'priti','p@gmail.com','54789',500,'18'),(9,'priti','p@gmail.com','54789',500,'18'),(10,'Rudra','p@gmail.com','54789',500,'18'),(11,'Abhi','ara@jh.com','Eddwe',2500,'10'),(12,'Abhi','ara@jh.com','Eddwe',2500,'10'),(13,'Abhi','ara@jh.com','Eddwe',2500,'10'),(14,'Piyush','pysh@gmail.com','Edww',1000,'18'),(15,'Piyush','pysh@gmail.com','Edww',1000,'18'),(16,'Sandhya','s@gmail.com','Fhsy',500,'10'),(17,'Sandhya','s@gmail.com','Fhsy',500,'10'),(18,'Sandhya','s@gmail.com','Fhsy',500,'10'),(19,'Sandhya','s@gmail.com','Fhsy',500,'10'),(20,'priyanshu','prishu@gmail.com','POYTREW',5000,'17'),(21,'priyanshu','prishu@gmail.com','POYTREW',5000,'17'),(22,'priti','p@gmail.com','POYTREW',100000,'18'),(23,'Abhi','ara@jh.com','POYTREW',500,'10'),(24,'Abhi','ara@jh.com','Eddwe',500,'18'),(25,'Rudra','pysh@gmail.com','Eddwe',5000,'10'),(26,'Kamal','k@gmail.com','Fhsy',2500,'10'),(27,'Piyush','p@gmail.com','Edww',1000,'17'),(28,'priti','ara@jh.com','Eddwe',500,'18'),(29,'Abhi','ara@jh.com','POYTREW',1000,'10'),(30,'Abhi','ara@jh.com','POYTREW',1000,'10'),(31,'Abhi','ara@jh.com','POYTREW',1000,'10'),(32,'Abhi','ara@jh.com','POYTREW',1000,'10'),(33,'Abhi','ara@jh.com','POYTREW',1000,'10'),(34,'Abhi','ara@jh.com','POYTREW',1000,'10'),(35,'Abhi','ara@jh.com','POYTREW',1000,'10'),(36,'Abhi','ara@jh.com','POYTREW',1000,'10'),(37,'Abhi','ara@jh.com','POYTREW',1000,'10'),(38,'Abhi','ara@jh.com','POYTREW',1000,'10'),(39,'Abhi','ara@jh.com','POYTREW',1000,'10'),(40,'Abhi','ara@jh.com','POYTREW',1000,'10'),(41,'Abhi','ara@jh.com','POYTREW',1000,'10'),(42,'Abhi','ara@jh.com','POYTREW',1000,'10'),(43,'Abhi','ara@jh.com','POYTREW',1000,'10'),(44,'Abhi','ara@jh.com','Edww',5000,'18'),(45,'Abhi','p@gmail.com','Eddwe',500,'17'),(46,'Sandhya','s@gmail.com','POYTREW',10000,'18'),(47,'Sandhya','pysh@gmail.com','54789',5000,'18'),(48,'Abhi','ara@jh.com','Edww',2500,'19'),(49,'Abhi','ara@jh.com','Edww',2500,'19'),(50,'Piyush','p@gmail.com','POYTREW',5000,'17'),(51,'Abhi','ara@jh.com','Edww',10000,'19'),(52,'Sandhya','prishu@gmail.com','Edww',1000,'17'),(53,'Abhi','s@gmail.com','POYTREW',500,'18'),(54,'Abhi','prishu@gmail.com','POYTREW',500,'18'),(55,'Abhi','ara@jh.com','POYTREW',5000,'10');
/*!40000 ALTER TABLE `donor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fund_info`
--

DROP TABLE IF EXISTS `fund_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fund_info` (
  `fund_id` int NOT NULL AUTO_INCREMENT,
  `case_id` varchar(255) DEFAULT NULL,
  `pay_id` varchar(255) DEFAULT NULL,
  `ord_id` varchar(255) DEFAULT NULL,
  `fund_amt` int DEFAULT NULL,
  `payable` double DEFAULT NULL,
  `donor_id` int DEFAULT NULL,
  `pay_date` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`fund_id`),
  KEY `donor_id_idx` (`donor_id`),
  CONSTRAINT `donor_id` FOREIGN KEY (`donor_id`) REFERENCES `donor` (`did`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fund_info`
--

LOCK TABLES `fund_info` WRITE;
/*!40000 ALTER TABLE `fund_info` DISABLE KEYS */;
INSERT INTO `fund_info` VALUES (52,'10','pay_NAxPMqm4ZArfZg','order_NAxP88Xt7kpxOj',5000,4750,25,'2023-12-11'),(53,'10','pay_NBKTmWGZFVtVhb','order_NBKTXQK3uBsFsF',2500,2375,26,'2023-12-12'),(54,'17','pay_NBKVdlFBcmUncA','order_NBKVPMUGwxlOxE',1000,950,27,'2023-12-12'),(55,'18','pay_NBimsqZtLLF5ps','order_NBimdnqzgJOHGu',500,475,28,'2023-12-13'),(56,'10','pay_NBizX6hIafFMzc','order_NBizH2daV6kUdF',1000,950,43,'2023-12-13'),(57,'18','pay_NBkLJxgcoayFCj','order_NBkL6yNPJSk38d',5000,4750,44,'2023-12-13'),(58,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(59,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(60,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(61,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(62,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(63,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(64,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(65,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(66,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(67,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(68,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(69,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(70,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(71,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(72,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(73,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(74,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(75,'17','pay_NC8negylcD8onL','order_NC8n5nPa2mxoVh',500,475,45,'2023-12-14'),(76,'18','pay_NC9RHdiM8wYtYS','order_NC9R4nDveYAfyN',10000,9500,46,'2023-12-14'),(77,'18','pay_NC9gB7KL4X1whj','order_NC9fyv6cjYPcin',5000,4750,47,'2023-12-14'),(78,'19','pay_NCujTp4kUQgY2j','order_NCuhOvdoaDCkpC',2500,2375,49,'2023-12-16'),(79,'17','pay_NDTOHs7jOGQZN2','order_NDTO1TqTbKUBdf',5000,4750,50,'2023-12-17'),(80,'19','pay_NEFIrzApKKnU2Z','order_NEFIaeSrd8LbKu',10000,9500,51,'2023-12-19'),(81,'17','pay_NEueLUoR9qTtj3','order_NEudwIRw4Jgh3J',1000,950,52,'2023-12-21'),(82,'18','pay_NGrhmLrrrBKoCN','order_NGrhGLSUN78YZT',500,450,54,'2023-12-26'),(83,'10','pay_NKa7sFauwRyYRo','order_NKa7Ontb1K48OB',5000,4500,55,'2024-1-4');
/*!40000 ALTER TABLE `fund_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `caseid` int NOT NULL AUTO_INCREMENT,
  `pname` varchar(255) NOT NULL,
  `pid` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `blood` varchar(255) NOT NULL,
  `cdetails` varchar(255) NOT NULL,
  `paddress` varchar(255) NOT NULL,
  `hname` varchar(255) NOT NULL,
  `haddress` varchar(255) NOT NULL,
  `amt` double NOT NULL,
  `photoa` varchar(255) DEFAULT NULL,
  `photob` varchar(255) DEFAULT NULL,
  `photoc` varchar(255) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  `status` int DEFAULT '1',
  PRIMARY KEY (`caseid`),
  UNIQUE KEY `pid_UNIQUE` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (10,'Arya','98757899','Male','58','B+','Fever','kjahsub','baghus','njagsv',120000,'1carousel.jpg','2carousel.jpg','3carousel.jpg','araj40132@gmail.com',1),(17,'Raj','16489461','Male','58','B-','Asthama','kjahsub','baghus','njagsv',15000,'1701330453a.jpg','1701330453b.jpg','1701330453c.jpg','araj40132@gmail.com',0),(18,'Rani','898745789','Female','25','Ab-','Cough','Ranchi','Apollo','Ranchi',100000,'1701673374a.jpg','1701673374b.jpg','1701673374c.jpg','sandhyak23901@gmail.com',1),(19,'Seema','578468797895','Female','32','o+','Cold','Patna','Aims','Patna',100000,'1702654758a.jpg','1702654758b.jpg','1702654758c.jpg','sandhyak23901@gmail.com',1);
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photo`
--

DROP TABLE IF EXISTS `photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `photo` (
  `photoid` int NOT NULL AUTO_INCREMENT,
  `photoa` varchar(255) DEFAULT NULL,
  `photob` varchar(255) DEFAULT NULL,
  `photoc` varchar(255) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`photoid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photo`
--

LOCK TABLES `photo` WRITE;
/*!40000 ALTER TABLE `photo` DISABLE KEYS */;
INSERT INTO `photo` VALUES (1,'2carousel.jpg','1carousel.jpg','3carousel.jpg','araj40132@gmail.com'),(2,'2carousel.jpg','1carousel.jpg','3carousel.jpg','araj40132@gmail.com'),(3,'1700148450.jpg','1700148450.jpg','1700148450.jpg','araj40132@gmail.com'),(4,'1700148660.jpg','1700148660.1carousel','1700148660.jpg','araj40132@gmail.com'),(5,'2carousel.jpg','3carousel.jpg','1carousel.jpg','araj40132@gmail.com');
/*!40000 ALTER TABLE `photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile` (
  `proid` int NOT NULL AUTO_INCREMENT,
  `propic` varchar(255) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`proid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (8,'1701330453b.jpg','araj40132@gmail.com'),(14,'trainer-3.jpg','sandhyak23901@gmail.com');
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `name` varchar(255) NOT NULL,
  `gid` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Abhishek Raj','24578928','7750057588','araj40132@gmail.com','81dc9bdb52d04dc20036dbd8313ed055'),('Ranjan Kumar','5878998799','7750057588','rajkumar40317306@gmail.com','81dc9bdb52d04dc20036dbd8313ed055'),('Sandhya ','879875248','578954789','sandhyak23901@gmail.com','81dc9bdb52d04dc20036dbd8313ed055');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-19 14:11:46
