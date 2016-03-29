<!DOCTYPE html>
<html>
<head>
	<title>Data science - Chinese vocabulary</title>
	<meta charset="UTF-8">
	<style type="text/css">
	body {
		font-family: sans-serif;
		background-color: rgb(29, 41, 41);
	}

	#main {
		margin-top: 200px;
		text-align: center;
	}

	.field {
		position: relative;
		width: 30%;
		margin-left: auto;
		margin-right: auto;
		padding: 0.5em;
		background-color: white;
		text-align: center;
		height: 1.1em;
	}

	#chinese {
		border-top-left-radius: 4px;
		border-top-right-radius: 4px;
		z-index: 10;
		box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.4);
		border-bottom: rgb(0, 195, 228) solid 1px;
	}

	.hidden {
		color: lightgray;
		box-shadow: 0px 0px 3px rgba(0, 0, 0, 0.5);
		z-index: 1;
	}

	.last {
		z-index: 0;
		border-bottom-left-radius: 4px;
		border-bottom-right-radius: 4px;
		margin-bottom: 2em;
	}

	button {
		box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.4);
	}

	#add{
		position: absolute;
		top: 10px;
		left: 10px;
	}
	</style>
</head>

<body>
	<a href="./add.php"><button id="add">Add</button></a>
	<div id="main">
		<div class="field first" id="chinese">chinese</div>
		<div class="field hidden" id="pinyin" onclick="reveal('pinyin')">--------</div>
		<div class="field hidden last" id="english" onclick="reveal('english')">--------</div>
	    <button onclick="next()">Next</button>
	</div>

<script type="text/javascript" id="dataJson">
<?php require './json/hsk1.json'; ?>
</script>
<script type="text/javascript" src="script.js"></script>
</body>
</html>