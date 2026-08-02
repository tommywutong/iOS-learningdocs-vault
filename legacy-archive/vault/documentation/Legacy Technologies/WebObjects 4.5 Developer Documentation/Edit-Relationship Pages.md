---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.62.html
archived_at: '2026-07-15T08:11:17.186580Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Dynamically%20Generated%20Pages.md) [!](Inspect%20and%20Edit%20Pages.md) [!](Master-Detail%20Pages.md)

---

#   Edit-Relationship Pages

An edit-relationship page allows users to add records to a relationship and remove records from the relationship. Users typically come to these pages when they click an Edit button next to a relationship in an edit page. Edit-relationship pages consist of three separate components, of which two are shown at any one time. The first component lists the relationships of a particular property and contains several controls. In addition, a query component initially appears for locating another object to link to for that property. The third component, a select component, appears after you have specified a query and is discussed below.

!

This user interface facilitates the following tasks:

- 

  To remove a record from the property, select the key identifying the record in the browser and click Remove.
- 

  To add a new record to the property, click New Record. An edit component appears underneath the list of relationships; fill out the fields of the edit component and click Save to add the new record to the database _and_
  the new relationship to the property above.
- 

  To locate an existing record to add to the relationship, enter the properties to search on in the query component and click Query DB.

When a query is executed (assuming matching records are found) a select component replaces the query component.

!

To add a listed record to the to-many relationship, click the Select button. To construct a new query, click the Build Query button.

When you have finished editing a relationship, click the Return button under the browser to return to the original edit page. You must click the Save button in this page to store the changed relationship in the database.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Dynamically%20Generated%20Pages.md) [!](Inspect%20and%20Edit%20Pages.md) [!](Master-Detail%20Pages.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
