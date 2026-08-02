---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/ManagingState9.html
archived_at: '2026-07-15T08:05:49.116350Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState8.md)

### Using Cookies

Storing the sessionID in a cookie can give your application added benefits. For example, if a client is required to log in to your application then by storing the IDs in a cookie that client will not be forced to log in again if they exit your application and then come back later. This is dependent, of course, on that session being around when the client comes back to your application. You must set the session timeouts to longer periods of time in these situations.
You configure this feature using the WOSession methods:

```
- setStoresIDsInURLs:
- storesIDsInURLs
- setStoresIDsInCookies:
- storesIDsInCookies
```

[!Table of Contents](Managing%20State.md) [!Next Section](Storing%20State%20for%20Custom%20Objects.md)
