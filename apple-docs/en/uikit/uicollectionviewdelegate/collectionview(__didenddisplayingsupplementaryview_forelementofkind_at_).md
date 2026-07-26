---
title: 'collectionView(_:didEndDisplayingSupplementaryView:forElementOfKind:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:didenddisplayingsupplementaryview:forelementofkind:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:didenddisplayingsupplementaryview:forelementofkind:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Adidenddisplayingsupplementaryview%3Aforelementofkind%3Aat%3A%29.json'
content_hash: 'sha256:3bb24ee3274c80b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:didEndDisplayingSupplementaryView:forElementOfKind:at:)

<sub>Instance Method</sub>

Tells the delegate that the specified supplementary view was removed from the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, didEndDisplayingSupplementaryView view: UICollectionReusableView, forElementOfKind elementKind: String, at indexPath: IndexPath)
```

## Parameters

- `collectionView` — The collection view object that removed the supplementary view.

- `view` — The view that was removed.

- `elementKind` — The type of the supplementary view. This string is defined by the layout that presents the view.

- `indexPath` — The index path of the data item that the supplementary view represented.

## Discussion

Use this method to detect when a supplementary view is removed from a collection view, as opposed to monitoring the view itself to see when it appears or disappears.

## See Also

### Tracking the addition and removal of views

- [- collectionView:willDisplayCell:forItemAtIndexPath:](<collectionview(__willdisplay_foritemat_).md>) — Tells the delegate that the specified cell is about to be displayed in the collection view.
- [- collectionView:willDisplaySupplementaryView:forElementKind:atIndexPath:](<collectionview(__willdisplaysupplementaryview_forelementkind_at_).md>) — Tells the delegate that the specified supplementary view is about to be displayed in the collection view.
- [- collectionView:didEndDisplayingCell:forItemAtIndexPath:](<collectionview(__didenddisplaying_foritemat_).md>) — Tells the delegate that the specified cell was removed from the collection view.
