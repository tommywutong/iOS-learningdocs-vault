---
title: contentOffsetAdjustment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutinvalidationcontext/contentoffsetadjustment
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/contentoffsetadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/contentoffsetadjustment.json'
content_hash: 'sha256:f97928a88d591480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# contentOffsetAdjustment

<sub>Instance Property</sub>

The delta value to be applied to the collection view’s content offset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentOffsetAdjustment: CGPoint { get set }
```

## Discussion

Use this property to update the content offset of the collection view. The default value of this property is [CGPointZero](../../coregraphics/cgpointzero.md). Changing the value causes the collection view to add the specified x and y values to its [contentOffset](../uiscrollview/contentoffset.md) property. Thus, positive values increase the content offset and negative values decrease it.

## See Also

### Invalidating the Content Area

- [contentSizeAdjustment](contentsizeadjustment.md) — The delta value to be applied to the collection view’s content size.
