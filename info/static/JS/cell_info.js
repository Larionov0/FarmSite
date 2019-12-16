function alerter(){
	alert('Привет! JS подключен!');
}

function set_check(element) {
	if (document.getElementById('moving_label').firstChild.checked == true){
		index = checked_animals.indexOf(element.id);
		if (index == -1){
			checked_animals.push(element.id);
		} else {
			checked_animals.splice(index, 1);
		}
		console.log(checked_animals);
		
	};
}

function start_moving(el) {
	if (el.checked) {
		checked_animals = [];
		document.getElementById('move').style.display = 'flex';
	} else {
		document.getElementById('move').style.display = 'none';

	}
}

function send_animals() {
	postData(url, checked_animals)
	  .then(data => console.log(JSON.stringify(data))) // JSON-строка полученная после вызова `response.json()`
	  .catch(error => console.error(error));
}

function postData(url = '', animals = {}) {
	let data = new FormData();
	alert(csrf_token);
	data.append('animals', animals);
  	data.append('csrfmiddlewaretoken',  csrf_token);
    return fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, cors, *same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token,
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        referrer: 'no-referrer', // no-referrer, *client
        body: JSON.stringify(data), // тип данных в body должен соответвовать значению заголовка "Content-Type"
    })
    .then(response => response.json()); // парсит JSON ответ в Javascript объект
}


checked_animals = [];
