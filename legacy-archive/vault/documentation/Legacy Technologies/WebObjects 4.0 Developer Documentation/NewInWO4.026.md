---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.026.html
archived_at: '2026-07-15T07:58:37.307990Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.025.md)

## WOActiveImage, WOForm, WOFrame, WOHyperlink, WOImageButton, WOSubmitButton

All elements that support direct actions have the following new attributes:

|  Attribute |  Description |
|  actionClass |  Specifies the WODirectAction subclass that contains the action named in the __directActionName__ attribute. The __actionClass__ attribute defaults to "DirectAction" if omitted. |
|  directActionName |  Specifies the action to invoke when this element is activated. The name of the corresponding method that is invoked is determined by appending "Action" to the __directActionName__ (for example, the "display" direct action corresponds to the "displayAction" method). The __directActionName__ attribute defaults to "defaultAction" if omitted. |

```
```

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.027.md)
