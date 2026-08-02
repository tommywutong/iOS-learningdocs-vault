---
title: Safari Client-Side Storage and Offline Applications Programming Guide
apple_id: TP40007256
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Data Management
technology: null
published: '2011-09-21'
source_url: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/SafariJSDatabaseGuide/UsingtheJavascriptDatabase/UsingtheJavascriptDatabase.html
archived_at: '2026-07-18T02:27:27.581517Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Client-Side Storage and Offline Applications Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Relational%20Database%20Basics.md)

# Using the JavaScript Database

Beginning in Safari 3.1 and iOS 2.0, Safari supports the HTML5 JavaScript database class. The JavaScript database class, based on SQLite, provides a relational database intended for local storage of content that is too large to conveniently store in cookies (or is too important to risk accidentally deleting when the user clears out his or her cookies).

Because it provides a relational database model, the JavaScript database class makes it easy to work with complex, interconnected data in a webpage. You might use it as an alternative to storing user-generated data on the server (in a text editor, for example), or you might use it as a high-speed local cache of information the user has recently queried from a server-side database.

The sections in this chapter guide you through the basic steps of creating a JavaScript-based application that takes advantage of the JavaScript database.

Before you can use a database or create tables within the database, you must first open a connection to the database. When you open a database, an empty database is automatically created if the database you request does not exist. Thus, the processes for opening and creating a database are identical.

To open a database, you must obtain a database object with the `openDatabase` method as follows:

__Listing 4-1__  Creating and opening a database

```
try {
    if (!window.openDatabase) {
        alert('not supported');
    } else {
        var shortName = 'mydatabase';
        var version = '1.0';
        var displayName = 'My Important Database';
        var maxSize = 65536; // in bytes
        var db = openDatabase(shortName, version, displayName, maxSize);

        // You should have a database instance in db.
    }
} catch(e) {
    // Error handling code goes here.
    if (e == 2) {
        // Version number mismatch.
        alert("Invalid database version.");
    } else {
        alert("Unknown error "+e+".");
    }
    return;
}

alert("Database is: "+db);
```

For now you should set the version number field to 1.0; database versioning is described in more detail in [Working With Database Versions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznlbjvomi).

The short name is the name for your database as stored on disk (usually in `~/Library/Safari/Databases/`). This argument controls which database you are accessing.

The display name field contains a name to be used by the browser if it needs to describe your database in any user interaction, such as asking permission to enlarge the database.

The maximum size field tells the browser the size to which you expect your database to grow. The browser normally prevents a runaway web application from using excessive local resources by setting limits on the size of each site’s database. When a database change would cause the database to exceed that limit, the user is notified and asked for permission to allow the database to grow further.

If you know that you are going to be filling the database with a lot of content, you should specify an ample size here. By so doing, the user is only asked for permission once when creating the database instead of every few megabytes as the database grows.

The browser may set limits on how large a value you can specify for this field, but the details of these limits are not yet fully defined.

The remainder of this chapter assumes a database that contains a single table with the following schema:

```
CREATE TABLE people(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL DEFAULT "John Doe",
    shirt TEXT NOT NULL DEFAULT "Purple"
);
```

You can create this table and insert a few initial values with the following functions:

__Listing 4-2__  Creating a SQL table

```
function nullDataHandler(transaction, results) { }

function createTables(db)
{
    db.transaction(
        function (transaction) {

            /* The first query causes the transaction to (intentionally) fail if the table exists. */
            transaction.executeSql('CREATE TABLE people(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL DEFAULT "John Doe", shirt TEXT NOT NULL DEFAULT "Purple");', [], nullDataHandler, errorHandler);
            /* These insertions will be skipped if the table already exists. */
            transaction.executeSql('insert into people (name, shirt) VALUES ("Joe", "Green");', [], nullDataHandler, errorHandler);
            transaction.executeSql('insert into people (name, shirt) VALUES ("Mark", "Blue");', [], nullDataHandler, errorHandler);
            transaction.executeSql('insert into people (name, shirt) VALUES ("Phil", "Orange");', [], nullDataHandler, errorHandler);
            transaction.executeSql('insert into people (name, shirt) VALUES ("jdoe", "Purple");', [], nullDataHandler, errorHandler);
        }
    );
}
```

The `errorHandler` function is shown and explained in [Per-Query Error Callbacks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknlto).

Executing a SQL query is fairly straightforward. All queries must be part of a transaction (though the transaction may contain only a single query if desired).

You could then modify the value as follows:

__Listing 4-3__  Changing values in a table

```
var name = 'jdoe';
var shirt = 'fuschia';

db.transaction(
    function (transaction) {
        transaction.executeSql("UPDATE people set shirt=? where name=?;",
            [ shirt, name ]); // array of values for the ? placeholders
    }
);
```

Notice that this transaction provides no data or error handlers. These handlers are entirely optional, and may be omitted if you don’t care about finding out whether an error occurs in a particular statement. (You can still detect a failure of the entire transaction, as described in [Transaction Callbacks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknltm).)

However, if you want to execute a query that returns data (a `SELECT` query, for example), you must use a data callback to process the results. This process is described in [Handling Result Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknlti).

The examples in the previous section did not return any data. Queries that return data are a little bit more complicated.

As noted in previous sections, every query _must_ be part of a transaction. You must provide a callback routine to handle the data returned by that transaction—store it, display it, or send it to remote server, for example.

The following code prints a list of names where the value of the shirt field is “Green”:

__Listing 4-4__  SQL query result and error handlers

```
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

function dataHandler(transaction, results)
{
    // Handle the results
    var string = "Green shirt list contains the following people:\n\n";
    for (var i=0; i<results.rows.length; i++) {
        // Each row is a standard JavaScript array indexed by
        // column names.
        var row = results.rows.item(i);
        string = string + row['name'] + " (ID "+row['id']+")\n";
    }
    alert(string);
}

db.transaction(
    function (transaction) {
        transaction.executeSql("SELECT * from people where shirt='Green';",
            [], // array of values for the ? placeholders
            dataHandler, errorHandler);
    }
);
```

This is, of course, a fairly simple example. Things get slightly more complicated when you are performing dependent queries, such as creating a new row in one table and inserting that row’s ID into a field in another table to create a relationship between those rows. For more complex examples, see the appendix.

To obtain the number of rows modified by a query, check the `rowsAffected` field of the result set object. To obtain the ID of the last row inserted, check the `insertId` field of the result set object, then perform the second query from within the data callback of the first query. For example:

__Listing 4-5__  SQL insert query example

```
db.transaction(
    function (transaction) {
        transaction.executeSql('INSERT into tbl_a (name) VALUES ( ? );',
            [ document.getElementById('nameElt').innerHTML ],
            function (transaction, resultSet) {
                if (!resultSet.rowsAffected) {
                    // Previous insert failed. Bail.
                    alert('No rows affected!');
                    return false;
                }
                alert('insert ID was '+resultSet.insertId);
                transaction.executeSql('INSERT into tbl_b (name_id, color) VALUES (?, ?);',
                    [ resultSet.insertId,
                      document.getElementById('colorElt').innerHTML ],
                    nullDataHandler, errorHandler);
            }, errorHandler);
    }, transactionErrorCallback, proveIt);
}
```

One more issue that you may run into is multiple tables that contain columns with the same name. Because result rows are indexed by column name, you _must_ alias any such columns to unique names if you want to access them. For example, the following query:

```
SELECT * FROM tbl_a,tbl_b ...
```

does not usefully allow access to `tbl_a.id` and `tbl_b.id`, but:

```
SELECT tbl_a.id AS tbl_a_id, tbl_b.id AS tbl_b_id, * FROM tbl_a, tbl_b ...
```

provides unique names for the `id` fields so that you can access them. The following snippet is an example of this query in actual use:

__Listing 4-6__  SQL query with aliased field names

```
function testAliases(){
        var db = getDB();

        if (!db) {
                alert('Could not open database connection.');
        }

db.transaction(
    function (transaction) {
        var query="SELECT tbl_a.id AS tbl_a_id, tbl_b.id AS tbl_b_id, * FROM tbl_a, tbl_b where tbl_b.name_id = tbl_a
.id;";

        transaction.executeSql(query, [],
                function (transaction, resultSet) {
                        var string = "";
                        for (var i=0; i<resultSet.rows.length; i++) {
                                var row = resultSet.rows.item(i);
                                alert('Alias test: Name: '+row['name']+' ('+row['tbl_a_id']+') Color: '+row['color']+' ('+row['tbl_b_id']+')');
                                // string = string + "ID: "+row['id']+" A_ID: "+row['tbl_a_id']+" B_ID: "+row['tbl_b_id']+"\n";
                        }
                        // alert("Alias test:\n"+string);
                }, errorHandler);
    }, transactionErrorCallback);
}
```


You can handle errors at two levels: at the query level and at the transaction level.

The per-query error-handling callback is rather straightforward. If the callback returns `true`, the entire transaction is rolled back. If the callback returns `false`, the transaction continues as if nothing had gone wrong.

Thus, if you are executing a query that is optional—if a failure of that particular query should not cause the transaction to fail—you should pass in a callback that returns `false`. If a failure of the query should cause the entire transaction to fail, you should pass in a callback that returns `true`.

Of course, you can also pass in a callback that decides whether to return `true` or `false` depending on the nature of the error.

If you do not provide an error callback at all, the error is treated as fatal and causes the transaction to roll back.

For a sample snippet, see `errorHandler` in [Listing 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknltcmq).

For a list of possible error codes that can appear in the `error.code` field, see [Error Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknlts).

In addition to handling errors on a per-query basis (as described in [Per-Query Error Callbacks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknlto)), you can also check for success or failure of the entire transaction.

For example:

__Listing 4-7__  Sample transaction error callback

```
function myTransactionErrorCallback(error)
{
    alert('Oops.  Error was '+error.message+' (Code '+error.code+')');
}

function myTransactionSuccessCallback()
{
    alert("J. Doe's shirt is Mauve.");
}

var name = 'jdoe';
var shirt = 'mauve';

db.transaction(
    function (transaction) {
        transaction.executeSql("UPDATE people set shirt=? where name=?;",
            [ shirt, name ]); // array of values for the ? placeholders
    }, myTransactionErrorCallback, myTransactionSuccessCallback
);
```

Upon successful completion of the transaction, the success callback is called. If the transaction fails because any portion thereof fails, the error callback is called instead.

As with the error callback for individual queries, the transaction error callback takes an error object parameter. For a list of possible error codes that can appear in the `error.code` field, see [Error Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknlts).

The error codes currently defined are as follows:

**`0`**
: Other non-database-related error.

**`1`**
: Other database-related error.

**`2`**
: The version of the database is not the version that you requested.

**`3`**
: Data set too large. There are limits in place on the maximum result size that can be returned by a single query. If you see this error, you should either use the `LIMIT` and `OFFSET` constraints in the query to reduce the number of results returned or rewrite the query to return a more specific subset of the results.

**`4`**
: Storage limit exceeded. Either the space available for storage is exhausted or the user declined to allow the database to grow beyond the existing limit.

**`5`**
: Lock contention error. If the first query in a transaction does not modify data, the transaction takes a read-write lock for reading. It then upgrades that lock to a writer lock if a subsequent query attempts to modify data. If another query takes a writer lock ahead of it, any reads prior to that point are untrustworthy, so the entire transaction must be repeated. If you receive this error, you should retry the transaction.

**`6`**
: Constraint failure. This occurs when an `INSERT`, `UPDATE`, or `REPLACE` query results in an empty set because a constraint on a table could not be met. For example, you might receive this error if it would cause two rows to contain the same non-null value in a column marked as the primary key or marked with the `UNIQUE` constraint.

Additional error codes may be added in the future as the need arises.

To make it easier for you to enhance your application without breaking compatibility with earlier versions of your databases, the JavaScript database supports versioning. With this support, you can modify the schema atomically, making changes in the process of doing so.

When you open a database, if the existing version matches the version you specify, the database is opened. Otherwise, the `openDatabase` call throws an exception with a value of `2`. See [Error Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknlts) for more possible exception values.

If you specify an empty string for the version, the database is opened regardless of the database version. You can then query the version by examining the database object’s version property. For example:

__Listing 4-8__  Obtaining the current database version

```
var db = openDatabase(shortName, "", displayName, maxSize);
var version = db.version; // For example, "1.0"
```

Once you know what version you are dealing with, you can atomically update the database to a new version (optionally with a modified schema or modified data) by calling the `changeVersion` method.

For example:

__Listing 4-9__  Changing database versions

```swift
function cv_1_0_2_0(transaction)
{
        transaction.executeSql('alter table people rename to person', [], nullDataHandler, errorHandler);
}

function oops_1_0_2_0(error)
{
    alert('oops in 1.0 -> 2.0 conversion.  Error was '+error.message);
    alert('DB Version: '+db.version);
    return true; // treat all errors as fatal
}

function success_1_0_2_0()
{
    alert("Database changed from version 1.0 to version 2.0.");
}

function testVersionChange()
{
    var db = getDB();

    if (!db) {
        alert('Could not open database connection.');
    }

    if (db.changeVersion) {
        alert('cv possible.');
    } else {
        alert('version changes not possible in this browser version.');
    }
    if (db.version == "1.0") {
        try {
            // comment out for crash recovery.
            db.changeVersion("1.0", "2.0", cv_1_0_2_0, oops_1_0_2_0, success_1_0_2_0);
        } catch(e) {
            alert('changeversion 1.0 -> 2.0 failed');
            alert('DB Version: '+db.version);
        }
    }
}
```

In some versions of Safari, the database version field does not change after a `changeVersion` call until you reload the page. Usually, this is not a problem. However, it is a problem if you call the `changeVersion` method more than once.

Unfortunately, the only way for your code to see the new version number is by closing the browser window. If you get an error code `2` (see [Error Codes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknlts)) and the database version you passed in for the old version matches the version in `db.version`, you should either assume that the version change already happened or display an alert instructing the user to close and reopen the browser window.

For a complete example of basic JavaScript database operations, see [Database Example: A Simple Text Editor](Database%20Example-%20A%20Simple%20Text%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnbnknlti).

[Next](Document%20Revision%20History.md)[Previous](Relational%20Database%20Basics.md)

