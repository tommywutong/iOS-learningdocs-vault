---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WOClasses6.html
archived_at: '2026-07-18T01:20:33.081306Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Previous Section](WOClasses5.md)

## Database Integration Level

Database integration is handled mainly by classes in the Enterprise Objects Framework (see [Figure 19](#apple-gq2damq)). The Enterprise Objects Framework converts operations on objects to database operations on records, thereby allowing your WebObjects application to interact with a database in an object-oriented manner.

!

Figure 19. Request-Response Loop: Database Access

Two classes are involved at this level:

- WODisplayGroup

Performs fetches, queries, creations, and deletions of records from one table in the database. WODisplayGroup is a sort of bridge between the dynamic elements on your page and the objects in the Enterprise Objects Framework.

- EOEditingContext (in Java, this is in the package __com.apple.yellow.eocontrol__)

Manages a graph of objects fetched from a database. The objects represent tables, rows, and columns in the database.

When a WebObjects application accesses a database, one or more of the components in the application contain one or more WODisplayGroup objects. The session object provides access to an EOEditingContext object that is used, for example, when changed data is saved to the database. Each session uses an EOEditingContext to manage graphs of objects fetched from a database and to ensure that all parts of an application remain synchronized. For read-only applications, you can customize WOSession to return a per-application EOEditingContext.
For more information on how the WebObjects and Enterprise Objects classes interact, see the _Enterprise Objects Framework Developer's Guide_.

[!Table of Contents](WebObjects%20Viewed%20Through%20Its%20Classes.md) [!Next Section](How%20WebObjects%20Works-A%20Class%20Perspective.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
