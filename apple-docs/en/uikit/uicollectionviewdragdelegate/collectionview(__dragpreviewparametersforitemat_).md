---
title: 'collectionView(_:dragPreviewParametersForItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragpreviewparametersforitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragpreviewparametersforitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdragdelegate/collectionview%28_%3Adragpreviewparametersforitemat%3A%29.json'
content_hash: 'sha256:c0b885720b76840f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDragDelegate](../uicollectionviewdragdelegate.md)

# collectionView(_:dragPreviewParametersForItemAt:)

<sub>Instance Method</sub>

Returns custom information about how to display the item at the specified location during the drag.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, dragPreviewParametersForItemAt indexPath: IndexPath) -> UIDragPreviewParameters?
```

## Parameters

- `collectionView` — The collection view from which the drag operation originated.

- `indexPath` — The index path of the item being dragged.

## Return Value

Drag parameters that indicate how to display the cell’s content during a drag.

## Discussion

Use this method to customize the appearance of the item during drags. If you don’t implement this method or if you implement it and return `nil`, the collection view uses the cell’s visible bounds to create the preview.

In your implementation, create a [UIDragPreviewParameters](../uidragpreviewparameters.md) object and update the preview information for the specified item. Use the parameters to specify the portion of the cell that you want to be included in the drag preview or to change the background color drawn beneath your cell.
