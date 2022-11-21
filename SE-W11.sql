-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主機： localhost:8889
-- 產生時間： 2022 年 11 月 21 日 08:11
-- 伺服器版本： 5.7.34
-- PHP 版本： 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `SE-W11`
--

-- --------------------------------------------------------

--
-- 資料表結構 `OrderCase`
--

CREATE TABLE `OrderCase` (
  `id` int(255) NOT NULL,
  `OiD` int(255) NOT NULL,
  `UiD` int(255) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `SaleCase`
--

CREATE TABLE `SaleCase` (
  `id` int(255) NOT NULL,
  `UiD` varchar(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `deadline` datetime NOT NULL,
  `first_price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `SaleCase`
--

INSERT INTO `SaleCase` (`id`, `UiD`, `name`, `deadline`, `first_price`) VALUES
(1, 'user1', 'case1', '2022-11-21 07:40:08', 0);

-- --------------------------------------------------------

--
-- 資料表結構 `User`
--

CREATE TABLE `User` (
  `id` varchar(15) NOT NULL,
  `name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `User`
--

INSERT INTO `User` (`id`, `name`) VALUES
('user1', 'userA'),
('user2', 'userB');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `OrderCase`
--
ALTER TABLE `OrderCase`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `SaleCase`
--
ALTER TABLE `SaleCase`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `OrderCase`
--
ALTER TABLE `OrderCase`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `SaleCase`
--
ALTER TABLE `SaleCase`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
