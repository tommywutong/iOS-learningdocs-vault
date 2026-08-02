---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.042.html
archived_at: '2026-07-15T07:58:47.915885Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](WOExtensions%20Changes.md)

### WOAppleScript

The WOAppleScript component provides the ability to include client-side AppleScript in web pages, allowing WebObjects to control Macintosh computers that have the appropriate browser plug-in.
WOAppleScript has the following attributes:

|  WOAppleScript |  |
|  Attribute |  Description |
|  scripttext |  A string identifying the AppleScript to be executed on the client. This attribute is required. |
|  controller |  An optional string containing either "True" or "False" that determines whether or not the controller panel should appear. |
|  height |  The height of the AppleScript component in client browser. Optional. |
|  width |  The width of the AppleScript component in the client browser. Optional. |
|  scriptcomment |  An optional comment for the AppleScript plug-in. |
|  scripttitle |  An optional title for the AppleScript. |

```
```


WOAppleScript is a non-synchronizing component. See "[Non-Synchronizing Components](NewInWO4.034.md#apple-gi2tgmry)" on [page 35](NewInWO4.034.md#apple-gi2tgmry) for more information.

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.043.md)
