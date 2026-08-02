---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToJavaClient/Tutorial/Examining_the_Application.html
archived_at: '2026-07-15T08:12:21.047808Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Building_an_Application.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](The_Assistant.md)

## Examining the Application

This section illustrates the application's functionality
by guiding you through the steps to search for records, modify records,
and add new ones.

When the application starts, it opens a window with which
you can search for database records. Each of the tabs in the Query
Window corresponds to an entity in one of the application's models.
Not all of the entities in the Movie and Rentals models have tabs
in the Query Window. The way Direct to Java Client chooses which
entities to represent in the Query Window is described in the section ["Main, Enumeration, and "Other" Entities"](#apple-ijbegrchjjcuc).

1. Focus the
   Query Window on the Movie entity.

   In the Query Window, click
   the Movie tab. The Query Window switches its contents to a user
   interface for searching for Movies.

   Note that the default
   Direct to Java Client application allows you to search on `title` and `plotSummary`.
   You can easily configure the application to search on different
   attributes using the Direct to Java Client Assistant (Assistant
   for short). In later sections, you are shown how to change the search
   attributes.
2. Search for Movies whose titles begin with the letter "A".

   Type `A` in
   the Title text box, and click Find. The application lists the Movies
   meeting the search criteria.

   Note that the application
   lists `title`, `category`, `dateReleased`, `posterName`, `revenue`, `trailerName`,
   and `plotSummary` for the
   Movies in the result set. As with the search attributes, you can
   easily configure the application to display different attributes
   in the table, which you do later.
3. Search for Movies whose titles begin with the letter "A"
   or "B".

   Click Clear. Although the "A" is cleared from
   the Name field, the Movies in the results table remain. To add Movies
   that start with the letter "B" to the results, type `B` in
   the Name text box, and click Append. Now the results table contains
   Movies that start with the letter "A" and the letter "B".

   The
   difference between Find and Append is this: Find replaces the records
   in the results list with the results of the most recent search.
   Append adds data from the most recent search to the records already
   in the results table. So using Append is a way to add the results
   of more than one query (for example, Movies whose titles start with
   "A" and Movies whose titles start with "B").
4. Open a Movie.

   Select a Movie in the result list and click
   Open, or simply double-click the Movie's title. Either action
   opens the Movie in a separate window that displays its attributes
   and relationships. The attributes-`title`, `category`, `dateReleased`, `posterName`, `revenue`,
   and `trailerName`-are
   in the top part of the window. You can edit any of the Movie's attributes
   here. After making changes, you can save them (click Save at the
   top of the Movie window) or revert back to the original values (click
   Revert).

   The Movie's relationships are in the bottom
   part of the window. One relationship-`studio`-is
   displayed by itself in the middle of the window while the others
   are displayed below in a tab view. The reason for this is explained
   later in the section ["Main, Enumeration, and "Other" Entities"](#apple-ijbegrchjjcuc).

   In
   the Studio area of the Movie window, you can change the Movie's
   Studio (Select), open the Movie's Studio (Open), or unassign the
   Movie's Studio (Deselect). Clicking the Open button simply opens
   the Movie's Studio in a Studio window that is similar to the Movie
   window in that it displays Studio attributes and relationships.
   Clicking Deselect unsets the Movie's `studio` relationship
   so that the Movie has no Studio.
5. Select a new Studio.

   In the Studio area of the Movie
   window, click Select. A dialog opens for searching for Studios.
   Type search criteria (`A` in
   the Name text box, for example), and click Find. Choose a Studio
   from the result list and click OK. The dialog closes, and the Movie's Studio
   is changed from the original to the one you selected.

   Note
   that the Movie window now has an asterisk ("\*") in the title
   bar. The asterisk indicates that the Movie has changes that haven't
   been saved. If you wanted to save the change, you would click Save.
   In this case, however, click Revert to discard the change.
6. Examine the relationship tabs at the bottom of the window.

   The
   relationships for the Plot Summary and Voting tabs-`plotSummary` and `voting`-are to-one
   relationships. Their respective panes allow you to modify the destination
   objects directly. For example, if you change the contents of the
   Summary text box in the Plot Summary pane and click Save, you change
   the PlotSummary object's `summary` value
   and commit the change to the database.

   The other relationships-`directors`, `reviews`,
   and `roles`-are to-many
   relationships. Their panes allow you to add destination objects
   to the relationships and to delete objects from them. Additionally
   you can open destination objects (in their own window) and edit
   them.
7. Create a new Movie.

   In the Movie window, click New. Alternatively,
   if the Query Window's Movie tab is still selected, you can click
   New in the Query Window. Either action creates a new Movie window
   into which you enter information about the new Movie. Fields with blue
   titles are required; that is, you can't save the new Movie if
   the blue titled fields are empty.

   Fill in the Movie's
   attributes as follows:

   - __Title__ Evil
     Dead 2
   - __Category__ Horror
   - __Date Released__ 4/1/1987

   Click
   Save to save the new Movie.
8. Set the Movie's Studio to Elite Entertainment.

   In the
   Studio area of the window, click Select. In the Studio dialog, type `E` in
   the Name text box, and click Find. No results are returned, so you
   have to create the Elite Entertainment Studio.

   Click
   New in the Studio dialog. The first dialog closes, and a new Studio
   dialog opens for creating a new Studio. Name the Studio "Elite
   Entertainment" and provide a budget. Click Save.

   The
   new Studio is saved to the database and assigned as the Studio for
   the _Evil Dead 2_ Movie.

   You can
   add directors and movie roles (and their actors) in a similar manner.

### Main, Enumeration, and "Other" Entities

Direct to Java Client divides entities into three types: main,
enumeration, and other. Each of an application's entities is exactly
one of these types.

#### Main Entities

A _main_ entity is generally a top-level
entity that users work with most frequently. Consequently, Direct
to Java Client creates a tab for each main entity in the Query Window and
provides form windows for editing each of the main entities. For
example, in this tutorial application, the main entities are Customer,
Movie, Studio, Talent, Unit, User, and Video.

Direct to Java Client by default defines a main entity as
one that is not the destination of any relationships that

- propagate
  primary key
- own destination
- use the cascade delete rule

#### Enumeration Entities

Direct to Java Client also defines the concept of an _enumeration_ entity.
An enumeration entity by default is an entity that conforms to the
conditions for main entities and additionally conforms to the following
conditions:

- The entity
  has fewer than five attributes.
- The entity has no relationships that are mandatory.
- All the entity's relationships use the deny delete rule.

In practice, enumeration entities should define a collection
of values that represent a list of choices. For example, in this
tutorial application, the enumeration entities are FeeTypes and
RentalTerms.

The values in enumeration entities are usually fairly static,
and you usually don't want a complex user-interface for changing
them. Consequently, Direct to Java Client applications provide a
single window for editing enumeration values, the Enumeration Window.

Choose Tools > Enumeration Window.

This opens the Enumeration Window containing a tab for each
of the application's enumeration entities. The tab for a particular
entity shows the complete set of values in that entity (that should
be a small number of values). You can add a new value to the enumeration's
collection (Add), delete a value from the collection (Remove), and
modify a value (simply make the changes and click Save).

By displaying enumeration values in this special window, an
application doesn't clutter the Query Window with tabs for enumeration
entities. This approach simplifies the application's user interface
in other ways, as well. The application doesn't provide form windows
for enumeration entities, and relationships to enumeration entities
can be represented simply with combo boxes (for to-one relationships)
and pick lists (for to-many relationships) instead of with tables
(to-ones) and select dialogs (to-manys).

#### "Other" Entities

Entities that aren't main or enumeration entities are simply _other_ entities.
For example, in this tutorial application, the _other_ entities
are CreditCard, Director, Fee, MovieRole, PlotSummary, Rental, Review,
TalentPhoto, and Voting.

_Other_ entities can be manipulated through
the master-detail user interfaces of main entities. This explains
why a Movie's `studio` relationship
is displayed by itself in the middle of the window while the other
relationships are displayed below in a tab view. The destination
entity of the `studio` relationship,
Studio, is a main entity. Main entities have their own form windows
with which you edit them. The destinations of the other relationships
are _other_ entities. Since they don't have
their own form windows, they are edited in master-detail interfaces
inside a main entity's form window.

### Customizing the Application

As you can see, the default application is fairly complete.
Direct to Java Client uses a sophisticated set of rules to assemble
the user interface. However, the default user interface isn't
exactly what you want in every case.

In the next sections you make changes to the application,
including the following:

- modify the
  set of main entities
- modify the search attributes in the Query Window, and specify
  the order in which the attributes are displayed. Similarly, modify
  the attributes displayed in the results table of the Query Window.
- specify the order of the attributes and relationships that
  can be edited in a form
- change the widget used to display and edit particular attributes

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Building_an_Application.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](The_Assistant.md)

© 2001 Apple Computer, Inc.
