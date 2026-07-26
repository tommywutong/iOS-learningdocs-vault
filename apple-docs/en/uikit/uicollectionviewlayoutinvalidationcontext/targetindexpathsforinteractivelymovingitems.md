---
title: targetIndexPathsForInteractivelyMovingItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutinvalidationcontext/targetindexpathsforinteractivelymovingitems
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/targetindexpathsforinteractivelymovingitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/targetindexpathsforinteractivelymovingitems.json'
content_hash: 'sha256:5ce5bd94c44ff9dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# targetIndexPathsForInteractivelyMovingItems

<sub>Instance Property</sub>

An array of index paths representing the new location of moving items in the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var targetIndexPathsForInteractivelyMovingItems: [IndexPath]? { get }
```

## Discussion

This property is filled when an interactive move is in progress or has just ended. Use this property together with the [previousIndexPathsForInteractivelyMovingItems](previousindexpathsforinteractivelymovingitems.md) property to determine what changes you need to make to the affected items. For most other updates, the value of this property is `nil`.

## See Also

### Invalidating the Order of Items

- [previousIndexPathsForInteractivelyMovingItems](previousindexpathsforinteractivelymovingitems.md) — An array of index paths representing the previous location of moving items in the collection view.
- [interactiveMovementTarget](interactivemovementtarget.md) — The current point used to determine the placement of moving items.
