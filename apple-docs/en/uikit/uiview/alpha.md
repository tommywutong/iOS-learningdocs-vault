---
title: alpha
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/alpha
source_url: 'https://developer.apple.com/documentation/uikit/uiview/alpha'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/alpha.json'
content_hash: 'sha256:5951db8f051773a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# alpha

<sub>Instance Property</sub>

The view’s alpha value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var alpha: CGFloat { get set }
```

## Discussion

The value of this property is a floating-point number in the range `0.0` to `1.0`, where `0.0` represents totally transparent and `1.0` represents totally opaque. Changing the value of this property updates the alpha value of the current view only. However, the transparency imparted by that alpha value affects all of the view’s contents, including its subviews. For example, a subview with an alpha value of `1.0` that is embedded in a parent view with an alpha value of `0.5,` appears onscreen as if its alpha value is also `0.5`.

Changes to this property can be animated.

## See Also

### Configuring a view’s visual appearance

- [backgroundColor](backgroundcolor.md) — The view’s background color.
- [hidden](ishidden.md) — A Boolean value that determines whether the view is hidden.
- [opaque](isopaque.md) — A Boolean value that determines whether the view is opaque.
- [tintColor](tintcolor.md) — The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [tintAdjustmentMode](tintadjustmentmode-swift.property.md) — The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [clipsToBounds](clipstobounds.md) — A Boolean value that determines whether subviews are confined to the bounds of the view.
- [clearsContextBeforeDrawing](clearscontextbeforedrawing.md) — A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [maskView](mask.md) — An optional view whose alpha channel is used to mask a view’s content.
- [layerClass](layerclass.md) — Returns the class used to create the layer for instances of this class.
- [layer](layer.md) — The view’s Core Animation layer to use for rendering.
