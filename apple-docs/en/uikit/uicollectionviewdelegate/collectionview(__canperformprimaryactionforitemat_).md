---
title: 'collectionView(_:canPerformPrimaryActionForItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:canperformprimaryactionforitemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:canperformprimaryactionforitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Acanperformprimaryactionforitemat%3A%29.json'
content_hash: 'sha256:dcc2940e396dcf67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:canPerformPrimaryActionForItemAt:)

<sub>Instance Method</sub>

Asks the delegate whether to perform a primary action for the cell at the specified index path.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, canPerformPrimaryActionForItemAt indexPath: IndexPath) -> Bool
```

## Parameters

- `collectionView` — The collection view object asking whether to perform a primary action.

- `indexPath` — The index path of the cell.

## Return Value

[true](../../swift/true.md) if the primary action can be performed; otherwise, [false](../../swift/false.md). If you don’t implement this method, the default return value is [true](../../swift/true.md) when the collection view isn’t in an editing state, and [false](../../swift/false.md) when it is.

## Discussion

Primary actions allow you to distinguish between a distinct user action and a change in selection (like a focus change or other indirect selection change). A primary action occurs when a person selects a single cell without extending an existing selection.

UIKit calls this method before [- collectionView:performPrimaryActionForItemAtIndexPath:](<collectionview(__performprimaryactionforitemat_).md>).

## See Also

### Managing actions for cells

- [- collectionView:performPrimaryActionForItemAtIndexPath:](<collectionview(__performprimaryactionforitemat_).md>) — Tells the delegate to perform the primary action for the cell at the specified index path.
