---
title: 'collectionView(_:shouldSpringLoadItemAt:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldspringloaditemat:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldspringloaditemat:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Ashouldspringloaditemat%3Awith%3A%29.json'
content_hash: 'sha256:f51f742dbc2194b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:shouldSpringLoadItemAt:with:)

<sub>Instance Method</sub>

Determines whether the spring-loading interaction effect is displayed for the specified item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, shouldSpringLoadItemAt indexPath: IndexPath, with context: any UISpringLoadedInteractionContext) -> Bool
```

## Parameters

- `collectionView` — The collection view object notifying you of the interaction.

- `indexPath` — The index path of the item for which the spring-loading behavior applies.

- `context` — A context object containing information about the item and view on which to display the spring-loading interaction.

## Return Value

[true](../../swift/true.md) to apply the spring-loading behavior for the item or [false](../../swift/false.md) to suppress the behavior altogether.

## Discussion

If you do not implement this method, the collection view assumes a return value of [true](../../swift/true.md).
