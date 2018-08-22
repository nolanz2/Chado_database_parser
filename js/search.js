// this function executes our search via an AJAX call
function runSearch( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#gene_search').serialize();
    
    $.ajax({
        url: './search_product.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON( data ) {
    // set the span that lists the match count
    $('#match_count').text( data.match_count );
    
    // this will be used to keep track of row identifiers
    var next_row_num = 1;
    
    // iterate over each match and add a row to the result table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;
    
        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');
        
        // add the uniquename column
        $('<td/>', { "text" : item.locus_id } ).appendTo('#' + this_row_id);
        
	// add the product column
        $('<td/>', { "text" : item.product } ).appendTo('#' + this_row_id);

        // add the fmin column
        $('<td/>', { "text" : item.fmin } ).appendTo('#' + this_row_id);

	// add the fmax column
        $('<td/>', { "text" : item.fmax } ).appendTo('#' + this_row_id);

    });


$('table th:nth-child(1), table td:nth-child(1)').addClass('locus_tag');
$('table th:nth-child(2), table td:nth-child(2)').addClass('prod');
$('table th:nth-child(3), table td:nth-child(3)').addClass('fmin');
$('table th:nth-child(4), table td:nth-child(4)').addClass('fmax');
$("input:checkbox:not(:checked)").each(function() {
    var column = "table ." + $(this).attr("name");
    $(column).hide();
});


$("input:checkbox").click(function(){
    var column = "table ." + $(this).attr("name");
    $(column).toggle();
});    
    // now show the result section that was previously hidden
    $('#results').show();
}


// run our javascript once the page is ready
$(document).ready( function() {
    
    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        runSearch();
        return false;  // prevents 'normal' form submission
    });
	
});
