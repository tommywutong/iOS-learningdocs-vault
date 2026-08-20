---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.040.html
archived_at: '2026-07-15T07:58:46.596829Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Cookie%20API.md)

## Storing Session and Instance IDs

The WOSession class provides methods for storing session and instance IDs in both cookies and in URLs. See [Cookie API](Cookie%20API.md#apple-gmydamjr) for a listing of the methods used to store IDs in cookies. The following table lists those WOSession methods you use to store IDs in URLs:

|  WOSession |  |
|  Method |  Description |
|  setStoresIDsInURLs: |  Controls whether session and instance IDs are stored in URLs. |
|  storesIDsInURLs |  Returns whether session and instance IDs are stored in URLs. |

```
```


You should store IDs either in URLs or in cookies, but not both. Enabling both ID storage mechanisms (cookies and URLs) can have unpredictable results.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](WOExtensions%20Changes.md)
