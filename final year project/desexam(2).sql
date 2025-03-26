-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 26, 2025 at 07:59 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `desexam`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE `answers` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `answer_given` varchar(255) NOT NULL,
  `mark` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`id`, `student_id`, `question_id`, `exam_id`, `answer_given`, `mark`) VALUES
(1, 9, 1, 2, 'bbbli', 0),
(2, 9, 1, 2, 'bbbli', 0),
(3, 9, 1, 2, 'bbbli', 0),
(4, 9, 2, 2, 'gigiy', 1),
(5, 9, 3, 3, 'java is a programming language and it\'s a compiled language. it\'s a open source.it support window and linux and macOs', 6),
(6, 9, 3, 3, 'java is a programming language and it\'s a compiled language. it\'s a open source.it support window and linux and macOs', 6),
(7, 9, 3, 3, 'java is a programming language and it\'s a compiled language. it\'s a open source.it support window and linux and macOs', 6),
(8, 9, 3, 3, 'java is a programming language and it\'s a compiled language. it\'s a open source.it support window and linux and macOs', 6),
(9, 9, 3, 3, 'java is a programming language and it\'s a compiled language. it\'s a open source.it support window and linux and macOs', 6),
(10, 9, 3, 3, 'html and css is web page designing work and its is open source', 2),
(11, 9, 3, 3, 'gdyusfufgafiyugif', 1),
(12, 9, 3, 3, 'gdyusfufgafiyugif', 0),
(13, 9, 3, 3, 'gdyusfufgafiyugif', 0),
(14, 9, 3, 3, 'html is mark up language.it used to design web page', 2),
(15, 9, 3, 3, 'html is mark up language.it used to design web page', 2),
(16, 9, 3, 3, 'html is mark up language.it used to design web page', 2),
(17, 9, 3, 3, 'what is java', 7),
(18, 9, 3, 3, 'what is java', 7),
(19, 9, 3, 3, 'what is java', 7),
(20, 9, 3, 3, 'what is java', 7),
(21, 9, 3, 3, 'what is java', 7),
(22, 9, 3, 3, 'what is java', 7),
(23, 9, 3, 3, 'what is java', 7),
(24, 9, 3, 3, 'what is java', 7),
(25, 9, 3, 3, 'what is java', 8),
(26, 9, 3, 3, 'what is java', 8),
(27, 9, 3, 3, 'what is java', 8),
(28, 9, 3, 3, 'what is java', 8),
(29, 9, 3, 3, 'what is java', 8),
(30, 9, 3, 3, 'what is java', 3),
(31, 9, 3, 3, 'what is java', 3),
(32, 9, 3, 3, 'what is java', 4),
(33, 9, 3, 3, 'what is java', 4),
(34, 9, 3, 3, 'what is java', 4),
(35, 9, 3, 3, 'what is java', 2),
(36, 9, 3, 3, 'what is java', 2),
(37, 9, 3, 3, 'what is java', 1),
(38, 9, 3, 3, 'what is java', 0),
(39, 9, 3, 3, 'what is java', 0),
(40, 9, 3, 3, 'what is java', 2),
(41, 9, 3, 3, 'what is java', 2),
(42, 9, 3, 3, 'what is java', 2),
(43, 9, 3, 3, 'what is java', 1),
(44, 9, 3, 3, 'what is java', 0),
(45, 9, 3, 3, 'java java java java java java java', 0),
(46, 9, 3, 3, 'java java java java java java java', 0),
(47, 9, 3, 3, 'hfulg', 0),
(48, 9, 3, 3, 'hueg', 0),
(49, 9, 3, 3, 'hffhf', 0),
(50, 9, 3, 3, 'what is java', 4),
(51, 9, 3, 3, 'what is java', 4),
(52, 9, 3, 3, 'what is java', 0),
(53, 9, 3, 3, 'java is object oriented language and platform indepentant', 2),
(54, 9, 3, 3, 'java is a high-level ,object-oriented programing language known for its platform independence,security and versatility in web,mobile,and enterprise application', 9),
(55, 9, 3, 3, 'java is a high-level ,object-oriented programing language known for its platform independence,security and versatility in web,mobile,and enterprise application', 9),
(56, 9, 3, 3, 'java is a high-level ,object-oriented programing language known for its platform independence,security and versatility in web,mobile,and enterprise application', 9),
(57, 9, 3, 3, 'java is a high-level ,object-oriented programing language known for its platform independence,security and versatility in web,mobile,and enterprise application', 9),
(58, 9, 3, 3, 'java is a high-level ,object-oriented programing language known for its platform independence,security and versatility in web,mobile,and enterprise application', 10),
(59, 9, 3, 3, 'jav is a hih-level ,object-orieted progaming language known for its latform independnce,secrity and versatlity in wb,mobie,and nterprise applcation', 1),
(60, 9, 3, 3, 'java java java', 0),
(61, 9, 3, 3, 'java java java', 0),
(62, 9, 3, 3, 'java java java java java java java java', 0),
(63, 9, 3, 3, 'java java java java java java java java', 0),
(64, 9, 3, 3, 'what is java', 0),
(65, 9, 3, 3, 'what is java', 0),
(66, 9, 3, 3, 'what is java', 0),
(67, 9, 3, 3, 'python is high level ,object oriented programming language known for its platform independecnce ,security and versatitlty in web', 0),
(68, 9, 3, 3, 'java is high level ,object oriented programming language known for its platform independecnce ,security and versatitlty in web', 5),
(69, 9, 3, 3, 'java is high level ,object oriented programming language known for its platform independecnce ,security and versatitlty in web', 5),
(70, 9, 3, 3, 'html is high level ,object oriented programming language known for its platform independecnce ,security and versatitlty in web', 0),
(71, 9, 3, 3, 'hdiufgifugfwugwriygfwyfgrf', 0),
(72, 9, 3, 3, 'html is joifhoff wfugw g eeug fu c', 0),
(73, 9, 3, 3, 'java is a high-level ,object-oriented programming language known for its platform independence,security and versatility in web,mobile and enterprise applications', 10),
(74, 9, 3, 3, 'java is a high-level ,object-oriented programming language known for its platform independence,security and versatility in web,mobile and enterprise applications', 10),
(75, 9, 3, 3, 'python is a high-level ,object-oriented programming language known for its platform independence,security and versatility in web,mobile and enterprise applications', 0),
(76, 9, 3, 3, 'java is a high-lvel ,object-oriented programming language known for its platform independence,security and versatility in web,mobile and enterprise applications', 10),
(77, 9, 3, 3, 'java is a high-lvel ,object-orieted programming language known for its platform independence,security and versatility in web,mobile and enterprise applications', 10),
(78, 9, 3, 3, 'java is a high-lvel ,object-orieted programming languae knn for its platform independence,security and versatility in web,mobile and enterprise applications', 8),
(79, 9, 3, 3, 'java is a high-lvel ,object-orieted programming languae known for its platform independence,security and versatility in web,mobile and enterprise applications', 9),
(80, 9, 3, 3, 'a high-lvel java is,object-orieted programming languae known for its platform independence,security and versatility in web,mobile and enterprise applications', 9),
(81, 9, 3, 3, 'java is a high-level ,object-orieted programming language known for its platform independence,security and versatility in web,mobile and enterprise applications', 10),
(82, 9, 3, 3, 'java is a high level ,object orieted programming language known for its platform independence,security and versatility in web,mobile and enterprise applications', 10),
(83, 16, 3, 3, 'what is java', 7),
(84, 16, 3, 3, 'what is java', 7),
(85, 16, 3, 3, 'what is java', 7),
(86, 16, 3, 3, 'what is java', 9),
(87, 16, 3, 3, 'what is java', 9),
(88, 16, 3, 3, 'what is java', 9),
(89, 16, 3, 3, 'what is java', 0),
(90, 16, 3, 3, 'what is java', 0),
(91, 16, 3, 3, 'html is high level langauge.it is platform independent lanaguage', 0),
(92, 16, 3, 3, 'java is high level langauge.it is platform independent lanaguage', 1),
(93, 16, 3, 3, 'java is high level langauge.it is platform independent lanaguage.it is object oriented lanaguage.it has more security and versatility in web,mobile,enterprise application', 6),
(94, 16, 3, 3, 'java is a high level,object oriented programming language known for its platform independence,security,and versatility in web,mobile,and enterprise applications', 9),
(95, 16, 3, 3, 'python is a high level,object oriented programming language known for its platform independence,security,and versatility in web,mobile,and enterprise applications', 0),
(96, 16, 3, 3, 'java is a high-level,object-oriented programming language known for its platform independence,security,and versatility in web,mobile,and enterprise applications', 9),
(97, 16, 3, 3, 'java was a high-level,object-oriented programming language known for its platform independence,security,and versatility in web,mobile,and enterprise applications', 9),
(98, 16, 3, 3, 'pol afd affggg java java java language', 1),
(99, 16, 3, 3, 'java is a low level language web security classes objects', 0),
(100, 16, 3, 3, 'java is a upper level language provide security objects oriented', 2),
(101, 16, 3, 3, 'java is a upper level language provide security objects oriented', 2),
(102, 16, 3, 3, 'java is a upper level language. It provide security and it is objects oriented', 2),
(103, 16, 3, 3, 'java is high level language.it is object oriented language', 1),
(104, 16, 3, 3, 'java is a high level,object oriented programming language known for its platform independence,security and versatility in web,mobile and enterprise applications', 9),
(105, 16, 3, 3, 'python is a high level,object oriented programming language known for its platform independence,security and versatility in web,mobile and enterprise applications', 0),
(106, 16, 3, 3, 'java java java java java java java', 0),
(107, 16, 3, 3, 'what is java', 0),
(108, 16, 3, 3, 'what is java', 0),
(109, 16, 3, 3, 'what is java', 0),
(110, 16, 3, 3, 'what is java', 0),
(111, 16, 3, 3, 'what is java', 0),
(112, 16, 3, 3, 'what is java', 0),
(113, 16, 3, 3, 'java', 0),
(114, 16, 3, 3, 'java', 0),
(115, 16, 3, 3, 'java', 0);

-- --------------------------------------------------------

--
-- Table structure for table `batches`
--

CREATE TABLE `batches` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `batches`
--

INSERT INTO `batches` (`id`, `name`) VALUES
(1, '2022-2025'),
(2, '2023-2026');

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`id`, `name`) VALUES
(1, 'COMPUTER SCIENCE');

-- --------------------------------------------------------

--
-- Table structure for table `exams`
--

CREATE TABLE `exams` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `time_limit` int(11) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `department_id` int(11) NOT NULL,
  `batch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `exams`
--

INSERT INTO `exams` (`id`, `name`, `date`, `time`, `time_limit`, `teacher_id`, `department_id`, `batch_id`) VALUES
(1, 'test 1', '2025-01-20', '17:23:08', 90, 1, 0, 0),
(2, 'test 2', '2025-01-24', '14:58:45', 90, 1, 0, 0),
(3, 'java', '2025-03-28', '16:24:00', 90, 1, 1, 1),
(4, 'python', '2025-02-28', '05:47:00', 90, 2, 1, 1),
(5, 'dc', '2025-03-22', '10:26:00', 90, 2, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `mail_id` varchar(255) NOT NULL,
  `mobile_number` text NOT NULL,
  `department` varchar(255) NOT NULL,
  `date_of_joining` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `password_reset_tokens`
--

CREATE TABLE `password_reset_tokens` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `token` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `used` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `password_reset_tokens`
--

INSERT INTO `password_reset_tokens` (`id`, `email`, `token`, `created_at`, `used`) VALUES
(15, 'vignesh.g2311@gmail.com', 'InZpZ25lc2guZzIzMTFAZ21haWwuY29tIg.Z-Lm2w.-t2AfIc5JF-ZSdMhXi28R-R1WzA', '2025-03-25 22:54:43', 0);

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(11) NOT NULL,
  `question` varchar(4000) NOT NULL,
  `answer` text NOT NULL,
  `marks` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id`, `question`, `answer`, `marks`, `exam_id`) VALUES
(1, 'q1', 'a1', 5, 2),
(2, 'q2', '\nThe Power and Versatility of Python: A Comprehensive Overview\n\nIntroduction\n\nPython, a high-level programming language known for its simplicity and versatility, has become one of the most widely used languages in the world of software development. From web development and automation to data science and artificial intelligence, Python’s ease of use, readability, and extensive library ecosystem make it a go-to choice for developers across various domains. This essay will explore Python’s history, core features, use cases, and why it has gained immense popularity among programmers and enterprises alike.\n\nA Brief History of Python\n\nPython was conceived in the late 1980s by Guido van Rossum at the Centrum Wiskunde & Informatica (CWI) in the Netherlands. Van Rossum began the project during the Christmas holidays of 1989, with the goal of creating a programming language that was easy to read and write, while also being powerful enough for complex tasks. Python was released to the public in 1991 as version 0.9.0.\n\nPython’s name was inspired by the British comedy series Monty Python’s Flying Circus, a favorite of van Rossum. This playful naming reflects the language\'s focus on simplicity and accessibility. The language has evolved significantly since its inception, with Python 2 being released in 2000 and the transition to Python 3 starting in 2008. Python 3, the version currently in use, introduced many improvements and fixes over Python 2, although the two versions are incompatible with each other. Python 3 became the standard in 2020, with Python 2 officially reaching its end of life.\n\nCore Features of Python\n\nSimplicity and Readability\nOne of Python’s defining features is its simple and clean syntax. The language emphasizes readability, making it accessible to both beginners and experienced programmers. Python’s syntax allows developers to express concepts in fewer lines of code than languages such as C++ or Java, which helps reduce development time and maintenance costs. The language\'s use of indentation to define code blocks rather than braces or keywords (as in other languages) contributes to its clean structure.\n\nDynamic Typing\nPython is dynamically typed, meaning variables are not bound to specific data types. This provides flexibility, allowing developers to easily manipulate variables without worrying about declaring types upfront. However, this can lead to potential runtime errors if a variable is used incorrectly. Despite this, Python’s dynamic typing allows for more agile and rapid development.\n\nInterpreted Language\nPython is an interpreted language, which means that code is executed line by line rather than being compiled into machine code. This makes it easier to test and debug, as developers can interactively test code without needing to compile it first. The interpreter also provides a rich set of debugging tools, such as the built-in pdb debugger.\n\nExtensive Standard Library\nPython comes with a vast standard library, which includes modules for handling a wide range of tasks such as file I/O, regular expressions, networking, web services, and database access. This makes Python a great choice for developing software quickly, as developers don’t have to reinvent the wheel when implementing common functionality.\n\nCross-Platform Compatibility\nPython is cross-platform, meaning Python code can be run on any operating system that has a Python interpreter installed, including Windows, macOS, and Linux. This makes Python an excellent choice for developing applications that need to work across different platforms with minimal changes.\n\nObject-Oriented and Functional Programming\nPython supports both object-oriented and functional programming paradigms. It allows developers to write code using objects, classes, and inheritance, but also supports functional programming techniques such as higher-order functions, closures, and lambda expressions. This versatility enables Python to cater to a wide range of programming styles and use cases.\n\nApplications of Python\n\nWeb Development\nPython is a popular choice for web development due to frameworks like Django and Flask. These frameworks provide tools for building robust, secure, and scalable web applications. Django is a high-level framework that encourages rapid development and clean design, while Flask is a lightweight, micro-framework ideal for smaller applications or microservices. Python\'s ease of integration with databases and its support for asynchronous programming make it a strong contender for modern web development.\n\nData Science and Machine Learning\nOne of Python’s most prominent applications today is in data science and machine learning. Libraries like NumPy, Pandas, and Matplotlib provide powerful tools for data manipulation, analysis, and visualization. Additionally, Python has become the go-to language for machine learning with frameworks such as TensorFlow, Keras, and PyTorch. These libraries offer pre-built functions for building, training, and evaluating machine learning models, making Python an ideal choice for data scientists and machine learning engineers.\n\nAutomation and Scripting\nPython’s simplicity makes it an excellent language for writing automation scripts. Whether it\'s automating tasks on a local machine, scraping data from websites, or interacting with APIs, Python provides a wealth of libraries to facilitate automation. Tools like Selenium are widely used for browser automation, while libraries such as os and shutil make it easy to manipulate files and directories.\n\nCybersecurity\nPython is increasingly being used in the field of cybersecurity for tasks like penetration testing, vulnerability scanning, and developing security tools. Libraries such as Scapy, PyCrypto, and Pwntools allow security professionals to write scripts for network analysis, cryptography, and exploitation. Python’s strong community support and extensive documentation make it an invaluable resource for cybersecurity experts.\n\nGame Development\nWhile Python may not be the first language that comes to mind for game development, it is used in various game creation contexts. Libraries like Pygame allow developers to build simple 2D games, while more advanced game engines, such as Panda3D, provide support for 3D game development. Python is also used for scripting in larger game engines, such as Blender for creating animations or Unreal Engine for game logic.\n\nArtificial Intelligence (AI)\nPython has become the dominant language in AI development, particularly due to its vast array of libraries designed for working with neural networks, natural language processing, and robotics. Libraries like OpenCV are used for computer vision, while NLTK and SpaCy are used for text processing. Python’s integration with AI frameworks makes it an indispensable tool for AI researchers and developers.\n\nWhy Python is Popular\n\nEase of Learning\nPython’s simple syntax and readability make it an ideal choice for beginners. Whether you\'re learning programming concepts, data structures, or algorithms, Python’s clear and concise syntax makes the learning process smoother compared to many other languages. This has made Python a favorite language for introductory programming courses around the world.\n\nLarge Community and Resources\nPython boasts one of the largest and most active developer communities. The Python Software Foundation (PSF) maintains a rich ecosystem of libraries, frameworks, and tools that extend Python’s capabilities. Additionally, the Python community is very supportive, with a vast array of tutorials, forums, and documentation available to help new and experienced developers.\n\nCorporate Adoption\nPython has seen widespread adoption in the corporate world, particularly in industries such as finance, healthcare, and technology. Companies like Google, Facebook, and Netflix use Python in production environments, and many large organizations rely on it for everything from web development to machine learning.\n\nVersatility\nFrom simple scripts to complex web applications and machine learning models, Python can be used for a wide range of tasks. Its versatility allows developers to use it for everything from rapid prototyping to production-grade systems, making it an essential tool for modern software development.\n\nConclusion\n\nPython’s simple syntax, powerful features, and wide-ranging applications make it one of the most important programming languages of the 21st century. Its presence in industries ranging from web development and data science to AI and cybersecurity is a testament to its flexibility and importance in the modern technological landscape. As Python continues to evolve and adapt to new challenges, it is poised to remain a cornerstone of the programming world for years to come. Whether you’re a beginner looking to start your programming journey or an experienced developer tackling complex projects, Python’s accessibility and versatility make it a valuable tool in any developer’s toolkit.', 10, 2),
(3, 'what is java', 'Java is a high-level, object-oriented programming language known for its platform independence, security, and versatility in web, mobile, and enterprise applications.', 10, 3),
(4, 'jihd', 'huid', 7, 4),
(5, 'question1', 'hoji', 5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `mail_id` varchar(255) NOT NULL,
  `password` varchar(5000) NOT NULL,
  `role` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `mail_id`, `password`, `role`) VALUES
(2, 'vignesh.g2311@gmail.com', 'scrypt:32768:8:1$GkqWHmvtpUkJUR1t$e7674a8673074defd728e87112f4bf511dd66c3dd23e9e09bf8aa28f5236686e555bcc594c0b54997b41283850992c9292ef5e60acd2daac3690e3c59707ed37', 'STUDENT'),
(3, 'vignesh.g367@gmail.com', 'scrypt:32768:8:1$XSllnqaytLbiMVKO$3f16eb806dd15f21acaac13081a8bda3ca8caea9afecb4f06286a274cee923e4569eb02afd41f46e4ab911340119a5777d8af0409cba84c2120fb5cc3ea1640a', 'STUDENT'),
(4, '22ucs17@tcarts.in', 'scrypt:32768:8:1$YPK1nfR5W277gvSV$5ae8f3a10b5ec2e9a1466efa274df5785075ac022da7dde33ae8ed525254587e2c0e532ad22513b4e0c3b54cba6eb3b38ae121b69fd9e1b55abeca2b4fea7382', 'ADMIN'),
(18, 'v@gmail.com', 'scrypt:32768:8:1$Xw5VPWBBQBuKUjDZ$ca9f64268ca4d195af9483ac4a9d448971a4652cc79f33ba73522d24063349f137b0a17f5cb1f0e387955bdb576ef89c9ab26f021db7277f02a8d91c958876da', 'TEACHER'),
(19, 'vignesh@gmail.com', 'scrypt:32768:8:1$I8a3s6a0xn07nPlJ$c6773872c13e01fd01e989e12958907b35de8e5a279a344ad8b4cbcee9d2d80cdb16d193f482db5d219390b7ba16d81af4ae873aa904ebf3906b9603d8566f8a', 'TEACHER'),
(20, 'guig@g.com', 'scrypt:32768:8:1$DNBF44MBJwfM8oxk$77464889bfc8e621f55958b6f22aeedf2a22d0f01f4001eb9e5eed71b6752cf5513d41408fba219af3d59fef13900ade5abbc067ad90301df0eebaa33ce6c38d', 'TEACHER'),
(21, 'nk@gu.com', 'scrypt:32768:8:1$GDt5lbiXQM1bAGlg$1ed70c5e80815dbef6d8aa6ffcb2d3478d04b12998a482eaa358704bb5b9723ddd54838ebdf9e0eaaed0856f4f52de86bb7377cc9c80471d107c945a50e38f8d', 'TEACHER'),
(22, 'a@gamil.com', 'scrypt:32768:8:1$nIxm5UbF8NYozwv4$23dc58a8ec3a165bfc09284c74b16717f7b99890adb3d1902cd30606a755548549a3a1357fb247cb8be3e9eee997755efd74e13ebfefadf5502c8edff9114727', 'student'),
(23, 'vignesh.g231104@gmail.com', 'scrypt:32768:8:1$kPSZ4seVm6Dcp6rC$29f8dbee46b3531ff1719e9fec36a57f26275ee552549e1c5879bbaa0023bf24a6fc2733d5671abfbc3c655331b32fbb932143a11f292d831d6dd9f2861a6f15', 'student'),
(24, 'vignes@gmail.com', 'scrypt:32768:8:1$I8aetBpqeXEf6Ho3$94c0328de1e437089eb41f4cef35ceb309069607ff073db525d0b5c7d9b9e1ed76a3b3a97c363aa67276377a07caca133b795b744e06efa9f79c19a943474b16', 'student'),
(25, 'ghug@gmail.com', 'scrypt:32768:8:1$0PcEpc4452lziqIE$b7e7bc994b2e08c4ce1bc9122850a9f6762d421cd910e56c25179b128906e3c278ad334719d1e41b48dec29a5930388935f1446bbce8b3adb1410d8a4b10b907', 'student'),
(26, 'vig@h.com', 'scrypt:32768:8:1$AoYx9UUoBpJm9T48$dd43e285b21e348c94c090412d3ad412bc77e491603110bb49bc3781ee5391ab6a3da34470547722bd8db5ae72fb7fb29e8940bece046b68425d8347d5f67fe8', 'STUDENT'),
(27, 'bbb@gmail.com', 'scrypt:32768:8:1$b5LOnDwPX9Lu5na7$2fdf92f6936998bb9daa7c2b13af6c1edc33e06052d3e62d68479bd3f39ac6380350b92b7e3083c2630a706e67b357a1185fd0383d2ef120499a1cd285222c30', 'STUDENT'),
(28, 'vigmm@gmail.com', 'scrypt:32768:8:1$hchiVToKySsnZX4p$a7224d65206eb4e1e052c2aa101de43ddc436891d79840934db564f0e1dba677955291c75cb2a482800585d65e09b249de6fd5590e10ecd221c2b00f2757f0ae', 'STUDENT'),
(29, 'bbbb@gmail.co', 'scrypt:32768:8:1$RaJl9caH6igVGp9m$89495f9f36eb5fadc1665e339a8bf2445b9039a6c2434a52a65a8de11a536d877df1fed40e734f91cb30dfd86cfc78343ffeb6c5dc3fa1cb9101f65f6daf44ea', 'STUDENT'),
(30, 'aaa@d.com', 'scrypt:32768:8:1$hIZu80lYl07JUu59$0469bc9ca7c025676d5359a47ec5a451465cf0d2b34cccebea0c70ec75af8184fb61b270dfa63d7b63bbe0c2b18be2fa2f1646aa73a85ef6c5a415cac0fb0684', 'STUDENT'),
(31, 'vvvv@gmail.com', 'scrypt:32768:8:1$RdjRlOGLJAGXQgaw$e73111decc02d71b48d4af35692c6e07c16ae655b453cfaee2999bb08b359e8e446c95dd2aa31a8ebd5699df111df4502d0565bbe77b149cef9c602051199a27', 'STUDENT'),
(32, 'f@gmail.com', 'scrypt:32768:8:1$rIyVB1owSagg18wC$3a42b5ca4cfabd8ea7426cf08e3934aff537e701861d7932bbcf016aae50d0e6d386b9bf9d018ce950939f908a245e8d4ee5727170df84f25b7618cd4eed953f', 'STUDENT');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `batch_id` int(11) NOT NULL,
  `department_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `name`, `email`, `batch_id`, `department_id`, `user_id`) VALUES
(1, 'new', 'new', 0, 0, 0),
(7, 'bb', 'ih', 0, 0, 0),
(9, 'bb', 'ihv', 0, 0, 0),
(16, 'new1', 'vignesh.g@2311@gmail.com', 0, 0, 2),
(17, 'newmmm', 'vigneshji@gmail.com', 0, 0, 0),
(18, 'by', 'vgv@gmail.com', 0, 0, 0),
(19, 'goy', 'hhiu@gy.com', 0, 0, 0),
(20, 'ubynynu', 'yfudt1d@gma.com', 1, 1, 0),
(21, 'a', 'aaa@d.com', 2, 1, 30),
(22, 'vvv', 'vvvv@gmail.com', 2, 1, 31),
(23, 'h', 'f@gmail.com', 1, 1, 32);

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `batch_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE `teachers` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `department_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`id`, `name`, `email`, `department_id`, `user_id`) VALUES
(1, 'new1', 'v@gmail.com', 1, 18),
(25, 'nn', 'guig@g.com', 1, 20),
(26, 'hi', 'nk@gu.com', 1, 21);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `question_id` (`question_id`),
  ADD KEY `exam_id` (`exam_id`);

--
-- Indexes for table `batches`
--
ALTER TABLE `batches`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `exams`
--
ALTER TABLE `exams`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `token` (`token`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mail_id` (`mail_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `batch_id` (`batch_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `batch_id` (`batch_id`);

--
-- Indexes for table `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `department_id` (`department_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answers`
--
ALTER TABLE `answers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=116;

--
-- AUTO_INCREMENT for table `batches`
--
ALTER TABLE `batches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `departments`
--
ALTER TABLE `departments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `exams`
--
ALTER TABLE `exams`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `faculty`
--
ALTER TABLE `faculty`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `password_reset_tokens`
--
ALTER TABLE `password_reset_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `subjects`
--
ALTER TABLE `subjects`
  ADD CONSTRAINT `subjects_ibfk_1` FOREIGN KEY (`batch_id`) REFERENCES `batches` (`id`);

--
-- Constraints for table `teachers`
--
ALTER TABLE `teachers`
  ADD CONSTRAINT `teachers_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
