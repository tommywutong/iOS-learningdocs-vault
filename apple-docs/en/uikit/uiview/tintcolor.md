---
title: tintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/tintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uiview/tintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/tintcolor.json'
content_hash: 'sha256:068975d2c85db7db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# tintColor

<sub>Instance Property</sub>

The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tintColor: UIColor! { get set }
```

## Discussion

If the system cannot find a nondefault color in the hierarchy, this property’s value is a system-defined color instead.

If the view’s [tintAdjustmentMode](tintadjustmentmode-swift.property.md) property’s value is [UIViewTintAdjustmentModeDimmed](tintadjustmentmode-swift.enum/dimmed.md), then the [tintColor](tintcolor.md) property value is automatically dimmed.

To refresh subview rendering when this property changes, override the [- tintColorDidChange](<tintcolordidchange().md>) method.

Colors that are pattern colors (as described in [UIColor](../uicolor.md)) are not supported.

> [!important] Important
> If you attempt to use a pattern color as a tint color, the system raises an exception.

## See Also

### Related Documentation

- [- tintColorDidChange](<tintcolordidchange().md>) — Called by the system when the tint color property changes.

### Configuring a view’s visual appearance

- [backgroundColor](backgroundcolor.md) — The view’s background color.
- [hidden](ishidden.md) — A Boolean value that determines whether the view is hidden.
- [alpha](alpha.md) — The view’s alpha value.
- [opaque](isopaque.md) — A Boolean value that determines whether the view is opaque.
- [tintAdjustmentMode](tintadjustmentmode-swift.property.md) — The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [clipsToBounds](clipstobounds.md) — A Boolean value that determines whether subviews are confined to the bounds of the view.
- [clearsContextBeforeDrawing](clearscontextbeforedrawing.md) — A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [maskView](mask.md) — An optional view whose alpha channel is used to mask a view’s content.
- [layerClass](layerclass.md) — Returns the class used to create the layer for instances of this class.
- [layer](layer.md) — The view’s Core Animation layer to use for rendering.
