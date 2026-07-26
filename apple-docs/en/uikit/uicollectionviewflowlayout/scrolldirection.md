---
title: scrollDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayout/scrolldirection
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout/scrolldirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayout/scrolldirection.json'
content_hash: 'sha256:2ccb69dda4a07c82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayout](../uicollectionviewflowlayout.md)

# scrollDirection

<sub>Instance Property</sub>

The scroll direction of the grid.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var scrollDirection: UICollectionView.ScrollDirection { get set }
```

## Discussion

The grid layout scrolls along one axis only, either horizontally or vertically. For the non scrolling axis, the width of the collection view in that dimension serves as starting width of the content.

The default value of this property is [UICollectionViewScrollDirectionVertical](../uicollectionview/scrolldirection/vertical.md).

## See Also

### Configuring the scroll direction

- [ScrollDirection](../uicollectionview/scrolldirection.md) — Constants that indicate the direction of scrolling for the layout.
