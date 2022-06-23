-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.6.7-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table mlb.batter
CREATE TABLE IF NOT EXISTS `batter` (
  `bID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Date_birth` date DEFAULT NULL,
  `Age` int(10) unsigned DEFAULT NULL,
  `At_bat` int(10) unsigned DEFAULT NULL,
  `Hits` int(10) unsigned DEFAULT NULL,
  `Bat_avg` float unsigned DEFAULT NULL,
  `RBI` int(10) unsigned DEFAULT NULL,
  `Home_runs` int(10) unsigned DEFAULT NULL,
  `Walks` int(10) unsigned DEFAULT NULL,
  `Position` varchar(2) DEFAULT NULL,
  `tID` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`bID`),
  KEY `FK_batter_team` (`tID`),
  CONSTRAINT `FK_batter_team` FOREIGN KEY (`tID`) REFERENCES `team` (`tID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

-- Dumping data for table mlb.batter: ~0 rows (approximately)
DELETE FROM `batter`;
/*!40000 ALTER TABLE `batter` DISABLE KEYS */;
INSERT INTO `batter` (`bID`, `Name`, `Date_birth`, `Age`, `At_bat`, `Hits`, `Bat_avg`, `RBI`, `Home_runs`, `Walks`, `Position`, `tID`) VALUES
	(1, 'Cedric Mullins', '1994-10-01', 27, 33, 12, 0.364, 17, 2, 3, 'CF', 1),
	(2, 'Ryan Mountcastle', '1997-02-18', 25, 24, 7, 0.292, 3, 1, 1, '1B', 1),
	(3, 'Trey Mancini', '1992-03-18', 30, 49, 31, 0.633, 28, 0, 1, '1B', 1),
	(4, 'Rafaei Devers', '1996-10-24', 25, 26, 9, 0.346, 5, 1, 1, '3B', 2),
	(5, 'Mike Trout', '1991-08-07', 30, 23, 6, 0.261, 2, 2, 6, 'CF', 4),
	(6, 'Nolan Arenado', '1991-04-16', 31, 23, 10, 0.435, 12, 4, 3, '3B', 3),
	(7, 'Austin Hays', '1995-07-05', 26, 33, 7, 0.212, 0, 0, 6, 'LF', 1),
	(8, 'Ramon Urias', '1994-06-03', 27, 32, 5, 0.156, 1, 0, 2, 'SS', 1),
	(9, 'Anthony Satander', '1994-10-19', 27, 26, 7, 0.269, 1, 1, 8, 'RF', 1),
	(10, 'Jorge Mateo', '1995-06-23', 26, 30, 8, 0.267, 3, 0, 4, 'SS', 1),
	(11, 'Bo Bichette', '1998-02-05', 24, 45, 10, 0.222, 1, 1, 0, 'SS', 7),
	(12, 'George Springer', '1989-09-19', 32, 41, 11, 0.268, 5, 2, 2, 'CF', 7),
	(13, 'Vladimir Guerrero Jr.', '1999-03-16', 23, 38, 11, 0.289, 10, 5, 2, '1B', 7),
	(14, 'Lourdes Gurriel Jr.', '1993-10-10', 28, 36, 11, 0.306, 5, 0, 2, 'LF', 7),
	(15, 'Matt Chapman', '1993-04-28', 28, 31, 7, 0.226, 7, 2, 5, '3B', 7),
	(16, 'Santiago Espinal', '1994-11-13', 27, 31, 8, 0.258, 4, 0, 3, '2B', 7),
	(17, 'Alejandro Kirk', '1998-11-06', 23, 26, 5, 0.192, 1, 0, 5, 'C', 7),
	(18, 'Wander Franco', '2001-03-01', 21, 42, 16, 0.381, 5, 0, 1, 'SS', 5),
	(19, 'Randy Arozarena', '1995-02-28', 27, 38, 9, 0.237, 2, 0, 0, 'RF', 5),
	(20, 'Brandon Lowe', '1994-07-06', 27, 38, 8, 0.211, 6, 3, 5, '2B', 5),
	(21, 'Manuel Margot', '1994-09-28', 27, 30, 11, 0.367, 5, 0, 3, 'RF', 5),
	(22, 'Yandy Diaz', '1991-08-08', 30, 29, 6, 0.207, 2, 0, 6, '1B', 5),
	(23, 'Josh Lowe', '1998-02-02', 24, 29, 4, 0.128, 1, 0, 5, 'CF', 5),
	(24, 'Ji-Man Choi', '1991-05-19', 30, 22, 10, 0.455, 7, 2, 9, '1B', 5),
	(25, 'Enrique Hernandez', '1991-08-24', 30, 28, 7, 0.184, 4, 1, 5, 'CF', 2),
	(26, 'J.D Martinez', '1987-08-21', 34, 32, 8, 0.25, 6, 1, 4, 'DH', 2),
	(27, 'Xander Bogaerts', '1992-01-10', 29, 31, 9, 0.29, 4, 1, 2, 'SS', 2),
	(28, 'Bobby Dalbec', '1995-06-29', 26, 30, 5, 0.167, 1, 1, 2, '1B', 2),
	(29, 'Alex Verdugo', '1006-05-15', 25, 30, 9, 8, 3, 0, 4, 'LF', 2),
	(30, 'Josh Donaldson', '1985-12-08', 36, 40, 8, 0.2, 3, 1, 3, '3B', 6),
	(31, 'Giancarlo Stanton', '1989-11-08', 32, 38, 10, 0.263, 8, 2, 1, 'DH', 6),
	(32, 'Aaron Judge', '1992-04-26', 29, 35, 9, 0.257, 1, 1, 5, 'RF', 6),
	(33, 'Anthony Rizzo', '1989-08-08', 32, 33, 7, 0.212, 8, 3, 5, '1B', 6),
	(34, 'Gleyber Torres', '1996-12-13', 25, 31, 7, 0.161, 2, 1, 2, '2B', 6),
	(35, 'Joey Gallo', '1993-11-19', 28, 29, 4, 0.138, 0, 0, 6, 'LF', 6),
	(36, 'DJ Lemahieu', '1988-07-13', 33, 28, 9, 0.321, 2, 1, 3, '2B', 6),
	(37, 'Aaron Hicks', '1989-02-10', 32, 27, 9, 0.333, 2, 1, 5, 'CF', 6),
	(38, 'Shohei Ohtani', '1994-07-05', 27, 49, 10, 0.204, 7, 3, 1, 'SP', 4),
	(39, 'Jared Walsh', '1993-07-30', 28, 31, 11, 0.227, 6, 2, 2, '1B', 4),
	(40, 'Jo Adell', '1999-04-08', 23, 30, 5, 0.167, 7, 3, 1, 'CF', 4),
	(41, 'Anthony Rendon', '1990-06-06', 31, 27, 5, 0.185, 3, 1, 5, '3B', 4),
	(42, 'Brandon Marsh', '1997-12-18', 24, 23, 6, 0.261, 8, 1, 3, 'CF', 4),
	(43, 'Dylan Carlson', '1998-10-23', 23, 33, 6, 0.182, 2, 0, 1, 'RF', 3),
	(44, 'Paul Goldschmidt', '1987-09-10', 34, 29, 4, 0.138, 1, 0, 6, '1B', 3),
	(45, 'Harrison Bader', '1994-06-03', 27, 29, 7, 0.241, 2, 0, 1, 'CF', 3),
	(46, 'Tyler O\'Neill', '1995-06-22', 26, 29, 7, 0.276, 6, 1, 4, 'LF', 3),
	(47, 'Tommy Edman', '1995-05-09', 26, 27, 9, 0.333, 5, 3, 3, '2B', 3),
	(48, 'Paul DeJong', '1993-08-02', 28, 24, 4, 0.167, 3, 1, 4, 'SS', 3);
/*!40000 ALTER TABLE `batter` ENABLE KEYS */;

-- Dumping structure for table mlb.conference
CREATE TABLE IF NOT EXISTS `conference` (
  `cID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL,
  `sID` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`cID`),
  KEY `FK_conference_sport` (`sID`),
  CONSTRAINT `FK_conference_sport` FOREIGN KEY (`sID`) REFERENCES `sport` (`sID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

-- Dumping data for table mlb.conference: ~2 rows (approximately)
DELETE FROM `conference`;
/*!40000 ALTER TABLE `conference` DISABLE KEYS */;
INSERT INTO `conference` (`cID`, `Name`, `Year`, `sID`) VALUES
	(1, 'American Leauge', 1901, 1),
	(2, 'National League', 1876, 1);
/*!40000 ALTER TABLE `conference` ENABLE KEYS */;

-- Dumping structure for table mlb.division
CREATE TABLE IF NOT EXISTS `division` (
  `dID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `conf_name` varchar(50) DEFAULT NULL,
  `div_name` varchar(50) DEFAULT NULL,
  `cID` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`dID`),
  KEY `FK_division_conference` (`cID`),
  CONSTRAINT `FK_division_conference` FOREIGN KEY (`cID`) REFERENCES `conference` (`cID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table mlb.division: ~3 rows (approximately)
DELETE FROM `division`;
/*!40000 ALTER TABLE `division` DISABLE KEYS */;
INSERT INTO `division` (`dID`, `conf_name`, `div_name`, `cID`) VALUES
	(1, 'AL', 'East', 1),
	(2, 'NL', 'Central', 2),
	(3, 'AL', 'West', 1);
/*!40000 ALTER TABLE `division` ENABLE KEYS */;

-- Dumping structure for table mlb.manager
CREATE TABLE IF NOT EXISTS `manager` (
  `mID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) DEFAULT NULL,
  `Wins` int(10) unsigned DEFAULT NULL,
  `Loses` int(10) unsigned DEFAULT NULL,
  `tID` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`mID`),
  KEY `FK_manager_team` (`tID`),
  CONSTRAINT `FK_manager_team` FOREIGN KEY (`tID`) REFERENCES `team` (`tID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Dumping data for table mlb.manager: ~7 rows (approximately)
DELETE FROM `manager`;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
INSERT INTO `manager` (`mID`, `Name`, `Wins`, `Loses`, `tID`) VALUES
	(1, 'Brandon Hyde', 138, 269, 1),
	(2, 'Alex Cora', 293, 214, 2),
	(3, 'Charlie Montoyo', 203, 202, 7),
	(4, 'Joe Maddon', 1369, 1194, 4),
	(5, 'Kevin Cash', 566, 486, 5),
	(6, 'Aaron Boone', 342, 224, 6),
	(7, 'Oliver Marmol', 11, 9, 3);
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;

-- Dumping structure for table mlb.pitcher
CREATE TABLE IF NOT EXISTS `pitcher` (
  `pID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Date_birth` date DEFAULT NULL,
  `Age` int(10) unsigned DEFAULT NULL,
  `Games_pitched` int(10) unsigned DEFAULT NULL,
  `Wins` int(10) unsigned DEFAULT NULL,
  `Loses` int(10) unsigned DEFAULT NULL,
  `Saves` int(10) unsigned DEFAULT NULL,
  `Batters_faced` int(10) unsigned DEFAULT NULL,
  `Hits` int(10) unsigned DEFAULT NULL,
  `Strikeouts` int(10) unsigned DEFAULT NULL,
  `Opp_avg` float unsigned DEFAULT NULL,
  `IP` double unsigned DEFAULT NULL,
  `Earned_runs` int(11) unsigned DEFAULT NULL,
  `ERA` double unsigned DEFAULT NULL,
  `tID` int(10) unsigned NOT NULL DEFAULT 0,
  PRIMARY KEY (`pID`),
  KEY `FK_pitcher_team` (`tID`),
  CONSTRAINT `FK_pitcher_team` FOREIGN KEY (`tID`) REFERENCES `team` (`tID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

-- Dumping data for table mlb.pitcher: ~23 rows (approximately)
DELETE FROM `pitcher`;
/*!40000 ALTER TABLE `pitcher` DISABLE KEYS */;
INSERT INTO `pitcher` (`pID`, `Name`, `Date_birth`, `Age`, `Games_pitched`, `Wins`, `Loses`, `Saves`, `Batters_faced`, `Hits`, `Strikeouts`, `Opp_avg`, `IP`, `Earned_runs`, `ERA`, `tID`) VALUES
	(1, 'John Means', '1993-04-24', 28, 2, 6, 0, 0, 38, 10, 11, 0.263, 11.2, 8, 6.17, 1),
	(2, 'Adam Wainwright', '1981-08-30', 40, 2, 1, 1, 0, 42, 13, 13, 0.312, 10.1, 4, 3.48, 3),
	(3, 'Nathan Eovaldi', '1990-02-13', 32, 2, 1, 0, 0, 40, 9, 13, 0.225, 10, 5, 4.5, 2),
	(4, 'Shohei Ohtani', '1994-04-07', 27, 2, 1, 2, 0, 38, 12, 15, 0.316, 8.2, 11, 11.43, 4),
	(5, 'Jordan Lyles', '1990-10-19', 31, 2, 0, 1, 0, 40, 13, 6, 0.325, 10.1, 6, 5.23, 1),
	(6, 'Bruce Zimmermann', '1995-02-09', 27, 2, 0, 0, 0, 33, 7, 10, 0.212, 9, 0, 0, 1),
	(7, 'Dillon Tate ', '1994-05-01', 27, 5, 0, 1, 0, 21, 3, 5, 0.143, 6.1, 1, 1.42, 1),
	(8, 'Bryan Baker', '1994-12-02', 27, 4, 0, 0, 0, 15, 2, 6, 0.133, 4.2, 1, 1.93, 1),
	(9, 'Michael Wacha', '1991-07-01', 30, 2, 0, 1, 0, 29, 3, 9, 0.103, 9.1, 1, 0.96, 2),
	(13, 'Tanner Houck', '1996-06-29', 25, 2, 1, 0, 0, 31, 11, 7, 0.258, 9, 3, 3, 2),
	(14, 'Jake Diekman', '1987-01-21', 35, 4, 0, 0, 1, 10, 1, 7, 0.1, 3, 0, 0, 2),
	(15, 'Gerrit Cole ', '1990-09-08', 31, 2, 0, 2, 0, 36, 8, 9, 0.222, 9.2, 6, 5.59, 6),
	(16, 'Nestor Cortes', '1994-12-10', 27, 2, 0, 0, 0, 34, 6, 17, 0.176, 9.1, 0, 0, 6),
	(17, 'Chad Green', '1991-05-24', 30, 5, 0, 1, 0, 18, 4, 3, 0.222, 5.1, 0, 0, 6),
	(18, 'Corey Kluber', '1986-04-10', 36, 2, 0, 0, 0, 35, 7, 9, 0.2, 9.2, 2, 1.86, 5),
	(19, 'Drew Rasmussen', '1995-07-27', 26, 2, 0, 1, 0, 35, 8, 5, 0.229, 9, 5, 5, 5),
	(20, 'Josh Fleming', '1996-05-18', 25, 2, 1, 1, 0, 29, 10, 11, 0.345, 6.2, 3, 4.05, 5),
	(21, 'Alek Monoah', '1998-01-09', 24, 2, 2, 0, 0, 39, 5, 13, 0.128, 12, 2, 1.5, 7),
	(23, 'Hyun Jin Ryu', '1987-03-25', 35, 2, 0, 1, 0, 33, 11, 5, 0.333, 7.1, 11, 13.5, 7),
	(26, 'Jordan Romano', '1993-04-21', 28, 6, 0, 0, 6, 20, 3, 6, 0.15, 6, 0, 0, 7),
	(27, 'Miles Mikolas', '1998-08-23', 33, 2, 1, 0, 0, 39, 9, 8, 0.231, 10.1, 3, 2.61, 3),
	(32, 'Steven Matz', '1991-05-29', 30, 2, 1, 1, 0, 38, 12, 11, 0.316, 8.2, 7, 7.27, 3),
	(35, 'Noah Syndergaard', '1992-08-29', 29, 2, 2, 0, 0, 40, 7, 5, 0.175, 11.1, 2, 1.59, 4);
/*!40000 ALTER TABLE `pitcher` ENABLE KEYS */;

-- Dumping structure for table mlb.sport
CREATE TABLE IF NOT EXISTS `sport` (
  `sID` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) DEFAULT NULL,
  `Commissioner` varchar(50) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL,
  PRIMARY KEY (`sID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Dumping data for table mlb.sport: ~1 rows (approximately)
DELETE FROM `sport`;
/*!40000 ALTER TABLE `sport` DISABLE KEYS */;
INSERT INTO `sport` (`sID`, `Name`, `Commissioner`, `Year`) VALUES
	(1, 'MLB', 'Rob Manfred', 1876);
/*!40000 ALTER TABLE `sport` ENABLE KEYS */;

-- Dumping structure for table mlb.team
CREATE TABLE IF NOT EXISTS `team` (
  `tID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `City` varchar(50) DEFAULT NULL,
  `Team_name` varchar(50) DEFAULT NULL,
  `State` varchar(50) DEFAULT NULL,
  `Year` int(11) DEFAULT NULL,
  `At_bat` int(11) DEFAULT NULL,
  `Hits` int(11) DEFAULT NULL,
  `Bat_avg` float DEFAULT NULL,
  `RBI` int(11) DEFAULT NULL,
  `Wins` int(10) unsigned DEFAULT NULL,
  `Loses` int(10) unsigned DEFAULT NULL,
  `dID` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`tID`),
  KEY `FK_team_division` (`dID`),
  CONSTRAINT `FK_team_division` FOREIGN KEY (`dID`) REFERENCES `division` (`dID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

-- Dumping data for table mlb.team: ~7 rows (approximately)
DELETE FROM `team`;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` (`tID`, `City`, `Team_name`, `State`, `Year`, `At_bat`, `Hits`, `Bat_avg`, `RBI`, `Wins`, `Loses`, `dID`) VALUES
	(1, 'Baltimore', 'Orioles', 'Maryland', 1901, 230, 45, 0.196, 14, 10, 7, 1),
	(2, 'Boston', 'RedSox', 'Massachusetts', 1882, 238, 52, 0.218, 30, 5, 9, 1),
	(3, 'St.Louis', 'Cardinals', 'Missouri', 1990, 199, 54, 0.271, 36, 5, 3, 2),
	(4, 'LosAngeles', 'Angels', 'California', 1966, 261, 63, 0.241, 33, 7, 5, 3),
	(5, 'TampaBay', 'Rays', 'Florida', 1998, 370, 91, 0.246, 45, 5, 6, 1),
	(6, 'NewYork', 'Yankees', 'New York', 1903, 328, 75, 0.229, 28, 5, 7, 1),
	(7, 'Toranto', 'BlueJays', 'Canada', 1977, 333, 84, 0.252, 41, 6, 5, 1);
/*!40000 ALTER TABLE `team` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
