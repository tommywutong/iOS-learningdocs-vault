---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/Using_Your__Application.html
archived_at: '2026-07-15T08:12:32.024247Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](The_Structu_Web_Project.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Customizing_ebAssistant.md)

## Using Your Direct to Web Application

Once you have created a Direct to Web application using Project
Builder and the WebObjects application wizard, and have compiled
the resulting project files, you can launch the application by clicking
Project Builder's Launch icon ![[image: ../Art/launchicon.gif]](../Art/launchicon.gif)
. The application pages are
displayed in a web browser, where you can test the application's
presentation of data and, with the WebAssistant enabled, modify
the layout of that data.

### Launching a Direct to Web Application

To launch your application from Project Builder, click
![[image: ../Art/launchicon.gif]](../Art/launchicon.gif)
in the toolbar
in Project Builder's main window.

Before you launch the application you might want to set some
command line options. For example, when running a Direct to Web
Application for deployment, you should turn on caching and disable
the WebAssistant (to prevent anyone from connecting to the application
using WebAssistant). To do this, set the `-WOCachingEnabled` and `-D2WWebAssistantEnabled` options,
respectively:

1. Click the
   Targets tab in Project Builder's main window.
2. Select the D2WTutorial target (the root target) from the Targets
   list.
3. Click the Executables tab in the content panel.
4. Click Add in the lower-right corner of the content panel.
5. Enter `-WOCachingEnabled YES -D2WLiveAssistantEnabled
   NO` in the Launch Arguments area.

![[image: ../Art/launcharguments.gif]](../Art/launcharguments.gif)

For other command-line options for WebObjects applications,
such as
`-WOPort`, see _Serving
WebObjects_.

You can test the Direct to Web application using a web browser
on a machine remote from the machine on which the application is
running (that is, the server). When you launch the application,
look in the console output, which is displayed in the Launch panel,
for the line containing application's URL.

```
Welcome to D2WTutorial!
Opening application's URL in browser: http://localhost:1234/cgi-bin/WebObjects/D2WTutorial
```

Enter the URL in your browser, after substituting the host
name of the server machine for "localhost". In fact, you can
exclude every thing in the URL after the application port number.
For example, if the server host name is "foobar" you would enter
the following URL in the browser to load the WebObjects application:

```
http://foobar:1234/
```


### The Login Page

When you launch your application, your web browser displays
the Direct to Web login screen:

![[image: ../Art/loginbrowser.gif]](../Art/loginbrowser.gif)

The login page is the default implementation of your Main
component, `Main.wo`. It
contains text fields to enter a name and password, as well as a
submit button (Login) and an Enable Assistant checkbox. To go to
the application's default first page, select Enable Assistant and
click Login button. You don't need to enter a name and password,
because the default application provides no password-checking logic.
If you don't select Enable Assistant before clicking Login, you
won't have access to the WebAssistant.

You can modify the login page (`Main.wo`)
to provide any behavior or appearance you like. For example, you
can add your own password-checking logic.

### Dynamically Generated Pages

Besides the login page, there are nine types of dynamically-generated
pages (or reusable components) in a Direct to Web application:

- __A
  query-all__ page that displays all entities that are currently
  exposed and lets users construct queries on the attributes (but
  not the relationships) of those entities; see ["Query Pages"](#apple-ijbusq2gjbcuu). The properties
  of this page cannot be customized.
- __A query page__ that allows the user to
  construct a query for a particular entity; see ["Query Pages"](#apple-ijbusq2gjbcuu).
- __A list page__ that displays one or more
  records of a particular entity in tabular form. List pages and select
  components are implemented with the same components; see ["List Pages and Select Components"](#apple-ijbusskjijcek).
  The result of a query is always a list page.
- __An inspect page__ that displays a single
  record of a given entity. Inspect pages and edit pages are implemented
  with the same components; see ["Inspect and Edit Pages"](#apple-ijbusrcbjjdek).
- __An edit page__ that displays a single
  record of a given entity and also allows you to make changes to
  the record and save it to the database. Edit and inspect pages are implemented
  with the same components; see ["Inspect and Edit Pages"](#apple-ijbusrcbjjdek).
- __A select component__ that lets users
  select a record from a list, thereby adding it to a relationship
  or populating an edit component with it. List pages and select components are
  implemented with the same components; see ["List Pages and Select Components"](#apple-ijbusskjijcek).
- __A confirm page__ that prompts users to
  confirm that they want to delete records. The properties of this
  page cannot be customized.
- __An edit-relationship page__ is a multiple
  component page for removing and adding objects to a relationship.
  See ["Edit-Relationship Pages"](#apple-ijbusrcgizfei).
- __An error page__ for displaying information
  related to exceptions and other errors. The properties of this page
  cannot be customized.

All pages in your application contain the standard Direct
to Web header (defined in `MenuHeader.wo`)
at the top of the page. This header provides a number of controls,
shown in [Figure 2-1](#apple-ijaueskjizauu).

__Figure
2-1 Header controls__

![[image: ../Art/headercontrols.gif]](../Art/headercontrols.gif)

For best results when navigating through a Direct to Web application,
don't use your web browser's backtrack buttons. Instead:

- To return
  to the previous page from an edit or inspect page, click Cancel.
- To return to a query page from a list page, click Return.

#### Query Pages

Direct To Web has two kinds of pages for constructing queries
on the properties of entities: a query-all page and a query page.
When you log into a Direct To Web application, the query-all page
is displayed first by default.

![[image: ../Art/queryallpage.gif]](../Art/queryallpage.gif)

The query-all page enables you to construct a query on an
attribute of a particular entity (queries on relationships are not
allowed). To use this page, select a property from an entity's
pop-up list, specify the comparison operator, type the string to
search on and click the magnifying-glass button.

The query page, on the other hand, is tied to a particular
entity but allows you to construct queries on relationships as well
as attributes. The following example illustrates a query page:

![[image: ../Art/querypage2.gif]](../Art/querypage2.gif)

The first column in the table lists the current entity's
properties. The second column contains pop-up lists and text fields
that let you enter values to construct queries on single and multiple
properties. When you specify values for multiple properties, the
query becomes the logical AND of the queries on the individual properties.

A property is either an _attribute_ (a
value stored directly in this entity's table) or a _relationship_ (an
association between this entity and another entity). For example,
in the figure above, Title is an attribute and Studio is a relationship.
You can use the WebAssistant to hide properties that you don't
want users to see.

`Note:` Direct to
Web only displays properties that are class properties. In addition,
primary keys and attributes marked as the source of a relationship
are hidden by default.

Properties are represented in various ways. For example, in
the figure, you enter a single string value for Title, while you
enter a range of values for Date Released. You can change the representation
of most properties using the WebAssistant. In particular, you may
want to change how relationships are shown, since by default, you
query them by specifying an ID, which is something the user is unlikely
to know. See ["Changing How Properties Are Displayed"](Changing_Ho_e_Displayed.md#apple-ijbussceifduu) for more information
on the different ways of representing properties in your application's
pages.

You can choose a string operator (starts with, contains, ends
with, is, like, =, <>, <, <=, >, >=) and specify
a string with optional special characters in query fields for string
searches. For example, you could select "starts with" in the
Movie entity's Title pop-up list and enter "sh" in the text
field to search for all movies that begin with those characters.
You can also use the "like" operator and enter a string with
the asterisk character to indicate "all occurrences." For instance,
you could enter "\*love\*" to return all movies that contain the substring
"love". Alternatively you could select "contains" in the
pop-up list and enter "love" to return the same movies.

In the Movie query, to get a list of all dramas released in
the 1990's, you would:

1. Select is
   in the Category pop-up list and enter Drama in the Category text
   field.
2. Enter 1980/1/1 and 1989/12/31 in the Date Released fields.
3. Click Query DB.

   The results are displayed in a list page;
   see ["List Pages and Select Components"](#apple-ijbusskjijcek).

To clear the query page, click Build Query.

#### List Pages and Select Components

A list page displays a table showing multiple records of an
entity. List pages are used to display the results of a query, or
to show the records satisfying a to-many relationship in another
list or inspect page.

![[image: ../Art/listpage.gif]](../Art/listpage.gif)

Each row in the table represents a record. By default, a batch
of ten records are shown in a page. To change the batch size, type
a number in the "Display _ Items" field and press Return or
Enter. To display additional records in either direction, click
the triangle buttons or enter the page number you want to go to.

Each column in the list represents one of the entity's properties.
By default, all properties are shown in alphabetical order. You
can hide columns and change their order by using the WebAssistant;
see ["Customizing Your Application With the WebAssistant"](Customizing_ebAssistant.md#apple-ijbusschjjbeu).

The symbols to the right of attribute names represent their
sort order:

- ![[image: ../Art/sortascending.gif]](../Art/sortascending.gif)
  : ascending
  order
- ![[image: ../Art/sortdescending.gif]](../Art/sortdescending.gif)
  :
  descending order
- ![[image: ../Art/sortunsorted.gif]](../Art/sortunsorted.gif)
  :
  unsorted

To change the sort order for any attribute, click the title
to cycle between ascending, descending, and unsorted. By default,
the records are sorted in ascending order by the attribute in the
first column. You can specify up to three columns to sort on; the
last one specified becomes the primary sort key.

For properties that represent relationships, an Inspect button
appears in the cell by default (DisplayToManyFault).

|  |
| --- |
| __Note:__ By default, the list page does not display relationships (including the Inspect buttons). You can configure the list page to display relationships using the WebAssistant; see ["Customizing Your Application With the WebAssistant"](Customizing_ebAssistant.md#apple-ijbusschjjbeu). |

When you click the Inspect button one of two things happen,
depending on the type of relationship:

- If it is
  a to-one relationship, an inspect page appears, showing the destination
  record.

  In the above example, the Movie entity's Studio relationship
  is a to-one relationship to the Studio entity. If you click the
  Inspect button, an inspect page appears for the Studio entity corresponding
  to the selected movie; see ["Inspect and Edit Pages"](#apple-ijbusrcbjjdek).
- If it is a to-many relationship, another list page appears,
  showing all the destination records in the relationship.

  In
  the above example, the Movie entity's Roles relationship is a
  to-many relationship to the MovieRole entity. If you click the Inspect
  button, a list page appears, showing all the roles in the selected
  movie.

  ![[image: ../Art/movierolelist.gif]](../Art/movierolelist.gif)

You can use the WebAssistant to display the related records
directly in the table instead of with an Inspect button; see ["Customizing Your Application With the WebAssistant"](Customizing_ebAssistant.md#apple-ijbusschjjbeu).

The select component looks a lot like the list page, but instead
of the Edit button there is a Select button. The select component
occurs in multiple-component pages. In the edit-relationship page
you click Select to add a record to a to-many relationship or select
a record for a to-one relationship. In the master-detail page you
click Select to select a record to edit. A select component looks
like this:

![[image: ../Art/selectcomponent.gif]](../Art/selectcomponent.gif)

#### Inspect and Edit Pages

Inspect pages and edit pages display the data for a single
record of an entity. An edit page allows you to make changes to
the record and save the changes, while an inspect page is read-only.

An inspect page looks like this

![[image: ../Art/inspectpage_1.gif]](../Art/inspectpage_1.gif)

Note the buttons at the bottom of the page:

- Delete allows
  you to delete the record from the database.
- Cancel takes you back to the page from which you accessed
  this inspect page.
- Edit brings up the equivalent edit page for this record, so
  that you can make changes. (However, if your application specifies
  a particular entity as read-only, you won't be able to edit it.)

Also note the Movies property in the example above. You click
the triangle to display the movies of this studio in a list, browser,
or table, as in the following example:

![[image: ../Art/inspectpage_2.gif]](../Art/inspectpage_2.gif)

This property is configured with the DisplayToManyTable component.
For more on how this is done, see ["Representation of Relationships"](Changing_Ho_e_Displayed.md#apple-ijbussccjjduu).

An edit page (or edit component) looks like this:

![[image: ../Art/editpage.gif]](../Art/editpage.gif)

It is similar to the inspect page, except that it has a Save
button (for saving changes to the database) instead of an Edit button.
If you click the Edit button next to the list of Movies, an edit-relationship
page is displayed for editing the records in the to-many relationship. Edit
components can occur in multiple-component pages, such as the master-detail
page.

#### Edit-Relationship Pages

An edit-relationship page allows users to add records to a
relationship and remove records from the relationship. Users typically
come to these pages when they click an Edit button next to a relationship
in an edit page. Edit-relationship pages consist of three separate components,
of which two are shown at any one time. The first component lists
the relationships of a particular property and contains several
controls. In addition, a query component initially appears for locating
another object to link to for that property. The third component,
a select component, appears after you have specified a query and
is discussed below.

![[image: ../Art/editrelationship.gif]](../Art/editrelationship.gif)

This user interface facilitates the following tasks:

- To remove
  a record from the property, select the key identifying the record
  in the browser and click Remove.
- To add a new record to the property, click New Record. An
  edit component appears underneath the list of relationships; fill
  out the fields of the edit component and click Save to add the new
  record to the database _and_ the new relationship
  to the property above.
- To locate an existing record to add to the relationship, enter
  the properties to search on in the query component and click Query
  DB.

When a query is executed (assuming matching records are found)
a select component replaces the query component.

![[image: ../Art/editrelationshipselect.gif]](../Art/editrelationshipselect.gif)

To add a listed record to the to-many relationship, click
the Select button. To construct a new query, click the Build Query
button.

When you have finished editing a relationship, click the Return
button under the browser to return to the original edit page. You
must click the Save button in this page to store the changed relationship
in the database.

#### Master-Detail Pages

Master-detail pages put a select component and an edit component
on the same page, thereby allowing users to select and edit records
without having to go to another page. The following is an example
of a master-detail page:

![[image: ../Art/masterdetailpage_roles.gif]](../Art/masterdetailpage_roles.gif)

To use a master-detail page, click Select next to a record
in the list component. The record is displayed in an edit component.
See ["Inspect and Edit Pages"](#apple-ijbusrcbjjdek) for usage information.

The master-detail page does not appear under Tasks in the
WebAssistant (expert mode). This is because it is defined as a type
of list page (BASMasterDetailPage, NEUMasterDetailPage, or WOLMasterDetail
page depending on the look) of the list task.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](The_Structu_Web_Project.md)[![Next](attachments/DirectToWeb/Images/next.gif)](Customizing_ebAssistant.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
