---
title: 'invalidateItems(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateitems(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateitems(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateitems%28at%3A%29.json'
content_hash: 'sha256:0e060587faa6f408'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# invalidateItems(at:)

<sub>Instance Method</sub>

Adds the cells at the specified index paths to the list of invalid items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateItems(at indexPaths: [IndexPath])
```

## Parameters

- `indexPaths` — An array of [NSIndexPath](../../foundation/nsindexpath.md) objects. Each index path represents a cell whose layout needs to be recomputed.

## Discussion

Call this method to identify the specific cells of your layout that require updates. The cells you specify are added to the array in the [invalidatedItemIndexPaths](invalidateditemindexpaths.md) property.

## See Also

### Invalidating Specific Items

- [- invalidateSupplementaryElementsOfKind:atIndexPaths:](<invalidatesupplementaryelements(ofkind_at_).md>) — Adds the supplementary views at the specified index paths to the list of invalid items.
- [- invalidateDecorationElementsOfKind:atIndexPaths:](<invalidatedecorationelements(ofkind_at_).md>) — Adds the decoration views at the specified index paths to the list of invalid items.
- [invalidatedItemIndexPaths](invalidateditemindexpaths.md) — An array of index paths representing the cells that were invalidated.
- [invalidatedSupplementaryIndexPaths](invalidatedsupplementaryindexpaths.md) — A dictionary that identifies the supplementary views that were invalidated.
- [invalidatedDecorationIndexPaths](invalidateddecorationindexpaths.md) — A dictionary that identifies the decoration views that were invalidated.
