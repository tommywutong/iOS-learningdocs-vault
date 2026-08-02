---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.025.html
archived_at: '2026-07-15T07:58:34.245685Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.024.md)

## WOActionResults Protocol and Interface

WOActionResults is an Objective-C protocol and Java interface that is now adopted by WOResponse and WOComponent. It defines one method:

|  WOActionResults |  |
|  Method |  Description |
|  generateResponse |  Returns a WOResponse object. WOResponse's implementation simply returns itself. WOComponent creates a WOResponse object by sending itself the __appendToResponse:inContext:__ message. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.026.md)
