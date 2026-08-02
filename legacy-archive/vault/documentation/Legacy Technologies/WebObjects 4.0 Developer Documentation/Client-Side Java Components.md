---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/DynamicElements5.html
archived_at: '2026-07-18T01:20:09.950587Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Dynamic%20Elements.md) [!Previous Section](DynamicElements4.md)

# Client-Side Java Components

Instead of using server-side dynamic elements, you could create Java applets that run on the client. Typically, applets are downloaded to the client once and then have virtually no communication with the server. Client-side Java components, however, run on the client and continuously synchronize their states with objects on the server.
Client-side components can also trigger action methods on the server. For this reason, they may be said to work in virtually the same way as server-side dynamic elements.
Prior to WebObjects 4.0, client-side components were the recommended way to enhance web pages with complex custom controls-controls that provided greater functionality and interactivity than those supported directly in HTML. Now, however, WebObjects allows you to create true three-tier applications (Web client, application server, and database server), with the interface written entirely in Java and running completely on the client. This allows your WebObjects applications to have a much richer, more responsive, and more active interface than traditional HTML-based web applications, while running on all Java-enabled platforms and browsers that support the "Swing" user interface toolkit. Although client-side components are still supported, the new JavaClient feature is now the preferred way to build client-side Java applications in WebObjects

[!Table of Contents](Dynamic%20Elements.md) [!Next Section](DynamicElements6.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
