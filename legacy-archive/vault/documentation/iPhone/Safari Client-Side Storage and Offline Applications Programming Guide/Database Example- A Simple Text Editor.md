---
title: Safari Client-Side Storage and Offline Applications Programming Guide
apple_id: TP40007256
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Data Management
technology: null
published: '2011-09-21'
source_url: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/SafariJSDatabaseGuide/ASimpleExample/ASimpleExample.html
archived_at: '2026-07-18T02:27:24.927115Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Client-Side Storage and Offline Applications Programming Guide](Introduction.md)


[Previous](Document%20Revision%20History.md)

# Database Example: A Simple Text Editor

This example shows a practical, real-world example of how to use the SQL database support. This example contains a very simple HTML editor that stores its content in a local database. This example also demonstrates how to tell Safari about unsaved edits to user-entered content.

This example builds upon the example in the sample code project _[HTML Editing Toolbar](../../../samplecode/HTML%20Editing%20Toolbar/HTML%20Editing%20Toolbar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzygm)_, available from the ADC Reference Library. To avoid code duplication, the code from that example is not repeated here. The HTML Editing Toolbar creates an editable region in an HTML page and displays a toolbar with various editing controls.

To create this example, either download the attached Companion Files archive or perform the following steps:

1. Download the _[HTML Editing Toolbar](../../../samplecode/HTML%20Editing%20Toolbar/HTML%20Editing%20Toolbar.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzygm)_ sample and extract the contents of the archive.
2. From the toolbar project folder, copy the files `FancyToolbar.js` and `FancyToolbar.css` into a new folder.

   Also copy the folder `FancyToolbarImages`.

   You do not need to copy the `index.html` or `content.html` files provided by that project.
3. Add a save button in the toolbar. This change is described in [Adding a Save Button to FancyToolbar.js](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnbnknltc).
4. Add the `index.html` and `SQLStore.js` files into the same directory. You can find listings for these files in [Creating the index.html File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnbnknlte) and [Creating the SQLStore.js File](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnbnknltg).

To use the editor, open the `index.html` file in Safari. Click the Create New File link to create a new “file”. Edit as desired, and click the save button in the toolbar.

Next, reload the `index.html` page. You should see the newly created file in the list of available files. If you click on its name, you will see the text you just edited.

In the the `FancyToolbar.js` (which you should have copied from the HTML Editing Toolbar sample previously), you need to add a few lines of code to add a Save button to the toolbar it displays.

Immediately _before_ the following line, which is near the bottom of the function `setupIfNeeded`:

```

    this.toolbarElement.appendChild(toolbarArea);
```

add the following block of code:

__Listing A-1__  Additions to FancyToolbar.js

```
    this.saveButton = document.createElement("button");
    this.saveButton.appendChild(document.createTextNode("Save"));
    this.saveButton.className = "fancy-toolbar-button fancy-toolbar-button-save";
    this.saveButton.addEventListener("click", function(event) { saveFile() }, false);
    toolbarArea.appendChild(this.saveButton);
```


This file provides some basic HTML elements that are used by the JavaScript code to display text and accept user input. Save the following as `index.html` (or any other name you choose):

__Listing A-2__  index.html

```
<html><head><title>JavaScript SQL Text Editor</title>
<script language="javascript" type="text/javascript" src="FancyToolbar.js"></script>
<script language="javascript" type="text/javascript" src="SQLStore.js"></script>
<link rel="stylesheet" type="text/css" href="FancyToolbar.css">

<style>
body {
    // margin: 80px;
    // background-color: rgb(153, 255, 255);
}

iframe.editable {
    width: 80%;
    height: 300px;
    margin-top: 60px;
    margin-left: 20px;
    margin-right: 20px;
    margin-bottom: 20px;
}

table.filetable {
    border-collapse: collapse;
}

tr.filerow {
    border-collapse: collapse;
}

td.filelinkcell {
    border-collapse: collapse;
    border-right: 1px solid #808080;
    border-bottom: 1px solid #808080;
    border-top: 1px solid #808080;
}

td.filenamecell {
    border-collapse: collapse;
    padding-right: 20px;
    border-bottom: 1px solid #808080;
    border-top: 1px solid #808080;
    border-left: 1px solid #808080;
    padding-left: 10px;
    padding-right: 30px;
}
</style>

</head><body onload="initDB(); setupEventListeners(); chooseDialog();">

<div id="controldiv"></div>
<iframe id="contentdiv" style="display: none" class="editable"></iframe>

<div id="origcontentdiv" style="display: none"></div>
<div id="tempdata"></div>


</body>
</html>
```


This script contains all of the database functionality for this example. The functions here are called from `index.html` and `FancyToolbar.js`.

The major functions are:

- `initDB`—opens a connection to the database and calls `createTables` to create tables if needed.
- `createTables`—creates tables in the database if they do not exist.
- `chooseDialog`—displays a “file” selection dialog
- `deleteFile`—displays a deletion confirmation dialog
- `reallyDelete`—flags a “file” for deletion
- `createNewFileAction`—creates a new “file” entry
- `saveFile`—saves a “file” into the database.
- `loadFile`—loads a “file” from the database.

In addition to these functions, this example contains several other functions that serve minor roles in modifying the HTML content or handling results and errors.

The function `saveChangesDialog` is also interesting to web application developers. It demonstrates one way to determine whether a user has made unsaved changes to user-entered content and to display a dialog allowing the user to choose whether to leave the page in such a state.

Save the following file as `SQLStore.js` (or modify the `index.html` file to refer to the name you choose):

__Listing A-3__  SQLStore.js

```

var systemDB;

/*! Initialize the systemDB global variable. */
function initDB()
{


try {
    if (!window.openDatabase) {
        alert('not supported');
    } else {
        var shortName = 'mydatabase';
        var version = '1.0';
        var displayName = 'My Important Database';
        var maxSize = 65536; // in bytes
        var myDB = openDatabase(shortName, version, displayName, maxSize);

        // You should have a database instance in myDB.

    }
} catch(e) {
    // Error handling code goes here.
    if (e == INVALID_STATE_ERR) {
        // Version number mismatch.
    alert("Invalid database version.");
    } else {
    alert("Unknown error "+e+".");
    }
    return;
}

// alert("Database is: "+myDB);

createTables(myDB);
systemDB = myDB;

}


/*! Format a link to a document for display in the "Choose a file" pane. */
function docLink(row)
{
    var name = row['name'];
    var files_id = row['id'];

    return "<tr class='filerow'><td class='filenamecell'>"+name+"</td><td class='filelinkcell'>(<a href='#' onClick=loadFile("+files_id+")>edit</a>)&nbsp;(<a href='#' onClick=deleteFile("+files_id+")>delete</a>)</td></tr>\n";
}

/*! If a deletion resulted in a change in the list of files, redraw the "Choose a file" pane. */
function deleteUpdateResults(transaction, results)
{
    if (results.rowsAffected) {
        chooseDialog();
    }
}

/*! Mark a file as "deleted". */
function reallyDelete(id)
{
    // alert('delete ID: '+id);
    var myDB = systemDB;

    myDB.transaction(
        new Function("transaction", "transaction.executeSql('UPDATE files set deleted=1 where id=?;', [ "+id+" ], /* array of values for the ? placeholders */"+
            "deleteUpdateResults, errorHandler);")
    );

}

/*! Ask for user confirmation before deleting a file. */
function deleteFile(id)
{
    var myDB = systemDB;

    myDB.transaction(
        new Function("transaction", "transaction.executeSql('SELECT id,name from files where id=?;', [ "+id+" ], /* array of values for the ? placeholders */"+
            "function (transaction, results) {"+
                "if (confirm('Really delete '+results.rows.item(0)['name']+'?')) {"+
                    "reallyDelete(results.rows.item(0)['id']);"+
                "}"+
            "}, errorHandler);")
    );
}

/*! This prints a list of "files" to edit. */
function chooseDialog()
{
    var myDB = systemDB;

    myDB.transaction(
        function (transaction) {
        transaction.executeSql("SELECT * from files where deleted=0;",
            [ ], // array of values for the ? placeholders
            function (transaction, results) {
                var string = '';
                var controldiv = document.getElementById('controldiv');
                for (var i=0; i<results.rows.length; i++) {
                    var row = results.rows.item(i);
                    string = string + docLink(row);
                }
                if (string == "") {
                    string = "No files.<br />\n";
                } else {
                    string = "<table class='filetable'>"+string+"</table>";
                }
                controldiv.innerHTML="<H1>Choose a file to edit</H1>"+string+linkToCreateNewFile();
            }, errorHandler);
        }
    );

}

/*! This prints a link to the "Create file" pane. */
function linkToCreateNewFile()
{
    return "<p><button onClick='createNewFile()'>Create New File</button>";
}


/*! This creates a new "file" in the database. */
function createNewFileAction()
{
    var myDB = systemDB;
    var name = document.getElementById('createFilename').value

    // alert('Name is "'+name+'"');

    myDB.transaction(
        function (transaction) {
            var myfunc = new Function("transaction", "results", "/* alert('insert ID is'+results.insertId); */ transaction.executeSql('INSERT INTO files (name, filedata_id) VALUES (?, ?);', [ '"+name+"', results.insertId], nullDataHandler, killTransaction);");

                transaction.executeSql('INSERT INTO filedata (datablob) VALUES ("");', [],
                myfunc, errorHandler);
        }
    );

    chooseDialog();
}

/*! This saves the contents of the file. */
function saveFile()
{
    var myDB = systemDB;
    // alert("Save not implemented.\n");

    var contentdiv = document.getElementById('contentdiv');
    var contents = contentdiv.contentDocument.body.innerHTML;

    // alert('file text is '+contents);

    myDB.transaction(
        function (transaction) {
            var contentdiv = document.getElementById('contentdiv');
            var datadiv = document.getElementById('tempdata');

            var filedata_id = datadiv.getAttribute('lfdataid');
            var contents = contentdiv.contentDocument.body.innerHTML;

            transaction.executeSql("UPDATE filedata set datablob=? where id=?;",
                [ contents, filedata_id ], // array of values for the ? placeholders
                nullDataHandler, errorHandler);
            // alert('Saved contents to '+filedata_id+': '+contents);
            var origcontentdiv = document.getElementById('origcontentdiv');
            origcontentdiv.innerHTML = contents;

            alert('Saved.');
            }
    );
}

/*! This displays the "Create file" pane. */
function createNewFile()
{
    var myDB = systemDB;
    var controldiv = document.getElementById('controldiv');
    var string = "";

    string += "<H1>Create New File</H1>\n";
    string += "<form action='javascript:createNewFileAction()'>\n";
    string += "<input id='createFilename' name='name'>Filename</input>\n";
    string += "<input type='submit' value='submit' />\n";
    string += "</form>\n";

    controldiv.innerHTML=string;

}

/*! This processes the data read from the database by loadFile and sets up the editing environment. */
function loadFileData(transaction, results)
{
    var controldiv = document.getElementById('controldiv');
    var contentdiv = document.getElementById('contentdiv');
    var origcontentdiv = document.getElementById('origcontentdiv');
    var datadiv = document.getElementById('tempdata');

    // alert('loadFileData called.');

    var data = results.rows.item(0);
    var filename = data['name'];
    var filedata = data['datablob'];
    datadiv.setAttribute('lfdataid', parseInt(data['filedata_id']));

    document.title="Editing "+filename;
    controldiv.innerHTML="";
    contentdiv.contentDocument.body.innerHTML=filedata;
    origcontentdiv.innerHTML=filedata;
    contentdiv.style.border="1px solid #000000";
    contentdiv.style['min-height']='20px';
    contentdiv.style.display='block';
    contentdiv.contentDocument.contentEditable=true;
}

/*! This loads a "file" from the database and calls loadFileData with the results. */
function loadFile(id)
{
    // alert('Loading file with id '+id);
    var datadiv = document.getElementById('tempdata');
    datadiv.setAttribute('lfid', parseInt(id));

    myDB = systemDB;
    myDB.transaction(
        function (transaction) {
            var datadiv = document.getElementById('tempdata');
            var id = datadiv.getAttribute('lfid');
            // alert('loading id' +id);
            transaction.executeSql('SELECT * from files, filedata where files.id=? and files.filedata_id = filedata.id;', [id ], loadFileData, errorHandler);
        }
    );

}

/*! This creates the database tables. */
function createTables(db)
{

/* To wipe out the table (if you are still experimenting with schemas,
   for example), enable this block. */
if (0) {
    db.transaction(
        function (transaction) {
        transaction.executeSql('DROP TABLE files;');
        transaction.executeSql('DROP TABLE filedata;');
        }
    );
}

db.transaction(
    function (transaction) {
        transaction.executeSql('CREATE TABLE IF NOT EXISTS files(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, filedata_id INTEGER NOT NULL, deleted INTEGER NOT NULL DEFAULT 0);', [], nullDataHandler, killTransaction);
        transaction.executeSql('CREATE TABLE IF NOT EXISTS filedata(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, datablob BLOB NOT NULL DEFAULT "");', [], nullDataHandler, errorHandler);
    }
);

}

/*! When passed as the error handler, this silently causes a transaction to fail. */
function killTransaction(transaction, error)
{
    return true; // fatal transaction error
}

/*! When passed as the error handler, this causes a transaction to fail with a warning message. */
function errorHandler(transaction, error)
{
    // error.message is a human-readable string.
    // error.code is a numeric error code
    alert('Oops.  Error was '+error.message+' (Code '+error.code+')');

    // Handle errors here
    var we_think_this_error_is_fatal = true;
    if (we_think_this_error_is_fatal) return true;
    return false;
}

/*! This is used as a data handler for a request that should return no data. */
function nullDataHandler(transaction, results)
{
}

/*! This returns a string if you have not yet saved changes.  This is used by the onbeforeunload
    handler to warn you if you are about to leave the page with unsaved changes. */
function saveChangesDialog(event)
{
    var contentdiv = document.getElementById('contentdiv');
    var contents = contentdiv.contentDocument.body.innerHTML;
    var origcontentdiv = document.getElementById('origcontentdiv');
    var origcontents = origcontentdiv.innerHTML;

    // alert('close dialog');

    if (contents == origcontents) {
    return NULL;
    }

    return "You have unsaved changes."; //   CMP "+contents+" TO "+origcontents;
}

/*! This sets up an onbeforeunload handler to avoid accidentally navigating away from the
    page without saving changes. */
function setupEventListeners()
{
    window.onbeforeunload = function () {
    return saveChangesDialog();
    };
}
```

[Previous](Document%20Revision%20History.md)

