---
title: currentLayout
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewtransitionlayout/currentlayout
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/currentlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewtransitionlayout/currentlayout.json'
content_hash: 'sha256:5d12f9d26f278ff6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewTransitionLayout](../uicollectionviewtransitionlayout.md)

# currentLayout

<sub>Instance Property</sub>

The collection view’s current layout object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var currentLayout: UICollectionViewLayout { get }
```

## Discussion

This object provides the layout attributes representing the initial position of items in the collection view. If you ultimately cancel the transition, the collection view animates its items back to the positions provided by this object.

## See Also

### Accessing the layout objects

- [nextLayout](nextlayout.md) — The collection view’s new layout object.
