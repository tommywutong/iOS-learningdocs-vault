---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/HowWOWorks/DBIntegration.html
archived_at: '2026-07-15T07:51:47.838857Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](HowWOWorks.md) [!Previous Section](PageComp.md)

## Database Integration Level

Database integration is handled mainly by classes in the Enterprise Objects Framework (see [Figure 18](#apple-gq2damq)). The Enterprise Objects Framework converts operations on objects to database operations on records, thereby allowing your WebObjects application to interact with a database in an object-oriented manner.

!Figure 18. Request-Response Loop: Database Access
Two classes are involved at this level:

- WODisplayGroup (in Java, DisplayGroup)

Performs fetches, queries, creations, and deletions of records from one table in the database. WODisplayGroup is a sort of bridge between the dynamic elements on your page and the objects in the Enterprise Objects Framework.

- EOEditingContext (in Java, next.eo.EditingContext)

Manages a graph of objects fetched from a database. The objects represent tables, rows, and columns in the database.

When a WebObjects application accesses a database, one or more of the components in the application contain one or more WODisplayGroup objects. The session object provides access to an EOEditingContext object that is used, for example, when changed data is saved to the database. Each session uses an EOEditingContext to manage graphs of objects fetched from a database and to ensure that all parts of an application remain synchronized. For read-only applications, you can customize WOSession to return a per-application EOEditingContext.
For more information on how the WebObjects and Enterprise Objects classes interact, see the _Enterprise Objects Developer's Guide_.

[!Table of Contents](HowWOWorks.md) [!Next Section](PhasesRRLoop.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
