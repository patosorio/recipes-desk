$(document).ready(function(){

    $('.sidenav').sidenav();
    $('input#input_text, textarea#textarea2').characterCounter();
    $('select').formSelect();
    $('.dropdown-trigger').dropdown();
    $('.modal').modal();
    $('.tabs').tabs();

    // add field functions

    var add_ingredient = $(".addIngredient");
    var add_step = $(".addStep");
    var ingredients_wrapper = $(".ingredients-wrapper");
    var steps_wrapper = $(".steps-wrapper")

    var i = 3
    $(add_ingredient).click(function(e){ 
		e.preventDefault();
		$(ingredients_wrapper).append('<textarea id="recipe_ingredients' + i + '" name="recipe_ingredients" class="materialize-textarea ingredient-field" data-length="20"></textarea>');
        i++;
	});

    var j = 3

    $(add_step).click(function(e){ 
		e.preventDefault();
		$(steps_wrapper).append('<textarea id="steps' + j + '" name="steps" class="materialize-textarea steps-field" data-length="100"></textarea>');
        j++;
	});


});