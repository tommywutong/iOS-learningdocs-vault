---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.60.html
archived_at: '2026-07-15T08:11:12.618726Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Dynamically%20Generated%20Pages.md) [!](Query%20Pages.md) [!](Inspect%20and%20Edit%20Pages.md)

---

#   List Pages and Select Components

A list page displays a table showing multiple records of an entity. List pages are used to display the results of a query, or to show the records satisfying a to-many relationship in another list or inspect page.

!

Each row in the table represents a record. By default, a batch of ten records are shown in a page. To change the batch size, type a number in the "Display _ Items" field and press Return or Enter. To display additional records in either direction, click the triangle buttons or enter the page number you want to go to.

Each column in the list represents one of the entity's properties. By default, all properties are shown in alphabetical order. You can hide columns and change their order by using the Web Assistant; see [Customizing Your Application With the Web Assistant](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md#apple-gmztimjy)
.

The symbols to the right of attribute names represent their sort order:

- 

  !
  : ascending order
- 

  !
  : descending order
- 

  !
  : unsorted

To change the sort order for any attribute, click the title to cycle between ascending, descending, and unsorted. By default, the records are sorted in ascending order by the attribute in the first column. You can specify up to three columns to sort on; the last one specified becomes the primary sort key.

For properties that represent relationships, an Inspect button appears in the cell by default (DisplayToManyFault).

__Note:__

By default, the list page does not display relationships (including the Inspect buttons). You can configure the list page to display relationships using the Web Assistant; see [Customizing Your Application With the Web Assistant](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md#apple-gmztimjy)
.

When you click the Inspect button one of two things happen, depending on the type of relationship:

- 

  If it is a to-one relationship, an inspect page appears, showing the destination record.

  In the above example, the Movie entity's Studio relationship is a to-one relationship to the Studio entity. If you click the Inspect button, an inspect page appears for the Studio entity corresponding to the selected movie; see [Inspect and Edit Pages](Inspect%20and%20Edit%20Pages.md#apple-gi4tgnjw)
  
  .
- 

  If it is a to-many relationship, another list page appears, showing all the destination records in the relationship.

  In the above example, the Movie entity's Roles relationship is a to-many relationship to the MovieRole entity. If you click the Inspect button, a list page appears, showing all the roles in the selected movie.
  
  !

You can use the Web Assistant to display the related records directly in the table instead of with an Inspect button; see [Customizing Your Application With the Web Assistant](Customizing%20Your%20Application%20With%20the%20Web%20Assistant.md#apple-gmztimjy)
.

The select component looks a lot like the list page, but instead of the Edit button there is a Select button. The select component occurs in multiple-component pages. In the edit-relationship page you click Select to add a record to a to-many relationship or select a record for a to-one relationship. In the master-detail page you click Select to select a record to edit. A select component looks like this:

!

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Dynamically%20Generated%20Pages.md) [!](Query%20Pages.md) [!](Inspect%20and%20Edit%20Pages.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
