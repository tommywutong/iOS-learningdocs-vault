---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/D2W/Direct_to_W_pplications.html
archived_at: '2026-07-15T08:14:58.775949Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/WOHTML/iGuidelines__ed_Approach.html)[![Next](attachments/WebObjectsOverview/Images/next.gif)](How_Direct_to_Web_Works.md)

# Direct to Web Applications

Direct to Web is a technology that creates
HTML-based Web applications that use enterprise objects and consequently
access databases. All you need to provide is the model that specifies
the database-to-objects mapping and Direct to Web instantly creates
an application.

Direct to Web applications have a particular structure. Every
Direct to Web application begins on a login page ( [Figure 5-1](#apple-ijauercgjfcec)). By
default, this page provides an interface to authenticate the user
but does not actually perform any authentication. Because the login page
is a standard WebObjects component, you can change its behavior.

__Figure
5-1 A login page__

![[image: ../Art/Login.gif]](../Art/Login.gif)

After the user logs in, Direct to Web displays its first dynamically
generated page: a query-all page ( [Figure 5-2](#apple-ijauerkeincec)). This page allows the
user to specify the enterprise objects he or she wants to work with.
The user can query for any type of enterprise object that is visible in
the application (the developer decides which types are visible and
which are not).

__Figure
5-2 A query-all page__

![[image: ../Art/QueryAll.gif]](../Art/QueryAll.gif)

If the query-all page is not specific enough, the user can
click one of the hyperlinks labeled "more..", which brings up
a query page specific to the corresponding type of enterprise object
( [Figure 5-3](#apple-inbeqskijfdee)). In
this page, the user can specify the values for several properties
at the same time. The resulting query is the logical "and" of
the individual queries for the properties.

__Figure
5-3 A query page__

![[image: ../Art/QueryPage.gif]](../Art/QueryPage.gif)

When the user clicks the Query button on the query page or
the magnifying glass icon on the query-all page, Direct to Web displays
the enterprise objects matching the query on a list page ( [Figure 5-4](#apple-inbeqssdjfceq)). This
page presents the enterprise objects in batches; the user can change
the batch size and navigate from batch to batch.

__Figure
5-4 A list page__

![[image: ../Art/ListPageBAS.gif]](../Art/ListPageBAS.gif)

Note that each Movie enterprise object on the list page in [Figure 5-4](#apple-inbeqssdjfceq) has
an Edit button, which indicates that Movie objects are read-write.
The developer can configure whether a type of enterprise object
is read-only or read-write.

If the Movie objects are read-only, an Inspect button appears
on each row instead of an Edit button. If the user clicks the Inspect
button next to one of the enterprise objects, Direct to Web displays
an inspect page for the object ( [Figure 5-5](#apple-inbeqrsjirfeg)) that reveals more detailed information
about the object.

__Figure
5-5 An inspect page__

![[image: ../Art/InspectPage.gif]](../Art/InspectPage.gif)

If the objects displayed on the list page are writable and
the user clicks the Edit button next to one of them, Direct to Web
displays an edit page for the object ( [Figure 5-6](#apple-inbeqqsdivbuo)). On the edit page, the
user can edit the attributes for the object or click the Edit button
next to one of the relationships to edit the relationship.

__Figure
5-6 An edit page__

![[image: ../Art/EditPage.gif]](../Art/EditPage.gif)

The user edits a relationship using an edit-relationship page
( [Figure 5-7](#apple-inbeqrscizeum)), which
edits to-many and to-one relationships.

__Figure
5-7 An edit relationship page__

![[image: ../Art/EditRelationshipPage.gif]](../Art/EditRelationshipPage.gif)

With the exception of the login page, every Direct to Web
page has an area containing a menu and buttons that assist in navigating
around the application ( [Figure 5-8](#apple-ijaueskfineug)). This is called the __menu header__.

__Figure
5-8 The menu header__

![[image: ../Art/MenuBar.gif]](../Art/MenuBar.gif)

Every Direct to Web application appears in one of three __looks__.
A look is a visual theme, and affects the layout and appearance
of the pages. The example pages you have seen are in the Basic look.
Direct to Web also supports two other looks: the Neutral look ( [Figure 5-9](#apple-inbeqr2kirfec)) and
the WebObjects look ( [Figure 5-10](#apple-inbeqrkfizduc)).

__Figure
5-9 An example Neutral look page__

![[image: ../Art/ListPageNEU.gif]](../Art/ListPageNEU.gif)

__Figure
5-10 An example WebObjects look page__

![[image: ../Art/ListPageWOL.gif]](../Art/ListPageWOL.gif)

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/WOHTML/iGuidelines__ed_Approach.html)[![Next](attachments/WebObjectsOverview/Images/next.gif)](How_Direct_to_Web_Works.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
