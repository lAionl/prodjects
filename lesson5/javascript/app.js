var main = function(){
	"use strict";
	$.getJSON("cards/aceOfSpades.json", function (card){
		//создаем элемент для хранения карты
		var $cardParagraph = $("<p>");
		//создаем
		$cardParagraph.text(card.rank + " of " + card.suit);
		//связываем абзац с картой main
		$("main").append($cardParagraph);	
	});
	$.getJSON("cards/hand.json", function (hand){
		var $list = $("<ul>");
		//hand - массив, поэтому можно применить к нему интерационный процесс
		//с помощью цыкла forEach
		hand.forEach(function (card){
			//создаем элемент списка для хранения карты
			//и присоединяем его к списку
			var $card = $("<li>");
			$card.text(card.rank + " of " + card.suit);
			$list.append($card);
		});
		//присоединяем список к элементу main
		$("main").append($list);
	});
};
$(document).ready(main);
