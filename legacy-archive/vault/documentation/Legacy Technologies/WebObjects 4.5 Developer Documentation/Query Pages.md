---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.5f.html
archived_at: '2026-07-15T08:11:10.650702Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Dynamically%20Generated%20Pages.md) [!](Dynamically%20Generated%20Pages.md) [!](List%20Pages%20and%20Select%20Components.md)

---

#   Query Pages

Direct To Web has two kinds of pages for constructing queries on the properties of entities: a query-all page and a query page. When you log into a Direct To Web application, the query-all page is displayed first by default.

!

The query-all page enables you to construct a query on an attribute of a particular entity (queries on relationships are not allowed). To use this page, select a property from an entity's pop-up list, specify the comparison operator, type the string to search on. and click the magnifying-glass button.

The query page, on the other hand, is tied to a particular entity but allows you to construct queries on relationships as well as attributes. The following example illustrates a query page:

!

The first column in the table lists the current entity's properties. The second column contains pop-up lists and text fields that let you enter values to construct queries on single and multiple properties. When you specify values for multiple properties, the query becomes the logical AND of the queries on the individual properties.

A property is either an _attribute_
(a value stored directly in this entity's table) or a _relationship_
(an association between this entity and another entity). For example, in the figure above, Title is an attribute and Studio is a relationship. You can use the Web Assistant to hide properties that you don't want users to see.

__Note:__
Direct to Web only displays properties that are class properties. In addition, primary keys and attributes marked as the source of a relationship are hidden by default.

Properties are represented in various ways. For example, in the figure, you enter a single string value for Title, while you enter a range of values for Date Released. You can change the representation of most properties using the Web Assistant. In particular, you may want to change how relationships are shown, since by default, you query them by specifying an ID, which is something the user is unlikely to know. See [Changing How Properties Are Displayed](Changing%20How%20Properties%20Are%20Displayed.md#apple-gm3denzv)
for more information on the different ways of representing properties in your application's pages.

You can use initial characters and special characters in query fields for string searches. For example, you could enter "sh" in the Movie entity's Title to search for all movies that begin with those characters. You can also use the asterisk character to indicate "all occurrences." For instance, "\*love" would return all movies that contain the substring "love".

In the Movie query, to get a list of all dramas released in the 1990's, you would:

1. 

   Enter
   Drama
   in the Category field.
2. 

   Enter
   1980/1/1
   and
   1989/12/31
   in the Date Released fields.
3. 

   Click Query DB.

   The results are displayed in a list page; see [List Pages and Select Components](List%20Pages%20and%20Select%20Components.md#apple-gezdqmzt)
   .

To clear the query page, click Build Query.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Dynamically%20Generated%20Pages.md) [!](Dynamically%20Generated%20Pages.md) [!](List%20Pages%20and%20Select%20Components.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
