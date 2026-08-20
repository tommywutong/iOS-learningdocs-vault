---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.031.html
archived_at: '2026-07-15T07:58:40.580488Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.030.md)

## WOContext Changes

The following methods have been added to WOContext to return information from the request URL:

|  WOContext |  |
|  Method |  Description |
|  directActionURLForActionNamed:queryDictionary: (Objective-C)  directActionURLforActionNamed (Java) |  Returns the complete URL for the specified action. |
|  componentActionURL |  Returns the complete URL for the component action. |
|  urlWithRequestHandlerKey:path:queryString: (Objective-C)  urlWithRequestHandlerKey (Java) |  Returns a URL relative to cgi-bin/WebObjects. |
|  completeURLWithRequestHandlerKey:path:queryString:isSecure:port: (Objective-C)  completeURLWithRequestHandlerKey (Java) |  Returns the complete URL for the specified request handler. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](Improved%20Nested%20Component%20Support.md)
