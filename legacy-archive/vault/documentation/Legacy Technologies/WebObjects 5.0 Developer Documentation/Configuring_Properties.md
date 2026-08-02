---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToJavaClient/Tutorial/Configuring_Properties.html
archived_at: '2026-07-15T08:12:20.983662Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Configuring_Entities.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Configuring_Widgets.md)

## Configuring Properties

The Assistant's Properties tab allows you to configure the
way an application handles properties (attributes and relationships).
For example, you can change the attributes that users search on
in the Query Window and specify the order in which they appear.

1. Set the property
   keys for querying the Movie entity.

   In the Assistant, click
   the Properties tab. The specification settings-the Question, Task, and
   Entity pull-down lists-should be set to <All>, query, and
   Movie, respectively. The settings are probably correct, but if any
   of the settings are different, change them. A simple way to set
   the Task and Entity pull-down lists is to select the Movie tab in
   the Query Window. The Assistant automatically updates to set the
   Task pull-down list to query and the Entity pull-down list to Movie.

   Move `plotSummary` and `voting` to
   the Other Property Keys list. Move `category` and `studio` to
   Property Keys. Using the up and down arrows, order the properties
   as follows: `title`, `category`, `studio`.

   Save
   the changes, and restart the application (from the Assistant). The
   Movie pane of the Query Window is reconfigured.

   Note
   that a Studio Name field is now available. This is because you specified
   the `studio` relationship
   as a property key for the query task. When a to-one relationship
   (such as `studio`) is specified
   as a property key, Direct to Java Client uses _identify_ property
   keys of the relationship's destination object to represent the
   relationship in the user interface.
2. Examine the identify property keys for the Studio entity.

   In
   the Assistant, choose `identify` from
   the Task pull-down list and choose Studio from the Entity pull-down
   list. Observe that the Studio has one identify property key-`name`. This
   attribute is used to identify a particular Studio when it appears
   in the user interface as a destination of a to-one relationship.

   One
   example of how the identify property keys are used is in the Movie
   pane of the Query Window. Movie's `studio` relationship
   is specified as a query property key. To represent `studio` as
   a property key in the Query Window, Direct to Java Client uses the identify
   property key (`name`) of
   the relationship's destination entity (Studio).

   Another
   example is the Studio part of a Movie window, in which the Movie's
   Studio is identified by its `name`.
3. Modify the identify property keys for the Movie entity.

   Choose
   Movie from the Entity pull-down list, keeping the Task as `identify`.
   Movie has one identify property key, `title`.
   Since it's quite common for movie remakes to use the same name
   as the original, a movie's title isn't always enough to identify
   it. Add `dateReleased` to
   Movie's list of identify properties, and save the change.
4. Configure the property keys for listing Movies.

   The property
   keys for the list task are used in result lists such as the ones
   in the Query Window. When you search for Movies, for example, the
   Movies in the result set are listed in the Query Window's table.
   The result table has a column for the list property keys, `title`, `category`, `dateReleased`, `posterName`, `revenue`, `trailerName`,
   and `plotSummary`. The
   columns for these properties are crowded into the table, and many
   aren't particularly helpful to users.

|  |
| --- |
| __Note:__ In addition to the property keys listed above, `voting` is also a list property key for the Movie entity. The `voting` relationship doesn't have a column in the results table. This is because Voting's identify property key is it's `movie` relationship, which Direct to Java Client omits from the table view to avoid recursion. |

   To pare down the set of columns, choose list from the
   Assistant's Task pull-down list, and choose Movie from the Entity
   pull-down list (if it isn't selected already). Move `posterName`, `revenue`, `trailerName`,
   and `plotSummary` to the
   Other Properties column.

   So users can verify that all
   the search criteria they specify is applied correctly, the list property
   keys should be a superset of the query properties. Since users can
   search for Movies by Studio, the list property keys should include `studio`,
   as well. Add `studio` to the
   list property keys.

   Save the changes. To see them, open
   a new Query Window.
5. Configure the property keys for Movie form windows.

   In
   the Query Window, click New to create a Movie form window. The Assistant updates
   to set the Task pull-down list to form and the Entity pull-down
   list to Movie.

   Examine the form window. As is most commonly
   the case, the default property keys for the form task are correct
   for this application. In general, the form window should allow users
   to edit all of an entity's client class properties. However, you
   might want to reorder the properties so they appear in different
   locations in the form window.

   Using the up and down
   buttons, order the properties as follows: `title`, `category`, `dateReleased`, `rated,
   revenue`, `posterName`, `trailerName`, `plotSummary`, `directors`, `roles`, `voting`, `reviews`, `studio`.
   Save the changes, and open a new Movie form window to see how they
   affect the form window layout.

[![Previous](attachments/DirectToJavaClient/Images/previous.gif)](Configuring_Entities.md)[![Next](attachments/DirectToJavaClient/Images/next.gif)](Configuring_Widgets.md)

© 2001 Apple Computer, Inc.
