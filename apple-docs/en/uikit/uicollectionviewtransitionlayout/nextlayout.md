---
title: nextLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewtransitionlayout/nextlayout
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/nextlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewtransitionlayout/nextlayout.json'
content_hash: 'sha256:9c62f92447e379b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewTransitionLayout](../uicollectionviewtransitionlayout.md)

# nextLayout

<sub>Instance Property</sub>

The collection view’s new layout object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var nextLayout: UICollectionViewLayout { get }
```

## Discussion

This object provides the layout attributes representing the new position of items in the collection view. If the transition completes as expected, the collection view animates its items to the positions provided by this object.

## See Also

### Accessing the layout objects

- [currentLayout](currentlayout.md) — The collection view’s current layout object.
