---
title: interactiveMovementTarget
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutinvalidationcontext/interactivemovementtarget
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/interactivemovementtarget'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/interactivemovementtarget.json'
content_hash: 'sha256:b02acebe25b6facb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# interactiveMovementTarget

<sub>Instance Property</sub>

The current point used to determine the placement of moving items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var interactiveMovementTarget: CGPoint { get }
```

## Discussion

This property is filled when an interactive move is in progress or has just ended. The value represents the point that was used to determine the new index paths in the [targetIndexPathsForInteractivelyMovingItems](targetindexpathsforinteractivelymovingitems.md) property. You can use this point as needed to calculate the position of items in your layout.

## See Also

### Invalidating the Order of Items

- [previousIndexPathsForInteractivelyMovingItems](previousindexpathsforinteractivelymovingitems.md) — An array of index paths representing the previous location of moving items in the collection view.
- [targetIndexPathsForInteractivelyMovingItems](targetindexpathsforinteractivelymovingitems.md) — An array of index paths representing the new location of moving items in the collection view.
