---
title: invalidateFlowLayoutDelegateMetrics
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutdelegatemetrics
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutdelegatemetrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewflowlayoutinvalidationcontext/invalidateflowlayoutdelegatemetrics.json'
content_hash: 'sha256:5b9b012f53ac2db9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewFlowLayoutInvalidationContext](../uicollectionviewflowlayoutinvalidationcontext.md)

# invalidateFlowLayoutDelegateMetrics

<sub>Instance Property</sub>

A Boolean indicating whether to recompute the size of items and views in the layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var invalidateFlowLayoutDelegateMetrics: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). Set this property to [true](../../swift/true.md) if you’re invalidating the layout because of changes to the size of any items.

When this property is set to [true](../../swift/true.md), the flow layout object recomputes the size of its items and views, querying the delegate object as needed for that information.

## See Also

### Specifying what to invalidate

- [invalidateFlowLayoutAttributes](invalidateflowlayoutattributes.md) — A Boolean indicating whether to recompute the layout attributes for items and views in the layout.
