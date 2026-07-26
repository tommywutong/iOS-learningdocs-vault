---
title: 'collectionView(_:dragSessionWillBegin:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessionwillbegin:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessionwillbegin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdragdelegate/collectionview%28_%3Adragsessionwillbegin%3A%29.json'
content_hash: 'sha256:982465ad5331f9d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDragDelegate](../uicollectionviewdragdelegate.md)

# collectionView(_:dragSessionWillBegin:)

<sub>Instance Method</sub>

Notifies you that a drag session is about to begin for the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, dragSessionWillBegin session: any UIDragSession)
```

## Parameters

- `collectionView` — The collection view from which the drag operation originated.

- `session` — The drag session that’s beginning.

## Discussion

This method is called after it has been determined that a drag will begin and after any lift animations have occurred, but before the position of the drag changes. Use this method to perform any tasks related to the management of the drag session in your app.

Each call to this method is always balanced by a call to the [- collectionView:dragSessionDidEnd:](<collectionview(__dragsessiondidend_).md>) method.

## See Also

### Tracking the drag session

- [- collectionView:dragSessionDidEnd:](<collectionview(__dragsessiondidend_).md>) — Notifies you that a drag session ended for the collection view.
