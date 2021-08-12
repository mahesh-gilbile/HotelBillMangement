-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 09, 2021 at 04:48 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `elm`
--

-- --------------------------------------------------------

--
-- Table structure for table `billing`
--

CREATE TABLE `billing` (
  `Index` int(5) NOT NULL,
  `Billno` int(3) NOT NULL,
  `Item` varchar(40) NOT NULL,
  `Rate` int(5) NOT NULL,
  `Quantity` int(5) NOT NULL,
  `TotalCost` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `Index` int(4) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `Cost` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`Index`, `Name`, `Cost`) VALUES
(1, 'Wada', 15),
(2, 'Bisleri', 20),
(3, 'Thali', 90),
(4, 'Idli', 25),
(5, 'EGG', 20),
(6, 'Dosa', 40);

-- --------------------------------------------------------

--
-- Table structure for table `setting`
--

CREATE TABLE `setting` (
  `index` int(1) NOT NULL,
  `Info` varchar(10) NOT NULL,
  `Value` float NOT NULL,
  `Password` int(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `setting`
--

INSERT INTO `setting` (`index`, `Info`, `Value`, `Password`) VALUES
(1, 'Manager', 0, 12345),
(2, 'Waiter', 0, 12345),
(3, 'CGST', 9.5, 0),
(4, 'SGST', 9.5, 0),
(5, 'TGST', 19, 0);

-- --------------------------------------------------------

--
-- Table structure for table `summary`
--

CREATE TABLE `summary` (
  `Index` int(5) NOT NULL,
  `Date` varchar(15) NOT NULL,
  `Day` int(2) NOT NULL,
  `Month` int(3) NOT NULL,
  `Year` int(4) NOT NULL,
  `Tableno` int(4) NOT NULL,
  `TotalAmount` float NOT NULL,
  `CGST` float NOT NULL,
  `SGST` float NOT NULL,
  `TGST` float NOT NULL,
  `SubTotal` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `summary`
--

INSERT INTO `summary` (`Index`, `Date`, `Day`, `Month`, `Year`, `Tableno`, `TotalAmount`, `CGST`, `SGST`, `TGST`, `SubTotal`) VALUES
(1, '2020-06-06', 6, 6, 2020, 1, 1217.05, 103.525, 103.525, 207.05, 1010),
(2, '2020-06-06', 6, 6, 2020, 2, 1325.5, 112.75, 112.75, 225.5, 1100),
(3, '2020-06-09', 9, 6, 2020, 1, 964, 82, 82, 164, 800),
(4, '2020-08-09', 9, 8, 2020, 1, 216.9, 18.45, 18.45, 36.9, 180),
(5, '2020-08-09', 9, 8, 2020, 2, 626.6, 53.3, 53.3, 106.6, 520),
(6, '2020-08-29', 29, 8, 2020, 1, 554.3, 47.15, 47.15, 94.3, 460),
(7, '2020-08-29', 29, 8, 2020, 2, 186.775, 15.8875, 15.8875, 31.775, 155),
(8, '2020-12-16', 16, 12, 2020, 1, 450.3, 35.15, 35.15, 70.3, 380),
(9, '2020-12-16', 16, 12, 2020, 2, 165.9, 12.95, 12.95, 25.9, 140),
(10, '2021-05-25', 25, 5, 2021, 1, 1205, 102.5, 102.5, 205, 1000),
(11, '2021-05-25', 25, 5, 2021, 2, 216.9, 18.45, 18.45, 36.9, 180),
(12, '2021-08-09', 9, 8, 2021, 1, 172.55, 13.775, 13.775, 27.55, 145),
(13, '2021-08-09', 9, 8, 2021, 2, 214.2, 17.1, 17.1, 34.2, 180);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `billing`
--
ALTER TABLE `billing`
  ADD PRIMARY KEY (`Index`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`Index`);

--
-- Indexes for table `setting`
--
ALTER TABLE `setting`
  ADD PRIMARY KEY (`index`);

--
-- Indexes for table `summary`
--
ALTER TABLE `summary`
  ADD PRIMARY KEY (`Index`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `billing`
--
ALTER TABLE `billing`
  MODIFY `Index` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `setting`
--
ALTER TABLE `setting`
  MODIFY `index` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `summary`
--
ALTER TABLE `summary`
  MODIFY `Index` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
