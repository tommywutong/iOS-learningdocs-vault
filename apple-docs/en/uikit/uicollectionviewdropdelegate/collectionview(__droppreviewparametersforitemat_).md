---
title: 'collectionView(_:dropPreviewParametersForItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:droppreviewparametersforitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:droppreviewparametersforitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropdelegate/collectionview%28_%3Adroppreviewparametersforitemat%3A%29.json'
content_hash: 'sha256:5f899286af9db1e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)

# collectionView(_:dropPreviewParametersForItemAt:)

<sub>Instance Method</sub>

Returns custom information about how to display the item at the specified location during the drop.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, dropPreviewParametersForItemAt indexPath: IndexPath) -> UIDragPreviewParameters?
```

## Parameters

- `collectionView` — The collection view that’s the destination for the drop.

- `indexPath` — The index path in the collection view to insert the item.

## Return Value

Drop parameters that indicate how to display the item during the drop.

## Discussion

Use this method to customize the appearance of the item during drops. If you don’t implement this method or if you implement it and return `nil`, the collection view uses the cell’s visible bounds to create the preview.
