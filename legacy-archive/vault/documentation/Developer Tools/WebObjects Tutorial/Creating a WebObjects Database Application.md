---
title: WebObjects Tutorial
apple_id: TP40008108
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/WOTutorial/DatabaseApplication/DatabaseApplication.html
archived_at: '2026-07-15T07:27:07.357713Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Tutorial](Introduction.md)


[Next](Deploying%20a%20WebObjects%20Application.md)[Previous](Installing%20WebObjects%2C%20Eclipse%2C%20and%20the%20WOLips%20Plug-in.md)

# Creating a WebObjects Database Application

This tutorial introduces you to the basic concepts and procedures of developing WebObjects applications by showing you how to create a simple database application. To provide access to a database, WebObjects uses a framework called the Enterprise Objects Framework. The Enterprise Objects Framework is at the heart of every WebObjects database application, managing the interaction between the database and objects in the application. The steps you take in creating this application demonstrate the principles you use in every other application you develop with WebObjects and the Enterprise Objects Framework.

The application you create in this tutorial is called Movies. It uses a sample Apache Derby database, the Movies database, that comes with WebObjects. If you have not installed Eclipse and the WOLips plug-in, follow the steps in [Installing WebObjects, Eclipse, and the WOLips Plug-in](Installing%20WebObjects%2C%20Eclipse%2C%20and%20the%20WOLips%20Plug-in.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcmbyfvbuqmjqgewvgvzr) before you continue with this tutorial.

In this tutorial, you will:

- Use the Entity Modeler included in the WOLips plug-in to maintain a model file
- Create custom enterprise object classes
- Create a Main component that reads from the Movies database
- Create a MovieDetails component that edits and deletes from the Movies database

Along the way, you will learn basic Enterprise Objects Framework concepts you can use to design your own database applications.

The Movies application has two webpages, each of which allows you to access information from the database in two different ways:

- MovieSearch (the main webpage) lets you search for movies that match user-specified criteria. For example, you can search for all comedies starting with the letter “A”. After you find the movie you are looking for, you can access its details to edit or delete it. Figure 2-1 shows the completed MovieSearch webpage.

  __Figure 2-1__  The MovieSearch webpage

  !
- MovieDetails displays the title, category, and release date of a movie. You can edit these properties or delete the movie from the database. Figure 2-2 shows the completed MovieDetails webpage.

  __Figure 2-2__  The MovieDetails webpage

  !

Properly setting up your WebObjects application before beginning development is critical to avoiding complications later on. This section leads you through installing the Movies database, creating a new WebObjects project, and configuring the project’s connection to the database.

This tutorial uses a sample Apache Derby database called Movies. The Apple developer tools include a script for installing the database at `/Developer/Examples/JavaWebObjects/installDatabases.sh`. The script must be run as root and requires your user name as an argument. After you run the script, the Movies database, along with several other sample databases, is installed in `~/Library/Databases/derby-10.3.2.1/data`. For reference, the SQL commands that create and populate the databases can be found in `/Developer/Examples/JavaWebObjects/Databases`.

1. In Eclipse, choose File > New > Project.
2. Choose WebObjects Application from the WOLips folder in the New Project dialog. Click Next.
3. Enter `Movies` as the project name in the New WebObjects Project dialog. Click Finish.

The new project appears in the Package Explorer window. Figure 2-3 shows the structure of the WebObjects application template.

__Figure 2-3__  The WebObjects application template

!

The following files are of particular importance:

- `Application.java` defines application variables that persist as long as the application does.
- `DirectAction.java` defines a subclass of `WODirectAction` that you use as a container class for your action methods. You can rename this class or create multiple subclasses of `WODirectAction` depending on your application needs.
- `Session.java` defines session variables that persist for the lifetime of one user’s session.
- `Main.java` is a file that allows you to specify behavior associated with the Main component. A corresponding file is generated for each subsequent component.
- `Main WO` is the Main component, which comprises three files:

  - `Main.html` is the HTML template for your webpage. It can include tags for dynamic WebObjects elements as well as regular HTML.
  - `Main.wod` is the declarations file that specifies bindings between the dynamic elements and variables or methods in your Java code.
  - `Main.woo` contains information that describes `WODisplayGroup` objects and other information for build tools, such as text encodings.
- `Properties` defines Java system properties for the application.

This template builds and runs without any modifications. Control-click the Movies project folder in Package Explorer and choose Run As > WOApplication. The first time you run the application, Eclipse prompts you for the main class. Select “Application - your.app”. Your default web browser opens and displays a white page with Hello World in the upper-left corner. Click the red Terminate button located above the Eclipse console to terminate the application.

In order for your application to find the Movies database, you must provide it with the path to the Derby home directory. Double-click the Properties file in the Resources folder in Package Explorer to open it and add the following, replacing the indicated portion with your user name:

```
derby.system.home=/Users/<REPLACE WITH YOUR USERNAME>/Library/Databases/derby-10.3.2.1/data
```

Java applications require a driver class to connect to a database. WebObjects provides a Derby JDBC driver in the `derby.jar` library. To reference the library, control-click your project folder in Package Explorer and choose Build Path > Add External Archives. Navigate to `/Library/WebObjects/Extensions` in the file chooser and select `derby.jar`. The library appears in the Package Explorer under Referenced Libraries. You provide the name of the driver when you configure your EOModel.

The Enterprise Objects Framework manages the interaction between the database and objects in a WebObjects application. Its primary responsibility is to fetch data from relational databases and represent them as enterprise objects. An enterprise object, like any other object, couples data with methods for operating on that data. In addition, an enterprise object has properties that map to stored data. An EOModel represents the entity-relationship model that maps tables and rows to enterprise objects. Enterprise object classes typically correspond to database tables. An enterprise object instance corresponds to a single row or record in a database table.

To create the EOModel for the Movies database, do the following:

1. Control-click your project folder in Package Explorer and choose New > Other.
2. Choose EOModel from the WOLips folder in the New dialog. Click Next.
3. Specify `Movies/Resources` as the parent folder for the model. WebObjects expects EOModel files to be in this folder.
4. Specify `Movies` as the name of the model.
5. Select JDBC as the Adaptor Type.
6. Ensure that the Use EOGenerator checkbox is selected. EOGenerator is a tool that generates Java classes from an EOModel.
7. Click Finish.

Eclipse will open the EOModel in a new perspective, called the Entity Modeler perspective. Figure 2-4 shows this perspective.

__Figure 2-4__  The Entity Modeler perspective

!!

The Entity Modeler perspective uses three primary windows:

- The Outline window, located in the upper left, shows the entities, attributes, and database configurations in the EOModel. A new EOModel contains only a single database configuration, named Default.
- The Properties window, located in the lower left, shows the properties for whatever element is selected in the Outline window.
- The Entity Modeler window, located on the right, shows an EOModel’s list of entities or an entity’s list of attributes, depending on what is selected in the Outline window.

Immediately after creating an EOModel, you should provide it with information about the database it communicates with—in this case, the Movies database:

1. Select the Default database configuration in the Outline window. The properties for the configuration will appear in the Properties window.
2. Change the value of the Name field to `Movies`.
3. Ensure that JDBC is specified as the adaptor type.
4. Leave the Username and Password fields blank—the Movies database requires neither.
5. In the URL field, enter `jdbc:derby:movies`.
6. In the Driver field, enter `org.apache.derby.jdbc.AutoloadedDriver`. This is the Derby JDBC driver included in `derby.jar`.

The EOModel is now configured to communicate with the Movies database.

Each entity in an EOModel corresponds to a table in the database. Each attribute in an entity corresponds to a column in the table. You can use entities and attributes to represent whatever portion of your database you want to interact with. For instance, the `MOVIE` table in the Movies database has nine columns, but this tutorial only uses four of them. If a column can have a null value, you do not need to create an attribute for it.

To create and configure the entity for the `MOVIE` table, do the following:

1. Control-click the Movies EOModel in the Outline window and choose New Entity. The entity’s properties appear in the Properties window.
2. Change the value of the Name field to `Movie` in the Properties window.
3. Change the value of the Table Name field to `MOVIE`. This is the name of the table in the database.
4. Change the value of the Class Name field to `your.app.eo.Movie`. This is the name of the Java class that will be generated by EOGenerator.

This tutorial uses four columns in the `MOVIE` table: `MOVIE_ID` (the primary key for the table), `TITLE`, `CATEGORY`, and `DATE_RELEASED`. A separate attribute must be created for each of these columns.

To create and configure the attribute for the `MOVIE_ID` column, do the following:

1. Control-click the Movie entity in the Outline window and choose New Attribute. The attribute’s properties appear in the Properties window.
2. Change the value of the Name field to `movieid`.
3. Ensure that the menu for the second field is set to `Column`. Enter `MOVIE_ID` as the value.
4. Change the value of the External Type field to `INTEGER`. This is the data type stored in the column.
5. Ensure that the Allows Null checkbox is not selected.
6. Select `Integer - Integer i` from the menu for the Data Type field. This is the Java class that corresponds to the data type in the column.

Repeat this process for the remaining three attributes. Table 2-1 indicates the values you should provide for each attribute in the Properties window.

__Table 2-1__  Values for entity attributes

| Name | Column | External Type | Allows Null | Data Type | External Width |
| `title` | `TITLE` | `CHAR` | Not selected | `String - String S` | `100` |
| `category` | `CATEGORY` | `CHAR` | Selected | `String - String S` | `20` |
| `datereleased` | `DATE_RELEASED` | `TIMESTAMP` | Selected | `Timestamp - NSTimestamp T` | N/A |

Figure 2-5 shows the state of the EOModeler window after the remaining steps in this section are performed.

__Figure 2-5__  Attributes in the Movies EOModeler window

!

Most of the columns in the Entity Modeler window correspond to fields in the Properties window and are self-explanatory. The four leftmost columns are more cryptic in appearance; their purposes are the following:

- The key column is used to indicate that an attribute represents a primary key in the table.
- The diamond column is used to indicate that accessors for an attribute should be added to the Java class generated for the attribute’s entity.
- The lock column is used to indicate that an attribute is well suited for detecting failures in optimistic locking. Data types of constant size are best suited for this.
- The zero column is used to indicate that an attribute can be null.

The primary key for the `MOVIE` table is `MOVIE_ID`. Click the key cell in the `movieid` row to indicate this fact. A key symbol appears in the cell. WOLips also automatically removes the diamond symbol from the row, as it is usually the case that the primary key for a table should not be exposed to the front end of an application.

After you have finished configuring your EOModel, WOLips can automatically generate the enterprise object classes.

1. Choose Window > Open Perspective > Other, choose WOLips from the dialog, and click OK to return to the WOLips perspective. Double-click the `Movies.eogen` file in the `Resources` folder in the Package Explorer window. The EOGenerator Editor appears, providing options for customizing the behavior of generating classes. No customization is necessary in this tutorial, so close the file.
2. Control-click `Movies.eogen` in the Package Explorer and choose EOGenerate. `Movie.java` appears in the `Sources` folder in Package Explorer. An additional file, `_Movie.java`, is created in the same folder but does not appear in the Package Explorer.

   `_Movie.java` is a fully functional enterprise object that enables you to create instances representing new or existing rows in the `MOVIE` table. `Movie.java` is a subclass of `_Movie.java` that you can customize and enhance to suit your needs. You should only alter the subclass of an enterprise object class. If you ever need to modify an enterprise object class, you can see it in the Package Explorer by switching to the standard Java perspective.

Every WebObjects application has at least one component—usually named Main—that represents the first webpage the application displays. Each component has four parts: an HTML file that defines the visual layout, a Java file that queries the database and maintains instance variables for dynamic portions of the webpage, a WOD file that binds the elements of the HTML to the logic of the Java, and a WOO file that describes `WODisplayGroup` objects and other information for build tools. The next three sections walk you through creating the HTML, Java, and WOD files for your Main component, which represents the MovieSearch webpage. The WOO file does not need to be modified in this tutorial.

A webpage consists of elements. In addition to the standard static HTML elements found in all webpages, WebObjects allows you to create dynamic elements, whose look and behavior are determined at runtime. In this step, you will create a basic interface for searching for information contained in the Movies database.

Double-click `Components > Main WO` in the Package Explorer to open both the HTML and WOD files for the component. The WOD file, displayed in the lower half of the main window, is blank, and the HTML file, displayed in the upper half of the main window, consists of the following template:

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">
<html>
    <head>
        <title>Untitled</title>
    </head>
    <body>
Hello World
    </body>
</html>
```

Change the text within the `title` element from `Untitled` to something more descriptive, such as `Movie Search`. Replace the “Hello World” text in the `body` element with the following HTML:

```
<h2>Search for Movies</h2>
Specify which movies to display below:<br>
<webobject name="SearchForm">
    Title:<webobject name="TitleField"></webobject><br>
    Category:<webobject name="CategoryField"></webobject><br>
    <webobject name="Submit"></webobject>
</webobject>
<br><br>
<h2>Results</h2>
<webobject name = "Results">
    <webobject name = "ResultTitle"></webobject><br>
</webobject>
```

The six `webobject` elements in this block of HTML compose the search form and the portion of the webpage that will display search results. Every `webobject` element requires a `name` attribute to map it to a definition that you will add to the WOD file.

Choose File > Save to save the Main component. When you save, Eclipse notes six errors in the application, one for each `webobject` HTML element. The Problems window explains that the elements have not been defined in `Main.wod`.

A WOD file is a list of definitions that bind the `webobject` elements of a component’s HTML file to variables and methods in the component’s Java class. To match the `webobject` elements defined in `Main.html`, add the following to `Main.wod`:

```
SearchForm : WOForm {
    enctype = "multipart/form-data";
}

TitleField : WOTextField {
    value = title;
}

CategoryField : WOTextField {
    value = category;
}

Submit : WOSubmitButton {
    action = searchMovies;
    value = "Search";
}

Results : WORepetition {
    list = resultsList;
    item = movie;
}

ResultTitle : WOString {
    value = movie.title;
}
```

Every dynamic element definition follows the same format: the name and type of the element, separated by a colon, followed by a bracketed list of attribute assignments. Each attribute is assigned either a constant value or a value that refers to a variable or method contained in the component’s Java file. For example, in the above code, `Submit` is of type `WOSubmitButton`, its attribute `value` is assigned the constant value `Search`, and its attribute `action` is assigned the value `searchMovies`, which will correspond to a method in `Main.java`.

Save the Main component. Eclipse notes six new errors, this time because `Main.java` does not yet have corresponding variables or methods for `title`, `category`, `searchMovies`, `resultsList`, or `movie`.

A component’s Java file must define any instance variables and methods that are mentioned in the component’s WOD file. In the Movies application, instance variables are defined to keep track of the user’s title and category search terms, and to store the results from a search. Methods are defined to provide access to these variables and to perform the search.

The Main class uses several classes to communicate with the Movie enterprise object. Add the following import statements to `Main.java`:

```
import com.webobjects.appserver.WOComponent;
import com.webobjects.appserver.WOContext;
import com.webobjects.eoaccess.EOUtilities;
import com.webobjects.eocontrol.EOQualifier;
import com.webobjects.eocontrol.EOSortOrdering;
import com.webobjects.foundation.NSArray;
import your.app.eo.Movie;
```

Add the following instance variables to the body of the Main class:

```
private String title;               // Stores the value of the Title search field.
private String category;            // Stores the value of the Category search field.
private Movie movie;                // Stores the current movie when looping through search results.
private NSArray<Movie> resultsList; // Stores the results of a search.
```

Each instance variable in a component’s Java file that contributes to HTML content requires standard setter and getter methods in order for your application to be able to access it. Each setter method should have a name of the form `set<Variablename>`, and each getter method should be the name of the instance variable. All of the instance variables in `Main.java` contribute to HTML content, so create setter and getter methods for all of them. All of the setter and getter methods in `Main.java` should consist of simple assignment statements and return statements, respectively.

Finally, `Main.java` needs to define the `searchMovies` method that is called when the Search button is clicked. Add the following method to the Main class:

```
public WOComponent searchMovies() {
    if (title == null && category == null) {
        return context().page();
    }
    if (title == null) {
        title = "";
    }
    if (category == null) {
        category = "";
    }
    NSArray<EOSortOrdering> sortOrdering = new NSArray<EOSortOrdering>(new EOSortOrdering("title", EOSortOrdering.CompareAscending));

    String[] argArray = new String[2];
    argArray[0] = title + "*";
    argArray[1] = category + "*";

    NSArray<String> args = new NSArray<String>(argArray);
    EOQualifier qualifier = EOQualifier.qualifierWithQualifierFormat("title LIKE %@ AND category LIKE %@", args);
    resultsList = Movie.fetchMovies(session().defaultEditingContext(), qualifier, sortOrdering);
    return context().page();
}
```

The first `if` statement in the method ensures that a value has been supplied for at least one search field, and reloads the current webpage without querying the database if this is not the case. The two subsequent `if` statements provide the empty string for any field the user chooses to omit. The remaining lines perform the following actions:

1. A sort ordering is created to indicate that results retrieved from the database should be sorted in ascending order by title.
2. An array of arguments for a formatting string is created. An asterisk is added to the end of both the `title` and `category` strings to indicate a wildcard suffix in a SQL LIKE clause.
3. A qualifier is created to specify the movies to be returned from the database query. The string passed into `EOQualifier.qualifierWithQualifierFormat` is the equivalent of a WHERE clause in a SQL statement that begins with `SELECT * FROM MOVIE`. The `%@` substring indicates a placeholder to be filled by an object in `args`.
4. The static method `Movie.fetchMovies` populates `resultsList` with the movies that meet the requirements set by `qualifier`, in the order specified by `sortOrdering`.
5. The response webpage is returned, in this case the same webpage. The Results section of the page is now populated with the titles of movies in `resultsList`.

Save your project and run it. Performing a search with `The` in the Title field and `Comedy` in the Category field produces the webpage shown in Figure 2-6.

__Figure 2-6__  The main webpage with search results

!

The MovieDetails webpage shows you the detailed information about a movie you select in the Main webpage. For this to work, the Main webpage has to tell the MovieDetails webpage which movie the user selected. The MovieDetails page keeps track of the selected movie in its own instance variable. In this section, you will perform the following tasks:

- Create a new component.
- Assign a movie selected on the Main webpage to a variable in the MovieDetails webpage.
- Create an interface for editing or deleting a movie’s information.
- Create a way to navigate from Main to MovieDetails and back.

Following this section, you will possess all of the fundamental skills necessary to create a dynamic multipage WebObjects database application.

To create a the MovieDetails component, control-click the Components folder in the Package Explorer and choose New > WOComponent. In the New WebObjects Component dialog, change the name of the component to `MovieDetails` and click Finish. The new component appears in the Components folder below `Main WO`.

The MovieDetails webpage is very similar to the Main webpage in structure and appearance, consisting of an input form with two submit buttons: a Save button and a Delete Movie button. Consequently, the HTML and WOD files for the MovieDetails webpage are nearly identical to their Main webpage counterparts.

Add the following HTML to `MovieDetails.html`:

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">
<html>
    <head>
        <title>Movie Details</title>
    </head>
    <body>
        <h2>Movie Details</h2>
        <webobject name="Message"></webobject><br>
        <webobject name="EditForm">
            Title:<webobject name="TitleField"></webobject><br>
            Category:<webobject name="CategoryField"></webobject><br>
            Date Released:<webobject name="DateField"></webobject><br>
            <webobject name="Save"></webobject><webobject name="Delete"></webobject>
        </webobject>
        <webobject name="LinkToMain">Back to Movie Search</webobject>
    </body>
</html>
```

Add the following dynamic element definitions to `MovieDetails.wod`:

```
Message : WOString {
    value = message;
}

EditForm : WOForm {
    enctype = "multipart/form-data";
    multipleSubmit = true;
}

TitleField : WOTextField {
    value = title;
}

CategoryField : WOTextField {
    value = category;
}

DateField : WOTextField {
    value = datereleased;
}

Save : WOSubmitButton {
    action = saveMovie;
    value = "Save";
}

Delete : WOSubmitButton {
    action = deleteMovie;
    value = "Delete Movie";
}

LinkToMain : WOHyperlink {
    pageName = "Main";
}
```

Setting the `multipleSubmit` attribute of a `WOForm` element to `true` allows more than one submit button to be associated with that form. In this case, the Save and Delete Movie buttons are associated with the same form.

Whereas the Java logic in the Main component deals with reading from the Movies database, the MovieDetails component deals with modifying the database. Users can change the title, category, and release date of a movie, or delete the movie from the database entirely.

Open `MovieDetails.java`. If Eclipse displays an error in the file, make sure that the `MovieDetails` class extends from the correct class, namely `WOComponent`.

Add the following import statements to `MovieDetails.java`:

```
import com.webobjects.foundation.NSTimestamp;
import java.text.SimpleDateFormat;
import java.text.ParseException;
import java.util.Date;
import your.app.eo.Movie;
```

The `MovieDetails` class requires the following instance variables:

```
private Movie movie;                   // The movie for which the details are displayed.
private SimpleDateFormat formatter;    // A utility class for converting between date formats.
private String category;               // The value of the Category text field.
private String datereleased;           // The value of the Date Released text field.
private String message;                // The value of a message that indicates operation success or errors.
private String title;                  // The value of the Title text field.
```

Create setter and getter accessor methods for each variable as you did in `Main.java`. The `formatter` instance variable does not directly contribute to HTML content, so it does not require setter or getter methods. The `MovieDetails` class populates the `category`, `datereleased`, and `title` instance variables with values taken from `movie`. As a result, `setMovie` requires slightly more logic than a simple assignment statement.

```
public void setMovie (Movie m) {
    movie = m;
    setTitle(movie.title().trim());
    setCategory(movie.category().trim());
    setDatereleased(formatter.format(movie.datereleased()));
}
```

Two instance variables, `formatter` and `message`, need to be instantiated in the constructor of `MovieDetails`. Add the following two lines to the constructor:

```
formatter = new SimpleDateFormat("M/d/y");
message = "";
```

The `MovieDetails` class requires two additional methods, one for each submit button. The first, `saveMovie`, alters the current movie’s row in the database to reflect changes made by the user:

```
public WOComponent saveMovie() {
    if (movie.title() == null) {
        setMessage("Error: Title is required.");
        return context().page();
    }

    Date newDate = null;
    try {
        newDate = formatter.parse(datereleased);
    } catch (ParseException e) {
        setMessage("Error: Date must be in mm/dd/yy format.");
        return context().page();
    }

    movie.setTitle(title);
    movie.setCategory(category);
    movie.setDatereleased(new NSTimestamp(newDate));
    session().defaultEditingContext().saveChanges();
    setMessage("Movie Saved.");
    return context().page();
}
```

Calling `saveChanges` on the default editing context will save any modifications of enterprise objects to the database. This includes alterations to a row, inserting a row, and deleting a row.

The second method, `deleteMovie`, deletes the movie from the database:

```
public WOComponent deleteMovie() {
    session().defaultEditingContext().deleteObject(movie);
    session().defaultEditingContext().saveChanges();
    return pageWithName("Main");
}
```

Because deleting a movie should prevent the user from subsequently editing it, `deleteMovie` returns the user to the Main webpage instead of reloading the MovieDetails webpage.

So far, there is no way to reach the MovieDetails webpage from the Main webpage, because the search results produced by the Main webpage are in plaintext. Each result should instead be a hyperlink to a corresponding MovieDetails webpage. This requires small changes to the HTML and WOD files of the Main component.

In `Main.html`, change the line that reads:

```
<webobject name = "ResultTitle"></webobject><br>
```

To the following:

```
<webobject name = "MovieLink"><webobject name = "ResultTitle"></webobject></webobject><br>
```

Add the following dynamic element definition to `Main.wod`:

```
MovieLink : WOHyperlink {
    action = showDetails;
}
```

Finally, add the `showDetails` method to `Main.java`:

```
public WOComponent showDetails() {
    MovieDetails detailsPage = (MovieDetails)pageWithName("MovieDetails");
    detailsPage.setMovie(movie);
    return detailsPage;
}
```


Database applications that support deleting from a database most likely support inserting into the database as well. The steps for creating this functionality are essentially identical to the steps you took to create the search functionality.

1. Add necessary `webobject` elements to `Main.html` to create a form that allows the user to specify a title, category, and release date.
2. Add corresponding element definitions to `Main.wod`.
3. Add necessary instance variables to `Main.java`, along with a method for adding a new movie. The main logic of the method looks like the following:

```
public WOComponent insertMovie() {
    Movie newMovie = Movie.createMovie(session().defaultEditingContext(), newtitle);
    newMovie.setCategory(newcategory);
    newMovie.setDatereleased(formatter.format(newdatereleased));
    session().defaultEditingContext().saveChanges();
    return context().page();
}
```

   For improved user experience, add error checking and message updates to the method.

[Next](Deploying%20a%20WebObjects%20Application.md)[Previous](Installing%20WebObjects%2C%20Eclipse%2C%20and%20the%20WOLips%20Plug-in.md)

