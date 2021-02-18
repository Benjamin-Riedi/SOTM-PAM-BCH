<html>
	<head>

		<title>LabBot21</title>
		<link rel="stylesheet" href="styles.css">
	
	</head>
	


	

	<body>
		<?php
		$inhalt = "0";
		$handle = fopen("test.txt", "w+"); 
		fwrite($handle, $inhalt);
		fclose($handle); 
		echo "fertig";
		?>
	<a href="index.html">Auftrag abbrechen</a>
	
	
	</body>
	
</html>
