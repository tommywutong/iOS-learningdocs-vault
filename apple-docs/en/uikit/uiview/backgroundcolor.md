---
title: backgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/backgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uiview/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/backgroundcolor.json'
content_hash: 'sha256:0dc7cac9edb74280'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# backgroundColor

<sub>Instance Property</sub>

The view’s background color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var backgroundColor: UIColor? { get set }
```

## Discussion

Changes to this property can be animated. The default value is `nil`, which results in a transparent background color.

## See Also

### Configuring a view’s visual appearance

- [hidden](ishidden.md) — A Boolean value that determines whether the view is hidden.
- [alpha](alpha.md) — The view’s alpha value.
- [opaque](isopaque.md) — A Boolean value that determines whether the view is opaque.
- [tintColor](tintcolor.md) — The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [tintAdjustmentMode](tintadjustmentmode-swift.property.md) — The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [clipsToBounds](clipstobounds.md) — A Boolean value that determines whether subviews are confined to the bounds of the view.
- [clearsContextBeforeDrawing](clearscontextbeforedrawing.md) — A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [maskView](mask.md) — An optional view whose alpha channel is used to mask a view’s content.
- [layerClass](layerclass.md) — Returns the class used to create the layer for instances of this class.
- [layer](layer.md) — The view’s Core Animation layer to use for rendering.
