---
title: contentSizeAdjustment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayoutinvalidationcontext/contentsizeadjustment
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/contentsizeadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayoutinvalidationcontext/contentsizeadjustment.json'
content_hash: 'sha256:3ccd98882fe9953c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayoutInvalidationContext](../uicollectionviewlayoutinvalidationcontext.md)

# contentSizeAdjustment

<sub>Instance Property</sub>

The delta value to be applied to the collection view’s content size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var contentSizeAdjustment: CGSize { get set }
```

## Discussion

Use this property to update the size of the collection view’s content area. The default value of this property is [CGSizeZero](../../coregraphics/cgsizezero.md). Changing the value causes the collection view to add the specified height and width values to its [contentSize](../uiscrollview/contentsize.md) property. Thus, positive values grow the content area and negative values shrink it.

## See Also

### Invalidating the Content Area

- [contentOffsetAdjustment](contentoffsetadjustment.md) — The delta value to be applied to the collection view’s content offset.
