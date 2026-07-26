---
title: pinToVisibleBounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutboundarysupplementaryitem/pintovisiblebounds
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutboundarysupplementaryitem/pintovisiblebounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutboundarysupplementaryitem/pintovisiblebounds.json'
content_hash: 'sha256:0e555117fcfaf9ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutBoundarySupplementaryItem](../nscollectionlayoutboundarysupplementaryitem.md)

# pinToVisibleBounds

<sub>Instance Property</sub>

A Boolean value that indicates whether a header or footer is pinned to the top or bottom visible boundary of the section or layout it’s attached to.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var pinToVisibleBounds: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md), which means that the boundary supplementary item (header or footer) remains in its original position during scrolling, and moves offscreen as its section or layout scrolls. Set the value of this property to [true](../../swift/true.md) to pin the boundary supplementary item to the visible bounds of the section or layout it’s attached to. This way, the boundary supplementary item is shown while any portion of the section or layout it’s attached to is visible.
