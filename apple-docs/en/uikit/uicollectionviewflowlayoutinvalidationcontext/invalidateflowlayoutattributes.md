---
title: invalidateFlowLayoutAttributes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutattributes.json'
content_hash: 'sha256:47f3a0d146c61966'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayoutInvalidationContext](../uicollectionviewflowlayoutinvalidationcontext.md)

# invalidateFlowLayoutAttributes

<sub>Instance Property</sub>

A Boolean indicating whether to recompute the layout attributes for items and views in the layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var invalidateFlowLayoutAttributes: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). Set this property to [true](../../swift/true.md) if there are changes to the position of items on the screen. For example, the flow layout object sets this property to [true](../../swift/true.md) when the collection view’s bounds change in a way that affects the number of items in a column or row.

When this property is set to [true](../../swift/true.md), the flow layout object recomputes the layout attributes for its items and views. If the [invalidateFlowLayoutDelegateMetrics](invalidateflowlayoutdelegatemetrics.md) property is set to [false](../../swift/false.md) it recomputes this information without asking for new size information.

## See Also

### Specifying what to invalidate

- [invalidateFlowLayoutDelegateMetrics](invalidateflowlayoutdelegatemetrics.md) — A Boolean indicating whether to recompute the size of items and views in the layout.
