---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.029.html
archived_at: '2026-07-15T07:58:39.223124Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.028.md)

## WORequest Methods

The following methods have been added to WORequest to support the use of WORequestHandler objects:

|  WORequest |  |
|  Method |  Description |
|  requestHandlerPathArray |  Returns an array containing the portion of the URL following the request handler key, up to the "?", if present. Each part of the string separated by a "/" is stored in a separate element of the returned array. |
|  requestHandlerPath |  Returns the portion of the URL following the request handler key, up to the "?", if present. |
|  requestHandlerKey |  Returns the part of the request's URL that identifies the request handler key. The returned key identifies a request handler for the receiving request. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.030.md)
