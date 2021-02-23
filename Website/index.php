<html>

	<head>

		<title>LabBot21</title>
		<link rel="stylesheet" href="styles.css">
	
	</head>

	<body>
		<h1>LabBot21</h1>
		<p>Klicken Sie auf den Link unten und legen Sie das Smartphone mit dem Bildschirm nach oben auf den Tisch, um den LabBot21 zu rufen</p>
		<br>
		
		<?php 
		
		$txt = file_get_contents("used.txt");
		$text = $_GET["send"];
		
		?>
		
		<?php if ($txt == 0): ?>
		
		<form method="get">
			<input type="submit" name="send" value="LabBot21 rufen">
		</form>
		<?php
		
		if ($text == "LabBot21 rufen"){
			if ($txt == 0){
				header("Location: site2.php");
			}
		}
		
		?>
	
		<?php else: ?>
		
		<p>LabBot21 wird zur Zeit benutzt</p>
		
		<?php 
		
			if ($text == "LabBot21 rufen"){
				header("Location: index.php");
			}
		
		?>
		
		<?php endif ?>
		<br>
		<a href="insiderLogin.php"><button>Zum Insider Login</button></a>
	</body>
		
</html>


