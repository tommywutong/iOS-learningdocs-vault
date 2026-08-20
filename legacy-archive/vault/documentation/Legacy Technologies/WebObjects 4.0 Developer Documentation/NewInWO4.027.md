---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.027.html
archived_at: '2026-07-15T07:58:37.958239Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.026.md)

## WORequestHandler Class

A WORequestHandler is an object that can handle requests received by the WebObjects application server. The WORequestHandler class defines three methods.

|  WORequestHandler |  |
|  Method |  Description |
|  handleRequest: |  Request handlers must implement this method and perform all request-specific handling. By default, a request is an HTTP request. You must supply your own server-side adaptor to accept anything other than HTTP. |
|  lock |  Locks access to the WORequestHandler object. |
|  unlock |  Unlocks access to the WORequestHandler object. |

```
```


A WORequestHandler class must be registered with the WOApplication object before it can be used. When you register a WORequestHandler, you specify a key for that handler, which is used in the URL. This key can be any alphanumeric string, but must contain at least one letter.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.028.md)
