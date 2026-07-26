---
title: 'collectionView(_:willDisplay:forItemAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:willdisplay:foritemat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:willdisplay:foritemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Awilldisplay%3Aforitemat%3A%29.json'
content_hash: 'sha256:3ea02ab6dfe3cd74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:willDisplay:forItemAt:)

<sub>Instance Method</sub>

Tells the delegate that the specified cell is about to be displayed in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, willDisplay cell: UICollectionViewCell, forItemAt indexPath: IndexPath)
```

## Parameters

- `collectionView` — The collection view object that is adding the cell.

- `cell` — The cell object being added.

- `indexPath` — The index path of the data item that the cell represents.

## Discussion

The collection view calls this method before adding a cell to its content. Use this method to detect cell additions, as opposed to monitoring the cell itself to see when it appears.

## See Also

### Tracking the addition and removal of views

- [- collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:](<collectionview(__willdisplaysupplementaryview_forelementkind_at_).md>) — Tells the delegate that the specified supplementary view is about to be displayed in the collection view.
- [- collectionView:didEndDisplayingCell:forItemAtIndexPath:](<collectionview(__didenddisplaying_foritemat_).md>) — Tells the delegate that the specified cell was removed from the collection view.
- [- collectionView:didEndDisplayingSupplementaryView:forElementOfKind:atIndexPath:](<collectionview(__didenddisplayingsupplementaryview_forelementofkind_at_).md>) — Tells the delegate that the specified supplementary view was removed from the collection view.
