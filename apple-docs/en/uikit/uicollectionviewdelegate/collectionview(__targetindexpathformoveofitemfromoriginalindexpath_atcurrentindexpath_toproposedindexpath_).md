---
title: 'collectionView(_:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:targetindexpathformoveofitemfromoriginalindexpath:atcurrentindexpath:toproposedindexpath:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:targetindexpathformoveofitemfromoriginalindexpath:atcurrentindexpath:toproposedindexpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Atargetindexpathformoveofitemfromoriginalindexpath%3Aatcurrentindexpath%3Atoproposedindexpath%3A%29.json'
content_hash: 'sha256:fad81e792c17ff4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:)

<sub>Instance Method</sub>

Asks the delegate for the index path to use when moving an item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, targetIndexPathForMoveOfItemFromOriginalIndexPath originalIndexPath: IndexPath, atCurrentIndexPath currentIndexPath: IndexPath, toProposedIndexPath proposedIndexPath: IndexPath) -> IndexPath
```

## Parameters

- `collectionView` — The collection view making the request.

- `originalIndexPath` — The item’s original index path. This value doesn’t change as the user interactively moves the item.

- `currentIndexPath` — The item’s current index path. This value changes as the user interactively moves the item, reflecting the item’s current position in the collection view.

- `proposedIndexPath` — The proposed index path of the item.

## Return Value

The index path you want to use for the item. If you don’t implement this method, the collection view uses the index path in the `proposedIndexPath` parameter.

## Discussion

During the interactive moving of an item, the collection view calls this method to see if you want to provide a different index path than the proposed path. You might use this method to prevent the user from dropping the item in an invalid location. For example, you might prevent the user from dropping the item in a specific section.

## See Also

### Handling layout changes

- [- collectionView:transitionLayoutForOldLayout:newLayout:](<collectionview(__transitionlayoutforoldlayout_newlayout_).md>) — Asks for the custom transition layout to use when moving between the specified layouts.
- [- collectionView:targetContentOffsetForProposedContentOffset:](<collectionview(__targetcontentoffsetforproposedcontentoffset_).md>) — Gives the delegate an opportunity to customize the content offset for layout changes and animated updates.
