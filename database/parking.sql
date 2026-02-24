-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 24, 2026 at 11:21 AM
-- Server version: 8.0.39
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `parking`
--

-- --------------------------------------------------------

--
-- Table structure for table `checkin_checkout`
--

CREATE TABLE `checkin_checkout` (
  `record_id` int NOT NULL,
  `vehicle_id` int DEFAULT NULL,
  `slot_id` int DEFAULT NULL,
  `checkin_time` datetime DEFAULT NULL,
  `checkout_time` datetime DEFAULT NULL,
  `amount_paid` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `checkin_checkout`
--

INSERT INTO `checkin_checkout` (`record_id`, `vehicle_id`, `slot_id`, `checkin_time`, `checkout_time`, `amount_paid`) VALUES
(19, 17, 11, '2025-09-28 19:26:00', '2025-09-28 19:26:14', NULL),
(20, 17, 11, '2025-09-28 19:27:57', '2025-09-28 19:28:10', NULL),
(21, 17, 11, '2025-09-28 20:06:43', '2025-09-28 20:07:20', NULL),
(22, 17, 1, '2025-09-28 20:19:40', '2025-09-28 20:20:07', NULL),
(23, 17, 1, '2025-09-28 20:21:00', '2025-09-28 20:21:14', NULL),
(24, 17, 1, '2025-09-28 20:24:22', '2025-09-28 21:02:45', NULL),
(25, 19, 2, '2025-09-28 20:24:45', '2025-09-28 20:28:15', NULL),
(27, 20, 4, '2025-09-28 20:27:50', '2025-09-28 21:07:10', NULL),
(28, 17, 1, '2025-09-28 21:20:14', '2025-09-28 21:25:08', NULL),
(29, 17, 1, '2025-09-28 21:27:54', '2025-09-28 21:32:12', NULL),
(30, 19, 2, '2025-09-28 21:28:13', NULL, NULL),
(31, 21, 1, '2025-09-28 21:33:15', '2025-09-28 21:33:41', NULL),
(32, 17, 1, '2025-09-29 08:01:53', '2025-09-29 08:03:13', NULL),
(33, 17, 1, '2025-09-29 08:06:22', '2025-09-29 08:07:26', NULL),
(34, 23, 1, '2025-09-29 08:10:14', '2025-09-29 08:10:46', NULL),
(35, 24, 1, '2026-02-24 15:09:57', '2026-02-24 15:10:14', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `slots`
--

CREATE TABLE `slots` (
  `slot_id` int NOT NULL,
  `is_available` tinyint(1) DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `slots`
--

INSERT INTO `slots` (`slot_id`, `is_available`) VALUES
(1, 1),
(2, 0),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1),
(16, 1),
(17, 1),
(18, 1),
(19, 1),
(20, 1);

-- --------------------------------------------------------

--
-- Table structure for table `vehicles`
--

CREATE TABLE `vehicles` (
  `vehicle_id` int NOT NULL,
  `owner_name` varchar(50) NOT NULL,
  `plate_no` varchar(20) NOT NULL,
  `vehicle_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `vehicles`
--

INSERT INTO `vehicles` (`vehicle_id`, `owner_name`, `plate_no`, `vehicle_type`) VALUES
(17, 'its me', 'mh18', 'Scooty'),
(19, 'Roshni Patil', 'Mh39AE3741', 'Scooty'),
(20, 'Kailas', 'MH18AE1111', 'Bike'),
(21, 'abc', '1234', 'Bike'),
(22, 'shakil', 'mh15hk3876', 'Bike'),
(23, 'Roshni Patil', 'mh39', 'Car'),
(24, 'ruhi', '11223', 'Bus');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `checkin_checkout`
--
ALTER TABLE `checkin_checkout`
  ADD PRIMARY KEY (`record_id`),
  ADD KEY `vehicle_id` (`vehicle_id`),
  ADD KEY `slot_id` (`slot_id`);

--
-- Indexes for table `slots`
--
ALTER TABLE `slots`
  ADD PRIMARY KEY (`slot_id`);

--
-- Indexes for table `vehicles`
--
ALTER TABLE `vehicles`
  ADD PRIMARY KEY (`vehicle_id`),
  ADD UNIQUE KEY `plate_no` (`plate_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `checkin_checkout`
--
ALTER TABLE `checkin_checkout`
  MODIFY `record_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `slots`
--
ALTER TABLE `slots`
  MODIFY `slot_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `vehicles`
--
ALTER TABLE `vehicles`
  MODIFY `vehicle_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `checkin_checkout`
--
ALTER TABLE `checkin_checkout`
  ADD CONSTRAINT `checkin_checkout_ibfk_1` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicles` (`vehicle_id`) ON DELETE SET NULL,
  ADD CONSTRAINT `checkin_checkout_ibfk_2` FOREIGN KEY (`slot_id`) REFERENCES `slots` (`slot_id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
