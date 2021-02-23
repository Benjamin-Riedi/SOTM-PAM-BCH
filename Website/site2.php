<html>
	<head>

		<title>LabBot21</title>
		<link rel="stylesheet" href="styles2.css">
	
	</head>
	


	

	<body>
		
		<?php
		$inhalt = "1";
		$handle = fopen("used.txt", "w"); 
		fwrite($handle, $inhalt);
		fclose($handle); 
		?>
		<a href="site3.php"><button>Auftrag abbrechen</button></a>
	
	
	</body>
	
</html>
