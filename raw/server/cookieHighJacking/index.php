
<html>
<head>
	<title>XD</title>
</head>
<body>
<script>alert('Hack by Mr.4fun');</script>
<?php
       
	$LOG=array(
		"ip" => $_SERVER["HTTP_X_FORWARDED_FOR"],
		"pr" => $_SERVER["REMOTE_PORT"],
		"ua" => $_SERVER["HTTP_USER_AGENT"],
		"rq" => $_SERVER["REQUEST_METHOD"]);
	$js=json_encode($LOG);
	$b=fopen("loggedIP.txt","a+");
	$c=fopen("haha.txt","w");
	fwrite($b,"$js
");
	fwrite($c,"$js
");
	fclose($b);
?>
deray
</body>
</html>
	