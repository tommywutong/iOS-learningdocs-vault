---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/WhatIsWebObjects2.html
archived_at: '2026-07-18T01:20:39.841563Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Previous Section](Dynamic%20HTML%20Publishing.md)

# Java Client

For some applications HTML is simply too restrictive for efficient client-server communications. Although dynamically-generated HTML pages can make for effective displays, using HTML forms for data entry into your application can be awkward at times. Because of this, WebObjects' Java Client capabilities allow you to partition your application so that a portion of it-including all or part of the user interface-runs in Java directly on the client. Client-server communication is handled by WebObjects.

!

Figure 3. A Web Site Running Java Client Applications

[Figure 3](#apple-gezdeobz) illustrates a Java Client application. As before, the browser can still communicate with your application using HTTP and HTML. In addition, Java Client passes objects between a portion of your application (written in Java) residing within the browser and the portion of your application that remains on the application server. Your WebObjects applications can therefore be a mix of Java Client and HTML-based pages.

[!Table of Contents](What%20Is%20a%20WebObjects%20Application.md) [!Next Section](How%20WebObjects%20Applications%20Work.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
