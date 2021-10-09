-- MySQL dump 10.13  Distrib 5.7.24, for osx10.9 (x86_64)
--
-- Host: localhost    Database: HospitalManagementSystem
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Appointment`
--

DROP TABLE IF EXISTS `Appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Appointment` (
  `appointmentID` int NOT NULL AUTO_INCREMENT,
  `patientID` int NOT NULL,
  `doctorID` int NOT NULL,
  `diseaseID` int NOT NULL,
  `roomID` int DEFAULT NULL,
  `type` varchar(15) NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date DEFAULT NULL,
  PRIMARY KEY (`appointmentID`),
  KEY `patientID` (`patientID`),
  KEY `doctorID` (`doctorID`),
  KEY `diseaseID` (`diseaseID`),
  KEY `roomID` (`roomID`),
  CONSTRAINT `appointment_ibfk_1` FOREIGN KEY (`patientID`) REFERENCES `Patient` (`patientID`),
  CONSTRAINT `appointment_ibfk_2` FOREIGN KEY (`doctorID`) REFERENCES `Doctor` (`doctorID`),
  CONSTRAINT `appointment_ibfk_3` FOREIGN KEY (`diseaseID`) REFERENCES `Disease` (`diseaseID`),
  CONSTRAINT `appointment_ibfk_4` FOREIGN KEY (`roomID`) REFERENCES `Room` (`roomID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Appointment`
--

LOCK TABLES `Appointment` WRITE;
/*!40000 ALTER TABLE `Appointment` DISABLE KEYS */;
INSERT INTO `Appointment` VALUES (1,1,1,1,NULL,'outpatient','2021-10-01',NULL),(2,2,2,2,101,'inpatient','2021-10-05',NULL),(3,3,4,3,102,'inpatient','2021-09-15','2021-09-30'),(4,4,1,1,NULL,'outpatient','2021-10-03',NULL),(5,5,5,4,103,'inpatient','1000-01-01','9999-12-31');
/*!40000 ALTER TABLE `Appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bill`
--

DROP TABLE IF EXISTS `Bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Bill` (
  `billID` int NOT NULL AUTO_INCREMENT,
  `appointmentID` int NOT NULL,
  `diseaseID` int NOT NULL,
  `amount` float DEFAULT NULL,
  PRIMARY KEY (`billID`),
  KEY `appointmentID` (`appointmentID`),
  KEY `diseaseID` (`diseaseID`),
  CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`appointmentID`) REFERENCES `Appointment` (`appointmentID`),
  CONSTRAINT `bill_ibfk_2` FOREIGN KEY (`diseaseID`) REFERENCES `Disease` (`diseaseID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bill`
--

LOCK TABLES `Bill` WRITE;
/*!40000 ALTER TABLE `Bill` DISABLE KEYS */;
INSERT INTO `Bill` VALUES (1,1,1,20),(2,2,3,50),(3,3,2,200.5),(4,5,3,999.99);
/*!40000 ALTER TABLE `Bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Disease`
--

DROP TABLE IF EXISTS `Disease`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Disease` (
  `diseaseID` int NOT NULL AUTO_INCREMENT,
  `diseaseName` varchar(50) NOT NULL,
  `diseaseDescription` varchar(255) DEFAULT NULL,
  `symptoms` varchar(255) NOT NULL,
  `deathRate` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`diseaseID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Disease`
--

LOCK TABLES `Disease` WRITE;
/*!40000 ALTER TABLE `Disease` DISABLE KEYS */;
INSERT INTO `Disease` VALUES (1,'none','patient shows no signs of illness','none','0'),(2,'Flu','patient has influenza','fever, cough','0.0005'),(3,'Covid','patient has covid-19','fever, sore muscles, loss of taste','0.02'),(4,'test','dummy entry','test','1');
/*!40000 ALTER TABLE `Disease` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Doctor`
--

DROP TABLE IF EXISTS `Doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Doctor` (
  `doctorID` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(20) NOT NULL,
  `lastName` varchar(20) NOT NULL,
  `birthDate` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phoneNumber` varchar(12) NOT NULL,
  `weight` float DEFAULT NULL,
  `height` float DEFAULT NULL,
  `address` varchar(255) NOT NULL,
  `hospitalName` varchar(100) DEFAULT NULL,
  `consultationCost` decimal(13,2) NOT NULL,
  PRIMARY KEY (`doctorID`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Doctor`
--

LOCK TABLES `Doctor` WRITE;
/*!40000 ALTER TABLE `Doctor` DISABLE KEYS */;
INSERT INTO `Doctor` VALUES (1,'Braylen','Stern','1989-03-15','female','braylen.stern@gmail.com','445-646-4268',120,68,'123 1st St','Test Hospital',500.00),(2,'Mitra','Holland','1978-08-04','female','mholland@yahoo.com','856-152-6256',105,64,'321 1st St','Test Hospital',600.00),(3,'Sneha','Miyake','1990-12-21','male','snehamiyake@gmail.com','256-958-6352',150,70,'555 41st St','Test Hospital',400.00),(4,'Amit','Moses','1000-01-01','male','Amit@yahoo.com','145-857-9431',100,60,'111 Fake Address Rd','Test Hospital',111111111.11),(5,'Vaiva','Mcalister','9999-12-31','female','new_email@gmail.com','778-965-4215',999,99,'999 Fake Address Rd','Test Hospital',999999999.99);
/*!40000 ALTER TABLE `Doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient`
--

DROP TABLE IF EXISTS `Patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Patient` (
  `patientID` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(20) NOT NULL,
  `lastName` varchar(20) NOT NULL,
  `birthDate` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phoneNumber` varchar(15) NOT NULL,
  `height` float DEFAULT NULL,
  `weight` float DEFAULT NULL,
  `address` varchar(200) NOT NULL,
  `SSN` varchar(11) NOT NULL,
  PRIMARY KEY (`patientID`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient`
--

LOCK TABLES `Patient` WRITE;
/*!40000 ALTER TABLE `Patient` DISABLE KEYS */;
INSERT INTO `Patient` VALUES (1,'Mike','Smith','1980-02-12','male','mike.smith@gmail.com','212-986-1314',68,180,'123 Main St','206-55-1024'),(2,'Mary','Jones','1976-04-22','female','mjones@yahoo.com','454-123-1812',60,105,'2788 Elm St','454-78-6598'),(3,'Duey','Cox','1958-02-14','male','dcox@gmail.com','703-376-2554',74,255,'1313 Mockingbird Lane','667-42-7412'),(4,'Meg','Griffin','1989-01-01','female','MGriffin66@yahoo.com','605-342-6529',63,133,'28 Spruce Drive','382-99-4658'),(5,'Elvis','Myers','1982-12-31','male','FatBoySlim@compuserve.com','778-965-4215',74,239,'2 Redwood Place','956-43-1614'),(6,'Dummy','Entry','1982-01-31','male','DummyEntry@compuserve.com','778-963-3315',70,230,'1 Redwood Place','956-23-1714');
/*!40000 ALTER TABLE `Patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Room`
--

DROP TABLE IF EXISTS `Room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Room` (
  `roomID` int NOT NULL AUTO_INCREMENT,
  `roomName` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  `roomDescription` varchar(255) DEFAULT NULL,
  `hospitalName` varchar(100) DEFAULT NULL,
  `roomCost` decimal(13,2) NOT NULL,
  PRIMARY KEY (`roomID`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Room`
--

LOCK TABLES `Room` WRITE;
/*!40000 ALTER TABLE `Room` DISABLE KEYS */;
INSERT INTO `Room` VALUES (101,'The Ward','Ward','It\'s the Ward','Test Hospital',100.00),(102,'Jerry','ICU','Intensive care unit','Test Hospital',250.00),(103,'RoomName?','Operating Theater','Operations happen here','Test Hospital',1000.00),(104,'DummyEntry','DummyRoom','Will use it to delete','Dummy Hospital',0.00);
/*!40000 ALTER TABLE `Room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RoomAssignments`
--

DROP TABLE IF EXISTS `RoomAssignments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RoomAssignments` (
  `staffID` int NOT NULL,
  `roomID` int NOT NULL,
  PRIMARY KEY (`staffID`,`roomID`),
  KEY `roomID` (`roomID`),
  CONSTRAINT `roomassignments_ibfk_1` FOREIGN KEY (`staffID`) REFERENCES `Staff` (`staffID`),
  CONSTRAINT `roomassignments_ibfk_2` FOREIGN KEY (`roomID`) REFERENCES `Room` (`roomID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RoomAssignments`
--

LOCK TABLES `RoomAssignments` WRITE;
/*!40000 ALTER TABLE `RoomAssignments` DISABLE KEYS */;
INSERT INTO `RoomAssignments` VALUES (1,101),(4,101),(5,101),(1,102),(2,102),(3,103);
/*!40000 ALTER TABLE `RoomAssignments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Staff`
--

DROP TABLE IF EXISTS `Staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Staff` (
  `staffID` int NOT NULL AUTO_INCREMENT,
  `firstName` varchar(20) NOT NULL,
  `lastName` varchar(20) NOT NULL,
  `birthDate` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phoneNumber` varchar(15) NOT NULL,
  `address` varchar(200) NOT NULL,
  `SSN` varchar(11) NOT NULL,
  `type` varchar(15) NOT NULL,
  `duties` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`staffID`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Staff`
--

LOCK TABLES `Staff` WRITE;
/*!40000 ALTER TABLE `Staff` DISABLE KEYS */;
INSERT INTO `Staff` VALUES (1,'Jerry','Jones','1965-05-01','male','JJ1965@gmail.com','305-911-8765','14 Cherry St','765-93-3324','ward boy','custodian'),(2,'Elizabeth','Ratchet','1970-01-15','female','NurseR@yahoo.com','410-556-1577','198 Pine St','542-19-4392','nurse','ER nurse'),(3,'Barry','Cosby','1989-06-18','male','bc1989@gmail.com','712-827-2141','1701 Starfleet Dr','612-26-1863','ward boy','custodian'),(4,'Margret','Perryman','1992-02-09','female','1992MP@yahoo.com','545-989-2165','11 Sycamore Drive','293-55-2819','nurse','Travel nurse'),(5,'Nacy','Spungeon','1966-08-18','female','BadNewsNurse@aol.com','212-827-8826','81 Sidney Lane','236-82-1392','nurse','Shift nurse');
/*!40000 ALTER TABLE `Staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Treatment`
--

DROP TABLE IF EXISTS `Treatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Treatment` (
  `treatmentID` int NOT NULL AUTO_INCREMENT,
  `treatmentName` varchar(50) NOT NULL,
  `treatmentDescription` varchar(255) DEFAULT NULL,
  `treatmentCost` decimal(13,2) DEFAULT NULL,
  `diseaseID` int DEFAULT NULL,
  PRIMARY KEY (`treatmentID`),
  KEY `diseaseID` (`diseaseID`),
  CONSTRAINT `treatment_ibfk_1` FOREIGN KEY (`diseaseID`) REFERENCES `Disease` (`diseaseID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Treatment`
--

LOCK TABLES `Treatment` WRITE;
/*!40000 ALTER TABLE `Treatment` DISABLE KEYS */;
INSERT INTO `Treatment` VALUES (1,'none','no treatment',0.00,1),(2,'ibuprofen','common anti-inflammatory',10.00,2),(3,'remdesivir','antiviral for treating covid',100.00,3),(4,'test','dummy entry',999.99,4);
/*!40000 ALTER TABLE `Treatment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-08 20:53:49
