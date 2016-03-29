var data = JSON.parse(document.getElementById("dataJson").innerHTML);

var i = Math.floor(Math.random() * data.length)
document.getElementById('chinese').innerHTML = data[i]["chinese"];

function next() {
	i = Math.floor(Math.random() * data.length)
	document.getElementById('chinese').innerHTML = data[i]["chinese"];
	document.getElementById('english').innerHTML = "--------";
	document.getElementById('pinyin').innerHTML = "--------";
}

function reveal(div) {
	if (document.getElementById(div).innerHTML == "--------") {};

	if (div == "english") {
		document.getElementById(div).innerHTML = data[i][div][Math.floor(Math.random() * data[i][div].length)]
	}  else {
		document.getElementById(div).innerHTML = data[i][div];
	}
}

document.onkeyup=function(e) {
	console.log(e);

    if(e.key == "e")
    	document.getElementById("english").innerHTML = data[i]["english"][Math.floor(Math.random() * data[i]["english"].length)]
    else if (e.key == "p")
		document.getElementById("pinyin").innerHTML = data[i]["pinyin"];
	else if (e.key == "n")
		next()
}