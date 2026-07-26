---
title: clearsContextBeforeDrawing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/clearscontextbeforedrawing
source_url: 'https://developer.apple.com/documentation/uikit/uiview/clearscontextbeforedrawing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/clearscontextbeforedrawing.json'
content_hash: 'sha256:19f682e9bd185ab3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# clearsContextBeforeDrawing

<sub>Instance Property</sub>

A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var clearsContextBeforeDrawing: Bool { get set }
```

## Discussion

When set to [true](../../swift/true.md), the drawing buffer is automatically cleared to transparent black before the [- drawRect:](<draw(__).md>) method is called. This behavior ensures that there are no visual artifacts left over when the view’s contents are redrawn. If the view’s [opaque](isopaque.md) property is also set to [true](../../swift/true.md), the [backgroundColor](backgroundcolor.md) property of the view must not be `nil` or drawing errors may occur. The default value of this property is [true](../../swift/true.md).

If you set the value of this property to [false](../../swift/false.md), you are responsible for ensuring the contents of the view are drawn properly in your [- drawRect:](<draw(__).md>) method. If your drawing code is already heavily optimized, setting this property is [false](../../swift/false.md) can improve performance, especially during scrolling when only a portion of the view might need to be redrawn.

## See Also

### Configuring a view’s visual appearance

- [backgroundColor](backgroundcolor.md) — The view’s background color.
- [hidden](ishidden.md) — A Boolean value that determines whether the view is hidden.
- [alpha](alpha.md) — The view’s alpha value.
- [opaque](isopaque.md) — A Boolean value that determines whether the view is opaque.
- [tintColor](tintcolor.md) — The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [tintAdjustmentMode](tintadjustmentmode-swift.property.md) — The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [clipsToBounds](clipstobounds.md) — A Boolean value that determines whether subviews are confined to the bounds of the view.
- [maskView](mask.md) — An optional view whose alpha channel is used to mask a view’s content.
- [layerClass](layerclass.md) — Returns the class used to create the layer for instances of this class.
- [layer](layer.md) — The view’s Core Animation layer to use for rendering.
