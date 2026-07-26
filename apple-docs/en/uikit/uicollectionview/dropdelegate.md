---
title: dropDelegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/dropdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/dropdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/dropdelegate.json'
content_hash: 'sha256:e9290bb461dc3c9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# dropDelegate

<sub>Instance Property</sub>

The delegate object that manages the dropping of items into the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var dropDelegate: (any UICollectionViewDropDelegate)? { get set }
```

## See Also

### Managing drop interactions

- [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md) — The interface for handling drops in a collection view.
- [hasActiveDrop](hasactivedrop.md) — A Boolean value that indicates whether the collection view is currently tracking a drop session.
- [reorderingCadence](reorderingcadence-swift.property.md) — The speed at which items in the collection view are reordered to show potential drop locations.
- [ReorderingCadence](reorderingcadence-swift.enum.md) — Constants indicating the speed at which collection view items are reorganized during a drop.
