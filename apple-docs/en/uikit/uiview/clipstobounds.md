---
title: clipsToBounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/clipstobounds
source_url: 'https://developer.apple.com/documentation/uikit/uiview/clipstobounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/clipstobounds.json'
content_hash: 'sha256:3e9eab3daffecc7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# clipsToBounds

<sub>Instance Property</sub>

A Boolean value that determines whether subviews are confined to the bounds of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var clipsToBounds: Bool { get set }
```

## Discussion

Setting this value to [true](../../swift/true.md) causes subviews to be clipped to the bounds of the view. If set to [false](../../swift/false.md), subviews whose frames extend beyond the visible bounds of the view aren’t clipped.

The default value is [false](../../swift/false.md). Some subclasses of [UIView](../uiview.md), like [UIScrollView](../uiscrollview.md), override the default value to [true](../../swift/true.md).

## See Also

### Configuring a view’s visual appearance

- [backgroundColor](backgroundcolor.md) — The view’s background color.
- [hidden](ishidden.md) — A Boolean value that determines whether the view is hidden.
- [alpha](alpha.md) — The view’s alpha value.
- [opaque](isopaque.md) — A Boolean value that determines whether the view is opaque.
- [tintColor](tintcolor.md) — The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [tintAdjustmentMode](tintadjustmentmode-swift.property.md) — The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [clearsContextBeforeDrawing](clearscontextbeforedrawing.md) — A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [maskView](mask.md) — An optional view whose alpha channel is used to mask a view’s content.
- [layerClass](layerclass.md) — Returns the class used to create the layer for instances of this class.
- [layer](layer.md) — The view’s Core Animation layer to use for rendering.
