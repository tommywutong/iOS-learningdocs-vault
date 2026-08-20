---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DirectToWeb/DirectToWeb.5.html
archived_at: '2026-07-15T07:52:56.285040Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.4.md)[Previous
Section](DirectToWeb.4.md) 

##   Query Pages

The query page for an entity is shown as a two-column table.

##### 

!

The first column in the table lists the entity's properties. The second column contains one or more text fields that let you enter values to query on each property.

A property is either an _attribute_
(a value stored directly in this entity's table) or a _relationship_
(an association between this entity and another entity). For example, in the figure, Title is an attribute and Studio is a relationship. You can use the WebAssistant to hide properties that you don't want users to see.

_Note:_
Direct to Web only displays properties that are class properties. In addition, primary keys and attributes marked as the source of a relationship are hidden by default.

Note that properties are represented in different ways. For example, in the figure, you enter a single string value for Title, while you enter a range of values for Date Released. You can change the representation of most properties using the WebAssistant. In particular, you may want to change how relationships are shown, since by default, you query them by specifying an ID, which is something the user is unlikely to know. See [See The Direct to Web Components](DirectToWeb.9.md#apple-ge2tgnzs)
for more information on the different ways of representing properties in your application's pages.

In the Movie query, to get a list of all dramas released in the 1990's, you would:

####  1. Enter _Drama_ in the Category field.

####  2. Enter _1/1/90_ and _12/31/99_ in the Date Released fields.

####  3. Click Query DB.

The results are displayed in a list page; see [See List Pages](DirectToWeb.6.md#apple-gezdqmzt)
.

[!](DirectToWeb.md)[Table
of Contents](DirectToWeb.md) [!](DirectToWeb.6.md)[Next
Section](DirectToWeb.6.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
