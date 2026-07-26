---
title: invalidatedItemIndexPaths
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateditemindexpaths
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateditemindexpaths'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/invalidateditemindexpaths.json'
content_hash: 'sha256:5e8b854cd13c4824'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# invalidatedItemIndexPaths

<sub>Instance Property</sub>

An array of index paths representing the cells that were invalidated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var invalidatedItemIndexPaths: [IndexPath]? { get }
```

## Discussion

The array contains zero or more [NSIndexPath](../../foundation/nsindexpath.md) objects, each of which represents a cell whose layout changed.

## See Also

### Invalidating Specific Items

- [- invalidateItemsAtIndexPaths:](<invalidateitems(at_).md>) — Adds the cells at the specified index paths to the list of invalid items.
- [- invalidateSupplementaryElementsOfKind:atIndexPaths:](<invalidatesupplementaryelements(ofkind_at_).md>) — Adds the supplementary views at the specified index paths to the list of invalid items.
- [- invalidateDecorationElementsOfKind:atIndexPaths:](<invalidatedecorationelements(ofkind_at_).md>) — Adds the decoration views at the specified index paths to the list of invalid items.
- [invalidatedSupplementaryIndexPaths](invalidatedsupplementaryindexpaths.md) — A dictionary that identifies the supplementary views that were invalidated.
- [invalidatedDecorationIndexPaths](invalidateddecorationindexpaths.md) — A dictionary that identifies the decoration views that were invalidated.
