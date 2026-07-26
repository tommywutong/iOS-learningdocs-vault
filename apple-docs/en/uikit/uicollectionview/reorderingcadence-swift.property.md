---
title: reorderingCadence
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/reorderingcadence-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/reorderingcadence-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/reorderingcadence-swift.property.json'
content_hash: 'sha256:8389c44ea469b095'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# reorderingCadence

<sub>Instance Property</sub>

The speed at which items in the collection view are reordered to show potential drop locations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var reorderingCadence: UICollectionView.ReorderingCadence { get set }
```

## Discussion

The default value in this property is [UICollectionViewReorderingCadenceImmediate](reorderingcadence-swift.enum/immediate.md). You might specify a slower cadence when you want to prevent the reordering of items from being a distraction to the user. For example, you might slow it down if immediate reordering makes it more difficult to drop items at the correct location.

## See Also

### Managing drop interactions

- [dropDelegate](dropdelegate.md) — The delegate object that manages the dropping of items into the collection view.
- [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md) — The interface for handling drops in a collection view.
- [hasActiveDrop](hasactivedrop.md) — A Boolean value that indicates whether the collection view is currently tracking a drop session.
- [ReorderingCadence](reorderingcadence-swift.enum.md) — Constants indicating the speed at which collection view items are reorganized during a drop.
