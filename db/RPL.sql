-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: rpl
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

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
-- Current Database: `rpl`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `rpl` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `rpl`;

--
-- Table structure for table `apoteker`
--

DROP TABLE IF EXISTS `apoteker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apoteker` (
  `IdApoteker` int(11) NOT NULL,
  `Nama` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `NoTelp` varchar(20) DEFAULT NULL,
  `Username` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`IdApoteker`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apoteker`
--

LOCK TABLES `apoteker` WRITE;
/*!40000 ALTER TABLE `apoteker` DISABLE KEYS */;
INSERT INTO `apoteker` (`IdApoteker`, `Nama`, `Email`, `NoTelp`, `Username`, `Password`) VALUES (1,'Admin','-','0','admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'),(2,'Admin 2','-','0','admin2','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918');
/*!40000 ALTER TABLE `apoteker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `IdAkun` int(11) NOT NULL,
  `Nama` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `NoTelp` varchar(20) DEFAULT NULL,
  `Username` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`IdAkun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` (`IdAkun`, `Nama`, `Email`, `NoTelp`, `Username`, `Password`) VALUES (1,'Shifa Salsabiila','salsabiilashifa11@gmail.com','081212637925','salsabiilashifa11','5db4fc92c667e6a472482ba71cf1c4d6bbafdd3e052a09ddf186426b01aa6eac'),(2,'Aulia Adila','auliadila@gmail.com','081212345678','auliadila','96b9a12c78b4a7c128e0d3c0b17718d361904ed77c8b787363e34a1b2013341f'),(3,'Sharon Bernadetha Marbun','sharondetha@gmail.com','081211112222','Sharon1234','6d4e9a15dc535e36f7f4d1a907ec86b3c66d7a704828aa97c701fcc16c4782fc'),(4,'Syarifah Aisha','saisha@gmail.com','08123334455','aishas123','9e691cc3bf80c4491b1b0ff55880e453bbe335d562e1c75f341b4af7ad35934c'),(5,'kucing','kucing@gmail.com','081222293002','kucing1','1c575651a095af2dffb21413df381064614f9d8de83ef36106a082de3933959c'),(6,'Hinata Shoyo','hinatashoyo@gmail.com','081010101010','hinata','197e8720acf8226d633f883ea02b0577a1068542f09d178b693184c341157676');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dokter`
--

DROP TABLE IF EXISTS `dokter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dokter` (
  `IdDokter` int(11) NOT NULL,
  `Nama` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `NoTelp` varchar(20) DEFAULT NULL,
  `Username` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`IdDokter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dokter`
--

LOCK TABLES `dokter` WRITE;
/*!40000 ALTER TABLE `dokter` DISABLE KEYS */;
INSERT INTO `dokter` (`IdDokter`, `Nama`, `Email`, `NoTelp`, `Username`, `Password`) VALUES (1,'Harry Setiawan','harry@gmail.com','081255556666','harrys','df46219531cb5d522d0845901978dccfa286a5b0437f4f9cd4e485064f6b632c');
/*!40000 ALTER TABLE `dokter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `obat`
--

DROP TABLE IF EXISTS `obat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `obat` (
  `IdObat` int(11) NOT NULL,
  `NamaObat` varchar(255) DEFAULT NULL,
  `Stok` int(11) DEFAULT NULL,
  `Harga` int(11) DEFAULT NULL,
  `PictObat` varchar(255) DEFAULT NULL,
  `Deskripsi` text DEFAULT NULL,
  PRIMARY KEY (`IdObat`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `obat`
--

LOCK TABLES `obat` WRITE;
/*!40000 ALTER TABLE `obat` DISABLE KEYS */;
INSERT INTO `obat` (`IdObat`, `NamaObat`, `Stok`, `Harga`, `PictObat`, `Deskripsi`) VALUES (1,'PROMAG 12 TABLET',20,15600,'../img/obat1.jpg','Deskripsi:\nPROMAG merupakan obat dengan kandungan Hydrotalcite,\nMg(OH)2, Simethicone dalam bentuk tablet. Obat ini digunakan\nuntuk mengurangi gejala-gejala yang berhubungan dengan: \nkelebihan asam lambung, gastritis, tukak lambung, tukak usus 12 jari.\nGejala seperti mual, nyeri lambung, nyeri ulu hati, kembung dan\nperasaan penuh pada lambung.\n\nKomposisi:\nHydrotalcite 200 mg, Mg(OH)2 150 mg, simethicone 50 mg\n\nAturan Pakai:\nDianjurkan untuk meminum obat ini segera pada saat timbul\ngejala dan dilanjutkan 1-2 jam sebelum makan atau sesudah\nmakan dan sebelum tidur.'),(2,'BYE BYE FEVER ANAK',20,25200,'../img/obat2.webp','Deskripsi:\nBYE BYE FEVER ANAK merupakan plester yang digunakan pada\nanak diatas 2 tahun untuk membantu meredakan demam, sakit\nkepala dan sakit gigi. Plester ini memberikan efek dingin bekerja\nsampai 10 jam. Plester BYE BYE FEVER ANAK memiliki daya lekat\nyang kuat dan aman digunakan bersama dengan obat lain.\n\nAturan Pakai:\nLepaskan lapisan transparan dan tempelkan permukaan yang melekat\npada daerah dahi/pipi/punggung/bagian yang nyeri. Patch diganti\nsetiap 10 jam.'),(3,'NESTLE ACTIVOR AVOCADO',20,14800,'../img/obat3.webp','Deskripsi:\nNESTLE ACTICOR AVOCADO merupakan minuman rendah lemak\ndengan rasa yang enak yang mengandung Betaglucan dan Inulin\nuntuk  membantu menurunkan kolesterol. Minuman ini merupakan\nsalah satu sumber vitamin B1 dan B2 serta serat pangan.\n\nKomposisi:\nMinuman penurun kolesterol yang mengandung: susu, Vitamin B1,\nVitamin B2, dan serat pangan.\n\nAturan Pakai:\nSebaiknya dikonsumsi setelah makan. Dapat disajikan dalam keadaan\ndingin. Sertai dengan diet rendah lemak jenuh dan rendah kolesterol.'),(4,'COOLING 5 PLUS ORANGE',20,62400,'../img/obat4.webp','Deskripsi:\nCOOLING 5 PLUS ORANGE merupakan obat anestesi atau bius lokal\nyang mengandung Benzocaine dan Phenol. Obat ini digunakan untuk\nmenghilangkan rasa sakit misalnya pada saat sariawan, sakit gigi,\nradang gusi, dan sakit saat pertumbuhan gigi. Benzocaine bekerja\ndengan menurunkan permeabilitas membran sel saraf terhadap ion\nnatrium, menghambat depolarisasi dan memblok konduksi impuls\nsaraf.\n\nKomposisi:\nBenzocaine, Phenol\n\nAturan Pakai:\nSemprotkan atau oleskan sedikit pada tempat yang sakit'),(5,'EPERISONE 10 TABLET',20,68000,'../img/obat5.webp','Deskripsi:\nEPERISONE TABLET merupakan obat yang mengandung Eperisone\nHCl. Eperisone HCl bekerja sebagai relaksan otot atau melemaskan\notot rangka dan otot polos vaskular, yang menghasilkan pengurangan\nmyotonia,peningkatan sirkulasi, dan penekanan refleks rasa sakit.\nEPERISONE digunakan untuk pengobatan simtomatik terhadap kondisi\nyang terkait dengan spasme muskuloskeletal atau kejang otot.\nPenggunaan obat ini HARUS SESUAI DENGAN PETUNJUK DOKTER.\n\nKomposisi:\nEperisone HCl 50 mg\n\nAturan Pakai:\nSesudah makan'),(6,'LAXING 10 KAPSUL',20,15500,'../img/obat6.webp','Deskripsi:\nLAXING merupakan obat tradisional yang terbuat dari bahan alam\nuntuk menjaga kesehatan pencernaan dan melancarkan buang air\nbesar (BAB).\n\nKomposisi:\nCassiae sennae folium 100 mg, Aloe vera folium 33 mg, Foeniculi\nvulgaris semen 20 mg\n\nAturan Pakai:\nDikonsumsi pada malam hari sebelum tidur.'),(7,'AMLODIPINE 10 TABLET',20,26000,'../img/obat7.webp','Deskripsi:\nAMLODIPINE merupakan obat antihipertensi golongan Calcium\nChannel Blockers (CCB). Obat ini bekerja dengan cara menghambat\nkalsium masuk ke dalam sel sehingga salah satu efeknya adalah\n menyebabkan vasodilatasi, memperlambat laju jantung, dan\nmenurunkan kontraktilitas miokard sehingga menurunkan tekanan\ndarah. Dalam penggunaan obat ini harus SESUAI DENGAN PETUNJUK\nDOKTER.\n\nKomposisi:\nTiap tablet mengandung Amlodipine 5 mg\n\nAturan Pakai:\nDikonsumsi sebelum atau sesudah makan.'),(8,'EASY TOUCH BLOOD GLUCOSE',20,194400,'../img/obat8.webp','Deskripsi:\nEASY TOUCH BLOOD GLUCOSE 25 STRIP merupakan test strip yang\ndigunakan untuk melakukan pemeriksaan kadar gula dalam darah.\nStrip Test ini hanya dapat digunakan satu kali pakai dan hanya \ndapat\nterbaca melalui alat EASYTOUCH.\n\nDosis:\nSesuai kebutuhan\n\nAturan Pakai:\nLetakkan sampel darah secukupnya pada test strip, masukkan ke\ndalam alat yang sesuai'),(9,'INPEPSA SIRUP 200 ML',20,166800,'../img/obat9.webp','Deskripsi:\nINPEPSA SIRUP merupakan obat dengan kandungan Sucralfate dalam\nbentuk sirup. Obat ini digunakan untuk pengobatan jangka pendek dan\njangka panjang pada tukak lambung dan usus, gastritis kronik. Dalam\npenggunaan obat ini harus SESUAI DENGAN PETUNJUK DOKTER.\n\nKomposisi:\nPer 5 mL sirup : Sucralfate 500 mg\n\nAturan Pakai:\nSaat perut kosong : 1 jam sebelum makan atau 2 jam sesudah makan\ndan menjelang tidur malam'),(10,'BISOLVON EXTRA SIRUP',20,72800,'../img/obat10.webp','Deskripsi:\nBISOLVON EXTRA SIRUP mengandung Bromhexine HCl dan\nGuaifenesin. Obat ini digunakan untuk mengatasi batuk berdahak yang\nbekerja sebagai sekretolitik (mukolitik) dan ekspektoran untuk\nmeredakan batuk berdahak dan mempermudah pengeluaran dahak\npada saat batuk. Obat ini akan membantu dengan 3 langkah kerja,\nyaitu: dengan Melepaskan, Mengencerkan, serta Mengeluarkan dahak,\nsehingga dahak dapat mudah dikeluarkan.\n\nKomposisi:\nPer 5 mL: Bromhexine HCl 4 mg, guaifenesin 100 mg\n\nAturan Pakai:\nDikonsumsi sesudah makan.');
/*!40000 ALTER TABLE `obat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pembelian`
--

DROP TABLE IF EXISTS `pembelian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pembelian` (
  `IdTransaksi` int(11) NOT NULL,
  `IdAkun` int(11) NOT NULL,
  `IdObat` int(11) NOT NULL,
  `Kuantitas` int(11) DEFAULT NULL,
  `HargaKumu` int(11) DEFAULT NULL,
  PRIMARY KEY (`IdTransaksi`,`IdAkun`,`IdObat`),
  KEY `IdAkun` (`IdAkun`),
  KEY `IdObat` (`IdObat`),
  CONSTRAINT `pembelian_ibfk_1` FOREIGN KEY (`IdAkun`) REFERENCES `customer` (`IdAkun`),
  CONSTRAINT `pembelian_ibfk_2` FOREIGN KEY (`IdObat`) REFERENCES `obat` (`IdObat`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pembelian`
--

LOCK TABLES `pembelian` WRITE;
/*!40000 ALTER TABLE `pembelian` DISABLE KEYS */;
INSERT INTO `pembelian` (`IdTransaksi`, `IdAkun`, `IdObat`, `Kuantitas`, `HargaKumu`) VALUES (1,5,1,2,10000),(2,5,1,1,15000),(2,5,2,1,10000);
/*!40000 ALTER TABLE `pembelian` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaksi`
--

DROP TABLE IF EXISTS `transaksi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaksi` (
  `IdTransaksi` int(11) NOT NULL,
  `IdAkun` int(11) NOT NULL,
  `IdObat` int(11) NOT NULL,
  `Kuantitas` int(11) DEFAULT NULL,
  `HargaKumu` int(11) DEFAULT NULL,
  PRIMARY KEY (`IdTransaksi`,`IdAkun`,`IdObat`),
  KEY `IdAkun` (`IdAkun`),
  KEY `IdObat` (`IdObat`),
  CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`IdAkun`) REFERENCES `customer` (`IdAkun`),
  CONSTRAINT `transaksi_ibfk_2` FOREIGN KEY (`IdObat`) REFERENCES `obat` (`IdObat`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaksi`
--

LOCK TABLES `transaksi` WRITE;
/*!40000 ALTER TABLE `transaksi` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaksi` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-21 22:34:56
