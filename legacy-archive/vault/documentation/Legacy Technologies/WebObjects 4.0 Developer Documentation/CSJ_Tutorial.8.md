---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.8.html
archived_at: '2026-07-15T08:00:03.818096Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.7.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.8a.md)

##  Programming With Java Client

Generally, programming a Java Client WebObjects application requires some skills and knowledge common to both Enterprise Objects Framework and WebObjects programmers. However, it also requires a specific design technique: object partitioning.

Objects on the server and the client can be instances of custom classes or generic enterprise objects (EOGenericRecord). Objects that derive from custom subclasses can have different sets of properties on both the server and the client. Usually, client objects have the more restricted set of data and behaviors, but it is really up to you to decide based on the requirements of the application and your business. As noted earlier, the primary criteria for partitioning are performance and security.

The basic tools and techniques for creating a Java Client application are covered in the tutorial for _Creating a Java Client WebObjects Application_
.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.7.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.8a.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
