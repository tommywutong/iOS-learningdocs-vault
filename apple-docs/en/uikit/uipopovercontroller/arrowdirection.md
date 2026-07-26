---
title: arrowDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopovercontroller/arrowdirection
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/arrowdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/arrowdirection.json'
content_hash: 'sha256:ea33f359f0cf2034'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# arrowDirection

<sub>Instance Property</sub>

The direction of the popover’s arrow.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var arrowDirection: UIPopoverArrowDirection { get }
```

## Discussion

The default value of this property is [UIPopoverArrowDirectionUnknown](../uipopoverarrowdirection/unknown.md). When you present the popover, the value changes to reflect the actual direction of the arrow being used by the popover. When the popover is subsequently dismissed, the value of this property returns to [UIPopoverArrowDirectionUnknown](../uipopoverarrowdirection/unknown.md).

## See Also

### Getting the popover attributes

- [popoverVisible](ispopovervisible.md) — A Boolean value indicating whether the popover is currently visible. _(deprecated)_
