---
title: 'collectionView(_:canHandle:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:canhandle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate/collectionview(_:canhandle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdropdelegate/collectionview%28_%3Acanhandle%3A%29.json'
content_hash: 'sha256:17c1b6b4c032941e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDropDelegate](../uicollectionviewdropdelegate.md)

# collectionView(_:canHandle:)

<sub>Instance Method</sub>

Asks your delegate whether the collection view can accept a drop with the specified type of data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, canHandle session: any UIDropSession) -> Bool
```

## Parameters

- `collectionView` — The collection view that’s attempting to handle the drop.

- `session` — The drop session object containing information about the type of data being dragged.

## Return Value

[true](../../swift/true.md) if the collection view can accept the dragged data or [false](../../swift/false.md) if it cannot.

## Discussion

Implement this method when you want to dynamically determine whether to accept dropped data in your collection view. In your implementation, check the type of the dragged data and return a Boolean value indicating whether you can accept the drop. For example, you might call the [- hasItemsConformingToTypeIdentifiers:](<../uidragdropsession/hasitemsconforming(totypeidentifiers_).md>) method of the session object to determine whether it contains data that your app can accept.

If you don’t implement this method, the collection view assumes a return value of [true](../../swift/true.md). If you return [false](../../swift/false.md) from this method, the collection view doesn’t call any more methods of your drop delegate for the given session.
