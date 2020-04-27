DROP TABLE IF EXISTS `car_list`;
DROP TABLE IF EXISTS `car_brands_category`;
DROP TABLE IF EXISTS `car_brands`;

CREATE TABLE `car_brands` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text` varchar(20) DEFAULT NULL,
  `qczj_id` int(11) DEFAULT NULL,
  `img_url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2101 DEFAULT CHARSET=utf8;

CREATE TABLE `car_brands_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fctname` varchar(100) DEFAULT NULL,
  `qczj_fctid` int(11) DEFAULT NULL,
  `seriesplace` varchar(100) DEFAULT NULL,
  `seriesplacenum` int(11) DEFAULT NULL,
  `brandsid` int(11) DEFAULT NULL,
  `qczj_brandsid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_brandsid` (`brandsid`),
  CONSTRAINT `FK_brandsid` FOREIGN KEY (`brandsid`) REFERENCES `car_brands` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=873 DEFAULT CHARSET=utf8;

CREATE TABLE `car_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `brands_category` int(11) DEFAULT NULL,
  `qczj_fctid` int(11) DEFAULT NULL,
  `containbookedspec` int(11) DEFAULT NULL,
  `fctname` varchar(50) DEFAULT NULL,
  `newenergy` int(11) DEFAULT NULL,
  `newenergySeriesId` int(11) DEFAULT NULL,
  `pnglogo` varchar(200) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  `seriesImg` varchar(200) DEFAULT NULL,
  `seriesName` varchar(50) DEFAULT NULL,
  `seriesPriceMax` int(11) DEFAULT NULL,
  `seriesPriceMin` int(11) DEFAULT NULL,
  `seriesState` int(11) DEFAULT NULL,
  `seriesid` int(11) DEFAULT NULL,
  `seriesplace` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7109 DEFAULT CHARSET=utf8;