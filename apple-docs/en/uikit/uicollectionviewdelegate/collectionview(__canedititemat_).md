---
title: 'collectionView(_:canEditItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:canedititemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canedititemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Acanedititemat%3A%29.json'
content_hash: 'sha256:b8fb8475b42fed75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:canEditItemAt:)

<sub>Instance Method</sub>

Determines whether the specified item is editable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, canEditItemAt indexPath: IndexPath) -> Bool
```

## Parameters

- `collectionView` — The collection view object requesting this information.

- `indexPath` — An index path locating an item in the collection view.

## Return Value

Returns [true](../../swift/true.md) if the item is editable, [false](../../swift/false.md) if it’s not. The default value is [true](../../swift/true.md).
