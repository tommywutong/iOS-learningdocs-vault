---
title: 'collectionView(_:dropSessionDidEnd:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidend:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:dropsessiondidend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropdelegate/collectionview%28_%3Adropsessiondidend%3A%29.json'
content_hash: 'sha256:b8268e0f3496f7e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)

# collectionView(_:dropSessionDidEnd:)

<sub>Instance Method</sub>

Notifies you when the drag operation ends.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, dropSessionDidEnd session: any UIDropSession)
```

## Parameters

- `collectionView` — The collection view that’s tracking the dragged content.

- `session` — The drop session object containing information about the data being dragged.

## Discussion

The collection view calls this method at the conclusion of a drag that was over the collection view at one point. Use it to clean up any state information that you used to handle the drag. This method is called regardless of whether the data was actually dropped onto the collection view.

## See Also

### Tracking the drag movements

- [- collectionView:dropSessionDidUpdate:withDestinationIndexPath:](<collectionview(__dropsessiondidupdate_withdestinationindexpath_).md>) — Tells your delegate that the position of the dragged data over the collection view changed.
- [- collectionView:dropSessionDidEnter:](<collectionview(__dropsessiondidenter_).md>) — Notifies you when dragged content enters the collection view’s bounds rectangle.
- [- collectionView:dropSessionDidExit:](<collectionview(__dropsessiondidexit_).md>) — Notifies you when dragged content exits the collection view’s bounds rectangle.
