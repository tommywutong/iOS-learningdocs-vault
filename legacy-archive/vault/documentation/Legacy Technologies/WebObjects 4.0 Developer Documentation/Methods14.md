---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Methods14.html
archived_at: '2026-07-18T01:20:16.944952Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods13.md)

### Application Awake

The application's __awake__ method is invoked at the start of every cycle of the request-response loop. Therefore, in the __awake__ method, you perform anything that should happen before each and every user request is processed. For example, if you wanted to keep track of the number of requests that an application receives, you could do that in the __awake__ method:

```
// WebScript Application.wos
- awake {
        ++requestCount;
        [self logWithFormat:@"Now serving request %@",
requestCount];
}
// Java Application.java
public void awake() {
        ++requestCount;
        this.logString("Now serving request " + requestCount);
}
```

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods15.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
