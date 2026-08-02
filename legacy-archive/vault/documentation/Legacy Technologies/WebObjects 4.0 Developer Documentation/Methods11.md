---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Methods11.html
archived_at: '2026-07-18T01:20:16.648498Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods10.md)

## WODirectAction Initialization

Unlike applications, components, and sessions, WODirectAction objects do not persist between cycles of the request-response loop. A WODirectAction object is initialized at the beginning of a direct action request-response loop cycle and is released or marked for garbage collection at the end of the cycle. The designated initializer for WODirectAction is __initWithRequest:__. In Java, the constructor must take a WORequest argument, for example:

```
public DirectAction(WORequest) { ... }
```


In the __initWithRequest:__ method (or constructor), you perform anything that should happen before the WODirectAction performs any of the actions that it declares.

[!Table of Contents](Common%20Methods.md) [!Next Section](Component%20Action%20Request-Handling%20Methods.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
