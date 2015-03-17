
<html>
<body>
<h1>PAGE DE baptiste</h1>
    <?php
	   echo"salut jb";
	    $connecte= mysql_connect("ftp.baptiste.fr","jb","jean") or die("impossible d'acceder a mysql");
		mysql_select_db("jb",$connecte);
		$sql="SELECT * FROM pacha";
		$requete=mysql_query($sql,$connecte);
		while($row=mysql_fetch_array($requete)) {
		    $id=$row['id'];
			$nom=$row['nom'];
			$prenom=$row['prenom'];
			echo" --$nom <br\> $prenom <br\>";
		}
		?>
		
</body>
</html>
