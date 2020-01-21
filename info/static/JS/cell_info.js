function alerter(){
	alert('Привет! JS подключен!');
}

function toPage(url, par){
  //par = _self
  window.open(url, par);
}

function set_check(element) {
	if (document.getElementById('moving_label').firstChild.checked == true){
		index = checked_animals.indexOf(element.id);
		if (index == -1){
		    // Если эта свинья еще не отмечена
			checked_animals.push(element.id);
			element.style['background-color'] = 'yellow';
		} else {
			checked_animals.splice(index, 1);
			element.style['background-color'] = 'white';
		}
		console.log(checked_animals);
	};
}

function start_moving(el) {
    // << Перемещать (поставили/убрали галочку) >>
	if (el.checked) {
		checked_animals = [];
		document.getElementById('move').style.display = 'flex';
	} else {
	    animals = document.getElementsByClassName('animal');  // Кривая структура ???
	    for (i=0; i<count_of_all_animals; i++){
            animal = animals.item(i);
	        animal.style['background-color'] = 'white';
	    }

		checked_animals = [];
		document.getElementById('move').style.display = 'none';
	}
}

function send_animals() {
    a = url + "?animals=" + JSON.stringify(checked_animals);
    toPage(a, "_self");
}

checked_animals = [];
