---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Methods15.html
archived_at: '2026-07-15T08:05:52.622484Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods14.md)

### Session Awake

After the application object has performed its own __awake__ method, it restores the appropriate session object and sends it the __awake__ message too.
If you wanted to keep track of the number of requests per session instead of per application, you could do so in the session's __awake__ method:

```
- awake {
    requestCount++;
}
```

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods16.md)
