var main = function(to_do_objects){
	"use strict";
	var $content;
	var toDos = to_do_objects.map(function (toDo){
		return toDo.description;
	});
	var $button = document.createElement("button");
        $button.type = "button";
        $button.id = "btnAC";
        $button.textContent = "Add Content";            
	var $input = document.createElement("input");
        $input.type = "text";
	
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
				console.log("Щелчок на вкладке Теги");
				organized.forEach(function (tag){
					var $tagName = $("<h3>").text(tag.name),
						$content = $("<ul>");
					tag.toDos.forEach(function (description){
						var $li = $("<li>").text(description);
						$content.append($li);
					});
					$("main .content").append($tagName);
					$("main .content").append($content);
				});
			}
			else if($element.parent().is(":nth-child(4)")){	
				$("main .content").append($button);
				$("main .content").append($input);
				var buttonAC = document.getElementById("btnAC");
        			buttonAC.addEventListener("click", function (){
                			console.log("it's Work!!!");
                			if($("main .content input").val() !== ""){
		                        	toDos.push($(".content input").val());
                		        	$("main .content input").val("");
               				}
        			},false);
			}
			return false;
		});
	});
	$(".tabs a:first-child span").trigger("click");
};
$(document).ready(function () {
	$.getJSON("javascripts/todos.json", function (to_do_objects){
		//вызов функции main с аргументом в виде объекта to_do_objects
		main(to_do_objects);
	});
});
