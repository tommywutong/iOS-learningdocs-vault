---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/HowWOWorks/DBIntegration.html
archived_at: '2026-07-15T07:46:52.201165Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.mif.book.md)
[!Previous Section](PageComp.md)

# __Database Integration__

WebObjects has been extended and enhanced in many ways to interact smoothly with the Enterprise Objects Framework, thereby enabling WebObjects applications to fetch, write, and query database records. A major factor behind this integration is WODisplayGroup. Instances of this class (commonly referred to as display groups) provide a simple interface allowing objects in a WebObjects application to interact with relational databases. Enterprise Objects Framework and WODisplayGroup convert operations on objects to database operations on records. Display groups use classes defined in Enterprise Objects to:

- Fetch data from the data.
- Insert, update, and delete database records.
- Build qualifiers from user input and order search results.
- Manage batches of search results.

The WOSession class also provides access to an EOEditingContext object that is used, for example, when changed data is saved to the database. Each session uses its own EOEditingContext to manage graphs of objects fetched from a database and to ensure that activity remains synchronized. For read-only applications you can customize WOSession to return a per-application EOEditingContext.

[!Table of Contents](HowWOWorks.mif.book.md)
[!Next Section](StartingRRLoop.md)
