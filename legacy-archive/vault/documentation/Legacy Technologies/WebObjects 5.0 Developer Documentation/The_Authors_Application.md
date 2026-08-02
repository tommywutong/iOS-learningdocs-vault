---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOMBasics/The_Authors_Application.html
archived_at: '2026-07-15T08:13:09.763229Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Working_Wit_ng_Contexts.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Further_Exploration.md)

## The Authors Application

In this section you'll create an application to edit the
AUTHOR table of the Books database. The table stores the first and
last names of book authors. Your application provides facilities
for adding, editing, and deleting authors.

The AUTHORS table contains three columns: FIRST_NAME, LAST_NAME,
and, AUTHOR_ID. The AUTHOR_ID column serves as the table's primary
key, and it's not shown in the application's user interface.
You don't even need to worry about updating the value of that
column; Enterprise Objects does it for you.

### Creating the Authors Database

The first step is to create the Authors database. You'll
user OpenBase Manager to create it.

1. Launch OpenBase
   Manager.

   The OpenBase Manager application is located in the `/Applications/OpenBase` directory.

   ![[image: ../Art/openbasemain.gif]](../Art/openbasemain.gif)
2. Create a new database.
   1. Choose Database >
      New.
   2. Enter `Authors` in
      the Database Name text field.
   3. Select the Start Database at Boot option.
   4. Choose ASCII from the Internal Encoding pop-up menu.
      ![[image: ../Art/openbaseadddatabase.gif]](../Art/openbaseadddatabase.gif)
   5. Click Set.
3. Start the database.
   1. Select the localhost/Authors
      database in the list.
   2. Click Start.
4. Quit OpenBase Manager.

You now have an empty database called Authors.

### Creating the Authors Model

EOModeler is the tool you use to model your data. In it you
define the entities that serve as the interface between your code
and the database. In this section, you'll use EOModeler to add
a table to the Authors database.

1. Launch EOModeler.

   The
   EOModeler application is located in the `/Developer/Applications` directory.
2. Choose Model > New.
3. Select the adaptor to use.

   With the JDBC adaptor provided
   with your WebObjects installation, you can communicate with any
   database that includes a JDBC driver.

    ![[image: ../Art/eomadaptor.gif]](../Art/eomadaptor.gif)

   Select JDBC from the list and
   click Next.
4. Provide JDBC connection information.

   Your model includes
   the information necessary to connect to your database. The JDBC Connection
   dialog is where you enter that information. For this exercise, you
   only need to specify the URL used to connect to the database.

   ![[image: ../Art/eomauthorsjdbcconn.gif]](../Art/eomauthorsjdbcconn.gif)

   Enter `jdbc:openbase://localhost/Authors` in
   the URL text field and click OK.
5. Select what to include in your model.

   This pane is where
   you tell EOModeler how to configure the model entities from an existing
   database. Because you are creating a new database, none of these
   options needs to be selected.

    ![[image: ../Art/eomwzrdwhat.gif]](../Art/eomwzrdwhat.gif)

   Deselect all the options and
   click Finish.

 ![[image: ../Art/eomemptymodel.gif]](../Art/eomemptymodel.gif)

#### Adding the Author Entity to the Model

In this section you'll add an entity called Author to the
new model. This entity maps to the AUTHOR table that EOModeler generates
from the entity's properties.

1. Add the entity.

   Choose
   Property > Add Entity.
2. Configure the entity.

   Choose Tools > Inspector.

   The
   Entity Inspector appears. It allows you to enter a variety of information
   pertaining to the new entity.

   1. Name the entity Author.
   2. Enter `AUTHOR` in
      the Table Name text field.
   3. Enter `Author` in
      the Class text field.
       ![[image: ../Art/eomauthor.gif]](../Art/eomauthor.gif)
3. Add and configure Author's attributes.

   The Author entity
   has two significant attributes: `firstName` and `lastName`.
   An additional attribute, `authorId`,
   serves as the entity's primary key.

   1. Make sure the Author
      entity is selected in the entity list.
   2. Choose Property > Add Attribute.
   3. Name the attribute `firstName`.
   4. Enter `FIRST_NAME` as
      the column name.
   5. Enter `char` in the
      External Type text field.
   6. Choose String as the internal data type.
   7. Enter `30` in the
      External Width text field.
       ![[image: ../Art/eomauthorfirstname.gif]](../Art/eomauthorfirstname.gif)
   8. Click ![[image: ../Art/eomadvancedattributeicon.gif]](../Art/eomadvancedattributeicon.gif)
      to display the Advanced Attribute
      Inspector.
   9. Select the Allow Null Value option.
       ![[image: ../Art/eomauthorfirstname2.gif]](../Art/eomauthorfirstname2.gif)
   10. Repeat steps a through i to add the `lastName` attribute.

   Now,
   you'll add the attribute that serves as the primary key.

   1. Add a new attribute
      and name it `authorId`.
   2. Enter `AUTHOR_ID` as
      the column name.
   3. Enter `int` in the
      External Type text field.
   4. Choose Integer as the internal data type.
   ![[image: ../Art/eomauthorauthorid.gif]](../Art/eomauthorauthorid.gif)
4. Select a primary key for the Author entity.
   1. In the `authorId` row
      of the Author Attributes list, click in the column with a key as its
      heading so that a key appears in the row.
   2. Click in the diamond column of the `authorId` row
      so that the diamond disappears.

      The `authorId` attribute
      is nothing more than a database artifact, required to make sure
      that rows in the AUTHOR table are unique; it has no meaning to you
      or the application's users. The diamond icon indicates that an
      attribute is a property that is made available to an application's
      custom logic and, if necessary, the application's user. Because `authorId` provides
      no additional information about an author, it is not required for
      the application's normal operation.

__Figure
10-1 Authors model with Authors entity__

![[image: ../Art/eomauthorcomplt.gif]](../Art/eomauthorcomplt.gif)

Save the model and name it Authors.

#### The EOModeler Window

The left pane of EOModeler's main window lists the entities
present in the model. If you click an entity, details about its
attributes are displayed in the right pane.

In [Figure 10-1](#apple-ijauur2fijduq), you see the Author entity and the definitions of
each of its attributes. The values of the columns indicate the properties
of each attribute.

By default, the most commonly used columns are enabled in
this view. To enable other columns, use the Add Column menu in the
bottom frame of the window. These are the available columns and
their meanings:

**Primary
Key**
: The primary key icon in the first column indicates that
the attribute is used to uniquely identify a row. In the Author
entity, only `authorId` is
a primary key.

**Class Property**
: The presence of a diamond in the second column indicates
that the attribute is a class property. A class property is one
for which EOModeler generates Java access methods. Generally, any
attributes that are actually a property of the entity are made class
properties, and attributes that are used for database level functionality
(such as the `authorId` attribute)
are not.

**Locking**
: Indicates whether an attribute should be used for locking
when an update is performed. That is, whether Enterprise Objects
uses this attribute to determine whether changes have been made.

**Allows Null**
: Indicates whether the database column can have a `null` value.

**Name**
: The name of the attribute, which determines the Java
method names that EOModeler generates when it creates the class
definition.

**Value Class (Java)**
: The class used to represent this attribute.

**External Type**
: The data type used by the database to represent this
attribute.

**Width**
: The maximum width of an attribute, usually used for
String attributes.

**Column**
: The name of the database column that corresponds to
this attribute.

**Definition**
: The definition for a derived column. A derived attribute
doesn't actually exist in the database and hence an attribute
can't have both a Definition and a Column. Setting one clears
the other.

**Precision**
: The number of significant digits to include. Used for
some numerical types.

**Prototype**
: The prototype from which this attribute inherits its
characteristics. You can use prototypes to set up default attribute
types.

**Read Only**
: Controls whether the attribute can be modified or only
read.

**Scale**
: The number of characters to the right of the decimal
point in a number attribute.

**Value Type**
: This type is used in decoding values for enterprise
objects represented by Objective-C classes rather than Java classes
and is not used in this text.

**Write Format**
: Used in tandem with Read Format to write data to the
database in a custom format.

The External Type attribute must be one of the types defined
by the JDBC adaptor. These are the most common ones:

**`blob`**
: A Binary Large Object. Used to store images and large
data files. Usually represented as an NSData object.

**`char`**
: Used to store character information and represented
with a Java String. An attribute declared to be a char must have
its width set, as well.

**`date`, `datetime`**
: Used to store date information and usually represented
by an NSTimestamp object.

**`double`**
: Used to store floating-point numbers and generically
represented by a Java Number.

**`int`**
: Used to store integer numbers and usually represented
by a Java Number. Foreign and primary keys are usually best modeled
as integers.

**`long`**
: Used to store very large integers.

#### Creating the AUTHOR Table

Now that you have created the Author entity, it is time to
create the AUTHOR table behind it.

1. Select the
   Author entity from the entity list.
2. Choose Property > Generate SQL.
3. Make sure that only the Create Tables option is selected.
   ![[image: ../Art/eomauthortblcreate.gif]](../Art/eomauthortblcreate.gif)
4. Click Execute SQL.
5. Quit EOModeler.

### Creating the Application

In this section you'll create the Authors application. The
application allows its users to add, edit, and remove authors from
the Authors database.

This section introduces the use of enterprise object classes
(custom Java classes derived from entities defined in a model to
access database information) and the methods used to add objects
into the data store (adding rows to the AUTHOR table in the Authors database).
You'll use EOModeler to create the `Author.java` class.
After adding it to your project, you'll be able to create Author
objects in your code. You'll then add those objects to the data
store.

Follow these steps to create the Authors application:

1. Create a
   new WebObjects application project and name it Authors.
2. Add the Authors model to the project.
   1. Select Resources from
      the Groups & Files list.
   2. Choose Project > Add Files.
   3. Choose the `Authors.eomodeld` file
      you created in ["Creating the Authors Model"](#apple-ijauurkgizcuq) and click Open.
   4. Select the "Copy items into destination group's folder
      (if needed)" option.
   5. Select the Application Server target and click Add.
      ![[image: ../Art/authorsaddmodel.gif]](../Art/authorsaddmodel.gif)

### Customizing the Main component

The entire application's functionality is provided by the
Main component. It includes an `authorList` array
where the authors are maintained while the application runs. When
the users clicks Save, the changes made to `authorList` are
saved to the database. `Main.wo` includes
elements to edit an author's information and actions to add, edit,
update, and delete authors. A WORepetition shows all the contents
of `authorList`.

#### Customizing Main.wo

After following these steps, `Main.wo` should
look like [Figure 10-2](#apple-ijauurkcincui).

1. Open `Main.wo` in
   WebObjects Builder.
2. Add three keys.
   1. Name the first key `author`,
      set its type as EOGenericRecord, and do not include accessor methods.
   2. Name the second key `authorItem`,
      set its type as EOGenericRecord, and do not include accessor methods.
   3. Name the third key `authorList`,
      choose "Mutable array of" and EOGenericRecord for its type,
      and do not include accessor methods.
3. Add six actions, all of them returning `null`,
   which tells WebObjects to return the current page, Main, instead
   of a new one (the same instance of Main persists throughout the application's
   operation):
   - `addAuthor`
   - `deleteAuthor`
   - `editAuthor`
   - `revertChanges`
   - `saveChanges`
   - `updateAuthor`
4. Add a WOForm element to edit author information.
   1. Choose Forms >
      WOForm.
   2. In the WOForm Binding Inspector, choose `true` for
      the `multipleSubmit` attribute.
   3. Inside the WOForm, enter the text "`Last
      Name:` ", follow it with a WOTextField, and press
      Shift-Enter.
   4. Bind the Last Name WOTextField's `value` attribute
      to `author.lastName`.

|  |
| --- |
| __Note:__ Since `author`, `authorItem`, and `authorList` are EOGenericRecords, WebObjects Builder does not know what their properties are. You must type the keypaths for them manually. |
   5. Enter the text "`First Name:` ",
      follow it with a WOTextField, and press Shift-Enter.
   6. Bind the First Name WOTextField's `value` attribute
      to `author.firstName`.
   7. Add two WOSubmitButtons to the WOForm.

      Enter `"Update"` for
      the first WOSubmitButton's `value` attribute
      (include the quotation marks), and bind its `action` attribute
      to the `updateAuthor` action.

      Enter `"Add"` for
      the second WOSubmitButton's `value` attribute,
      and bind its `action` attribute
      to the `addAuthor` action.
5. Add a second WOForm below the first one for the Save and Revert
   WOSubmitButtons.
   1. Set the WOForm's `multipleSubmit` attribute
      to `true`.
   2. Add a WOSubmitButton inside the WOForm, enter `"Revert"` for
      its value attribute, and bind its action attribute to `revertChanges`.
   3. Add another WOSubmitButton to the right of the Revert WOSubmitButton,
      enter `"Save"` for
      its `value` attribute,
      and bind its `action` attribute
      to `saveChanges`.
6. Add a WORepetition to display the list of authors.
   1. Add the WORepetition
      below the second WOForm.
   2. Add two WOHyperlinks, separated by a space character, inside
      the WORepetition.

      Enter `Edit` as
      the first WOHyperlink's caption and bind its `action` attribute
      to `editAuthor`.

      Enter `Delete` as
      the second WOHyperlink's caption and bind its `action` attribute
      to `deleteAuthor`.
   3. Add two WOStrings, separated by ", " to the right of the
      Delete WOHyperlink.

      Bind the first WOString to `authorItem.lastName` and
      the second to `authorItem.firstName`.

      Put
      the cursor on the right of the second WOString and press Shift-Enter.
   4. Bind WORepetition's `list` attribute
      to `authorList`, and its `item` attribute
      to `authorItem`.
7. Save `Main.wo`.

__Figure
10-2 Main.wo with elements to maintain
author information__

![[image: ../Art/authorsmainwo.gif]](../Art/authorsmainwo.gif)

#### Customizing Main.java

Now you'll edit `Main.java` to
add the application's custom logic.

1. Add the following
   instance variables:

   ```
   private EOEditingContext editingContext;
   private EOClassDescription authorClassDescription;
   private EOFetchSpecification fetchSpec;
   ```

   Several
   methods in the Main class require the use of the editing context,
   class description, and fetch specification. Having the class's
   constructor store these objects in instance variables reduces the
   lines of code required to implement those methods.
2. Edit the constructor to perform custom initialization.

   When
   the Main component is created, it needs to request and store the
   editing context and retrieve the authors stored in the database
   (the first time you run the application, there's nothing to retrieve).

   Edit
   the constructor so that it looks like [Listing 10-1](#apple-ijauurkbivfem).

   __Listing
   10-1 The constructor in Main.java__

   ```
   public Main(WOContext context) {
       super(context);

       // build fetch specification
       fetchSpec = new EOFetchSpecification("Author", null, null);

       // get editing context
       editingContext = session().defaultEditingContext();

       // fetch
       authorList = new  NSMutableArray(editingContext.objectsWithFetchSpecification(fetchSpec));

       // get Author class description
       authorClassDescription =  EOClassDescription.classDescriptionForEntityName("Author");

       // create a new Author object (where form data is stored)
       author = new EOGenericRecord(authorClassDescription);
   }
   ```

   There
   are three parts to retrieving data from a database with WebObjects:
   the fetch specification, the editing context, and the fetch.

   - __EOFetchSpecification__ An
     EOFetchSpecification is an object representation of a request for
     objects from the object store (database). It describes the objects
     that you want to retrieve. You can create fetch specifications programmatically
     or define them in the EOModel file.

     A fetch specification is
     defined in three parts—the entity to fetch, restrictions used to
     filter the fetched objects, and the order of the result. The last
     two are optional, but the first one must be provided when the fetch
     specification is created.
   - __Editing Context__ Fetches are performed
     through an editing context, which is responsible for maintaining
     the object graph for the fetched objects.
   - __Fetch__ After a fetch specification has
     been defined, it can be used to fetch data from the object store.
     WebObjects translates the fetch specification into SQL statements that
     your database system can understand. The database returns a list
     of rows that WebObjects translates into enterprise objects (instances
     of EOGenericRecord) before returning them in an NSArray.
3. Edit the `addAuthor` method
   to that it looks like [Listing 10-2](#apple-ijauursfizdum).

   __Listing
   10-2 The addAuthor method in Main.java__

   ```
   public WOComponent addAuthor() {
       // add only if the author is not already in the list
       if (! authorList.containsObject(author)) {
           // add author to list
           authorList.addObject(author);

           // insert author into editing context
           editingContext.insertObject(author);

           // create a new author
           author = new EOGenericRecord(authorClassDescription);
       }

       return null;
   }
   ```

   Because
   of Enterprise Objects's Java integration, inserting a new row
   in your database is almost as simple as adding an item to an array.
   Once your class is defined as a subclass of EOGenericRecord, all
   you need to do is insert the object into an editing context; it
   is then maintained in the object graph like other objects fetched
   from the database. When the `saveChanges` method
   is called, a new row is created in the database for each object
   added to the editing context.

   The `addAuthor` method
   is invoked when the user clicks Add. If the user isn't editing
   an existing author, it inserts the Author object that the user edited
   (through the first form's text fields) into `authorList`,
   and inserts it in the object graph maintained by the editing context
   as well. It then creates a new Author object, where another author's
   data can be stored. (Note that the new instance is added to the
   object graph only if the user clicks Add again.)
4. Edit the `deleteAuthor` method
   so that it looks like [Listing 10-3](#apple-ijauusciivauu).

   __Listing
   10-3 The deleteAuthor method in Main.java__

   ```
   public WOComponent deleteAuthor() {
       // remove author from authorList
       authorList.removeObject(authorItem);

       // get object's editing context
       EOEditingContext ec = authorItem.editingContext();

       // remove author from object graph
       ec.deleteObject(authorItem);

       return null;
   }
   ```

   In
   multiuser applications an object can be in a different editing context
   than the default one. When you need to delete an enterprise object
   from a data store, you should ask the object itself for its editing
   context. Then you invoke that editing context's `deleteObject` method.
5. Edit the `editAuthor` method
   so that it looks like [Listing 10-4](#apple-ijauuqsbijdeg).

   __Listing
   10-4 The editAuthor method in Main.java__

   ```
   public WOComponent editAuthor() {
       // set the author to edit to the one the user selected
       author = authorItem;

       return null;
   }
   ```

   When
   the user clicks Edit, `authorItem` contains
   the author object to be edited. The next time the page is drawn,
   the text fields are populated with the information for the selected
   author.
6. Edit the `updateAuthor` method
   so that it looks like [Listing 10-5](#apple-ijauurkbizces).

   __Listing
   10-5 The updateAuthor method in Main.java__

   ```
   public WOComponent updateAuthor() {
       // create a new author
       author = new EOGenericRecord(authorClassDescription);

       return null;
   }
   ```

   When
   the user clicks Update, the Author object she edited gets updated
   with the values entered in the form's text fields (the object
   is already in the list). Therefore, the only thing this method needs
   to do is create a new Author object. The next time the page is drawn,
   the text fields are populated with nothing (because they get their
   data from the new, empty Author object), enabling the user to enter
   the information for a new author.
7. Edit the `saveChanges` method
   so that it looks like [Listing 10-6](#apple-ijauursbifaug).

   __Listing
   10-6 The saveChanges method in Main.java__

   ```
   public WOComponent saveChanges() {
       // save changes made in editing context to object store
       editingContext.saveChanges();

       return null;
   }
   ```
8. Edit the `revertChanges` method
   so that it looks like [Listing 10-7](#apple-ijauuqsgizbuu).

   __Listing
   10-7 The revertChanges method in Main.java__

   ```
   public WOComponent revertChanges() {
       // revert changes made in editing context
       editingContext.revert();

       // re-fetch
       authorList = new  NSMutableArray(editingContext.objectsWithFetchSpecification(fetchSpec));

       return null;
   }
   ```

   When
   the user clicks Revert, the `revertChanges` method
   tells the editing context to discard any changes made since the
   enterprise objects in it were last fetched or saved. However, the `authorList` array
   isn't tied to the editing context in any way. Therefore, you must
   retrieve a new list of authors from the object store and assign
   it to `authorList`, so
   that the user sees up-to-date information. (The previous list is
   garbage-collected by the Java runtime after it is no longer referenced
   by variables in your application.)
9. Save `Main.java`.

### Running the Authors Application

[Figure 10-3](#apple-ijauuscfireuo) shows the Authors application after the names of
some authors have been entered.

__Figure
10-3 The Authors application__

![[image: ../Art/authorsie.gif]](../Art/authorsie.gif)

There is only one instance of Main throughout the application's
execution (all the actions return `null`).
When Main is created, it reads the authors from the database and
stores them in the `authorList` instance
variable. As the user makes changes, `authorList` (and
its editing context) is updated. The WORepetition element displays
the contents of `authorList` and links
so that the user can edit or delete a particular author. Changes
are saved when the user clicks Save.

Notice that all the complexities normally required when dealing
with databases have been replaced with the straightforward use of
enterprise objects.

### Browsing the Database

It is frequently convenient to browse the raw data in a database,
including attributes that may not be displayed by your WebObjects
components. EOModeler has the ability to browse tables and perform
basic filtering, which is useful during application development. This
simple facility lets you get a "behind the scenes" look at your
data.

1. Open the
   Authors model in EOModeler
2. Select the Author entity.
3. Choose Tools > Data Browser.

   __Figure 10-4 EOModeler's
   Data Browser__

   ![[image: ../Art/databrowser.gif]](../Art/databrowser.gif)

   Current
   database data is displayed. The Refetch button allows you to refresh
   this data on demand.

   EOModeler also lets you perform
   simple filters to limit the number of rows displayed as [Figure 10-5](#apple-ijauur2hircuo) shows.

   __Figure
   10-5 Data Browser using filter__

   ![[image: ../Art/databrowser2.gif]](../Art/databrowser2.gif)

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](Working_Wit_ng_Contexts.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](Further_Exploration.md)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
