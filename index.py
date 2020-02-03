<!-- <!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>

<div class="profile">
	<h1>Davud Seyfullayev</h1>
	<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdpBEf6Zmjl40AHZpsNq32fnSw5MaZbwLz_-clppwuTjBLqWQE&s" alt="">
</div>

<div class="melumatlar">
	<table border="1">
		<thead>
			<tr>
				<th>Ad</th>
				<th>Soyad</th>
				<th>Yash</th>
				<th>Email</th>
				<th>Nomre</th>
			</tr>
		</thead>
		<tbody>
			<tr style="color: blue; text-align: center;">
				<td>Davud</td>
				<td>Seyfullayev</td>
				<td>18</td>
				<td>davud.seyfullayev44@gmail.com</td>
				<td>050-555-37-98</td>
			</tr>
			<tr style="color: red; text-align: center;">
				<td>Davud</td>
				<td>Seyfullayev</td>
				<td>18</td>
				<td>davud.seyfullayev44@gmail.com</td>
				<td>050-555-37-98</td>
			</tr>
			<tr style="color: green; text-align: center;">
				<td>Davud</td>
				<td>Seyfullayev</td>
				<td>18</td>
				<td>davud.seyfullayev44@gmail.com</td>
				<td>050-555-37-98</td>
			</tr>
		</tbody>
	</table>
</div>

<div class="bg-image">
	<p>burada background-image var</p>
</div>
</body>
</html>

<style >
.profile{
	width:60%;
	margin-left: 20%;
	text-align: center;
	background-color: aqua;
	outline: 10px solid red;
}
.profile img{
	border-radius: 50%;
}
.profile h1{
	text-shadow: 5px 5px 5px black;
	color: white;	
}
.melumatlar{
	width:60%;
	margin-left: 20%;
	outline: 10px solid green;
	padding:10px 0px	10px  0px;
	margin-top: 2%;
}
.melumatlar table{
	margin-left: 20%;
}
.bg-image{
	margin-top: 2%;
	height: 200px;
	width: 100%;
	background-image: url(https://mobilistanbul.org/wp-content/uploads/2014/07/section-BG-dark.jpg);
	text-align: center;
}
.bg-image p{
font-size: 50px;
color: white;
text-decoration: underline;
}
</style> -->


<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	
		<p id="p">abcd</p>
	
	<button onclick="change()">click me</button>
</body>
</html>


<script>
	function change()
	{

		a= '#';
		var p = document.getElementById('p').innerHTML;
		var div = document.getElementById('div')
		div.innerHTML = ''
		for(var i = 0; i < 6;  i++){
		a= a + Math.floor(Math.random() * 10);
		var span = document.createElement('span')
		span.innerHTML = p.charAt(i)
		div.appendChild(span)
		span.style.color = a
		}
		
		
	}
</script>