---
title: 'collectionView(_:dragSessionDidEnd:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessiondidend:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:dragsessiondidend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdragdelegate/collectionview%28_%3Adragsessiondidend%3A%29.json'
content_hash: 'sha256:d87afd3490740768'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDragDelegate](../uicollectionviewdragdelegate.md)

# collectionView(_:dragSessionDidEnd:)

<sub>Instance Method</sub>

Notifies you that a drag session ended for the collection view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, dragSessionDidEnd session: any UIDragSession)
```

## Parameters

- `collectionView` — The collection view from which the drag operation originated.

- `session` — The drag session that ended.

## Discussion

This method is called after the drag session ended, usually because the content was dropped but possibly because the drag was terminated. Use this method to close out any tasks related to the management of the drag session in your app.

Each call to this method is always balanced by a call to the [- collectionView:dragSessionWillBegin:](<collectionview(__dragsessionwillbegin_).md>) method.

## See Also

### Tracking the drag session

- [- collectionView:dragSessionWillBegin:](<collectionview(__dragsessionwillbegin_).md>) — Notifies you that a drag session is about to begin for the collection view.
