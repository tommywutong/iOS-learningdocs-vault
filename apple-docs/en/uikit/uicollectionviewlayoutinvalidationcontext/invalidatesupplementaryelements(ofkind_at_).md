---
title: 'invalidateSupplementaryElements(ofKind:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements(ofkind:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatesupplementaryelements%28ofkind%3Aat%3A%29.json'
content_hash: 'sha256:793a19d0de0a38a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# invalidateSupplementaryElements(ofKind:at:)

<sub>Instance Method</sub>

Adds the supplementary views at the specified index paths to the list of invalid items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateSupplementaryElements(ofKind elementKind: String, at indexPaths: [IndexPath])
```

## Parameters

- `elementKind` — A string that identifies the type of the supplementary views. This parameter must not be `nil`.

- `indexPaths` — An array of [NSIndexPath](../../foundation/nsindexpath.md) objects. Each index path represents a supplementary view of the given kind whose layout needs to be recomputed.

## Discussion

Call this method to identify the specific supplementary views of your layout that require updates. The views you specify are added to the dictionary in the [invalidatedSupplementaryIndexPaths](invalidatedsupplementaryindexpaths.md) property. All of the views you specify should be of the type that you specified in the `elementKind` parameter. If you call this method two or more times with the same value for the `elementKind` parameter, this method merges the new index paths with the ones previously specified.

## See Also

### Invalidating Specific Items

- [- invalidateItemsAtIndexPaths:](<invalidateitems(at_).md>) — Adds the cells at the specified index paths to the list of invalid items.
- [- invalidateDecorationElementsOfKind:atIndexPaths:](<invalidatedecorationelements(ofkind_at_).md>) — Adds the decoration views at the specified index paths to the list of invalid items.
- [invalidatedItemIndexPaths](invalidateditemindexpaths.md) — An array of index paths representing the cells that were invalidated.
- [invalidatedSupplementaryIndexPaths](invalidatedsupplementaryindexpaths.md) — A dictionary that identifies the supplementary views that were invalidated.
- [invalidatedDecorationIndexPaths](invalidateddecorationindexpaths.md) — A dictionary that identifies the decoration views that were invalidated.
