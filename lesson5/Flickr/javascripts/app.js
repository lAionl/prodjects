var main = function(){
	"use strict";
	var url = "https://api.flickr.com/services/feeds/photos_public.gne?tags=dogs&format=json&jsoncallback=?";
	$.getJSON(url, function(flickr_response){
		//выводим ответ в консоль
		flickr_response.items.forEach(function (photo){
			//создаем новый элемент jQuery для помещения в него изображения
			var $img = $("<img>").hide();
			//помещаем в атрибут URL, хранящийся в ответе Flickr
			$img.attr("src", photo.media.m);
			//прикрепляем тек img к элементу main.photos
			$("main .photos").append($img);
			$img.fadeIn();
		});
	});
};
$(document).ready(main);
