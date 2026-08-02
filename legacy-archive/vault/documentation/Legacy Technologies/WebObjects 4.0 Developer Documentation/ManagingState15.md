---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ManagingState15.html
archived_at: '2026-07-18T01:20:14.057627Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState14.md)

## Using awake and sleep

Another strategy for managing session state is to create it at the beginning of the request-response loop and then release it at the end. The session object's __awake__ and __sleep__ methods provide the hooks you need to implement this strategy. A session object receives an __awake__ message at the beginning of the request-response loop (where you can re-initialize the session state) and a __sleep__ message at the end (where you can release it). Remember that __awake__ and __sleep__ are not sent during the direct action request-response loop, but the direct action request-response loop does not use session objects by default.

[!Table of Contents](Managing%20State.md) [!Next Section](Controlling%20Component%20State.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
