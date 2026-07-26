---
title: UICollectionView.ReorderingCadence
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionview/reorderingcadence-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/reorderingcadence-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/reorderingcadence-swift.enum.json'
content_hash: 'sha256:58c6df43e6cf71a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# UICollectionView.ReorderingCadence

<sub>Enumeration</sub>

Constants indicating the speed at which collection view items are reorganized during a drop.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum ReorderingCadence
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UICollectionViewReorderingCadenceImmediate](reorderingcadence-swift.enum/immediate.md) — Items are reordered into place immediately.
- [UICollectionViewReorderingCadenceFast](reorderingcadence-swift.enum/fast.md) — Items are reordered quickly, but with a short delay.
- [UICollectionViewReorderingCadenceSlow](reorderingcadence-swift.enum/slow.md) — Items are reordered after a delay.

### Initializers

- [init(rawValue:)](<reorderingcadence-swift.enum/init(rawvalue_).md>)

## See Also

### Managing drop interactions

- [dropDelegate](dropdelegate.md) — The delegate object that manages the dropping of items into the collection view.
- [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md) — The interface for handling drops in a collection view.
- [hasActiveDrop](hasactivedrop.md) — A Boolean value that indicates whether the collection view is currently tracking a drop session.
- [reorderingCadence](reorderingcadence-swift.property.md) — The speed at which items in the collection view are reordered to show potential drop locations.
