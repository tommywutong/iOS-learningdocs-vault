---
title: dragDelegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/dragdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/dragdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/dragdelegate.json'
content_hash: 'sha256:68b72c32e96991cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# dragDelegate

<sub>Instance Property</sub>

The delegate object that manages the dragging of items from the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var dragDelegate: (any UICollectionViewDragDelegate)? { get set }
```

## See Also

### Managing drag interactions

- [UICollectionViewDragDelegate](../uicollectionviewdragdelegate.md) — The interface for initiating drags from a collection view.
- [hasActiveDrag](hasactivedrag.md) — A Boolean value that indicates whether items were lifted from the collection view and have not yet been dropped.
- [dragInteractionEnabled](draginteractionenabled.md) — A Boolean value that indicates whether the collection view supports dragging content.
