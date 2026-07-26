---
title: arrowDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/arrowdirection
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/arrowdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/arrowdirection.json'
content_hash: 'sha256:02316e2344674d6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# arrowDirection

<sub>Instance Property</sub>

The arrow direction in use by the popover.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var arrowDirection: UIPopoverArrowDirection { get }
```

## Discussion

When the popover is onscreen, this property reflects the actual arrow direction. Before and after presentation, the value of this property is [UIPopoverArrowDirectionUnknown](../uipopoverarrowdirection/unknown.md).

## See Also

### Configuring the popover arrows

- [permittedArrowDirections](permittedarrowdirections.md) — The arrow directions that you allow for the popover.
