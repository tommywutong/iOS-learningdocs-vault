---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Deployment10.html
archived_at: '2026-07-18T01:20:03.923685Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Deployment9.md)

## Control Memory Leaks

Make sure that all objects allocated by your application are being deallocated. The Yellow Box provides some tools that can help you check your code for memory leaks, such as the ObjectAlloc application. For more information, see ObjectAlloc's on-line help or the MallocDebug application.
Another way to control leaks is to have the application shut down and restart periodically, as described in the section ["Automatically Terminating an Application"](Automatically%20Terminating%20an%20Application.md#apple-gq3temy).

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](Deployment11.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
