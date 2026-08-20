---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods14.html
archived_at: '2026-07-15T08:05:52.116603Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

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
