---
title: 'collectionView(_:transitionLayoutForOldLayout:newLayout:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewdelegate/collectionview(_:transitionlayoutforoldlayout:newlayout:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:transitionlayoutforoldlayout:newlayout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewdelegate/collectionview%28_%3Atransitionlayoutforoldlayout%3Anewlayout%3A%29.json'
content_hash: 'sha256:811af236a532c4a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewDelegate](../uicollectionviewdelegate.md)

# collectionView(_:transitionLayoutForOldLayout:newLayout:)

<sub>Instance Method</sub>

Asks for the custom transition layout to use when moving between the specified layouts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func collectionView(_ collectionView: UICollectionView, transitionLayoutForOldLayout fromLayout: UICollectionViewLayout, newLayout toLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout
```

## Parameters

- `collectionView` — The collection view whose layout object is changing.

- `fromLayout` — The current layout of the collection view. This is the starting point for the transition.

- `toLayout` — The new layout for the collection view.

## Return Value

The collection view transition layout object to use to perform the transition.

## Discussion

Implement this method if you want to return a custom [UICollectionViewTransitionLayout](../uicollectionviewtransitionlayout.md) object for use during the transition. A transition layout object lets you customize the behavior of cells and decoration views when transitioning from one layout to the next. Normally, transitioning between layouts causes items to animate directly from their current locations to their new locations. With a transition layout object, you can have objects follow a non linear path, use a different timing algorithm, or move according to incoming touch events.

If your delegate does not implement this method, the collection view creates a standard [UICollectionViewTransitionLayout](../uicollectionviewtransitionlayout.md) object and uses that object to manage the transition.

## See Also

### Handling layout changes

- [- collectionView:targetContentOffsetForProposedContentOffset:](<collectionview(__targetcontentoffsetforproposedcontentoffset_).md>) — Gives the delegate an opportunity to customize the content offset for layout changes and animated updates.
- [- collectionView:targetIndexPathForMoveOfItemFromOriginalIndexPath:atCurrentIndexPath:toProposedIndexPath:](<collectionview(__targetindexpathformoveofitemfromoriginalindexpath_atcurrentindexpath_toproposedindexpath_).md>) — Asks the delegate for the index path to use when moving an item.
