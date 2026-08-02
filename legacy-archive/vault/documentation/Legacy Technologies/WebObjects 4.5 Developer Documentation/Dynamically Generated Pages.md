---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.5e.html
archived_at: '2026-07-15T08:11:10.120582Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Using%20Your%20Direct%20to%20Web%20Application.md) [!](The%20Login%20Page.md) [!](Query%20Pages.md)

---

#  Dynamically Generated Pages

Besides the login page, there are nine types of dynamically-generated pages (or reusable components) in a Direct to Web application:

- 

  A _query-all page_
  that displays all entities that are currently exposed and lets users construct queries on the attributes (but not the relationships) of those entities; see [Query Pages](Query%20Pages.md#apple-gmztamjy)
  . The properties of this page cannot be customized.
- 

  A _query page_
  that allows the user to construct a query for a particular entity; see [Query Pages](Query%20Pages.md#apple-gmztamjy)
  .
- 

  A _list page_
  that displays one or more records of a particular entity in tabular form. List pages and select components are implemented with the same components; see [List Pages and Select Components](List%20Pages%20and%20Select%20Components.md#apple-gezdqmzt)
  . The result of a query is always a list page.
- 

  An _inspect page_
  that displays a single record of a given entity. Inspect pages and edit pages are implemented with the same components; see [Inspect and Edit Pages](Inspect%20and%20Edit%20Pages.md#apple-gi4tgnjw)
  
  .
- 

  An _edit page_
  that displays a single record of a given entity and also allows you to make changes to the record and save it to the database. Edit and inspect pages are implemented with the same components; see [Inspect and Edit Pages](Inspect%20and%20Edit%20Pages.md#apple-gi4tgnjw)
  
  .
- 

  A _select component_
  that lets users select a record from a list, thereby adding it to a relationship or populating an edit component with it. List pages and select components are implemented with the same components; see [List Pages and Select Components](List%20Pages%20and%20Select%20Components.md#apple-gezdqmzt)
  .
- 

  A _confirm page_
  that prompts users to confirm that they want to delete records. The properties of this page cannot be customized.
- 

  An _edit-relationship page_
  is a multiple component page for removing and adding objects to a relationship. See [Edit-Relationship Pages](Edit-Relationship%20Pages.md#apple-gmztambx)
  .
- 

  An _error page_
  for displaying information related to exceptions and other errors. The properties of this page cannot be customized.

All pages in your application contain the standard Direct to Web header (defined in __MenuHeader.wo__
) at the top of the page. This header provides a number of controls, described in the following figure.

!

For best results when navigating through a Direct to Web application, don't use your web browser's backtrack buttons. Instead:

- 

  To return to the previous page from an edit or inspect page, click Cancel.
- 

  To return to a query page from a list page, click Return.

#### [Query Pages](Query%20Pages.md#apple-obtwmslehu2tcnjv)

#### [List Pages and Select Components](List%20Pages%20and%20Select%20Components.md#apple-obtwmslehu4dambs)

#### [Inspect and Edit Pages](Inspect%20and%20Edit%20Pages.md#apple-obtwmslehuytknbqgm)

#### [Edit-Relationship Pages](Edit-Relationship%20Pages.md#apple-obtwmslehuytanjyge)

#### [Master-Detail Pages](Master-Detail%20Pages.md#apple-obtwmslehuytanjyhe)

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Using%20Your%20Direct%20to%20Web%20Application.md) [!](The%20Login%20Page.md) [!](Query%20Pages.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
