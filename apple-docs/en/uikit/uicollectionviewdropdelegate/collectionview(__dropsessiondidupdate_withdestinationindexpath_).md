---
title: 'collectionView(_:dropSessionDidUpdate:withDestinationIndexPath:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidupdate:withdestinationindexpath:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidupdate:withdestinationindexpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropdelegate/collectionview%28_%3Adropsessiondidupdate%3Awithdestinationindexpath%3A%29.json'
content_hash: 'sha256:b71ba4ad6ebcbc28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)

# collectionView(_:dropSessionDidUpdate:withDestinationIndexPath:)

<sub>Instance Method</sub>

Tells your delegate that the position of the dragged data over the collection view changed.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, dropSessionDidUpdate session: any UIDropSession, withDestinationIndexPath destinationIndexPath: IndexPath?) -> UICollectionViewDropProposal
```

## Parameters

- `collectionView` — The collection view that’s tracking the dragged content.

- `session` — The drop session object containing information about the type of data being dragged.

- `destinationIndexPath` — The index path at which the content would be dropped.

## Return Value

Your proposal for how to handle the content if it is dropped at the specified location.

## Discussion

While the user is dragging content, the collection view calls this method repeatedly to determine how you would handle the drop if it occurred at the specified location. The collection view provides visual feedback to the user based on your proposal.

In your implementation of this method, create a [UICollectionViewDropProposal](../uicollectionviewdropproposal.md) object and use it to convey your intentions. Because this method is called repeatedly while the user drags over the table view, your implementation should return as quickly as possible.

## See Also

### Tracking the drag movements

- [- collectionView:dropSessionDidEnter:](<collectionview(__dropsessiondidenter_).md>) — Notifies you when dragged content enters the collection view’s bounds rectangle.
- [- collectionView:dropSessionDidExit:](<collectionview(__dropsessiondidexit_).md>) — Notifies you when dragged content exits the collection view’s bounds rectangle.
- [- collectionView:dropSessionDidEnd:](<collectionview(__dropsessiondidend_).md>) — Notifies you when the drag operation ends.
