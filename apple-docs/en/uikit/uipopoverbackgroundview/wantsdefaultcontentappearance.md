---
title: wantsDefaultContentAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+（13.0 起废弃）, iPadOS 6.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopoverbackgroundview/wantsdefaultcontentappearance
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverbackgroundview/wantsdefaultcontentappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverbackgroundview/wantsdefaultcontentappearance.json'
content_hash: 'sha256:5ebb145b938fab78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverBackgroundView](../uipopoverbackgroundview.md)

# wantsDefaultContentAppearance

<sub>Type Property</sub>

Determines whether the default content appearance should be used for the popover.

> [!warning] Deprecated
> The system no longer supports this feature.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class var wantsDefaultContentAppearance: Bool { get }
```

## Discussion

This method may be overridden to prevent the drawing of the content inset and drop shadow inside the popover. The default implementation of this method returns [true](../../swift/true.md), which means that the content inset and drop shadow will be drawn. Overriding this method simply means implementing it to return [false](../../swift/false.md), which would mean that the content inset and drop shadow will not be drawn.
