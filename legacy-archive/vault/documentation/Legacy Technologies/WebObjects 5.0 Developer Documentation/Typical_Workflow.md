---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToJavaClient/Tutorial/Typical_Workflow.html
archived_at: '2026-07-15T08:12:21.113577Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Configuring_Widgets.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Configuring_Windows.md)

## Typical Workflow

The most natural way to customize an application's property
keys and widgets is to examine and modify one window at a time,
as outlined by the steps below:

1. With the
   Assistant open, click the first tab in the Query Window.
2. Examine the search properties for the current entity. Remove
   any fields necessary, add others, and then order the property keys
   as you want them to appear in the Query Window.
3. Choose list in the Assistant's Task pull-down list, and
   modify the list property keys. Since the Query Window displays list
   properties as well as query properties, you can see what changes
   you need to make.
4. Click the next tab in the Query Window. The Assistant automatically
   updates to track your movements in the application. This saves you
   setting the Entity pull-down list in the Assistant.
5. Repeat steps 2 through 4, until you've set the query and
   list property keys for all the main entities.
6. Click the first tab in the Query Window.
7. Click New to open a form window for the current entity. Make
   necessary changes to the entity's form property keys.
8. Make any necessary changes to property keys of any other entity
   that appears in the current entity's form window. To do so, choose `list` or `identify` from
   the Assistant's Task pull-down list, and set the Entity pull-down
   list to the other entity.
9. Click the next tab in the Query Window.
10. Repeat steps 7 and 9.

The following sections demonstrate this approach. Before
continuing, open the Assistant if it isn't open already, and select
the Properties tab.

### Examining the Panes of the Query Window

You've already configured the Movie pane of the Query Window,
so examine the next pane, Talent. The window allows you to search
on a talent's first and last names, and it shows the first and
last names in the results table. This is fine, so move on to the
next pane, Studio.

#### Configuring the Studio Pane of the Query Window

The Studio pane allows you to search for studios by their
name and budget. It seems unlikely that users want to search on
budget.

Remove `budget` from
the query property keys list.

The results table shows the studio name and budget. This seems
fine, so move on to the next pane.

#### Configuring the Customer Pane of the Query Window

The Customer pane allows you to search for customers by their
city, first name, last name, credit card number, and credit card
authorization. Users should not look up customers by credit card
information, so you should remove it.

1. Remove `creditCard` from
   the query property keys.

   The `creditCard` property
   is a to-one relationship that Direct to Java Client expands to the
   identify property keys (`cardNumber` and `authorizationNum`)
   of the relationship's destination entity (a CreditCard). By removing `creditCard` from
   the property keys, you remove the `cardNumber` and `authorizationNum` fields
   from the query interface.
2. Add `memberSince` and `phone` to
   the property keys.

   Two other Customer properties, `memberSince` and `phone`,
   seem like reasonable attributes to query on, so add them.
3. Order the keys as follows: `firstName`, `lastName`, `city`, `phone`, `memberSince`.
4. Modify the list property keys.

   The results table is far
   too crowded with properties to be useful, so pare down the set of
   list property keys. Remove `state`, `streetAddress`, `zip`,
   and `creditCard` from the
   list property keys. Order the remaining keys as follows: `firstName`, `lastName`, `city`, `phone`, `memberSince`.

Move on to the next pane.

#### Configuring the Unit Pane of the Query Window

The Unit pane allows you to search for units by unit ID, date
acquired, movie name, and movie release date. It seems unlikely
that users want to search for particular units by movie release
date, so remove it.

Note that the query property keys for Unit are `unitID`, `dateAcquired`,
and `video`. Through the `video` key,
Direct to Java Client gets both a movie name and movie release date,
which correspond to the Movie `identify` property
keys. You want to keep the movie name in the interface, but not
the movie release date.

1. Remove `video` from
   the property keys.

   Using the `video` key,
   you can't get one `identify` Movie
   property without the other one, so remove it. You'll add the Movie `name` property
   to the query interface another way.
2. Add `video.movie.title` to
   the property keys.

   Type `video.movie.title` in
   the Additional Property Key Path text box at the bottom of the Properties
   pane, and click Add.
3. Save and restart to observe these changes.

   Adding key
   paths to an entity's property keys flattens attributes into the
   entity for display purposes: the attribute identified by the key
   path is treated in the user-interface as if it's one of the entity's
   own attributes rather than an attribute of a related entity.
4. Change the label for `video.movie.title`.

   The
   label for `video.movie.title`,
   "Video Movie Title", seems unnecessarily wordy. "Movie Title"
   is better.

   Click the Widgets tab in the Assistant. Set
   the Task pull-down list to <ALL> if it isn't already, then
   choose `video.movie.title` from
   the Property Key pull-down list. In the Label field, delete the
   word "Video" so the label is simply "Movie Title".
5. Save and restart to observe this change.

   Notice that
   the movie title label is now "Movie Title" for both the search
   field and for the column in the results table. To set one, but not
   the other, you would simply set the Task pull-down list to the appropriate
   task before making the change.
6. Examine Unit's list properties.

   The `notes` property
   contains free-form text, and doesn't display well in a list, so
   remove `notes` from Unit's
   list property keys.

Move on to the next pane.

#### Configuring the Video Pane of the Query Window

Video's query interface has the same problem as Unit's.
It seems unlikely that users want to search for videos by movie
release date. Remove it from the query interface the same way you
did for Unit. That is, remove the `movie` relationship
from the property keys and add `movie.title`.

### Examining Form Windows

Now that you've configured the panes of the Query Window,
move on to the form windows. You've already configured Movie's
form window, so start with Talent.

Open a Talent form. It looks fine, so move on to Studio. It,
too, looks fine, so move on to Customer.

#### Configuring the Customer Form Window

All the Customer properties are property keys. This is fine;
users need to be able to edit all of a customer's data. However,
the properties are ordered poorly. A customer's name should come
first, and the components of a customer's address should be grouped together
and ordered so they appear as a proper address.

1. Order the
   Customer form property keys as follows: `firstName`, `lastName`, `memberSince`, `phone`, `streetAddress`, `city`, `state`, `zip`, `creditCard`, `rentals`.
2. Examine the Credit Card pane at the bottom of the Customer
   window.

   The property keys are poorly ordered, and the "Num"
   in the "Authorization Num" label should be spelled out.
3. Using the Properties Assistant, order CreditCard's form
   property keys as: `cardNumber`, `expirationDate`, `limit`, `authorizationNum`, `authorizationDate`, `customer`.

   Note
   that `customer` is a to-one
   relationship from CreditCard to Customer. Ordinarily, a to-one relationship
   is represented in a form, but `customer` isn't
   represented here. That's because Direct to Java Client filters
   the `customer` property
   key out of the user interface rather than display it recursively.
   Since the CreditCard form is contained within a Customer form, Customer
   information is already displayed. This feature is called _entity hierarchy
   filtering_.

|  |
| --- |
| __WARNING__ |
| Be careful about removing relationships from the set of property keys. Even though a relationship isn't necessary for a window you're looking at, it might be needed by another window. |

   As
   an example, consider the MovieRole entity, which has to-one relationships
   to Movie and Talent. Similarly, Movie and Talent have to-many relationships
   back to their MovieRoles. Since MovieRole is an _other_ entity,
   MovieRole records are manipulated in a master-detail user interface
   in Movie and Talent form windows. In a Movie form window, the interface
   for displaying and setting a MovieRole's value uses only the `roleName` attribute
   and the `talent` relationship.
   Entity hierarchy filtering prevents the interface from using the `movie` relationship.
   When you're looking at the Movie form window, you might consider
   removing MovieRole's `movie` relationship
   from the form task's property keys. It's filtered out, but you
   might think of removing it anyway for clarity. However, if you remove
   it, the `movie` relationship
   won't be displayed in the Talent form window either. In the Talent window
   a MovieRole's `movie` relationship
   is important information.
4. In the Widgets pane of the Assistant, change the `authorizationNum` label
   to "Authorization Number".
5. Examine the Rentals pane.

   The Rentals pane looks OK,
   so move on to the next form window.

#### Configuring the Unit Form Window

The form property keys for Unit are correct, and their order
is fine, too. However, the notes property should be in a text area
instead of a field.

1. Change the `notes` widget
   to a text area.

   Click the Widgets tab in the Assistant. Set
   the Task pull-down list to form, and choose `notes` from
   the Property Key pull-down list. Set the Widget Type to EOTextAreaController.
   Save the change, and open a new Unit form window to see the result.
2. Examine the Rentals area of the window.

   You need to resize
   the windows to read the Rental table columns. Each Rental line displays
   Customer identify properties: `city`, `firstName`,
   and `lastName`. The `city` attribute
   isn't really necessary, and it would be more helpful if a customer's
   last name were to appear first.
3. Modify Customer's identify property keys.

   Remove `city` from
   Customer's identify property keys. Order `lastName` first.
   Save your changes.

Move on to the next form window, Video. It's fine.

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Configuring_Widgets.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Configuring_Windows.md)

© 2001 Apple Computer, Inc.
