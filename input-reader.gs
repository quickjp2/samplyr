/**
 * doPost() function to add data to a spreadsheet.
 *
 * Spreadsheet data is provided as a querystring, e.g. ?col1=1&col2='pizza'
 *
 * @param {event} e Event passed to doPost, with querystring
 * @returns {String/html} Html to be served
 *
 * Test URLs (adjust ID as needed):
 *   https://script.google.com/macros/s/--PUB-SCRIPT-ID--/exec?col1=1&col2='pizza'
 */
function doPost(e) {  
  Logger.log( JSON.stringify(e) );  // view parameters

  var result = 'Ok'; // assume success

  if (e.parameter == undefined) {
    result = 'No Parameters';
  }
  else {
   addBootLog(e);
  }

  // Return result of operation
  return ContentService.createTextOutput(result);
}

/**
 * Remove leading and trailing single or double quotes
 */
function stripQuotes( value ) {
  return value.replace(/^["']|['"]$/g, "");
}

function addBootLog(e){
    var id = '<Name of spreadsheet used for logs>'; // Spreadsheet id for responses
    //var sheet = SpreadsheetApp.openById(id).getActiveSheet();
    var sheet = SpreadsheetApp.openByUrl('<Sharable URL for editors>').getActiveSheet();
    var newRow = sheet.getLastRow() + 1;
    var rowData = [];
    var date = new Date();
    rowData[0] = date + " " + date.toLocaleTimeString() // Timestamp
    for (var param in e.parameter) {
      Logger.log('In for loop, param='+param);
      var value = stripQuotes(e.parameter[param]);
      //Logger.log(param + ':' + e.parameter[param]);
      switch (param) {
        case 'P1G': 
          rowData[1] = value;
          break;
        case 'P1R':
          rowData[2] = value;
          break;
        case 'P2G':
          rowData[3] = value;
          break;
        case 'P2R':
          rowData[4] = value;
          break;
        case 'P3G':
          rowData[5] = value;
          break;
        case 'P3R':
          rowData[6] = value;
          break;
        case 'P4G':
          rowData[7] = value;
          break;
        case 'P4R':
          rowData[8] = value;
          break;
        default:
          result = "unsupported parameter";
      }
    }
    Logger.log(JSON.stringify(rowData));

    // Write new row to spreadsheet
    var newRange = sheet.getRange(newRow, 1, 1, rowData.length);
    newRange.setValues([rowData]);
}
