---
title: prefersEdgeAttachedInCompactHeight
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/prefersedgeattachedincompactheight
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersedgeattachedincompactheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/prefersedgeattachedincompactheight.json'
content_hash: 'sha256:cdd78026593886be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# prefersEdgeAttachedInCompactHeight

<sub>Instance Property</sub>

A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var prefersEdgeAttachedInCompactHeight: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md), which means the sheet defaults to a full screen appearance at compact height. Set this value to [true](../../swift/true.md) to use an alternate appearance in a compact-height size class, causing the sheet to only attach to the screen on its bottom edge.

## See Also

### Managing the appearance

- [prefersGrabberVisible](prefersgrabbervisible.md) — A Boolean value that determines whether the sheet shows a grabber at the top.
- [prefersPageSizing](preferspagesizing.md) — A Boolean value that indicates whether the sheet sizes itself for readable content.
- [widthFollowsPreferredContentSizeWhenEdgeAttached](widthfollowspreferredcontentsizewhenedgeattached.md) — A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [preferredCornerRadius](preferredcornerradius-3mb5.md) — The corner radius that the sheet attempts to present with.
