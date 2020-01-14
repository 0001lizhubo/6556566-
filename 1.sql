
CREATE TABLE `course` (
  `ID` varchar(10) DEFAULT NULL,
  `name` varchar(15) NOT NULL,
  `cno` varchar(15) NOT NULL,
  `cname` varchar(20) NOT NULL,
  `times` varchar(5) DEFAULT NULL,
  `credit` varchar(5) DEFAULT NULL,
  `kechengxingzhi` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `keyan` (
  `ID` varchar(10) NOT NULL DEFAULT '',
  `Proname` varchar(100) NOT NULL,
  `direction` varchar(100) NOT NULL,
  `station` varchar(100) DEFAULT NULL,
  `papers` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Proname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `teacher` (
  `ID` varchar(10) NOT NULL DEFAULT '',
  `name` varchar(15) NOT NULL,
  `age` varchar(3) DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  `education` varchar(100) DEFAULT NULL,
  `department` varchar(100) DEFAULT NULL,
  `school` varchar(200) DEFAULT NULL,
  `health` varchar(40) DEFAULT NULL,
  `title` varchar(40) DEFAULT NULL,
  `post` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `user` (
  `ID` varchar(10) NOT NULL DEFAULT '',
  `password` varchar(100) DEFAULT NULL,
  `role` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

