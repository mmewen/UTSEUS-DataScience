<!DOCTYPE html>
<html>
<head>
	<title>Data science - Chinese vocabulary</title>
	<meta charset="UTF-8">
	<style type="text/css">
	body {
		font-family: sans-serif;
		background-color: rgb(173, 200, 200);
	}

	#main {
		text-align: center;
	}

	.field {
		display: inline;
		position: relative;
		width: 30%;
		padding: 0.5em;
		background-color: white;
		text-align: center;
		height: 1.1em;
		border-radius: 4px;
		color: lightgray;
		box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.4);
	}

	.last {
		z-index: 0;
		margin-right: 2em;
	}

	button {
		box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.4);
	}

	#add{
		position: absolute;
		top: 10px;
		left: 10px;
	}

	input {
		margin-left: 0.5em;
	}

	textarea {
		width: 100%;
		bottom: 0px;
		left: 0px;
		position: fixed;
		height: 90%;
		overflow: scroll;
	}

	#ip{
		position: absolute;
		top: 35px;
		left: 10px;
		color: white;
	}
	</style>
</head>

<body>
	<a href="./add.php"><button id="add">Index</button></a>
	<div id="ip"></div>
	<div id="main">
		<div class="field first" id="chinese">Chinese<input id="ichinese" type="text"></input></div>
		<div class="field hidden" id="pinyin" onclick="reveal('pinyin')">Pinyin<input id="ipinyin" type="text"></input></div>
		<div class="field hidden last" id="english" onclick="reveal('english')">English<input id="ienglish" type="text"></input></div>
	    <button onclick="add()">Add</button>
	</div>
	<textarea id="textarea" spellcheck="false"></textarea>
<script type="text/javascript" id="dataJson">
<?php require './json/hsk1.json'; ?>
</script>
<script type="application/javascript" src="http://www.telize.com/jsonip?callback=getip"></script>
<script type="text/javascript" src="scriptAdd.js"></script>
</body>
</html>