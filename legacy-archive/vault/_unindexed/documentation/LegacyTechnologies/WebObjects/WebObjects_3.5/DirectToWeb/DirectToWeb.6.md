---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.6.html
archived_at: '2026-07-15T07:52:57.596048Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.5.md)[Previous
Section](DirectToWeb.5.md) 

##   List Pages

A list page displays a table showing multiple records of an entity. List pages are used to display the results of a query, or to show the records satisyfing a to-many relationship in another list or inspect page.

##### 

!

Each row in the table represents a record. By default, up to ten records are shown in a page. To display additional records, use the Next and Previous hyperlinks above the table. To change the batch size to a number other than ten, type it in the text field and press Enter.

Each column in the list represents one of the entity's properties. By default, all properties are shown in alphabetical order. You can hide columns and change their order by using the WebAssistant; see [See Customizing Your Application With WebAssistant](DirectToWeb.8.md#apple-gmztimjy)
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

To change the sort order for any attribute, click the title to cycle between ascending, descending, and unsorted.

_Note:_
By default, the records are sorted in ascending order by the attribute in the first column. You can specify up to three columns to sort on; the last one specified becomes the primary sort key.

For properties that represent relationships, an Inspect button appears in the cell by default. When you click the Inspect button:

- 

  If it is a to-one relationship, an inspect page appears, showing the destination record.

In the above example, the Movie entity's Studio relationship is a to-one relationship to the Studio entity. If you click the Inspect button, an inspect page appears for the Studio entity corresponding to the selected movie; see [See Inspect and Edit Pages](DirectToWeb.7.md#apple-gi3dqobt)
.

- 

  If it is a to-many relationship, another list page appears, showing all the destination records in the relationship.

In the above example, the Movie entity's Roles relationship is a to-many relationship to the MovieRole entity. If you click the Inspect button, a list page appears, showing all the roles in the selected movie.

##### 

!

You can use the WebAssistant to display the related records directly in the table instead of with an Inspect button; see [See Customizing Your Application With WebAssistant](DirectToWeb.8.md#apple-gmztimjy)
.

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.7.md)[Next
Section](DirectToWeb.7.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
