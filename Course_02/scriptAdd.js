var data = JSON.parse(document.getElementById("dataJson").innerHTML);



update();

function getip(json){
	document.getElementById("ip").innerHTML = json.ip;
}

function add() {
	data.push({
		"chinese": document.getElementById("ichinese").value,
		"pinyin": document.getElementById("ipinyin").value,
		"english": document.getElementById("ienglish").value.split("; ")
	});

	update();
}

function update(){
	document.getElementById("textarea").value = JSON.stringify(data);
}

