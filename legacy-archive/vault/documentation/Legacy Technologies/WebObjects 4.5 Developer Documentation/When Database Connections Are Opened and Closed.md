---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/Connect1.html
archived_at: '2026-07-15T08:02:55.697175Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Previous Section](Connecting%20to%20a%20Database.md)

# When Database Connections Are Opened and Closed

If you're using an EOEditingContext in your application, Enterprise Objects Framework connects to the database automatically. It makes a connection the first time a database operation is initiated, and reuses that same connection for subsequent database operations.
Enterprise Objects Framework doesn't close its connections to the database. It leaves the connections open until the application terminates. If you need to close database connections that aren't in use, see the section ["Limiting the Number of Database Connections"](Limiting%20the%20Number%20of%20Database%20Connections.md#apple-gi3dg).

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Next Section](Logging%20into%20a%20Database.md)
