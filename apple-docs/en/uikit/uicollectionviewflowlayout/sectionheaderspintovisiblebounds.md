---
title: sectionHeadersPinToVisibleBounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/sectionheaderspintovisiblebounds
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/sectionheaderspintovisiblebounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/sectionheaderspintovisiblebounds.json'
content_hash: 'sha256:c5fa4d5226bc0de6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# sectionHeadersPinToVisibleBounds

<sub>Instance Property</sub>

A Boolean value that indicates whether headers pin to the top of the collection view bounds during scrolling.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sectionHeadersPinToVisibleBounds: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md), section header views scroll with content until they reach the top of the screen, at which point they are pinned to the upper bounds of the collection view. Each new header view that scrolls to the top of the screen pushes the previously pinned header view offscreen.

The default value of this property is [false](../../swift/false.md).

## See Also

### Pinning headers and footers

- [sectionFootersPinToVisibleBounds](sectionfooterspintovisiblebounds.md) — A Boolean value that indicates whether footers pin to the bottom of the collection view bounds during scrolling.
