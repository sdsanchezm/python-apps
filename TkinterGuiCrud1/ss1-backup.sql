-- MySQL dump 10.17  Distrib 10.3.21-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: ss1
-- ------------------------------------------------------
-- Server version	10.3.21-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `ss1`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `ss1` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `ss1`;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Employee` (
  `name1` varchar(255) DEFAULT NULL,
  `number1` varchar(255) DEFAULT NULL,
  `kw1` int(5) DEFAULT NULL,
  `idq` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idq`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES ('kraus','12221',121,1),('konrad','ljsd123',344,2),('konrad','ljsd123',344,3),('merk','ljs523',998,4),('oply','1ew21',556,5),('merk','ljs523',998,6),('merk','ljs523',998,7),('banu','ee998',332,8),('banu','ee998',332,9),('cleaire','ee218',152,12),('cleaire','ee218',152,13),('cleaire','ee218',152,14),('cleaire','ee218',152,15),('cleaire','ee218',152,16),('cleaire','ee218',152,17),('cleaire','ee218',152,18),('cppre','1et18',102,19),('cppre','1et18',102,20),('cppre','1et18',102,21),('cppre','1et18',102,22),('cppre','1et18',102,23),('cxyqe','o18q',120,24),('cxyqe','o18q',120,25),('cxyqe','o18q',120,26),('cxyqe','o18q',120,27),('cxyqe','o18q',120,28),('cxyqe','o18q',120,29),('cxyqe','o18q',120,30),('cxyqe','o18q',120,31),('cxyqe','o18q',120,32),('cxyqe','o18q',120,33),('cyyye','21tt',444,34),('cyyye','21tt',444,35),('cyyye','21tt',444,36),('cyyye','21tt',444,37),('cyyye','21tt',778,38),('cyyye','21tt',778,39),('cyyye','21tt',778,40),('cyyye','21tt',778,41),('cyyye','21tt',778,42),('cyyye','21tt',778,43),('cyyye','21tt',778,44),('cyyye','21tt',778,45),('cyyye','21tt',778,46),('cyyye','21tt',778,47),('cyyye','21tt',778,48),('cyyye','21tt',778,49),('cyyye','21tt',778,50),('kraus','x21xx',2121,51),('ppyyg','245a',778,52),('kraus','x21xx',2121,53),('ppyyg','245a',778,54),('ppyyg','245a',778,55),('ppyyg','245a',778,56),('ppyyg','245a',778,57),('ppyyg','245a',778,58),('ppyyg','245a',778,59),('ppyyg','245a',778,60),('tturk','88w',445,61),('ppyyg','245a',778,62),('ppyyg','245a',778,64),('tturk','88w',445,65),('ppyyg','245a',778,66),('tturk','88w',445,67),('kraus','32ew',445,68),('ppyyg','245a',778,69),('tturk','88w',445,70),('jamecho','21ee',9998,71),('ppyyg','245a',778,72),('tturk','88w',445,73),('korken','32yy',9997,74),('ppyyg','245a',778,75),('tturk','88w',445,76),('ppyyg','245a',778,78),('tturk','88w',445,79),('jalal','21332',998,80),('banu','ee998',332,81),('banu','ee998',332,83),('ppyyg','245a',778,84),('tturk','88w',445,85),('Jara','2121w',4321,86),('kokot','915g',228,87),('kortx','11pw',7777,88),('Jara','2121qq',323232,89),('cacarot','21xx',555,90),('kortx','11pw',7777,91),('Jajar','2121wq',8887,92),('cacarot','21xx',555,93),('cacarot','21xx',555,94),('cacarot','21xx',555,95),('cacarot','21xx',555,96),('cacarot','21xx',555,97),('cacarot','21xx',555,98),('cacarot','21xx',555,99),('cacarot','21xx',555,100),('kortz','21p21',8877,101),('hocken','Pork21',6655,102),('banu','ee998',332,103),('banu','ee998',332,104);
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-02 17:16:00
