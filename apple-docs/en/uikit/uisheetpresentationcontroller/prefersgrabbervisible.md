---
title: prefersGrabberVisible
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/prefersgrabbervisible
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersgrabbervisible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/prefersgrabbervisible.json'
content_hash: 'sha256:4912e98c81558296'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# prefersGrabberVisible

<sub>Instance Property</sub>

A Boolean value that determines whether the sheet shows a grabber at the top.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var prefersGrabberVisible: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md), which means the sheet doesn’t show a grabber. A _grabber_ is a visual affordance that indicates that a sheet is resizable. Showing a grabber may be useful when it isn’t apparent that a sheet can resize or when the sheet can’t dismiss interactively.

Set this value to [true](../../swift/true.md) for the system to draw a grabber in the standard system-defined location. The system automatically hides the grabber at appropriate times, like when the sheet is full screen in a compact-height size class or when another sheet presents on top of it.

## See Also

### Managing the appearance

- [prefersPageSizing](preferspagesizing.md) — A Boolean value that indicates whether the sheet sizes itself for readable content.
- [prefersEdgeAttachedInCompactHeight](prefersedgeattachedincompactheight.md) — A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [widthFollowsPreferredContentSizeWhenEdgeAttached](widthfollowspreferredcontentsizewhenedgeattached.md) — A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [preferredCornerRadius](preferredcornerradius-3mb5.md) — The corner radius that the sheet attempts to present with.
