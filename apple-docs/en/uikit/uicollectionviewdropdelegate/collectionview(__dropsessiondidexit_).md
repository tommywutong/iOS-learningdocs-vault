---
title: 'collectionView(_:dropSessionDidExit:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidexit:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidexit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropdelegate/collectionview%28_%3Adropsessiondidexit%3A%29.json'
content_hash: 'sha256:350fad04b33fee63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)

# collectionView(_:dropSessionDidExit:)

<sub>Instance Method</sub>

Notifies you when dragged content exits the collection view’s bounds rectangle.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, dropSessionDidExit session: any UIDropSession)
```

## Parameters

- `collectionView` — The collection view that was tracking the dragged content.

- `session` — The drop session object containing information about the type of data being dragged.

## Discussion

UIKit calls this method when dragged content exits the bounds rectangle of the specified collection view. The method isn’t called again until the dragged content enters the collection view’s bounds (triggering a call to the [- collectionView:dropSessionDidEnter:](<collectionview(__dropsessiondidenter_).md>) method) and exits again.

Use this method to clean up any state information that you configured in your [- collectionView:dropSessionDidEnter:](<collectionview(__dropsessiondidenter_).md>) method.

## See Also

### Tracking the drag movements

- [- collectionView:dropSessionDidUpdate:withDestinationIndexPath:](<collectionview(__dropsessiondidupdate_withdestinationindexpath_).md>) — Tells your delegate that the position of the dragged data over the collection view changed.
- [- collectionView:dropSessionDidEnter:](<collectionview(__dropsessiondidenter_).md>) — Notifies you when dragged content enters the collection view’s bounds rectangle.
- [- collectionView:dropSessionDidEnd:](<collectionview(__dropsessiondidend_).md>) — Notifies you when the drag operation ends.
