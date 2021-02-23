<html>

	<head>

		<title>LabBot21</title>
		<link rel="stylesheet" href="styles.css">
	
	</head>
	<body>
		<h1>LabBot21</h1>
		<?php
			$Password = $_GET["Password"];
			$mode = $_GET["Mode"];
			if($mode != ""){
				$handle = fopen("mode.txt", "w"); 
				fwrite($handle, $mode);
				fclose($handle);
			}
			$rightPassword = file_get_contents("Login.txt");
			$mode = file_get_contents("mode.txt");
					
		?>
		
		<?php if($Password != $rightPassword): ?>
		<?php 
		if($mode == 1){
			echo "Momentaner Modus: Stand-By-Modus";
		}
		if($mode == 2){
			echo "Momentaner Modus: Circle-Without-Orders";
		}
		if($mode == 3){
			echo "Momentaner Modus: Circle-With-Orders";
		}
		?>
		<p>Bitte geben Sie das Passwort für das InsiderLogin ein.</p>
		
		<form method="get">
			<input type="text" name="Password">
			<input type="submit" value="Login">
		</form>
		
		<?php endif ?>
		
		
		<?php if ($Password == $rightPassword): ?>
		<h2>Administrator Login</h2>
		<?php 
		if($mode == 1){
			echo "Momentaner Modus: Stand-By-Modus";
		}
		if($mode == 2){
			echo "Momentaner Modus: Circle-Without-Orders";
		}
		if($mode == 3){
			echo "Momentaner Modus: Circle-With-Orders";
		}
		?>
		<form method="get">
			<table>
				<tr>
					<td>
						<input type="radio" name="Mode" value="1">
					</td>
					<td>
						<p>Stand-By</p>
					</td>
				</tr>
				<tr>
					<td>
						<input type="radio" name="Mode" value="2">
					</td>
					<td>
						<p>Circle without Orders</p>
					</td>
				</tr>
				<tr>
					<td>
						<input type="radio" name="Mode" value="3">
					</td>
					<td>
						<p>Circle with Orders</p>
					</td>
				</tr>
				<tr>
					<td>
					
					</td>
					<td>
						<input type="submit" value="Speichern und LogOut">
					</td>			
				</tr>
			
			</table>
			
			
		</form>
		
		
		<?php else: ?>
		
		<?php
		if($Password != ""){
			echo "Falsche Passwort";
		}
		?>
		
		<?php endif ?>
		<br>
		<br>
		<a href="index.php"><button>Zurück zur Startseite</button></a>
	
	
	
	</body>
	
	
</html>
