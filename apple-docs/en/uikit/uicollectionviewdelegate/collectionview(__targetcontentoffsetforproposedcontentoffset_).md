---
title: 'collectionView(_:targetContentOffsetForProposedContentOffset:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:targetcontentoffsetforproposedcontentoffset:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:targetcontentoffsetforproposedcontentoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Atargetcontentoffsetforproposedcontentoffset%3A%29.json'
content_hash: 'sha256:12f0fa9da9e46dbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:targetContentOffsetForProposedContentOffset:)

<sub>Instance Method</sub>

Gives the delegate an opportunity to customize the content offset for layout changes and animated updates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, targetContentOffsetForProposedContentOffset proposedContentOffset: CGPoint) -> CGPoint
```

## Parameters

- `collectionView` — The collection view making the request.

- `proposedContentOffset` — The proposed point (in the coordinate space of the collection view’s content view) for the upper-left corner of the visible content. This represents the point that the collection view has calculated as the most likely value to use for the animations or layout update.

## Return Value

The content offset that you want to use instead. If you do not implement this method, the collection view uses the value in the `proposedContentOffset` parameter.

## Discussion

During layout updates, or when transitioning between layouts, the collection view calls this method to give you the opportunity to change the proposed content offset to use at the end of the animation. You might return a new value if the layout or animations might cause items to be positioned in a way that is not optimal for your design.

This method is called after the layout object’s [- targetContentOffsetForProposedContentOffset:](<../uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset_).md>) method. Implement this method in situations where you do not want to subclass your layout object to modify the content offset.

## See Also

### Handling layout changes

- [- collectionView:transitionLayoutForOldLayout:newLayout:](<collectionview(__transitionlayoutforoldlayout_newlayout_).md>) — Asks for the custom transition layout to use when moving between the specified layouts.
- [- collectionView:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:](<collectionview(__targetindexpathformoveofitemfromoriginalindexpath_atcurrentindexpath_toproposedindexpath_).md>) — Asks the delegate for the index path to use when moving an item.
