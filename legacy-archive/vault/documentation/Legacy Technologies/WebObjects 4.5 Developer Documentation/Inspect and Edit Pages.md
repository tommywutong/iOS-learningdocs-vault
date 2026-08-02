---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.61.html
archived_at: '2026-07-15T08:11:15.590746Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Dynamically%20Generated%20Pages.md) [!](List%20Pages%20and%20Select%20Components.md) [!](Edit-Relationship%20Pages.md)

---

#   Inspect and Edit Pages

Inspect pages and edit pages display the data for a single record of an entity. An edit page allows you to make changes to the record and save the changes, while an inspect page is read-only.

An inspect page looks like this:

!

Note the buttons at the bottom of the page:

- 

  Delete allows you to delete the record from the database.
- 

  Cancel takes you back to the page from which you accessed this inspect page.
- 

  Edit brings up the equivalent edit page for this record, so that you can make changes. (However, if your application specifies a particular entity as read-only, you won't be able to edit it.)

Also note the Movies property in the example above. You click the triangle to display the movies of this studio in a list, browser, or table, as in the following example:

!

This property is configured with the DisplayToManyTable component. For more on how this is done, see [Representation of Relationships](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.6c.html#21759)
.

An edit page (or edit component) looks like this:

!

It is similar to the inspect page, except that it has a Save button (for saving changes to the database) instead of an Edit button. If you click the Edit button next to the list of Movies, an edit-relationship page is displayed for editing the records in the to-many relationship. Edit components can occur in multiple-component pages, such as the master-detail page.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Dynamically%20Generated%20Pages.md) [!](List%20Pages%20and%20Select%20Components.md) [!](Edit-Relationship%20Pages.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
