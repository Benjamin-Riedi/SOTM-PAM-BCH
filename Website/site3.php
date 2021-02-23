<html>
	<head>

		<title>LabBot21</title>
		<link rel="stylesheet" href="styles.css">
	
	</head>
	<body>
		<?php
		$inhalt = "0";
		$handle = fopen("used.txt", "w"); 
		fwrite($handle, $inhalt);
		fclose($handle); 
		?>
		<h1>LabBot21</h1>
		<br>
		<p>Der Auftrag von LabBot21 wurde abgebrochen.</p>
		<br>
		<a href="index.php"><button>Zurück zur Startseite</button></a>
		
	</body>


</html>
