---
title: invalidatedSupplementaryIndexPaths
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidatedsupplementaryindexpaths.json'
content_hash: 'sha256:8133341f120b2c5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# invalidatedSupplementaryIndexPaths

<sub>Instance Property</sub>

A dictionary that identifies the supplementary views that were invalidated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var invalidatedSupplementaryIndexPaths: [String : [IndexPath]]? { get }
```

## Discussion

The keys in this dictionary are the element kind strings of the invalid supplementary views. The value for each key is an array of [NSIndexPath](../../foundation/nsindexpath.md) objects indicating which specific supplementary views have layout changes.

## See Also

### Invalidating Specific Items

- [- invalidateItemsAtIndexPaths:](<invalidateitems(at_).md>) — Adds the cells at the specified index paths to the list of invalid items.
- [- invalidateSupplementaryElementsOfKind:atIndexPaths:](<invalidatesupplementaryelements(ofkind_at_).md>) — Adds the supplementary views at the specified index paths to the list of invalid items.
- [- invalidateDecorationElementsOfKind:atIndexPaths:](<invalidatedecorationelements(ofkind_at_).md>) — Adds the decoration views at the specified index paths to the list of invalid items.
- [invalidatedItemIndexPaths](invalidateditemindexpaths.md) — An array of index paths representing the cells that were invalidated.
- [invalidatedDecorationIndexPaths](invalidateddecorationindexpaths.md) — A dictionary that identifies the decoration views that were invalidated.
