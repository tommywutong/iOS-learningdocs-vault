---
title: permittedArrowDirections
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverpresentationcontroller/permittedarrowdirections
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/permittedarrowdirections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverpresentationcontroller/permittedarrowdirections.json'
content_hash: 'sha256:77b2f743d4821905'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverPresentationController](../uipopoverpresentationcontroller.md)

# permittedArrowDirections

<sub>Instance Property</sub>

The arrow directions that you allow for the popover.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var permittedArrowDirections: UIPopoverArrowDirection { get set }
```

## Discussion

Prior to displaying the popover, set this property to the arrow directions that you allow for your popover. The actual arrow direction in use by the popover is stored in the [arrowDirection](arrowdirection.md) property.

The default value of this property is [UIPopoverArrowDirectionAny](../uipopoverarrowdirection/any.md).

## See Also

### Configuring the popover arrows

- [arrowDirection](arrowdirection.md) — The arrow direction in use by the popover.
