---
title: orthogonalScrollingBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutsection/orthogonalscrollingbehavior
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/orthogonalscrollingbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutsection/orthogonalscrollingbehavior.json'
content_hash: 'sha256:6dee121942f66627'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutSection](../nscollectionlayoutsection.md)

# orthogonalScrollingBehavior

<sub>Instance Property</sub>

The section’s scrolling behavior in relation to the main layout axis.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var orthogonalScrollingBehavior: UICollectionLayoutSectionOrthogonalScrollingBehavior { get set }
```

## Discussion

The default value of this property is [UICollectionLayoutSectionOrthogonalScrollingBehaviorNone](../uicollectionlayoutsectionorthogonalscrollingbehavior/none.md), which means the section lays out its content along the main axis of its layout, defined by the layout configuration’s [scrollDirection](../uicollectionviewcompositionallayoutconfiguration/scrolldirection.md) property. Set a different value for this property to get the section to lay out its content orthogonally to the main layout axis.

## See Also

### Specifying scrolling behavior

- [orthogonalScrollingProperties](orthogonalscrollingproperties.md) — The section’s orthogonal scrolling properties.
- [UICollectionLayoutSectionOrthogonalScrollingProperties](../uicollectionlayoutsectionorthogonalscrollingproperties.md) — An object that specifies properties for a layout section that scrolls orthogonally in relation to the main layout axis.
