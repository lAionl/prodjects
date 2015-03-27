var main = function(){
	"use strict";
	var $content;
	var toDos = [
		"Закончить писать эту книгу",
		"Вывести Грейси на прогулку в парк",
		"Ответить на электронные письма",
		"Подготовиться к лекции в понедельник",
		"Обновить несколько новых задач",
		"Купить продукты"
	];
	var showTabContent = function(massOfContent){
		$content = $("<ul>");
		massOfContent.forEach(function (todo){
			$content.append($("<li>").text(todo))
		});
		$("main .content").append($content);
	};
	var addTask = function(massOfContent){
		if($("main .content input").val() !== ""){
                        massOfContent.push($(".content input").val());
                        $("main .content input").val("");
                }
	}
	$(".tabs a span").toArray().forEach(function (element){
		//создаем обработчик щелчков для этого элемента
		$(element).on("click", function(){
			//поскольку мы используем версию элемента jQuery,
			//нужно создать временную переменную,
			//чтобы избежать постоянного обновления
			var $element = $(element);
			$(".tabs a span").removeClass("active");
			$(element).addClass("active");
			$("main .content").empty();
			if($element.parent().is(":nth-child(1)")){
				showTabContent(toDos.reverse());
				toDos.reverse();
			}
			else if($element.parent().is(":nth-child(2)")){
				showTabContent(toDos);
			}
			else if($element.parent().is(":nth-child(3)")){
				var button = document.createElement("button");
		                button.type = "button";
               			button.id = "btnAC";
                		button.textContent = "Add Content";
				button.onclick = "addTask(toDos);";				

				var input = document.createElement("input");
				input.type = "text";
				
				$("main .content").append(button);
				$("main .content").append(input);
			}
			return false;
		});
	});
	$(".tabs a:first-child span").trigger("click");
};
$(document).ready(main);
