---
title: 'collectionView(_:dropSessionDidEnter:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidenter:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidenter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropdelegate/collectionview%28_%3Adropsessiondidenter%3A%29.json'
content_hash: 'sha256:b5f843cd564886f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)

# collectionView(_:dropSessionDidEnter:)

<sub>Instance Method</sub>

Notifies you when dragged content enters the collection view’s bounds rectangle.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, dropSessionDidEnter session: any UIDropSession)
```

## Parameters

- `collectionView` — The collection view that’s tracking the dragged content.

- `session` — The drop session object containing information about the type of data being dragged.

## Discussion

The collection view calls this method when dragged content enters its bounds rectangle. The method isn’t called again until the dragged content exits the collection view’s bounds (triggering a call to the [- collectionView:dropSessionDidExit:](<collectionview(__dropsessiondidexit_).md>) method) and enters again.

Use this method to perform any one-time setup associated with tracking dragged content over the collection view.

## See Also

### Tracking the drag movements

- [- collectionView:dropSessionDidUpdate:withDestinationIndexPath:](<collectionview(__dropsessiondidupdate_withdestinationindexpath_).md>) — Tells your delegate that the position of the dragged data over the collection view changed.
- [- collectionView:dropSessionDidExit:](<collectionview(__dropsessiondidexit_).md>) — Notifies you when dragged content exits the collection view’s bounds rectangle.
- [- collectionView:dropSessionDidEnd:](<collectionview(__dropsessiondidend_).md>) — Notifies you when the drag operation ends.
