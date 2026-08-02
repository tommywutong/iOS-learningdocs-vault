---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/Connect1.html
archived_at: '2026-07-18T01:19:24.247708Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Previous Section](Connecting%20to%20a%20Database.md)

# When Database Connections Are Opened and Closed

If you're using an EOEditingContext in your application, Enterprise Objects Framework connects to the database automatically. It makes a connection the first time a database operation is initiated, and reuses that same connection for subsequent database operations.
Enterprise Objects Framework doesn't close its connections to the database. It leaves the connections open until the application terminates. If you need to close database connections that aren't in use, see the section ["Limiting the Number of Database Connections"](Limiting%20the%20Number%20of%20Database%20Connections.md#apple-gi3dg).

[!Table of Contents](Connecting%20to%20a%20Database.md) [!Next Section](Logging%20into%20a%20Database.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
