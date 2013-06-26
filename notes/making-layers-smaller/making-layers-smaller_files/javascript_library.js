/* Global JavaScript function library */

function nonEmptyString(str) {
// tests whether the parameter is of type string
// and is not the empty string
	if (typeof(str) != 'string') {
	    return false; // not a string
	} else if (str == '') {
	    return false; // empty string
	}
	return true;
}

function altTableBodyRows(tableClass, evenRowClass, oddRowClass) {
// sets class attributes on tr elements
// within body of tables having class matching
// tableClass parameter
  	if (! nonEmptyString(tableClass)) {
  	  return false; // tableClass undefined or invalid
  	}
  	var evenClass = ( nonEmptyString(evenRowClass) ? evenRowClass : 'even' );
  	var oddClass = ( nonEmptyString(oddRowClass) ? oddRowClass : 'odd' );
  	var classPattern = '\\b' + tableClass + '\\b'; // regex
  	var classRegexp = new RegExp(classPattern);
  	var allTables = document.getElementsByTagName('table');
  	for ( var i=0; i < allTables.length; i++ ) {      	    
  		if ( classRegexp.test(allTables[i].className) ) {   		    
			var rowcount = 1; // initialize row count
			var tbodies = allTables[i].tBodies; // get tbody sections
			// loop through tbody sections
			for ( var j=0; j < tbodies.length; j++ ) {
				var rows = tbodies[j].rows;
				for ( var k=0; k < rows.length; k++ ) {
					var rowClass = ( rowcount % 2 == 0 ? evenClass : oddClass );
					// append class if not empty
					rows[k].className += ( rows[k].className == '' ? rowClass : ' ' + rowClass );
					rowcount++; // increment row counter
				}
			}  		
  		}
  	}
}

function simpleHttpGet(url) {
// performs an HTTP GET request, typically used for click tracking
// modelled on guardar(url) function in heat map functionality
    var xmlDoc = null;
    if (typeof window.ActiveXObject != 'undefined') {
        xmlDoc = new ActiveXObject('Microsoft.XMLHTTP');
    } else {
        xmlDoc = new XMLHttpRequest();
    }
    xmlDoc.open('GET', url, true);
    xmlDoc.send(null);
}
